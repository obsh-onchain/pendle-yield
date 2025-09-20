"""
Main client for the pendle-yield package.

This module contains the PendleYieldClient class, which provides the primary
interface for interacting with Pendle Finance data.
"""

from typing import Any

from .etherscan import EtherscanClient
from .exceptions import APIError, ValidationError
from .models import EnrichedVoteEvent, VoteEvent
from .pendle import PendleClient


class PendleYieldClient:
    """
    Main client for interacting with Pendle Finance data.

    This client provides methods to fetch vote events from Etherscan,
    pool information from Pendle voter APR API, and combine them into enriched datasets.
    """

    def __init__(
        self,
        etherscan_api_key: str,
        etherscan_base_url: str = "https://api.etherscan.io/api",
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
        self._pendle_client = PendleClient(
            base_url=pendle_base_url,
            timeout=timeout,
            max_retries=max_retries,
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
        self._pendle_client.close()

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
            voter_apr_response = self._pendle_client.get_pool_voter_apr_data()
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

        return enriched_votes
