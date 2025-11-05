"""
Cached Etherscan API client using SQLite for persistent storage.

This module provides a caching layer for the EtherscanClient that stores
vote events in a SQLite database to avoid redundant API calls.
"""

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from .etherscan import EtherscanClient
from .exceptions import ValidationError
from .models import VoteEvent


class CachedEtherscanClient:
    """
    Cached wrapper around EtherscanClient that persists vote events in SQLite.

    This client provides the same interface as EtherscanClient but stores
    fetched vote events in a SQLite database. Subsequent requests for the
    same block ranges will be served from the cache, avoiding API calls.
    """

    def __init__(
        self,
        api_key: str,
        db_path: str,
        base_url: str = "https://api.etherscan.io/v2/api",
        timeout: float = 30.0,
        max_retries: int = 3,
        requests_per_second: float = 5.0,
    ) -> None:
        """
        Initialize the CachedEtherscanClient.

        Args:
            api_key: API key for Etherscan
            db_path: Path to SQLite database file (required)
            base_url: Base URL for Etherscan API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            requests_per_second: Maximum requests per second

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

        # Initialize the underlying Etherscan client
        self._client = EtherscanClient(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            requests_per_second=requests_per_second,
        )

        # Initialize database
        self._init_database()

    def _init_database(self) -> None:
        """
        Initialize the SQLite database with required tables and indices.

        Creates the vote_events table and scanned_blocks table.
        The scanned_blocks table tracks which blocks have been fetched,
        even if they had no events.

        Note: weight, bias, and slope are stored as TEXT because they can
        exceed SQLite's INTEGER maximum (2^63-1) for uint256 values.
        """
        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Create vote_events table
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS vote_events (
                    block_number INTEGER NOT NULL,
                    transaction_hash TEXT NOT NULL,
                    voter_address TEXT NOT NULL,
                    pool_address TEXT NOT NULL,
                    weight TEXT NOT NULL,
                    bias TEXT NOT NULL,
                    slope TEXT NOT NULL,
                    timestamp INTEGER,
                    PRIMARY KEY (block_number, transaction_hash, voter_address, pool_address)
                )
                """
            )

            # Create scanned_blocks table to track fetched blocks (even if empty)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS scanned_blocks (
                    block_number INTEGER PRIMARY KEY,
                    scanned_at INTEGER NOT NULL
                )
                """
            )

            # Create index on block_number for efficient range queries
            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_block_number
                ON vote_events(block_number)
                """
            )

            conn.commit()
        finally:
            conn.close()

    def _get_cached_events(self, from_block: int, to_block: int) -> list[VoteEvent]:
        """
        Retrieve cached vote events for the specified block range.

        Converts TEXT fields back to integers for weight, bias, and slope.

        Args:
            from_block: Starting block number
            to_block: Ending block number

        Returns:
            List of cached vote events
        """
        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT block_number, transaction_hash, voter_address, pool_address,
                       weight, bias, slope, timestamp
                FROM vote_events
                WHERE block_number >= ? AND block_number <= ?
                ORDER BY block_number, transaction_hash
                """,
                (from_block, to_block),
            )

            events = []
            for row in cursor.fetchall():
                # Convert Unix timestamp back to datetime
                timestamp = (
                    datetime.fromtimestamp(row[7]) if row[7] is not None else None
                )

                event = VoteEvent(
                    block_number=row[0],
                    transaction_hash=row[1],
                    voter_address=row[2],
                    pool_address=row[3],
                    weight=int(row[4]),  # Convert from TEXT to int
                    bias=int(row[5]),  # Convert from TEXT to int
                    slope=int(row[6]),  # Convert from TEXT to int
                    timestamp=timestamp,
                )
                events.append(event)

            return events
        finally:
            conn.close()

    def _get_cached_blocks(self, from_block: int, to_block: int) -> set[int]:
        """
        Get set of block numbers that have been scanned.

        This checks the scanned_blocks table to determine which blocks
        have been fetched from the API, regardless of whether they
        contained any events.

        Args:
            from_block: Starting block number
            to_block: Ending block number

        Returns:
            Set of block numbers that have been scanned
        """
        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT block_number
                FROM scanned_blocks
                WHERE block_number >= ? AND block_number <= ?
                """,
                (from_block, to_block),
            )

            return {row[0] for row in cursor.fetchall()}
        finally:
            conn.close()

    def _mark_blocks_as_scanned(self, from_block: int, to_block: int) -> None:
        """
        Mark a range of blocks as scanned in the database.

        This records that we've fetched data for these blocks from the API,
        even if no events were found.

        Args:
            from_block: Starting block number
            to_block: Ending block number
        """
        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Get current timestamp
            scanned_at = int(datetime.now().timestamp())

            # Prepare rows for all blocks in range
            rows = [(block, scanned_at) for block in range(from_block, to_block + 1)]

            # Use INSERT OR IGNORE to avoid errors if block already scanned
            cursor.executemany(
                """
                INSERT OR IGNORE INTO scanned_blocks (block_number, scanned_at)
                VALUES (?, ?)
                """,
                rows,
            )

            conn.commit()
        finally:
            conn.close()

    def _find_missing_ranges(
        self, from_block: int, to_block: int, cached_blocks: set[int]
    ) -> list[tuple[int, int]]:
        """
        Find continuous ranges of blocks that are missing from cache.

        Args:
            from_block: Starting block number
            to_block: Ending block number
            cached_blocks: Set of blocks that are already cached

        Returns:
            List of (start, end) tuples representing missing block ranges
        """
        missing_ranges: list[tuple[int, int]] = []
        range_start: int | None = None

        for block in range(from_block, to_block + 1):
            if block not in cached_blocks:
                if range_start is None:
                    range_start = block
            else:
                if range_start is not None:
                    missing_ranges.append((range_start, block - 1))
                    range_start = None

        # Handle case where missing range extends to end
        if range_start is not None:
            missing_ranges.append((range_start, to_block))

        return missing_ranges

    def _store_events(self, events: list[VoteEvent]) -> None:
        """
        Store vote events in the database.

        Uses INSERT OR IGNORE to avoid duplicate key errors.
        Converts large integers to strings to avoid SQLite INTEGER overflow.

        Args:
            events: List of vote events to store
        """
        if not events:
            return

        conn = sqlite3.connect(str(self.db_path))
        try:
            cursor = conn.cursor()

            # Prepare data for bulk insert
            rows = []
            for event in events:
                timestamp = (
                    int(event.timestamp.timestamp())
                    if event.timestamp is not None
                    else None
                )

                rows.append(
                    (
                        event.block_number,
                        event.transaction_hash,
                        event.voter_address,
                        event.pool_address,
                        str(event.weight),  # Convert to string to avoid overflow
                        str(event.bias),  # Convert to string to avoid overflow
                        str(event.slope),  # Convert to string to avoid overflow
                        timestamp,
                    )
                )

            # Use INSERT OR IGNORE to handle duplicates gracefully
            cursor.executemany(
                """
                INSERT OR IGNORE INTO vote_events
                (block_number, transaction_hash, voter_address, pool_address,
                 weight, bias, slope, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )

            conn.commit()
        finally:
            conn.close()

    def get_vote_events(
        self, from_block: int, to_block: int, max_pages: int | None = None
    ) -> list[VoteEvent]:
        """
        Fetch vote events for a specific block range, using cache when available.

        This method first checks the cache for existing events. For any missing
        block ranges, it fetches data from the Etherscan API and stores it in
        the cache for future use.

        Only caches blocks that are confirmed to be mined. Future blocks that
        haven't been mined yet will not be cached, as they might contain events
        once they are mined.

        Args:
            from_block: Starting block number
            to_block: Ending block number
            max_pages: Maximum number of pages to fetch per block batch (None for unlimited)

        Returns:
            List of vote events, combining cached and newly fetched data

        Raises:
            ValidationError: If block numbers are invalid
            APIError: If the API request fails
        """
        # Get cached blocks in the requested range
        cached_blocks = self._get_cached_blocks(from_block, to_block)

        # Find missing block ranges
        missing_ranges = self._find_missing_ranges(from_block, to_block, cached_blocks)

        # Fetch missing data from API
        for range_start, range_end in missing_ranges:
            events = self._client.get_vote_events(range_start, range_end, max_pages)

            # Store newly fetched events in cache
            self._store_events(events)

            # Only cache blocks that are confirmed to exist
            # Get the latest block number to avoid caching future blocks
            latest_block = self._get_latest_block_number()

            # Only mark blocks as scanned if they're not in the future
            cacheable_end = min(range_end, latest_block)
            if range_start <= cacheable_end:
                self._mark_blocks_as_scanned(range_start, cacheable_end)

        # Get all cached events (including newly stored ones)
        all_events = self._get_cached_events(from_block, to_block)

        return all_events

    def _get_latest_block_number(self) -> int:
        """
        Get the latest block number from the blockchain.

        Uses the current timestamp to fetch the latest confirmed block.

        Returns:
            Latest block number

        Raises:
            APIError: If the API request fails
        """
        # Get current timestamp
        current_timestamp = int(datetime.now().timestamp())

        # Get the block number for current timestamp
        # Using "before" to ensure we get a confirmed block
        latest_block = self._client.get_block_number_by_timestamp(
            current_timestamp, "before"
        )

        return latest_block

    def __enter__(self) -> "CachedEtherscanClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def get_block_number_by_timestamp(
        self, timestamp: int, closest: str = "before"
    ) -> int:
        """
        Get block number by timestamp using Etherscan API.

        Delegates to the underlying EtherscanClient.

        Args:
            timestamp: Unix timestamp to find the block for
            closest: Direction to search - "before" or "after" the timestamp

        Returns:
            Block number as integer

        Raises:
            ValidationError: If timestamp or closest parameter is invalid
            APIError: If the API request fails
        """
        return self._client.get_block_number_by_timestamp(timestamp, closest)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()
