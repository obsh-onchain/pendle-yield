"""
Etherscan API client for the pendle-yield package.

This module provides functionality to interact with the Etherscan API
to fetch blockchain data, specifically vote events and swap events.
"""

import time
from datetime import datetime
from typing import Any

import httpx
from pydantic import ValidationError as PydanticValidationError

from .exceptions import APIError, RateLimitError, ValidationError
from .models import EtherscanResponse, SwapEvent, VoteEvent

# Topic for the 'Vote' event: Vote(address indexed user, address indexed pool, uint256 weight, int256 bias, int256 slope)
VOTE_TOPIC = "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1"

# Topic for the 'Swap' event: Swap(address indexed caller, address indexed receiver, int256 netPtOut, int256 netSyOut, uint256 netSyFee, uint256 netSyToReserve)
SWAP_TOPIC = "0x829000a5bc6a12d46e30cdcecd7c56b1efd88f6d7d059da6734a04f3764557c4"

# Block batch size for handling Etherscan API limitation (page × offset ≤ 10,000)
# This splits large block ranges into smaller chunks to avoid hitting the limit
BLOCK_BATCH_SIZE = 1000


class EtherscanClient:
    """
    Client for interacting with the Etherscan API.

    This client provides methods to fetch vote events and other blockchain data
    from the Etherscan API.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.etherscan.io/v2/api",
        timeout: float = 30.0,
        max_retries: int = 3,
        requests_per_second: float = 5.0,
    ) -> None:
        """
        Initialize the EtherscanClient.

        Args:
            api_key: API key for Etherscan
            base_url: Base URL for Etherscan API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            requests_per_second: Maximum requests per second (default: 5 for free tier)
        """
        if not api_key:
            raise ValidationError("Etherscan API key is required", field="api_key")

        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

        # Rate limiting configuration
        self._requests_per_second = requests_per_second
        self._min_request_interval = 1.0 / requests_per_second
        self._last_request_time = 0.0

        # HTTP client configuration
        self._client = httpx.Client(
            timeout=httpx.Timeout(timeout),
            limits=httpx.Limits(max_keepalive_connections=10, max_connections=20),
        )

    def __enter__(self) -> "EtherscanClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _enforce_rate_limit(self) -> None:
        """
        Enforce rate limiting by sleeping if necessary.

        Ensures that requests are spaced at least _min_request_interval apart.
        """
        current_time = time.time()
        time_since_last_request = current_time - self._last_request_time

        if time_since_last_request < self._min_request_interval:
            time.sleep(self._min_request_interval)
            self._last_request_time = current_time + self._min_request_interval
        else:
            self._last_request_time = current_time

    def _parse_vote_events(
        self, etherscan_response: EtherscanResponse
    ) -> list[VoteEvent]:
        """
        Parse log entries into vote events.

        Args:
            etherscan_response: Validated Etherscan API response

        Returns:
            List of parsed vote events
        """
        vote_events = []
        if isinstance(etherscan_response.result, list):
            for log_entry in etherscan_response.result:
                try:
                    # Parse the log data to extract vote information
                    # Vote event signature: Vote(address indexed user, address indexed pool, uint256 weight, int256 bias, int256 slope)
                    # topics[0] = event signature
                    # topics[1] = user address (indexed)
                    # topics[2] = pool address (indexed)
                    # data contains: weight, bias, slope (each 32 bytes / 64 hex chars)

                    if len(log_entry.topics) < 3:
                        continue  # Skip malformed entries

                    # Extract addresses from topics (remove padding zeros)
                    voter_address = "0x" + log_entry.topics[1][-40:]
                    pool_address = "0x" + log_entry.topics[2][-40:]

                    # Parse data field - remove '0x' prefix and split into 64-char chunks
                    data_hex = (
                        log_entry.data[2:]
                        if log_entry.data.startswith("0x")
                        else log_entry.data
                    )

                    # Each parameter is 32 bytes (64 hex chars)
                    if len(data_hex) >= 192:  # 3 * 64 chars for weight, bias, slope
                        weight_hex = data_hex[0:64]
                        bias_hex = data_hex[64:128]
                        slope_hex = data_hex[128:192]

                        # Convert hex to integers
                        weight = int(
                            weight_hex, 16
                        )  # weight is uint256, always positive
                        bias = int(bias_hex, 16)
                        slope = int(slope_hex, 16)

                        # Convert slope to signed integer if needed (check if MSB is set)
                        if slope >= 2**255:
                            slope = slope - 2**256

                        # Convert bias to signed integer if needed (check if MSB is set)
                        if bias >= 2**255:
                            bias = bias - 2**256
                    else:
                        # Handle case where data might be shorter (like in the second log entry)
                        weight = 0
                        bias = 0
                        slope = 0

                    # Convert hex timestamp to datetime
                    timestamp_int = int(log_entry.time_stamp, 16)
                    timestamp = datetime.fromtimestamp(timestamp_int)

                    vote_event = VoteEvent(
                        block_number=int(log_entry.block_number, 16),
                        transaction_hash=log_entry.transaction_hash,
                        voter_address=voter_address,
                        pool_address=pool_address,
                        weight=weight,  # weight is always positive (uint256)
                        bias=abs(bias),  # Store as positive value
                        slope=abs(slope),  # Store as positive value
                        timestamp=timestamp,
                    )
                    vote_events.append(vote_event)
                except (ValueError, IndexError, AttributeError):
                    # Skip malformed log entries
                    continue

        return vote_events

    def _parse_swap_events(
        self, etherscan_response: EtherscanResponse
    ) -> list[SwapEvent]:
        """
        Parse log entries into swap events.

        Args:
            etherscan_response: Validated Etherscan API response

        Returns:
            List of parsed swap events
        """
        swap_events = []
        if isinstance(etherscan_response.result, list):
            for log_entry in etherscan_response.result:
                try:
                    # Parse the log data to extract swap information
                    # Swap event signature: Swap(address indexed caller, address indexed receiver, int256 netPtOut, int256 netSyOut, uint256 netSyFee, uint256 netSyToReserve)
                    # topics[0] = event signature
                    # topics[1] = caller address (indexed)
                    # topics[2] = receiver address (indexed)
                    # data contains: netPtOut, netSyOut, netSyFee, netSyToReserve (each 32 bytes / 64 hex chars)

                    if len(log_entry.topics) < 3:
                        continue  # Skip malformed entries

                    # Extract addresses from topics (remove padding zeros)
                    caller = "0x" + log_entry.topics[1][-40:]
                    receiver = "0x" + log_entry.topics[2][-40:]

                    # Parse data field - remove '0x' prefix and split into 64-char chunks
                    data_hex = (
                        log_entry.data[2:]
                        if log_entry.data.startswith("0x")
                        else log_entry.data
                    )

                    # Each parameter is 32 bytes (64 hex chars)
                    # We need 4 parameters: netPtOut, netSyOut, netSyFee, netSyToReserve
                    if len(data_hex) >= 256:  # 4 * 64 chars
                        net_pt_out_hex = data_hex[0:64]
                        net_sy_out_hex = data_hex[64:128]
                        net_sy_fee_hex = data_hex[128:192]
                        net_sy_to_reserve_hex = data_hex[192:256]

                        # Convert hex to integers
                        net_pt_out = int(net_pt_out_hex, 16)
                        net_sy_out = int(net_sy_out_hex, 16)
                        net_sy_fee = int(net_sy_fee_hex, 16)
                        net_sy_to_reserve = int(net_sy_to_reserve_hex, 16)

                        # Convert to signed integers for netPtOut and netSyOut (int256)
                        if net_pt_out >= 2**255:
                            net_pt_out = net_pt_out - 2**256

                        if net_sy_out >= 2**255:
                            net_sy_out = net_sy_out - 2**256

                        # netSyFee and netSyToReserve are uint256, so they remain positive
                    else:
                        # Handle case where data might be shorter
                        net_pt_out = 0
                        net_sy_out = 0
                        net_sy_fee = 0
                        net_sy_to_reserve = 0

                    # Convert hex timestamp to datetime
                    timestamp_int = int(log_entry.time_stamp, 16)
                    timestamp = datetime.fromtimestamp(timestamp_int)

                    swap_event = SwapEvent(
                        block_number=int(log_entry.block_number, 16),
                        transaction_hash=log_entry.transaction_hash,
                        pool_address=log_entry.address.lower(),
                        caller=caller,
                        receiver=receiver,
                        net_pt_out=net_pt_out,
                        net_sy_out=net_sy_out,
                        net_sy_fee=net_sy_fee,
                        net_sy_to_reserve=net_sy_to_reserve,
                        timestamp=timestamp,
                    )
                    swap_events.append(swap_event)
                except (ValueError, IndexError, AttributeError):
                    # Skip malformed log entries
                    continue

        return swap_events

    def _make_request(
        self, url: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Make an HTTP request with retry logic.

        Args:
            url: URL to request
            params: Query parameters

        Returns:
            JSON response data

        Raises:
            APIError: If the request fails
            RateLimitError: If rate limit is exceeded
        """
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.get(url, params=params)

                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 60))
                    raise RateLimitError(
                        "Rate limit exceeded",
                        retry_after=retry_after,
                        status_code=response.status_code,
                        url=url,
                    )

                response.raise_for_status()
                json_response: dict[str, Any] = response.json()
                return json_response

            except httpx.HTTPStatusError as e:
                last_exception = APIError(
                    f"HTTP {e.response.status_code}: {e.response.text}",
                    status_code=e.response.status_code,
                    response_text=e.response.text,
                    url=url,
                )
            except httpx.RequestError as e:
                last_exception = APIError(f"Request failed: {str(e)}", url=url)
            except RateLimitError:
                # Re-raise RateLimitError as-is
                raise
            except Exception as e:
                last_exception = APIError(f"Unexpected error: {str(e)}", url=url)

            if attempt < self.max_retries:
                time.sleep(2**attempt)  # Exponential backoff

        # This should never be reached due to the loop logic, but mypy needs this
        if last_exception is not None:
            raise last_exception
        raise APIError("All retry attempts failed", url=url)

    def get_vote_events(
        self, from_block: int, to_block: int, max_pages: int | None = None
    ) -> list[VoteEvent]:
        """
        Fetch vote events for a specific block range from Etherscan with pagination.

        Uses block range batching to handle Etherscan API limitation where page × offset ≤ 10,000.
        Large block ranges are split into smaller chunks to avoid hitting this limit.

        Args:
            from_block: Starting block number
            to_block: Ending block number
            max_pages: Maximum number of pages to fetch per block batch (None for unlimited)

        Returns:
            List of vote events

        Raises:
            ValidationError: If block numbers are invalid
            APIError: If the API request fails
        """
        # Validate block numbers
        if from_block <= 0 or to_block <= 0:
            raise ValidationError(
                "Block numbers must be positive",
                field="block_numbers",
                value=f"from_block={from_block}, to_block={to_block}",
            )

        if from_block > to_block:
            raise ValidationError(
                "from_block must be less than or equal to to_block",
                field="block_range",
                value=f"from_block={from_block}, to_block={to_block}",
            )

        all_vote_events = []

        # Split the block range into batches to avoid Etherscan API limitation
        current_from = from_block
        while current_from <= to_block:
            current_to = min(current_from + BLOCK_BATCH_SIZE - 1, to_block)

            # Fetch events for current block batch with pagination
            batch_events = self._get_vote_events_for_batch(
                current_from, current_to, max_pages
            )
            all_vote_events.extend(batch_events)

            current_from = current_to + 1

        return all_vote_events

    def _get_vote_events_for_batch(
        self, from_block: int, to_block: int, max_pages: int | None = None
    ) -> list[VoteEvent]:
        """
        Fetch vote events for a single block batch with pagination.

        Args:
            from_block: Starting block number for this batch
            to_block: Ending block number for this batch
            max_pages: Maximum number of pages to fetch (None for unlimited)

        Returns:
            List of vote events for this batch

        Raises:
            APIError: If the API request fails
        """
        batch_events = []
        page = 1

        while True:
            # Enforce rate limiting before each request
            self._enforce_rate_limit()

            # Etherscan API parameters for getting logs with pagination
            params = {
                "chainid": "1",  # Ethereum mainnet
                "module": "logs",
                "action": "getLogs",
                "fromBlock": str(from_block),
                "toBlock": str(to_block),
                "topic0": VOTE_TOPIC,  # Vote event signature
                "page": str(page),
                "offset": "1000",  # Maximum results per page
                "apikey": self.api_key,
            }

            url = self.base_url
            response_data = self._make_request(url, params)

            try:
                etherscan_response = EtherscanResponse(**response_data)
            except PydanticValidationError as e:
                raise ValidationError(f"Invalid response format: {str(e)}") from e

            if etherscan_response.status != "1":
                # Handle "No records found" gracefully - this is normal for empty block ranges
                if etherscan_response.message == "No records found":
                    return []  # Return empty list instead of raising error

                # Include more details about other errors
                error_details = {
                    "status": etherscan_response.status,
                    "message": etherscan_response.message,
                    "result": etherscan_response.result,
                    "params": params,
                }
                raise APIError(
                    f"Etherscan API error: {etherscan_response.message}",
                    status_code=None,
                    response_text=str(error_details),
                    url=url,
                )

            # Parse log entries into vote events
            page_events = self._parse_vote_events(etherscan_response)
            batch_events.extend(page_events)

            # Check if we should continue pagination
            if len(page_events) < 1000:
                # Less than 1000 results means this is the last page
                break

            if max_pages is not None and page >= max_pages:
                # Reached maximum page limit
                break

            # Check if we're approaching the API limit (page × offset ≤ 10,000)
            if page >= 10:  # With offset=1000, page 10 gives us 10,000 results
                # Stop pagination to avoid hitting the limit
                break

            page += 1

        return batch_events

    def get_swap_events(
        self, from_block: int, to_block: int, max_pages: int | None = None
    ) -> list[SwapEvent]:
        """
        Fetch swap events for all pools in a specific block range from Etherscan with pagination.

        Uses block range batching to handle Etherscan API limitation where page × offset ≤ 10,000.
        Large block ranges are split into smaller chunks to avoid hitting this limit.

        Args:
            from_block: Starting block number
            to_block: Ending block number
            max_pages: Maximum number of pages to fetch per block batch (None for unlimited)

        Returns:
            List of swap events from all pools

        Raises:
            ValidationError: If block numbers are invalid
            APIError: If the API request fails
        """
        # Validate block numbers
        if from_block <= 0 or to_block <= 0:
            raise ValidationError(
                "Block numbers must be positive",
                field="block_numbers",
                value=f"from_block={from_block}, to_block={to_block}",
            )

        if from_block > to_block:
            raise ValidationError(
                "from_block must be less than or equal to to_block",
                field="block_range",
                value=f"from_block={from_block}, to_block={to_block}",
            )

        all_swap_events = []

        # Split the block range into batches to avoid Etherscan API limitation
        current_from = from_block
        while current_from <= to_block:
            current_to = min(current_from + BLOCK_BATCH_SIZE - 1, to_block)

            # Fetch events for current block batch with pagination
            batch_events = self._get_swap_events_for_batch(
                current_from, current_to, max_pages
            )
            all_swap_events.extend(batch_events)

            current_from = current_to + 1

        return all_swap_events

    def _get_swap_events_for_batch(
        self, from_block: int, to_block: int, max_pages: int | None = None
    ) -> list[SwapEvent]:
        """
        Fetch swap events for a single block batch with pagination.

        Args:
            from_block: Starting block number for this batch
            to_block: Ending block number for this batch
            max_pages: Maximum number of pages to fetch (None for unlimited)

        Returns:
            List of swap events for this batch

        Raises:
            APIError: If the API request fails
        """
        batch_events = []
        page = 1

        while True:
            # Enforce rate limiting before each request
            self._enforce_rate_limit()

            # Etherscan API parameters for getting logs with pagination
            params = {
                "chainid": "1",  # Ethereum mainnet
                "module": "logs",
                "action": "getLogs",
                "fromBlock": str(from_block),
                "toBlock": str(to_block),
                "topic0": SWAP_TOPIC,  # Swap event signature
                "page": str(page),
                "offset": "1000",  # Maximum results per page
                "apikey": self.api_key,
            }

            url = self.base_url
            response_data = self._make_request(url, params)

            try:
                etherscan_response = EtherscanResponse(**response_data)
            except PydanticValidationError as e:
                raise ValidationError(f"Invalid response format: {str(e)}") from e

            if etherscan_response.status != "1":
                # Handle "No records found" gracefully - this is normal for empty block ranges
                if etherscan_response.message == "No records found":
                    return []  # Return empty list instead of raising error

                # Include more details about other errors
                error_details = {
                    "status": etherscan_response.status,
                    "message": etherscan_response.message,
                    "result": etherscan_response.result,
                    "params": params,
                }
                raise APIError(
                    f"Etherscan API error: {etherscan_response.message}",
                    status_code=None,
                    response_text=str(error_details),
                    url=url,
                )

            # Parse log entries into swap events
            page_events = self._parse_swap_events(etherscan_response)
            batch_events.extend(page_events)

            # Check if we should continue pagination
            if len(page_events) < 1000:
                # Less than 1000 results means this is the last page
                break

            if max_pages is not None and page >= max_pages:
                # Reached maximum page limit
                break

            # Check if we're approaching the API limit (page × offset ≤ 10,000)
            if page >= 10:  # With offset=1000, page 10 gives us 10,000 results
                # Stop pagination to avoid hitting the limit
                break

            page += 1

        return batch_events

    def get_block_number_by_timestamp(
        self, timestamp: int, closest: str = "before"
    ) -> int:
        """
        Get block number by timestamp using Etherscan API.

        Args:
            timestamp: Unix timestamp to find the block for
            closest: Direction to search - "before" or "after" the timestamp

        Returns:
            Block number as integer

        Raises:
            ValidationError: If timestamp or closest parameter is invalid
            APIError: If the API request fails
        """
        # Validate timestamp
        if timestamp <= 0:
            raise ValidationError(
                "Timestamp must be positive",
                field="timestamp",
                value=str(timestamp),
            )

        # Validate closest parameter
        if closest not in ("before", "after"):
            raise ValidationError(
                "closest parameter must be 'before' or 'after'",
                field="closest",
                value=closest,
            )

        # Etherscan API parameters for getting block by timestamp
        params = {
            "chainid": "1",  # Ethereum mainnet
            "module": "block",
            "action": "getblocknobytime",
            "timestamp": str(timestamp),
            "closest": closest,
            "apikey": self.api_key,
        }

        url = self.base_url
        response_data = self._make_request(url, params)

        try:
            etherscan_response = EtherscanResponse(**response_data)
        except PydanticValidationError as e:
            raise ValidationError(f"Invalid response format: {str(e)}") from e

        if etherscan_response.status != "1":
            # Include more details about the error
            error_details = {
                "status": etherscan_response.status,
                "message": etherscan_response.message,
                "result": etherscan_response.result,
                "params": params,
            }
            raise APIError(
                f"Etherscan API error: {etherscan_response.message}",
                status_code=None,
                response_text=str(error_details),
                url=url,
            )

        # Parse the result as block number
        if isinstance(etherscan_response.result, str):
            try:
                block_number = int(etherscan_response.result)
                return block_number
            except ValueError as e:
                raise ValidationError(
                    f"Invalid block number format: {etherscan_response.result}"
                ) from e
        else:
            raise ValidationError(
                f"Expected string result, got {type(etherscan_response.result)}"
            )
