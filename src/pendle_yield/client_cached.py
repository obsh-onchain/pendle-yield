"""
Cached Pendle Yield client using SQLite for persistent storage.

This module provides a caching layer for the PendleYieldClient that stores
market fees in a SQLite database to avoid redundant API calls.
"""

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from .client import PendleYieldClient
from .epoch import PendleEpoch
from .exceptions import ValidationError
from .models import EpochMarketFee


class CachedPendleYieldClient:
    """
    Cached wrapper around PendleYieldClient that persists market fees in SQLite.

    This client provides the same interface as PendleYieldClient but stores
    fetched market fees in a SQLite database. Finished epochs are cached permanently
    since their data is immutable, while current epochs are always fetched fresh.
    """

    def __init__(
        self,
        etherscan_api_key: str,
        db_path: str,
        etherscan_base_url: str = "https://api.etherscan.io/v2/api",
        pendle_base_url: str = "https://api-v2.pendle.finance/core",
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the CachedPendleYieldClient.

        Args:
            etherscan_api_key: API key for Etherscan
            db_path: Path to SQLite database file (required)
            etherscan_base_url: Base URL for Etherscan API
            pendle_base_url: Base URL for Pendle API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests

        Raises:
            ValidationError: If db_path is not provided or invalid
        """
        if not db_path:
            raise ValidationError(
                "Database path is required", field="db_path", value=db_path
            )

        self.db_path = Path(db_path)

        # Create parent directory if it doesn't exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Initialize the underlying Pendle Yield client
        self._client = PendleYieldClient(
            etherscan_api_key=etherscan_api_key,
            etherscan_base_url=etherscan_base_url,
            pendle_base_url=pendle_base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

        # Initialize database
        self._init_database()

    def _init_database(self) -> None:
        """
        Initialize the SQLite database with required tables and indices.

        Creates the epoch_market_fees table to store market fee data for epochs.
        """
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

            conn.commit()
        finally:
            conn.close()

    def _get_cached_epoch_fees(self, epoch: PendleEpoch) -> list[EpochMarketFee] | None:
        """
        Retrieve cached market fees for a specific epoch.

        Args:
            epoch: PendleEpoch object

        Returns:
            List of cached EpochMarketFee objects, or None if not cached
        """
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

        Uses INSERT OR REPLACE to update existing entries.

        Args:
            epoch: PendleEpoch object
            epoch_fees: List of EpochMarketFee objects to store
        """
        if not epoch_fees:
            # Still store an empty marker to indicate this epoch was fetched
            # This prevents repeated API calls for epochs with no fees
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

    def get_market_fees_by_epoch(self, epoch: PendleEpoch) -> list[EpochMarketFee]:
        """
        Get market fees for a specific Pendle epoch, using cache when available.

        This method checks if the epoch is finished (immutable). If so, it attempts
        to retrieve the data from cache. If not cached or if the epoch is current,
        it fetches fresh data from the API.

        Finished epochs are cached permanently since their fee data is immutable.
        Current epochs are always fetched fresh since the data may change.

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

        # Check if this is a finished epoch (immutable data)
        if epoch.is_past:
            # Try to get from cache first
            cached_fees = self._get_cached_epoch_fees(epoch)
            if cached_fees is not None:
                # Filter out the marker row if present
                return [
                    fee
                    for fee in cached_fees
                    if fee.market_address
                    != "0x0000000000000000000000000000000000000000"
                ]

        # Either current epoch or cache miss - fetch from API
        epoch_fees = self._client.get_market_fees_by_epoch(epoch)

        # Only cache if this is a finished epoch
        if epoch.is_past:
            self._store_epoch_fees(epoch, epoch_fees)

        return epoch_fees

    def __enter__(self) -> "CachedPendleYieldClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the underlying HTTP clients."""
        self._client.close()

    # Delegate other methods to the underlying client
    def get_vote_events(self, from_block: int, to_block: int) -> Any:
        """Delegate to underlying client."""
        return self._client.get_vote_events(from_block, to_block)

    def get_votes(self, from_block: int, to_block: int) -> Any:
        """Delegate to underlying client."""
        return self._client.get_votes(from_block, to_block)

    def get_votes_by_epoch(self, epoch: PendleEpoch) -> Any:
        """Delegate to underlying client."""
        return self._client.get_votes_by_epoch(epoch)

    def get_market_fees_for_period(
        self, timestamp_start: str, timestamp_end: str
    ) -> Any:
        """Delegate to underlying client."""
        return self._client.get_market_fees_for_period(timestamp_start, timestamp_end)
