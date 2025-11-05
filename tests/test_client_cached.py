"""
Tests for the CachedPendleYieldClient.
"""

import sqlite3
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from pendle_yield import CachedPendleYieldClient, PendleEpoch
from pendle_yield.exceptions import ValidationError
from pendle_yield.models import EpochMarketFee


class TestCachedPendleYieldClient:
    """Test suite for CachedPendleYieldClient."""

    @pytest.fixture
    def temp_db_path(self) -> str:
        """Create a temporary database path for testing."""
        temp_dir = tempfile.mkdtemp()
        return str(Path(temp_dir) / "test_cache.db")

    @pytest.fixture
    def mock_client(self, temp_db_path: str) -> CachedPendleYieldClient:
        """Create a cached client with a mocked underlying client."""
        with patch("pendle_yield.client_cached.PendleYieldClient") as mock_client_class:
            mock_instance = MagicMock()
            mock_client_class.return_value = mock_instance

            client = CachedPendleYieldClient(
                etherscan_api_key="test_key", db_path=temp_db_path
            )

            # Store the mock instance for later access
            client._mock_instance = mock_instance

            return client

    def test_init_creates_database(self, temp_db_path: str) -> None:
        """Test that initialization creates the database file."""
        with patch("pendle_yield.client_cached.PendleYieldClient"):
            CachedPendleYieldClient(etherscan_api_key="test_key", db_path=temp_db_path)

        # Check that database file was created
        assert Path(temp_db_path).exists()

        # Verify table structure
        conn = sqlite3.connect(temp_db_path)
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='epoch_market_fees'
                """
            )
            result = cursor.fetchone()
            assert result is not None
            assert result[0] == "epoch_market_fees"
        finally:
            conn.close()

    def test_init_requires_db_path(self) -> None:
        """Test that initialization requires a database path."""
        with pytest.raises(ValidationError) as exc_info:
            with patch("pendle_yield.client_cached.PendleYieldClient"):
                CachedPendleYieldClient(etherscan_api_key="test_key", db_path="")

        assert "Database path is required" in str(exc_info.value)

    def test_cache_finished_epoch(self, mock_client: CachedPendleYieldClient) -> None:
        """Test that finished epochs are cached correctly."""
        # Create a past epoch (2 weeks ago)
        past_time = datetime.now() - timedelta(days=14)
        epoch = PendleEpoch(past_time)

        # Mock data to return
        mock_fees = [
            EpochMarketFee(
                chain_id=1,
                market_address="0x1234567890123456789012345678901234567890",
                total_fee=100.5,
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
            ),
            EpochMarketFee(
                chain_id=1,
                market_address="0xabcdefabcdefabcdefabcdefabcdefabcdefabcd",
                total_fee=200.75,
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
            ),
        ]

        mock_client._mock_instance.get_market_fees_by_epoch.return_value = mock_fees

        # First call - should fetch from API and cache
        result1 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result1) == 2
        assert result1[0].total_fee == 100.5
        assert result1[1].total_fee == 200.75
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 1

        # Second call - should return from cache without calling API
        result2 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result2) == 2
        assert result2[0].total_fee == 100.5
        assert result2[1].total_fee == 200.75
        # Call count should still be 1
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 1

    def test_no_cache_current_epoch(self, mock_client: CachedPendleYieldClient) -> None:
        """Test that current epochs are not cached and always fetch fresh data."""
        # Create current epoch
        current_time = datetime.now()
        epoch = PendleEpoch(current_time)

        # Mock data to return
        mock_fees = [
            EpochMarketFee(
                chain_id=1,
                market_address="0x1234567890123456789012345678901234567890",
                total_fee=100.5,
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
            ),
        ]

        mock_client._mock_instance.get_market_fees_by_epoch.return_value = mock_fees

        # First call
        result1 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result1) == 1
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 1

        # Second call - should call API again since it's current epoch
        result2 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result2) == 1
        # Call count should be 2 now
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 2

    def test_reject_future_epoch(self, mock_client: CachedPendleYieldClient) -> None:
        """Test that future epochs are rejected."""
        # Create future epoch (2 weeks from now)
        future_time = datetime.now() + timedelta(days=14)
        epoch = PendleEpoch(future_time)

        with pytest.raises(ValidationError) as exc_info:
            mock_client.get_market_fees_by_epoch(epoch)

        assert "Cannot get market fees for future epoch" in str(exc_info.value)

    def test_cache_empty_epoch(self, mock_client: CachedPendleYieldClient) -> None:
        """Test that empty epochs (no fees) are cached correctly."""
        # Create a past epoch
        past_time = datetime.now() - timedelta(days=14)
        epoch = PendleEpoch(past_time)

        # Mock empty data
        mock_client._mock_instance.get_market_fees_by_epoch.return_value = []

        # First call - should fetch from API and cache
        result1 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result1) == 0
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 1

        # Second call - should return from cache without calling API
        result2 = mock_client.get_market_fees_by_epoch(epoch)
        assert len(result2) == 0
        # Call count should still be 1
        assert mock_client._mock_instance.get_market_fees_by_epoch.call_count == 1

    def test_context_manager(self, temp_db_path: str) -> None:
        """Test that the client works as a context manager."""
        with patch("pendle_yield.client_cached.PendleYieldClient") as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance

            with CachedPendleYieldClient(
                etherscan_api_key="test_key", db_path=temp_db_path
            ) as client:
                assert client is not None

            # Verify close was called
            mock_instance.close.assert_called_once()

    def test_delegate_methods(self, mock_client: CachedPendleYieldClient) -> None:
        """Test that other methods are properly delegated to the underlying client."""
        # Test get_vote_events delegation
        mock_client.get_vote_events(1, 100)
        mock_client._mock_instance.get_vote_events.assert_called_once_with(1, 100)

        # Test get_votes delegation
        mock_client.get_votes(1, 100)
        mock_client._mock_instance.get_votes.assert_called_once_with(1, 100)

        # Test get_market_fees_for_period delegation
        mock_client.get_market_fees_for_period("2025-01-01", "2025-01-08")
        mock_client._mock_instance.get_market_fees_for_period.assert_called_once_with(
            "2025-01-01", "2025-01-08"
        )

    def test_cache_persistence(self, temp_db_path: str) -> None:
        """Test that cached data persists across client instances."""
        # Create a past epoch
        past_time = datetime.now() - timedelta(days=14)
        epoch = PendleEpoch(past_time)

        mock_fees = [
            EpochMarketFee(
                chain_id=1,
                market_address="0x1234567890123456789012345678901234567890",
                total_fee=100.5,
                epoch_start=epoch.start_datetime,
                epoch_end=epoch.end_datetime,
            ),
        ]

        # First client instance
        with patch("pendle_yield.client_cached.PendleYieldClient") as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance
            mock_instance.get_market_fees_by_epoch.return_value = mock_fees

            client1 = CachedPendleYieldClient(
                etherscan_api_key="test_key", db_path=temp_db_path
            )
            result1 = client1.get_market_fees_by_epoch(epoch)
            assert len(result1) == 1
            assert mock_instance.get_market_fees_by_epoch.call_count == 1
            client1.close()

        # Second client instance - should read from cache
        with patch("pendle_yield.client_cached.PendleYieldClient") as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance

            client2 = CachedPendleYieldClient(
                etherscan_api_key="test_key", db_path=temp_db_path
            )
            result2 = client2.get_market_fees_by_epoch(epoch)
            assert len(result2) == 1
            assert result2[0].total_fee == 100.5
            # Should not have called the API
            assert mock_instance.get_market_fees_by_epoch.call_count == 0
            client2.close()
