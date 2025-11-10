"""
Main client for the pendle-yield package.

This module contains the PendleYieldClient class, which provides the primary
interface for interacting with Pendle Finance data.
"""

import sqlite3
import time
from datetime import UTC, datetime, timedelta
from datetime import datetime as dt
from pathlib import Path
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
from .etherscan_cached import CachedEtherscanClient
from .exceptions import APIError, ValidationError
from .models import (
    EnrichedVoteEvent,
    EpochMarketFee,
    EpochVotesSnapshot,
    MarketFeeData,
    MarketFeesResponse,
    MarketFeeValue,
    MarketInfo,
    PoolInfo,
    PoolVoterData,
    VoteEvent,
    VoterAprResponse,
    VoteSnapshot,
)

# First epoch when Pendle voting started (2022-11-23 00:00 UTC)
FIRST_EPOCH_START = datetime(2022, 11, 23, 0, 0, 0, tzinfo=UTC)


class PendleYieldClient:
    """
    Main client for interacting with Pendle Finance data.

    This client provides methods to fetch vote events from Etherscan,
    pool information from Pendle voter APR API, and combine them into enriched datasets.

    Caching is enabled when db_path is provided, storing data in SQLite
    to avoid redundant API calls. When caching is enabled:
    - Vote events are cached per block range (via CachedEtherscanClient)
    - Market fees are cached for past epochs
    - Vote snapshots are cached for past and current epochs
    """

    def __init__(
        self,
        etherscan_api_key: str,
        db_path: str | None = None,
        etherscan_base_url: str = "https://api.etherscan.io/v2/api",
        pendle_base_url: str = "https://api-v2.pendle.finance/core",
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the PendleYieldClient.

        Args:
            etherscan_api_key: API key for Etherscan
            db_path: Optional path to SQLite database file for caching.
                    If provided, enables caching for:
                    - Vote events (per block range)
                    - Market fees (past epochs)
                    - Vote snapshots (past and current epochs)
                    If None, all data is fetched fresh from APIs.
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

        # Caching configuration
        self.db_path = Path(db_path) if db_path else None
        self._caching_enabled = db_path is not None

        # Initialize database if caching is enabled
        if self._caching_enabled:
            # Create parent directory if it doesn't exist
            assert self.db_path is not None  # Type narrowing for mypy
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self._init_database()

        # Rate limiting for Pendle API based on Computing Units (CU)
        # Pendle API limit: 100 CU per minute
        self._pendle_cu_limit = 100.0  # CU per minute
        self._pendle_cu_window = 60.0  # 1 minute window in seconds
        self._pendle_cu_consumed: list[tuple[float, float]] = []  # (timestamp, cu_cost)

        # Initialize composed clients
        # Use CachedEtherscanClient if caching is enabled, otherwise use regular client
        if self._caching_enabled:
            assert self.db_path is not None  # Type narrowing for mypy
            self._etherscan_client: EtherscanClient | CachedEtherscanClient = (
                CachedEtherscanClient(
                    api_key=etherscan_api_key,
                    db_path=str(self.db_path),
                    base_url=etherscan_base_url,
                    timeout=timeout,
                    max_retries=max_retries,
                )
            )
        else:
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

    def _init_database(self) -> None:
        """
        Initialize the SQLite database with required tables and indices.

        Creates tables for caching market fees and vote snapshots.
        Only called when caching is enabled (db_path is provided).
        """
        if not self._caching_enabled:
            return

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Create epoch_market_fees table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS epoch_market_fees (
                    epoch_start INTEGER NOT NULL,
                    epoch_end INTEGER NOT NULL,
                    chain_id INTEGER NOT NULL,
                    market_address TEXT NOT NULL,
                    total_fee REAL NOT NULL,
                    cached_at INTEGER NOT NULL,
                    PRIMARY KEY (epoch_start, epoch_end, chain_id, market_address)
                )
                """
            )

            # Create index for efficient epoch lookups
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_epoch_range
                ON epoch_market_fees(epoch_start, epoch_end)
                """
            )

            # Create epoch_votes_snapshots table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS epoch_votes_snapshots (
                    epoch_start INTEGER NOT NULL,
                    epoch_end INTEGER NOT NULL,
                    voter_address TEXT NOT NULL,
                    pool_address TEXT NOT NULL,
                    bias TEXT NOT NULL,
                    slope TEXT NOT NULL,
                    ve_pendle_value REAL NOT NULL,
                    last_vote_block INTEGER NOT NULL,
                    last_vote_timestamp INTEGER NOT NULL,
                    cached_at INTEGER NOT NULL,
                    PRIMARY KEY (epoch_start, epoch_end, voter_address, pool_address)
                )
                """
            )

            # Create index for efficient snapshot epoch lookups
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_snapshot_epoch
                ON epoch_votes_snapshots(epoch_start, epoch_end)
                """
            )

            conn.commit()
        finally:
            conn.close()

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

    def _enforce_pendle_rate_limit(self, cu_cost: float) -> None:
        """
        Enforce rate limiting for Pendle API based on Computing Units (CU).

        Pendle API has a limit of 100 CU per minute. This method ensures we don't
        exceed this limit by tracking CU consumption and sleeping if necessary.

        Args:
            cu_cost: The CU cost of the API call to be made
        """
        current_time = time.time()

        # Remove entries older than the rate limit window (1 minute)
        self._pendle_cu_consumed = [
            (timestamp, cu)
            for timestamp, cu in self._pendle_cu_consumed
            if current_time - timestamp < self._pendle_cu_window
        ]

        # Calculate current CU usage in the window
        current_cu_usage = sum(cu for _, cu in self._pendle_cu_consumed)

        # If adding this request would exceed the limit, sleep until we have capacity
        if current_cu_usage + cu_cost > self._pendle_cu_limit:
            # Find the oldest request that needs to age out to make room
            needed_cu = cu_cost - (self._pendle_cu_limit - current_cu_usage)
            cu_accumulated = 0.0
            sleep_until_time = current_time

            for timestamp, cu in self._pendle_cu_consumed:
                cu_accumulated += cu
                if cu_accumulated >= needed_cu:
                    # We need to wait until this request ages out
                    sleep_until_time = timestamp + self._pendle_cu_window
                    break

            sleep_time = max(0, sleep_until_time - current_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
                current_time = time.time()

                # Clean up again after sleeping
                self._pendle_cu_consumed = [
                    (timestamp, cu)
                    for timestamp, cu in self._pendle_cu_consumed
                    if current_time - timestamp < self._pendle_cu_window
                ]

        # Record this request
        self._pendle_cu_consumed.append((current_time, cu_cost))

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

    def _get_cached_epoch_fees(self, epoch: PendleEpoch) -> list[EpochMarketFee] | None:
        """
        Retrieve cached market fees for a specific epoch.

        Args:
            epoch: PendleEpoch object

        Returns:
            List of cached EpochMarketFee objects, or None if not cached or caching disabled
        """
        if not self._caching_enabled:
            return None

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Convert epoch timestamps to integers for comparison
            epoch_start = epoch.start_timestamp
            epoch_end = epoch.end_timestamp

            cursor.execute(
                """
                SELECT chain_id, market_address, total_fee, epoch_start, epoch_end
                FROM epoch_market_fees
                WHERE epoch_start = ? AND epoch_end = ?
                ORDER BY chain_id, market_address
                """,
                (epoch_start, epoch_end),
            )

            rows = cursor.fetchall()

            # If no rows found, cache miss
            if not rows:
                return None

            # Convert rows to EpochMarketFee objects
            epoch_fees = []
            for row in rows:
                epoch_fee = EpochMarketFee(
                    chain_id=row[0],
                    market_address=row[1],
                    total_fee=row[2],
                    epoch_start=datetime.fromtimestamp(row[3]),
                    epoch_end=datetime.fromtimestamp(row[4]),
                )
                epoch_fees.append(epoch_fee)

            return epoch_fees
        finally:
            conn.close()

    def _store_epoch_fees(
        self, epoch: PendleEpoch, epoch_fees: list[EpochMarketFee]
    ) -> None:
        """
        Store epoch market fees in the database.

        Args:
            epoch: PendleEpoch object
            epoch_fees: List of EpochMarketFee objects to store
        """
        if not self._caching_enabled:
            return

        if not epoch_fees:
            # Still store an empty marker to indicate this epoch was fetched
            conn = sqlite3.connect(str(self.db_path))
            try:
                cursor = conn.cursor()
                cached_at = int(datetime.now().timestamp())

                # Insert a marker row with a special market_address
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO epoch_market_fees
                    (epoch_start, epoch_end, chain_id, market_address, total_fee, cached_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        epoch.start_timestamp,
                        epoch.end_timestamp,
                        0,  # chain_id 0 as marker
                        "0x0000000000000000000000000000000000000000",  # zero address
                        0.0,
                        cached_at,
                    ),
                )
                conn.commit()
            finally:
                conn.close()
            return

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Get current timestamp for cache metadata
            cached_at = int(datetime.now().timestamp())

            # Prepare data for bulk insert
            rows = []
            for fee in epoch_fees:
                rows.append(
                    (
                        epoch.start_timestamp,
                        epoch.end_timestamp,
                        fee.chain_id,
                        fee.market_address,
                        fee.total_fee,
                        cached_at,
                    )
                )

            # Use INSERT OR REPLACE to handle updates gracefully
            cursor.executemany(
                """
                INSERT OR REPLACE INTO epoch_market_fees
                (epoch_start, epoch_end, chain_id, market_address, total_fee, cached_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                rows,
            )

            conn.commit()
        finally:
            conn.close()

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
        and aggregates the total fees per market. If caching is enabled, finished epochs
        are cached permanently.

        Args:
            epoch: PendleEpoch object representing the period

        Returns:
            List of EpochMarketFee objects containing fee data per market

        Raises:
            ValidationError: If epoch is invalid or future
            APIError: If the API request fails
        """
        # Validate epoch - don't allow future epochs
        if epoch.is_future:
            raise ValidationError(
                "Cannot get market fees for future epoch",
                field="epoch_status",
                value="future",
            )

        # Try to get from cache first (if caching is enabled and epoch is past)
        if self._caching_enabled and epoch.is_past:
            cached_fees = self._get_cached_epoch_fees(epoch)
            if cached_fees is not None:
                # Filter out the marker row if present
                return [
                    fee
                    for fee in cached_fees
                    if fee.market_address
                    != "0x0000000000000000000000000000000000000000"
                ]

        # Cache miss or current epoch - fetch from API
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

        # Cache if this is a finished epoch
        if self._caching_enabled and epoch.is_past:
            self._store_epoch_fees(epoch, epoch_market_fees)

        return epoch_market_fees

    def _get_pool_voter_apr_data(self) -> VoterAprResponse:
        """
        Fetch pool voter APR data from the Pendle V2 API.

        This endpoint costs 3 CU (Computing Units).

        Returns:
            Voter APR response containing pool data with APR metrics

        Raises:
            APIError: If the API request fails
        """
        # Enforce rate limiting before making Pendle API request (3 CU)
        self._enforce_pendle_rate_limit(cu_cost=3.0)

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

        This endpoint costs 8 CU (Computing Units).

        Args:
            timestamp_start: Start timestamp in ISO format (e.g., "2025-07-30")
            timestamp_end: End timestamp in ISO format (e.g., "2025-09-01")

        Returns:
            Market fees response containing fee data for all markets

        Raises:
            APIError: If the API request fails
        """
        # Enforce rate limiting before making Pendle API request (8 CU)
        self._enforce_pendle_rate_limit(cu_cost=8.0)

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

    def _get_cached_votes_snapshot(
        self, epoch: PendleEpoch
    ) -> EpochVotesSnapshot | None:
        """
        Retrieve cached votes snapshot for a specific epoch.

        Args:
            epoch: PendleEpoch object

        Returns:
            EpochVotesSnapshot object, or None if not cached or caching disabled
        """
        if not self._caching_enabled:
            return None

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Convert epoch timestamps to integers for comparison
            epoch_start = epoch.start_timestamp
            epoch_end = epoch.end_timestamp

            cursor.execute(
                """
                SELECT voter_address, pool_address, bias, slope, ve_pendle_value,
                       last_vote_block, last_vote_timestamp
                FROM epoch_votes_snapshots
                WHERE epoch_start = ? AND epoch_end = ?
                ORDER BY voter_address, pool_address
                """,
                (epoch_start, epoch_end),
            )

            rows = cursor.fetchall()

            # If no rows found, cache miss
            if not rows:
                return None

            # Convert rows to VoteSnapshot objects
            votes = []
            for row in rows:
                # Skip marker row for empty snapshots
                if row[0] == "0x0000000000000000000000000000000000000000":
                    continue

                vote = VoteSnapshot(
                    voter_address=row[0],
                    pool_address=row[1],
                    bias=int(row[2]),  # Convert from TEXT to int
                    slope=int(row[3]),  # Convert from TEXT to int
                    ve_pendle_value=row[4],
                    last_vote_block=row[5],
                    last_vote_timestamp=datetime.fromtimestamp(row[6]),
                )
                votes.append(vote)

            # Calculate total vePendle
            total_ve_pendle = sum(v.ve_pendle_value for v in votes)

            # Create and return snapshot
            return EpochVotesSnapshot(
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
                snapshot_timestamp=epoch.start_datetime,
                votes=votes,
                total_ve_pendle=total_ve_pendle,
            )
        finally:
            conn.close()

    def _store_votes_snapshot(
        self, epoch: PendleEpoch, snapshot: EpochVotesSnapshot
    ) -> None:
        """
        Store epoch votes snapshot in the database.

        Args:
            epoch: PendleEpoch object
            snapshot: EpochVotesSnapshot object to store
        """
        if not self._caching_enabled:
            return

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Get current timestamp for cache metadata
            cached_at = int(datetime.now().timestamp())

            # Delete existing entries for this epoch first
            cursor.execute(
                """
                DELETE FROM epoch_votes_snapshots
                WHERE epoch_start = ? AND epoch_end = ?
                """,
                (epoch.start_timestamp, epoch.end_timestamp),
            )

            # If snapshot is empty, insert a marker to indicate it was cached
            if not snapshot.votes:
                cursor.execute(
                    """
                    INSERT INTO epoch_votes_snapshots
                    (epoch_start, epoch_end, voter_address, pool_address, bias, slope,
                     ve_pendle_value, last_vote_block, last_vote_timestamp, cached_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        epoch.start_timestamp,
                        epoch.end_timestamp,
                        "0x0000000000000000000000000000000000000000",  # marker
                        "0x0000000000000000000000000000000000000000",  # marker
                        "0",
                        "0",
                        0.0,
                        0,
                        epoch.start_timestamp,
                        cached_at,
                    ),
                )
            else:
                # Prepare data for bulk insert
                rows = []
                for vote in snapshot.votes:
                    rows.append(
                        (
                            epoch.start_timestamp,
                            epoch.end_timestamp,
                            vote.voter_address,
                            vote.pool_address,
                            str(vote.bias),  # Convert to TEXT
                            str(vote.slope),  # Convert to TEXT
                            vote.ve_pendle_value,
                            vote.last_vote_block,
                            int(vote.last_vote_timestamp.timestamp()),
                            cached_at,
                        )
                    )

                # Insert new snapshot data
                cursor.executemany(
                    """
                    INSERT INTO epoch_votes_snapshots
                    (epoch_start, epoch_end, voter_address, pool_address, bias, slope,
                     ve_pendle_value, last_vote_block, last_vote_timestamp, cached_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    rows,
                )

            conn.commit()
        finally:
            conn.close()

    def get_epoch_votes_snapshot(self, epoch: PendleEpoch) -> EpochVotesSnapshot:
        """
        Get the votes snapshot at the START of the epoch.

        A snapshot represents the state of all active votes at Thursday 00:00 UTC
        when the epoch begins. This is when incentive rates are adjusted.

        Important: The snapshot is calculated at epoch start. Votes cast DURING
        this epoch do NOT affect this epoch's snapshot - they affect the NEXT
        epoch's snapshot.

        If caching is enabled, snapshots are cached permanently for both past and
        current epochs (since the snapshot is always at epoch start, which is in the past).

        Args:
            epoch: PendleEpoch object representing the period

        Returns:
            EpochVotesSnapshot with all active votes and their vePendle values
            at the epoch start time

        Raises:
            ValidationError: If epoch is future (snapshot time hasn't occurred yet)
            APIError: If any API request fails
        """
        # Validate - cannot get snapshot for future epochs
        if epoch.is_future:
            raise ValidationError(
                "Cannot get votes snapshot for future epoch - snapshot time hasn't occurred yet",
                field="epoch_status",
                value="future",
            )

        # Try to get from cache first (if caching is enabled)
        # Both past and current epochs can be cached since snapshot is at epoch start
        if self._caching_enabled:
            cached_snapshot = self._get_cached_votes_snapshot(epoch)
            if cached_snapshot is not None:
                return cached_snapshot

        # Cache miss - build snapshot from scratch
        # Strategy: Build snapshot from previous epoch's snapshot + previous epoch's votes
        # This is more efficient than processing all historical votes

        # Get the previous epoch
        previous_epoch_start = epoch.start_datetime - timedelta(days=7)
        previous_epoch = PendleEpoch(previous_epoch_start)

        # Base case: If this is before the first epoch, start with empty state
        vote_state: dict[tuple[str, str], VoteSnapshot]
        if previous_epoch.start_datetime < FIRST_EPOCH_START:
            vote_state = {}
        else:
            # Recursive case: Get previous epoch's snapshot
            previous_snapshot = self.get_epoch_votes_snapshot(previous_epoch)

            # Start with previous snapshot's vote state
            vote_state = {
                (vote.voter_address, vote.pool_address): VoteSnapshot(
                    voter_address=vote.voter_address,
                    pool_address=vote.pool_address,
                    bias=vote.bias,
                    slope=vote.slope,
                    ve_pendle_value=0.0,  # Will recalculate for new snapshot time
                    last_vote_block=vote.last_vote_block,
                    last_vote_timestamp=vote.last_vote_timestamp,
                )
                for vote in previous_snapshot.votes
            }

        # Get all votes from the PREVIOUS epoch (not current epoch)
        # These votes affect the current epoch's snapshot
        try:
            previous_epoch_votes = self.get_votes_by_epoch(previous_epoch)
        except ValidationError:
            # If previous epoch is before first epoch, no votes exist
            previous_epoch_votes = []

        # Apply votes chronologically to update state
        for vote in sorted(previous_epoch_votes, key=lambda v: v.block_number):
            key = (vote.voter_address, vote.pool_address)

            if vote.weight == 0:
                # Remove vote for this pool
                vote_state.pop(key, None)
            else:
                # Add or update vote
                vote_state[key] = VoteSnapshot(
                    voter_address=vote.voter_address,
                    pool_address=vote.pool_address,
                    bias=vote.bias,
                    slope=vote.slope,
                    ve_pendle_value=0.0,  # Will calculate below
                    last_vote_block=vote.block_number,
                    last_vote_timestamp=vote.timestamp or epoch.start_datetime,
                )

        # Calculate vePendle values at the snapshot time (epoch start)
        snapshot_timestamp = epoch.start_timestamp
        active_votes: list[VoteSnapshot] = []

        vote_snapshot: VoteSnapshot
        for vote_snapshot in vote_state.values():
            # Calculate vePendle at snapshot time
            # Formula: (bias - slope × timestamp) / 10^18
            ve_value_wei = vote_snapshot.bias - vote_snapshot.slope * snapshot_timestamp

            # Convert from wei to readable units
            ve_value = float(ve_value_wei) / 10**18

            # Only include votes with positive vePendle value
            if ve_value > 0:
                # Update the vote with calculated vePendle value
                vote_snapshot.ve_pendle_value = ve_value
                active_votes.append(vote_snapshot)

        # Create snapshot
        snapshot = EpochVotesSnapshot(
            epoch_start=epoch.start_datetime,
            epoch_end=epoch.end_datetime,
            snapshot_timestamp=epoch.start_datetime,
            votes=active_votes,
            total_ve_pendle=sum(v.ve_pendle_value for v in active_votes),
        )

        # Cache the snapshot (works for both past and current epochs)
        if self._caching_enabled:
            self._store_votes_snapshot(epoch, snapshot)

        return snapshot
