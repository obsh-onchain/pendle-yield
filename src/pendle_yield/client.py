"""
Main client for the pendle-yield package.

This module contains the PendleYieldClient class, which provides the primary
interface for interacting with Pendle Finance data.
"""

from datetime import datetime
from datetime import datetime as dt
from typing import Any

import httpx

from pendle_v2 import Client as PendleV2Client
from pendle_v2.api.ve_pendle import (
    ve_pendle_controller_all_market_total_fees,
    ve_pendle_controller_get_pool_voter_apr_and_swap_fee,
)
from pendle_v2.types import UNSET

from .epoch import PendleEpoch
from .etherscan import EtherscanClient
from .exceptions import APIError, ValidationError
from .models import (
    EnrichedVoteEvent,
    EpochMarketFee,
    MarketFeeData,
    MarketFeesResponse,
    MarketFeeValue,
    MarketInfo,
    PoolInfo,
    PoolVoterData,
    VoteEvent,
    VoterAprResponse,
)


class PendleYieldClient:
    """
    Main client for interacting with Pendle Finance data.

    This client provides methods to fetch vote events from Etherscan,
    pool information from Pendle voter APR API, and combine them into enriched datasets.
    """

    def __init__(
        self,
        etherscan_api_key: str,
        etherscan_base_url: str = "https://api.etherscan.io/v2/api",
        pendle_base_url: str = "https://api-v2.pendle.finance/core",
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the PendleYieldClient.

        Args:
            etherscan_api_key: API key for Etherscan
            etherscan_base_url: Base URL for Etherscan API
            pendle_base_url: Base URL for Pendle API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
        """
        if not etherscan_api_key:
            raise ValidationError(
                "Etherscan API key is required", field="etherscan_api_key"
            )

        self.etherscan_api_key = etherscan_api_key
        self.etherscan_base_url = etherscan_base_url
        self.pendle_base_url = pendle_base_url
        self.timeout = timeout
        self.max_retries = max_retries

        # Initialize composed clients
        self._etherscan_client = EtherscanClient(
            api_key=etherscan_api_key,
            base_url=etherscan_base_url,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._pendle_v2_client = PendleV2Client(
            base_url=pendle_base_url,
            timeout=httpx.Timeout(timeout),
        )

    def __enter__(self) -> "PendleYieldClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP clients."""
        self._etherscan_client.close()
        self._pendle_v2_client.get_httpx_client().close()

    def get_vote_events(self, from_block: int, to_block: int) -> list[VoteEvent]:
        """
        Fetch vote events for a specific block range from Etherscan.

        Args:
            from_block: Starting block number
            to_block: Ending block number

        Returns:
            List of vote events

        Raises:
            ValidationError: If block numbers are invalid
            APIError: If the API request fails
        """
        return self._etherscan_client.get_vote_events(from_block, to_block)

    def get_votes(self, from_block: int, to_block: int) -> list[EnrichedVoteEvent]:
        """
        Get enriched vote events for a specific block range.

        This method fetches vote events from Etherscan and enriches them with
        pool information from the Pendle voter APR API.

        Args:
            from_block: Starting block number
            to_block: Ending block number

        Returns:
            List of enriched vote events

        Raises:
            ValidationError: If block numbers are invalid
            APIError: If any API request fails
        """
        # Fetch vote events from Etherscan
        vote_events = self.get_vote_events(from_block, to_block)

        # Fetch voter APR data from Pendle API (contains pool information)
        try:
            voter_apr_response = self._get_pool_voter_apr_data()
        except APIError:
            # If we can't fetch voter APR data, return vote events without enrichment
            return []

        # Create a mapping of pool addresses to pool info
        pool_info_map = {}
        for pool_voter_data in voter_apr_response.results:
            pool_address = pool_voter_data.pool.address.lower()
            pool_info_map[pool_address] = pool_voter_data.pool

        # Enrich vote events with pool information
        enriched_votes = []
        for vote_event in vote_events:
            pool_info = pool_info_map.get(vote_event.pool_address)
            if pool_info is not None:
                enriched_vote = EnrichedVoteEvent.from_vote_and_pool(
                    vote_event, pool_info
                )
                enriched_votes.append(enriched_vote)
            else:
                # Create a dummy pool info for historical pools not in current API
                from .models import PoolInfo

                dummy_pool_info = PoolInfo(
                    id=f"1-{vote_event.pool_address}",
                    chainId=1,
                    address=vote_event.pool_address,
                    symbol="UNKNOWN",
                    expiry=datetime(2025, 1, 1),  # Default expiry
                    protocol="Unknown",
                    underlyingPool="",
                    voterApy=0.0,
                    accentColor="#000000",
                    name="Historical Pool",
                    farmSimpleName="Historical Pool",
                    farmSimpleIcon="",
                    farmProName="Historical Pool",
                    farmProIcon="",
                )
                enriched_vote = EnrichedVoteEvent.from_vote_and_pool(
                    vote_event, dummy_pool_info
                )
                enriched_votes.append(enriched_vote)

        return enriched_votes

    def get_votes_by_epoch(self, epoch: PendleEpoch) -> list[EnrichedVoteEvent]:
        """
        Get enriched vote events for a specific Pendle epoch.

        Args:
            epoch: PendleEpoch object representing the voting period

        Returns:
            List of enriched vote events for the epoch

        Raises:
            ValidationError: If epoch is invalid or current/future
            APIError: If any API request fails
        """
        # Get block range from epoch
        from_block, to_block = epoch.get_block_range(
            self._etherscan_client, use_latest_for_current=True
        )

        # Handle case where to_block might be None for current epochs
        if to_block is None:
            raise ValidationError(
                "Cannot get votes for current epoch without end block. "
                "Use use_latest_for_current=True in get_block_range.",
                field="to_block",
                value=None,
            )

        # Delegate to existing get_votes method
        return self.get_votes(from_block, to_block)

    def get_market_fees_for_period(
        self, timestamp_start: str, timestamp_end: str
    ) -> MarketFeesResponse:
        """
        Get market fees chart data for a specific time period.

        Args:
            timestamp_start: Start timestamp in ISO format (e.g., "2025-07-30")
            timestamp_end: End timestamp in ISO format (e.g., "2025-09-01")

        Returns:
            Market fees response containing fee data for all markets

        Raises:
            APIError: If the API request fails
            ValidationError: If the response format is invalid
        """
        return self._get_market_fees_chart(timestamp_start, timestamp_end)

    def get_market_fees_by_epoch(self, epoch: PendleEpoch) -> list[EpochMarketFee]:
        """
        Get market fees for a specific Pendle epoch.

        This method fetches market fee data from the Pendle V2 API for the epoch period
        and aggregates the total fees per market.

        Args:
            epoch: PendleEpoch object representing the period

        Returns:
            List of EpochMarketFee objects containing fee data per market

        Raises:
            ValidationError: If epoch is invalid
            APIError: If the API request fails
        """
        # Format timestamps for API request (ISO format)
        timestamp_start = epoch.start_datetime.isoformat()
        timestamp_end = epoch.end_datetime.isoformat()

        # Fetch market fees data from Pendle V2 API
        market_fees_response = self._get_market_fees_chart(
            timestamp_start, timestamp_end
        )

        # Process each market's fee data
        epoch_market_fees = []
        for market_data in market_fees_response.results:
            # Parse market ID to get chain_id and address
            try:
                chain_id, market_address = EpochMarketFee.parse_market_id(
                    market_data.market.id
                )
            except ValueError:
                # Skip markets with invalid IDs
                continue

            # Sum up all fees in the epoch period
            total_fee = sum(value.total_fees for value in market_data.values)

            # Create EpochMarketFee object
            epoch_market_fee = EpochMarketFee(
                chain_id=chain_id,
                market_address=market_address,
                total_fee=total_fee,
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
            )
            epoch_market_fees.append(epoch_market_fee)

        return epoch_market_fees

    def _get_pool_voter_apr_data(self) -> VoterAprResponse:
        """
        Fetch pool voter APR data from the Pendle V2 API.

        Returns:
            Voter APR response containing pool data with APR metrics

        Raises:
            APIError: If the API request fails
        """
        try:
            response = ve_pendle_controller_get_pool_voter_apr_and_swap_fee.sync(
                client=self._pendle_v2_client,
                order_by="voterApr:-1",
            )

            if response is None:
                raise APIError("Failed to fetch pool voter APR data")

            # Convert pendle_v2 response to our VoterAprResponse model
            pool_voter_data_list = []
            for result in response.results:
                # Handle optional fields
                protocol = (
                    result.pool.protocol
                    if not isinstance(result.pool.protocol, type(UNSET))
                    else "Unknown"
                )
                underlying_pool = (
                    result.pool.underlying_pool
                    if not isinstance(result.pool.underlying_pool, type(UNSET))
                    else ""
                )
                accent_color = (
                    result.pool.accent_color
                    if not isinstance(result.pool.accent_color, type(UNSET))
                    else "#000000"
                )

                # Convert pool data
                pool_info = PoolInfo(
                    id=result.pool.id,
                    chainId=int(result.pool.chain_id),
                    address=result.pool.address,
                    symbol=result.pool.symbol,
                    expiry=dt.fromisoformat(result.pool.expiry),
                    protocol=protocol if protocol else "Unknown",
                    underlyingPool=underlying_pool if underlying_pool else "",
                    voterApy=result.pool.voter_apy,
                    accentColor=accent_color if accent_color else "#000000",
                    name=result.pool.name,
                    farmSimpleName=result.pool.farm_simple_name,
                    farmSimpleIcon=result.pool.farm_simple_icon,
                    farmProName=result.pool.farm_pro_name,
                    farmProIcon=result.pool.farm_pro_icon,
                )

                pool_voter_data = PoolVoterData(
                    pool=pool_info,
                    currentVoterApr=result.current_voter_apr,
                    lastEpochVoterApr=result.last_epoch_voter_apr,
                    currentSwapFee=result.current_swap_fee,
                    lastEpochSwapFee=result.last_epoch_swap_fee,
                    projectedVoterApr=result.projected_voter_apr,
                )
                pool_voter_data_list.append(pool_voter_data)

            return VoterAprResponse(
                results=pool_voter_data_list,
                totalPools=int(response.total_pools),
                totalFee=response.total_fee,
                timestamp=response.timestamp,
            )
        except Exception as e:
            raise APIError(f"Failed to fetch pool voter APR data: {str(e)}") from e

    def _get_market_fees_chart(
        self, timestamp_start: str, timestamp_end: str
    ) -> MarketFeesResponse:
        """
        Fetch market fees chart data from the Pendle V2 API.

        Args:
            timestamp_start: Start timestamp in ISO format (e.g., "2025-07-30")
            timestamp_end: End timestamp in ISO format (e.g., "2025-09-01")

        Returns:
            Market fees response containing fee data for all markets

        Raises:
            APIError: If the API request fails
        """
        try:
            # Parse ISO format timestamps to datetime objects
            start_dt = dt.fromisoformat(timestamp_start)
            end_dt = dt.fromisoformat(timestamp_end)

            response = ve_pendle_controller_all_market_total_fees.sync(
                client=self._pendle_v2_client,
                timestamp_start=start_dt,
                timestamp_end=end_dt,
            )

            if response is None:
                raise APIError("Failed to fetch market fees data")

            # Convert pendle_v2 response to our MarketFeesResponse model
            market_fee_data_list = []
            for result in response.results:
                market_info = MarketInfo(id=result.market.id)

                fee_values = [
                    MarketFeeValue(
                        time=value.time,
                        totalFees=value.total_fees,
                    )
                    for value in result.values
                ]

                market_fee_data = MarketFeeData(
                    market=market_info,
                    values=fee_values,
                )
                market_fee_data_list.append(market_fee_data)

            return MarketFeesResponse(results=market_fee_data_list)
        except Exception as e:
            raise APIError(f"Failed to fetch market fees data: {str(e)}") from e
