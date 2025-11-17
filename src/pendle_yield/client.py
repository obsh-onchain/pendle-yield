"""
Main client for the pendle-yield package.

This module contains the PendleYieldClient class, which provides the primary
interface for interacting with Pendle Finance data.
"""

import logging
import sqlite3
import time
from datetime import UTC, date, datetime, timedelta
from datetime import datetime as dt
from pathlib import Path
from typing import Any

import httpx

from pendle_v2 import Client as PendleV2Client
from pendle_v2.api.markets import markets_controller_market_historical_data_v_2
from pendle_v2.api.ve_pendle import (
    ve_pendle_controller_all_market_total_fees,
    ve_pendle_controller_get_pool_voter_apr_and_swap_fee,
)
from pendle_v2.models.market_historical_data_response import (
    MarketHistoricalDataResponse,
)
from pendle_v2.models.markets_controller_market_historical_data_v2_time_frame import (
    MarketsControllerMarketHistoricalDataV2TimeFrame,
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

            # Create market_historical_data table for caching daily historical data
            # Using flat structure with individual columns for efficient SQL queries
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS market_historical_data (
                    chain_id INTEGER NOT NULL,
                    market_address TEXT NOT NULL,
                    date TEXT NOT NULL,
                    timestamp TEXT,  -- Nullable to support marker rows for empty results
                    -- APY metrics (all REAL for float values, nullable)
                    max_apy REAL,
                    base_apy REAL,
                    underlying_apy REAL,
                    implied_apy REAL,
                    underlying_interest_apy REAL,
                    underlying_reward_apy REAL,
                    yt_floating_apy REAL,
                    swap_fee_apy REAL,
                    voter_apr REAL,
                    pendle_apy REAL,
                    lp_reward_apy REAL,
                    -- TVL and volume metrics
                    tvl REAL,
                    total_tvl REAL,
                    trading_volume REAL,
                    -- Price metrics
                    pt_price REAL,
                    yt_price REAL,
                    sy_price REAL,
                    lp_price REAL,
                    -- Supply metrics
                    total_pt REAL,
                    total_sy REAL,
                    total_supply REAL,
                    -- Fee breakdown (daily/weekly only)
                    explicit_swap_fee REAL,
                    implicit_swap_fee REAL,
                    limit_order_fee REAL,
                    -- Other metrics
                    last_epoch_votes REAL,
                    -- Metadata
                    created_at INTEGER NOT NULL,
                    PRIMARY KEY (chain_id, market_address, date)
                )
                """
            )

            # Create index for efficient market lookups
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_market_historical_market
                ON market_historical_data(chain_id, market_address)
                """
            )

            # Migrate existing table if needed: make timestamp column nullable
            # Check if the table exists and has the old schema
            cursor.execute(
                """
                SELECT sql FROM sqlite_master
                WHERE type='table' AND name='market_historical_data'
                """
            )

            # Create index for efficient date range queries
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_market_historical_date
                ON market_historical_data(date)
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

    def get_market_historical_data_cached(
        self,
        chain_id: int,
        market_address: str,
        start_date: date,
        end_date: date,
        force_refresh: bool = False,
    ) -> MarketHistoricalDataResponse:
        """
        Get market historical data with caching support.

        This method fetches daily historical data from the Pendle v2 API with intelligent
        caching behavior:
        - Past dates (before today UTC): Served from cache if available, never refetched
        - Current date (today UTC): Always fetched fresh from API and cache updated
        - Future dates: Not supported

        The method uses daily resolution and includes all available fields with fee breakdown.

        Args:
            chain_id: Chain ID (e.g., 1 for Ethereum mainnet)
            market_address: Market address (case-insensitive)
            start_date: Start date for the data range (inclusive)
            end_date: End date for the data range (inclusive)
            force_refresh: If True, bypass cache and fetch fresh data for all dates
                          (useful for testing/debugging)

        Returns:
            MarketHistoricalDataResponse containing daily data points

        Raises:
            ValidationError: If date range is invalid
            APIError: If the API request fails

        Example:
            >>> from datetime import date
            >>> client = PendleYieldClient(etherscan_api_key="...", db_path="cache.db")
            >>> response = client.get_market_historical_data_cached(
            ...     chain_id=1,
            ...     market_address="0xb4460e76d99ecad95030204d3c25fb33c4833997",
            ...     start_date=date(2024, 1, 1),
            ...     end_date=date(2024, 1, 31)
            ... )
            >>> print(f"Retrieved {len(response.results)} data points")
        """
        # Normalize market address to lowercase
        market_address = market_address.lower()

        # Validate date range
        if start_date > end_date:
            raise ValidationError(
                "Start date must be before or equal to end date",
                field="date_range",
                value=f"{start_date} to {end_date}",
            )

        # Get current date in UTC for cache invalidation logic
        today_utc = datetime.now(UTC).date()

        # Logging for debugging
        import logging
        logger = logging.getLogger("pendle_yield.cache")
        logger.info(
            f"get_market_historical_data_cached: chain_id={chain_id}, "
            f"market={market_address[:10]}..., dates={start_date} to {end_date}, "
            f"today_utc={today_utc}, caching_enabled={self._caching_enabled}, "
            f"force_refresh={force_refresh}"
        )

        # Collect all data points (will be populated from cache and/or API)
        all_data_points: dict[str, dict[str, Any]] = {}

        # Determine which dates need to be fetched from API
        dates_to_fetch: list[date] = []
        current_date = start_date

        while current_date <= end_date:
            # Skip future dates
            if current_date > today_utc:
                logger.debug(f"  {current_date}: SKIP (future date)")
                current_date += timedelta(days=1)
                continue

            # Check if we should use cache for this date
            use_cache = (
                self._caching_enabled
                and not force_refresh
                and current_date < today_utc  # Only cache past dates
            )

            if use_cache:
                # Try to get from cache
                cached_data = self._get_cached_historical_data(
                    chain_id, market_address, current_date
                )
                if cached_data is not None:
                    # Cache hit - use cached data (may be empty dict for marker rows)
                    if cached_data:
                        logger.info(f"  {current_date}: CACHE HIT (has data)")
                    else:
                        logger.info(f"  {current_date}: CACHE HIT (empty result marker)")
                    all_data_points[current_date.isoformat()] = cached_data
                    current_date += timedelta(days=1)
                    continue
                # Cache miss - will need to fetch from API
                logger.info(f"  {current_date}: CACHE MISS (will fetch from API)")
            else:
                # Not using cache for this date (force_refresh=True or current_date >= today)
                reason = "force_refresh" if force_refresh else "current/future date"
                logger.info(f"  {current_date}: NO CACHE ({reason}, will fetch from API)")

            # Cache miss or current date - need to fetch from API
            dates_to_fetch.append(current_date)
            current_date += timedelta(days=1)

        # Fetch missing dates from API if needed
        if dates_to_fetch:
            logger.info(f"Need to fetch {len(dates_to_fetch)} dates from API")

            # Group consecutive dates into ranges to minimize API calls
            date_ranges: list[tuple[date, date]] = []
            range_start = dates_to_fetch[0]
            range_end = dates_to_fetch[0]

            for i in range(1, len(dates_to_fetch)):
                if dates_to_fetch[i] == range_end + timedelta(days=1):
                    # Extend current range
                    range_end = dates_to_fetch[i]
                else:
                    # Start new range
                    date_ranges.append((range_start, range_end))
                    range_start = dates_to_fetch[i]
                    range_end = dates_to_fetch[i]

            # Add the last range
            date_ranges.append((range_start, range_end))

            logger.info(f"Grouped into {len(date_ranges)} API call(s)")

            # Fetch each range from API
            for fetch_start, fetch_end in date_ranges:
                logger.info(f"Calling API for date range: {fetch_start} to {fetch_end}")
                api_response = self._fetch_market_historical_data_from_api(
                    chain_id, market_address, fetch_start, fetch_end
                )
                logger.info(f"API returned {len(api_response.results)} data points")

                # Track which dates in this range were returned by the API
                returned_dates: set[date] = set()

                # Process and cache the results
                for data_point in api_response.results:
                    # Extract date from timestamp
                    point_date = data_point.timestamp.date()
                    returned_dates.add(point_date)

                    # Convert data point to dictionary for storage
                    point_dict = data_point.to_dict()

                    # Store in our collection
                    all_data_points[point_date.isoformat()] = point_dict

                    # Cache past dates (not today)
                    if self._caching_enabled and point_date < today_utc:
                        logger.info(f"  Caching data for {point_date}")
                        self._store_historical_data(
                            chain_id, market_address, point_date, point_dict
                        )
                    elif self._caching_enabled:
                        logger.info(f"  NOT caching {point_date} (today or future)")

                # Cache marker rows for dates that were requested but not returned
                # This prevents re-fetching empty results on subsequent runs
                if self._caching_enabled:
                    current = fetch_start
                    while current <= fetch_end:
                        if current < today_utc and current not in returned_dates:
                            logger.info(
                                f"  Caching EMPTY result marker for {current} "
                                "(API returned no data for this date)"
                            )
                            self._store_historical_data(
                                chain_id, market_address, current, None
                            )
                        current += timedelta(days=1)
        else:
            logger.info("All dates found in cache, no API calls needed")

        # Build response from collected data points
        # Filter out empty dicts (marker rows for dates with no data)
        # and sort by date to ensure chronological order
        non_empty_data_points = {
            date_str: data
            for date_str, data in all_data_points.items()
            if data  # Filters out empty dicts {}
        }
        sorted_dates = sorted(non_empty_data_points.keys())

        if not sorted_dates:
            # No data available (all dates were marker rows or no dates requested)
            return MarketHistoricalDataResponse(
                total=0,
                timestamp_start=datetime.combine(start_date, datetime.min.time()).replace(
                    tzinfo=UTC
                ),
                timestamp_end=datetime.combine(end_date, datetime.min.time()).replace(
                    tzinfo=UTC
                ),
                results=[],
            )

        # Convert dictionaries back to MarketHistoricalDataPoint objects
        from pendle_v2.models.market_historical_data_point import (
            MarketHistoricalDataPoint,
        )

        results = [
            MarketHistoricalDataPoint.from_dict(non_empty_data_points[date_str])
            for date_str in sorted_dates
        ]

        # Create response
        return MarketHistoricalDataResponse(
            total=len(results),
            timestamp_start=results[0].timestamp,
            timestamp_end=results[-1].timestamp,
            results=results,
        )

    def _fetch_market_historical_data_from_api(
        self, chain_id: int, market_address: str, start_date: date, end_date: date
    ) -> MarketHistoricalDataResponse:
        """
        Fetch market historical data from the Pendle v2 API.

        This is a low-level method that directly calls the API without caching.
        Use get_market_historical_data_cached() for the caching version.

        Args:
            chain_id: Chain ID (e.g., 1 for Ethereum mainnet)
            market_address: Market address (lowercase)
            start_date: Start date for the data range
            end_date: End date for the data range

        Returns:
            MarketHistoricalDataResponse from the API

        Raises:
            APIError: If the API request fails
        """
        # Note: This endpoint costs approximately 5 CU per request
        # (actual cost may vary based on date range and fields requested)
        self._enforce_pendle_rate_limit(cu_cost=5.0)

        # Convert dates to datetime objects for the API
        timestamp_start = datetime.combine(start_date, datetime.min.time()).replace(
            tzinfo=UTC
        )
        timestamp_end = datetime.combine(
            end_date, datetime.max.time()
        ).replace(tzinfo=UTC)

        try:
            # Request all available fields with fee breakdown
            fields = (
                "timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,"
                "underlyingInterestApy,underlyingRewardApy,ytFloatingApy,swapFeeApy,"
                "voterApr,pendleApy,lpRewardApy,totalPt,totalSy,totalSupply,ptPrice,"
                "ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume"
            )

            response = markets_controller_market_historical_data_v_2.sync(
                chain_id=float(chain_id),
                address=market_address,
                client=self._pendle_v2_client,
                time_frame=MarketsControllerMarketHistoricalDataV2TimeFrame.DAY,
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                fields=fields,
                include_fee_breakdown=True,
            )

            if response is None:
                raise APIError(
                    f"Failed to fetch historical data for market {market_address}"
                )

            # Handle empty results - API may return response without timestamp_start/end
            # when there are no data points
            if response.total == 0 or not response.results:
                # Return empty response with our requested date range
                return MarketHistoricalDataResponse(
                    total=0,
                    timestamp_start=timestamp_start,
                    timestamp_end=timestamp_end,
                    results=[],
                )

            return response
        except KeyError as e:
            # Handle empty API responses that are missing timestamp_start/timestamp_end
            # This happens when the API returns {"total": 0, "results": []}
            if "timestamp_start" in str(e) or "timestamp_end" in str(e):
                logger = logging.getLogger("pendle_yield.cache")
                logger.debug(
                    f"API returned empty result (missing {e}), "
                    f"returning empty response for {start_date} to {end_date}"
                )
                return MarketHistoricalDataResponse(
                    total=0,
                    timestamp_start=timestamp_start,
                    timestamp_end=timestamp_end,
                    results=[],
                )
            # Re-raise if it's a different KeyError
            raise APIError(
                f"Failed to fetch market historical data from API: {str(e)}"
            ) from e
        except Exception as e:
            raise APIError(
                f"Failed to fetch market historical data from API: {str(e)}"
            ) from e

    def _get_cached_historical_data(
        self, chain_id: int, market_address: str, target_date: date
    ) -> dict[str, Any] | None:
        """
        Retrieve cached historical data for a specific market and date.

        Args:
            chain_id: Chain ID (e.g., 1 for Ethereum mainnet)
            market_address: Market address (lowercase)
            target_date: Date to retrieve data for

        Returns:
            Dictionary containing the cached data, or None if not cached.
            Returns an empty dict {} for marker rows (dates that were fetched but had no data).
        """
        if not self._caching_enabled:
            return None

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Query for the specific date - select all data columns
            date_str = target_date.isoformat()
            cursor.execute(
                """
                SELECT
                    timestamp,
                    max_apy, base_apy, underlying_apy, implied_apy,
                    underlying_interest_apy, underlying_reward_apy, yt_floating_apy,
                    swap_fee_apy, voter_apr, pendle_apy, lp_reward_apy,
                    tvl, total_tvl, trading_volume,
                    pt_price, yt_price, sy_price, lp_price,
                    total_pt, total_sy, total_supply,
                    explicit_swap_fee, implicit_swap_fee, limit_order_fee,
                    last_epoch_votes
                FROM market_historical_data
                WHERE chain_id = ? AND market_address = ? AND date = ?
                """,
                (chain_id, market_address.lower(), date_str),
            )

            row = cursor.fetchone()
            if row is None:
                # No row found - this date was never fetched
                return None

            # Check if this is a marker row (all data fields are NULL)
            # Marker rows indicate the date was fetched but had no data
            timestamp = row[0]

            # Reconstruct the data dictionary from individual columns
            # Use the same camelCase keys as the API response
            data: dict[str, Any] = {}

            # Add timestamp if present
            if timestamp is not None:
                data["timestamp"] = timestamp

            # Map column indices to field names (camelCase for API compatibility)
            field_mapping = [
                (1, "maxApy"),
                (2, "baseApy"),
                (3, "underlyingApy"),
                (4, "impliedApy"),
                (5, "underlyingInterestApy"),
                (6, "underlyingRewardApy"),
                (7, "ytFloatingApy"),
                (8, "swapFeeApy"),
                (9, "voterApr"),
                (10, "pendleApy"),
                (11, "lpRewardApy"),
                (12, "tvl"),
                (13, "totalTvl"),
                (14, "tradingVolume"),
                (15, "ptPrice"),
                (16, "ytPrice"),
                (17, "syPrice"),
                (18, "lpPrice"),
                (19, "totalPt"),
                (20, "totalSy"),
                (21, "totalSupply"),
                (22, "explicitSwapFee"),
                (23, "implicitSwapFee"),
                (24, "limitOrderFee"),
                (25, "lastEpochVotes"),
            ]

            # Only include fields that are not None (matching API behavior)
            for idx, field_name in field_mapping:
                if row[idx] is not None:
                    data[field_name] = row[idx]

            # Return the data dict (may be empty {} for marker rows)
            return data
        finally:
            conn.close()

    def _store_historical_data(
        self,
        chain_id: int,
        market_address: str,
        target_date: date,
        data: dict[str, Any] | None,
    ) -> None:
        """
        Store historical data for a specific market and date in the cache.

        Args:
            chain_id: Chain ID (e.g., 1 for Ethereum mainnet)
            market_address: Market address (lowercase)
            target_date: Date of the data
            data: Dictionary containing the historical data to store, or None to store
                  a marker row indicating this date was fetched but had no data
        """
        if not self._caching_enabled:
            return

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Get current timestamp for cache metadata
            created_at = int(datetime.now(UTC).timestamp())
            date_str = target_date.isoformat()

            # Extract individual fields from data dictionary
            # Use .get() with None default for optional fields
            # If data is None (marker row for empty results), all fields will be None
            timestamp = data.get("timestamp") if data else None
            max_apy = data.get("maxApy") if data else None
            base_apy = data.get("baseApy") if data else None
            underlying_apy = data.get("underlyingApy") if data else None
            implied_apy = data.get("impliedApy") if data else None
            underlying_interest_apy = data.get("underlyingInterestApy") if data else None
            underlying_reward_apy = data.get("underlyingRewardApy") if data else None
            yt_floating_apy = data.get("ytFloatingApy") if data else None
            swap_fee_apy = data.get("swapFeeApy") if data else None
            voter_apr = data.get("voterApr") if data else None
            pendle_apy = data.get("pendleApy") if data else None
            lp_reward_apy = data.get("lpRewardApy") if data else None
            tvl = data.get("tvl") if data else None
            total_tvl = data.get("totalTvl") if data else None
            trading_volume = data.get("tradingVolume") if data else None
            pt_price = data.get("ptPrice") if data else None
            yt_price = data.get("ytPrice") if data else None
            sy_price = data.get("syPrice") if data else None
            lp_price = data.get("lpPrice") if data else None
            total_pt = data.get("totalPt") if data else None
            total_sy = data.get("totalSy") if data else None
            total_supply = data.get("totalSupply") if data else None
            explicit_swap_fee = data.get("explicitSwapFee") if data else None
            implicit_swap_fee = data.get("implicitSwapFee") if data else None
            limit_order_fee = data.get("limitOrderFee") if data else None
            last_epoch_votes = data.get("lastEpochVotes") if data else None

            # Use INSERT OR REPLACE to handle duplicates
            cursor.execute(
                """
                INSERT OR REPLACE INTO market_historical_data (
                    chain_id, market_address, date, timestamp,
                    max_apy, base_apy, underlying_apy, implied_apy,
                    underlying_interest_apy, underlying_reward_apy, yt_floating_apy,
                    swap_fee_apy, voter_apr, pendle_apy, lp_reward_apy,
                    tvl, total_tvl, trading_volume,
                    pt_price, yt_price, sy_price, lp_price,
                    total_pt, total_sy, total_supply,
                    explicit_swap_fee, implicit_swap_fee, limit_order_fee,
                    last_epoch_votes, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    chain_id,
                    market_address.lower(),
                    date_str,
                    timestamp,
                    max_apy,
                    base_apy,
                    underlying_apy,
                    implied_apy,
                    underlying_interest_apy,
                    underlying_reward_apy,
                    yt_floating_apy,
                    swap_fee_apy,
                    voter_apr,
                    pendle_apy,
                    lp_reward_apy,
                    tvl,
                    total_tvl,
                    trading_volume,
                    pt_price,
                    yt_price,
                    sy_price,
                    lp_price,
                    total_pt,
                    total_sy,
                    total_supply,
                    explicit_swap_fee,
                    implicit_swap_fee,
                    limit_order_fee,
                    last_epoch_votes,
                    created_at,
                ),
            )

            conn.commit()
        finally:
            conn.close()
