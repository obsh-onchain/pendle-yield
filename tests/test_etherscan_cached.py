"""
Unit tests for the CachedEtherscanClient class.
"""

import sqlite3
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from pendle_yield.etherscan_cached import CachedEtherscanClient
from pendle_yield.exceptions import ValidationError
from pendle_yield.models import VoteEvent


class TestCachedEtherscanClient:
    """Test cases for CachedEtherscanClient."""

    @pytest.fixture
    def temp_db(self):
        """Create a temporary database file."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            db_path = f.name
        yield db_path
        # Cleanup
        Path(db_path).unlink(missing_ok=True)

    @pytest.fixture
    def mock_vote_event(self):
        """Create a mock vote event."""
        return VoteEvent(
            block_number=12345,
            transaction_hash="0xabc123",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            weight=2000,
            bias=1000,
            slope=500,
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
        )

    @pytest.fixture
    def client(self, temp_db):
        """Create a test client instance."""
        return CachedEtherscanClient(api_key="test_key", db_path=temp_db)

    def test_init_valid_db_path(self, temp_db):
        """Test client initialization with valid database path."""
        client = CachedEtherscanClient(api_key="test_key", db_path=temp_db)
        assert client.db_path == Path(temp_db)
        assert client.db_path.exists()

    def test_init_empty_db_path(self):
        """Test client initialization with empty database path raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            CachedEtherscanClient(api_key="test_key", db_path="")

        assert "Database path is required" in str(exc_info.value)
        assert exc_info.value.field == "db_path"

    def test_init_creates_parent_directory(self):
        """Test that client creates parent directory if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "subdir" / "cache.db"
            client = CachedEtherscanClient(api_key="test_key", db_path=str(db_path))
            assert db_path.parent.exists()
            assert db_path.exists()
            client.close()

    def test_database_initialization(self, temp_db):
        """Test that database tables and indices are created."""
        client = CachedEtherscanClient(api_key="test_key", db_path=temp_db)

        conn = sqlite3.connect(temp_db)
        try:
            cursor = conn.cursor()

            # Check that vote_events table exists
            cursor.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='vote_events'
                """
            )
            assert cursor.fetchone() is not None

            # Check that scanned_blocks table exists
            cursor.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='scanned_blocks'
                """
            )
            assert cursor.fetchone() is not None

            # Check that index exists
            cursor.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type='index' AND name='idx_block_number'
                """
            )
            assert cursor.fetchone() is not None
        finally:
            conn.close()
            client.close()

    def test_context_manager(self, temp_db):
        """Test client as context manager."""
        with CachedEtherscanClient(api_key="test_key", db_path=temp_db) as client:
            assert isinstance(client, CachedEtherscanClient)
        # Client should be closed after context exit

    def test_store_and_retrieve_events(self, client, mock_vote_event):
        """Test storing and retrieving events from cache."""
        # Store event
        client._store_events([mock_vote_event])

        # Retrieve event
        events = client._get_cached_events(12345, 12345)

        assert len(events) == 1
        event = events[0]
        assert event.block_number == mock_vote_event.block_number
        assert event.transaction_hash == mock_vote_event.transaction_hash
        assert event.voter_address == mock_vote_event.voter_address
        assert event.pool_address == mock_vote_event.pool_address
        assert event.weight == mock_vote_event.weight
        assert event.bias == mock_vote_event.bias
        assert event.slope == mock_vote_event.slope
        assert event.timestamp == mock_vote_event.timestamp

    def test_store_duplicate_events(self, client, mock_vote_event):
        """Test that storing duplicate events doesn't cause errors."""
        # Store same event twice
        client._store_events([mock_vote_event])
        client._store_events([mock_vote_event])

        # Should only have one event
        events = client._get_cached_events(12345, 12345)
        assert len(events) == 1

    def test_store_events_with_null_timestamp(self, client):
        """Test storing events with null timestamp."""
        event = VoteEvent(
            block_number=12345,
            transaction_hash="0xabc123",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            weight=2000,
            bias=1000,
            slope=500,
            timestamp=None,
        )

        client._store_events([event])
        events = client._get_cached_events(12345, 12345)

        assert len(events) == 1
        assert events[0].timestamp is None

    def test_get_cached_blocks(self, client):
        """Test getting set of scanned block numbers."""
        # Mark blocks as scanned
        client._mark_blocks_as_scanned(100, 100)
        client._mark_blocks_as_scanned(101, 101)
        client._mark_blocks_as_scanned(103, 103)

        # Get cached blocks in range 100-105
        cached_blocks = client._get_cached_blocks(100, 105)

        assert cached_blocks == {100, 101, 103}

    def test_mark_blocks_as_scanned(self, client):
        """Test marking blocks as scanned."""
        # Mark a range of blocks as scanned
        client._mark_blocks_as_scanned(100, 105)

        # Verify all blocks in range are marked
        cached_blocks = client._get_cached_blocks(100, 105)
        assert cached_blocks == {100, 101, 102, 103, 104, 105}

        # Mark duplicate - should not cause error
        client._mark_blocks_as_scanned(103, 107)

        # Verify extended range
        cached_blocks = client._get_cached_blocks(100, 107)
        assert cached_blocks == {100, 101, 102, 103, 104, 105, 106, 107}

    def test_get_vote_events_marks_empty_blocks_as_scanned(self, client):
        """Test that blocks without events are still marked as scanned."""
        # Mock API to return no events and mock latest block
        with (
            patch.object(client._client, "get_vote_events", return_value=[]),
            patch.object(client, "_get_latest_block_number", return_value=1000),
        ):
            # Fetch events for a range
            events = client.get_vote_events(100, 105)

            # Should return empty list
            assert len(events) == 0

            # But blocks should be marked as scanned
            cached_blocks = client._get_cached_blocks(100, 105)
            assert cached_blocks == {100, 101, 102, 103, 104, 105}

        # Second call should not make API request
        with (
            patch.object(client._client, "get_vote_events") as mock_get,
            patch.object(client, "_get_latest_block_number", return_value=1000),
        ):
            events = client.get_vote_events(100, 105)

            # Should NOT call API
            mock_get.assert_not_called()
            assert len(events) == 0

    def test_find_missing_ranges_no_gaps(self, client):
        """Test finding missing ranges when there are no gaps."""
        cached_blocks = {100, 101, 102, 103, 104, 105}
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == []

    def test_find_missing_ranges_all_missing(self, client):
        """Test finding missing ranges when all blocks are missing."""
        cached_blocks = set()
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == [(100, 105)]

    def test_find_missing_ranges_single_gap(self, client):
        """Test finding missing ranges with a single gap."""
        cached_blocks = {100, 101, 105}
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == [(102, 104)]

    def test_find_missing_ranges_multiple_gaps(self, client):
        """Test finding missing ranges with multiple gaps."""
        cached_blocks = {100, 101, 104, 105}
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == [(102, 103)]

    def test_find_missing_ranges_gap_at_start(self, client):
        """Test finding missing ranges with gap at start."""
        cached_blocks = {103, 104, 105}
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == [(100, 102)]

    def test_find_missing_ranges_gap_at_end(self, client):
        """Test finding missing ranges with gap at end."""
        cached_blocks = {100, 101, 102}
        missing = client._find_missing_ranges(100, 105, cached_blocks)

        assert missing == [(103, 105)]

    def test_find_missing_ranges_complex(self, client):
        """Test finding missing ranges with complex pattern."""
        cached_blocks = {100, 102, 105, 107}
        missing = client._find_missing_ranges(100, 110, cached_blocks)

        assert missing == [(101, 101), (103, 104), (106, 106), (108, 110)]

    def test_get_vote_events_cache_miss(self, client):
        """Test fetching vote events when cache is empty."""
        mock_events = [
            VoteEvent(
                block_number=12345,
                transaction_hash="0xabc1",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=2000,
                bias=1000,
                slope=500,
            )
        ]

        with (
            patch.object(client._client, "get_vote_events", return_value=mock_events) as mock_get,
            patch.object(client, "_get_latest_block_number", return_value=50000),
        ):
            events = client.get_vote_events(12345, 12345)

            # Should call underlying client
            mock_get.assert_called_once_with(12345, 12345, None)

            # Should return the events
            assert len(events) == 1
            assert events[0].block_number == 12345

            # Events should now be cached
            cached_blocks = client._get_cached_blocks(12345, 12345)
            assert 12345 in cached_blocks

    def test_get_vote_events_cache_hit(self, client, mock_vote_event):
        """Test fetching vote events when all data is cached."""
        # Pre-populate cache
        client._store_events([mock_vote_event])
        client._mark_blocks_as_scanned(12345, 12345)

        with patch.object(client._client, "get_vote_events") as mock_get:
            events = client.get_vote_events(12345, 12345)

            # Should NOT call underlying client
            mock_get.assert_not_called()

            # Should return cached event
            assert len(events) == 1
            assert events[0].block_number == 12345

    def test_get_vote_events_partial_cache(self, client):
        """Test fetching vote events with partial cache coverage."""
        # Pre-populate cache with events for blocks 100-102
        cached_events = [
            VoteEvent(
                block_number=100,
                transaction_hash="0xabc1",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=101,
                transaction_hash="0xabc2",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=102,
                transaction_hash="0xabc3",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
        ]
        client._store_events(cached_events)
        client._mark_blocks_as_scanned(100, 102)

        # Mock API to return events for blocks 103-105
        new_events = [
            VoteEvent(
                block_number=103,
                transaction_hash="0xabc4",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=104,
                transaction_hash="0xabc5",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=105,
                transaction_hash="0xabc6",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
        ]

        with (
            patch.object(client._client, "get_vote_events", return_value=new_events) as mock_get,
            patch.object(client, "_get_latest_block_number", return_value=50000),
        ):
            events = client.get_vote_events(100, 105)

            # Should only fetch missing range
            mock_get.assert_called_once_with(103, 105, None)

            # Should return all events
            assert len(events) == 6
            assert {e.block_number for e in events} == {100, 101, 102, 103, 104, 105}

    def test_get_vote_events_multiple_gaps(self, client):
        """Test fetching vote events with multiple gaps in cache."""
        # Pre-populate cache with blocks 100, 102, 104
        cached_events = [
            VoteEvent(
                block_number=100,
                transaction_hash="0xabc1",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=102,
                transaction_hash="0xabc2",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=104,
                transaction_hash="0xabc3",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
        ]
        client._store_events(cached_events)
        # Mark these blocks as scanned
        client._mark_blocks_as_scanned(100, 100)
        client._mark_blocks_as_scanned(102, 102)
        client._mark_blocks_as_scanned(104, 104)

        # Mock API to return events for missing blocks
        gap1_events = [
            VoteEvent(
                block_number=101,
                transaction_hash="0xabc4",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            )
        ]
        gap2_events = [
            VoteEvent(
                block_number=103,
                transaction_hash="0xabc5",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            )
        ]

        with (
            patch.object(client._client, "get_vote_events", side_effect=[gap1_events, gap2_events]) as mock_get,
            patch.object(client, "_get_latest_block_number", return_value=50000),
        ):
            events = client.get_vote_events(100, 104)

            # Should fetch both gaps
            assert mock_get.call_count == 2
            mock_get.assert_any_call(101, 101, None)
            mock_get.assert_any_call(103, 103, None)

            # Should return all events
            assert len(events) == 5
            assert {e.block_number for e in events} == {100, 101, 102, 103, 104}

    def test_get_vote_events_with_max_pages(self, client):
        """Test that max_pages parameter is passed through to underlying client."""
        mock_events = [
            VoteEvent(
                block_number=12345,
                transaction_hash="0xabc1",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=2000,
                bias=1000,
                slope=500,
            )
        ]

        with (
            patch.object(client._client, "get_vote_events", return_value=mock_events) as mock_get,
            patch.object(client, "_get_latest_block_number", return_value=50000),
        ):
            client.get_vote_events(12345, 12345, max_pages=5)

            # Should pass max_pages to underlying client
            mock_get.assert_called_once_with(12345, 12345, 5)

    def test_get_vote_events_invalid_blocks(self, client):
        """Test that invalid block numbers are handled by underlying client."""
        with patch.object(
            client._client, "get_vote_events", side_effect=ValidationError("Invalid")
        ):
            with pytest.raises(ValidationError):
                client.get_vote_events(-1, 1000)

    def test_database_persistence(self, temp_db):
        """Test that database persists across client instances."""
        # Create first client and store data
        client1 = CachedEtherscanClient(api_key="test_key", db_path=temp_db)
        event = VoteEvent(
            block_number=12345,
            transaction_hash="0xabc123",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            weight=2000,
            bias=1000,
            slope=500,
        )
        client1._store_events([event])
        client1.close()

        # Create second client and verify data is still there
        client2 = CachedEtherscanClient(api_key="test_key", db_path=temp_db)
        events = client2._get_cached_events(12345, 12345)
        assert len(events) == 1
        assert events[0].block_number == 12345
        client2.close()

    def test_store_empty_event_list(self, client):
        """Test that storing empty event list doesn't cause errors."""
        client._store_events([])

        # Should not raise any errors
        events = client._get_cached_events(100, 200)
        assert len(events) == 0

    def test_get_cached_events_empty_range(self, client):
        """Test getting cached events when range has no data."""
        events = client._get_cached_events(1000, 2000)
        assert len(events) == 0

    def test_get_cached_events_ordering(self, client):
        """Test that cached events are returned in correct order."""
        events = [
            VoteEvent(
                block_number=103,
                transaction_hash="0xabc3",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=101,
                transaction_hash="0xabc1",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
            VoteEvent(
                block_number=102,
                transaction_hash="0xabc2",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                weight=1000,
                bias=500,
                slope=250,
            ),
        ]
        client._store_events(events)

        # Retrieve events
        retrieved = client._get_cached_events(101, 103)

        # Should be ordered by block_number
        assert len(retrieved) == 3
        assert retrieved[0].block_number == 101
        assert retrieved[1].block_number == 102
        assert retrieved[2].block_number == 103

    def test_close_method(self, client):
        """Test that close method closes underlying client."""
        with patch.object(client._client, "close") as mock_close:
            client.close()
            mock_close.assert_called_once()

    def test_store_large_uint256_values(self, client):
        """Test storing and retrieving events with large uint256 values."""
        # Create event with very large values that exceed SQLite INTEGER max (2^63-1)
        large_value = 2**200  # Much larger than SQLite INTEGER can handle
        event = VoteEvent(
            block_number=12345,
            transaction_hash="0xabc123",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            weight=large_value,
            bias=large_value + 1,
            slope=large_value + 2,
            timestamp=datetime(2024, 1, 1, 12, 0, 0),
        )

        # Store event
        client._store_events([event])

        # Retrieve event
        events = client._get_cached_events(12345, 12345)

        assert len(events) == 1
        retrieved_event = events[0]
        assert retrieved_event.weight == large_value
        assert retrieved_event.bias == large_value + 1
        assert retrieved_event.slope == large_value + 2

    def test_future_blocks_not_cached(self, client):
        """Test that future blocks (beyond latest block) are not cached."""
        # Mock get_block_number_by_timestamp to return a specific "latest" block
        latest_block = 1000

        with (
            patch.object(
                client, "_get_latest_block_number", return_value=latest_block
            ),
            patch.object(client._client, "get_vote_events", return_value=[]),
        ):
            # Request blocks that extend into the future
            client.get_vote_events(900, 1100)

            # Only blocks up to latest_block should be cached
            cached_blocks = client._get_cached_blocks(900, 1100)

            # Blocks 900-1000 should be cached (confirmed blocks)
            assert all(block in cached_blocks for block in range(900, 1001))

            # Blocks 1001-1100 should NOT be cached (future blocks)
            assert all(block not in cached_blocks for block in range(1001, 1101))

    def test_all_future_blocks_not_cached(self, client):
        """Test that requesting only future blocks doesn't cache anything."""
        # Mock get_block_number_by_timestamp to return a specific "latest" block
        latest_block = 1000

        with (
            patch.object(
                client, "_get_latest_block_number", return_value=latest_block
            ),
            patch.object(client._client, "get_vote_events", return_value=[]),
        ):
            # Request only future blocks
            client.get_vote_events(1100, 1200)

            # No blocks should be cached
            cached_blocks = client._get_cached_blocks(1100, 1200)
            assert len(cached_blocks) == 0

    def test_exact_latest_block_is_cached(self, client):
        """Test that the exact latest block is cached."""
        # Mock get_block_number_by_timestamp to return a specific "latest" block
        latest_block = 1000

        with (
            patch.object(
                client, "_get_latest_block_number", return_value=latest_block
            ),
            patch.object(client._client, "get_vote_events", return_value=[]),
        ):
            # Request blocks up to and including the latest block
            client.get_vote_events(1000, 1000)

            # The latest block should be cached
            cached_blocks = client._get_cached_blocks(1000, 1000)
            assert 1000 in cached_blocks
