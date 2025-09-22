"""
Tests for the PendleEpoch class.

This module contains unit tests for the epoch management functionality,
including epoch boundary calculations, input validation, and integration
with Etherscan block lookups.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock

import pytest

from pendle_yield.epoch import PendleEpoch
from pendle_yield.exceptions import ValidationError


class TestPendleEpoch:
    """Test cases for the PendleEpoch class."""

    def test_init_with_none_uses_current_time(self):
        """Test that initializing with None uses current time."""
        epoch = PendleEpoch(None)

        # Should have valid start and end times
        assert epoch.start_datetime is not None
        assert epoch.end_datetime is not None
        assert epoch.end_datetime > epoch.start_datetime

        # Should be exactly 7 days apart
        assert epoch.end_datetime - epoch.start_datetime == timedelta(days=7)

    def test_init_with_datetime(self):
        """Test initialization with datetime object."""
        # Test with a specific Thursday
        test_time = datetime(2024, 1, 18, 12, 0, 0, tzinfo=UTC)  # Thursday
        epoch = PendleEpoch(test_time)

        # Should start at Thursday 00:00 UTC
        expected_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        assert epoch.start_datetime == expected_start
        assert epoch.end_datetime == expected_start + timedelta(days=7)

    def test_init_with_naive_datetime(self):
        """Test initialization with naive datetime (no timezone)."""
        # Test with naive datetime - should be treated as UTC
        test_time = datetime(2024, 1, 18, 12, 0, 0)  # Thursday, no timezone
        epoch = PendleEpoch(test_time)

        expected_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        assert epoch.start_datetime == expected_start

    def test_init_with_timestamp(self):
        """Test initialization with Unix timestamp."""
        # Thursday, January 18, 2024 12:00:00 UTC
        timestamp = 1705579200
        epoch = PendleEpoch(timestamp)

        expected_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        assert epoch.start_datetime == expected_start

    def test_init_with_iso_string(self):
        """Test initialization with ISO format string."""
        # Test various ISO formats
        test_cases = [
            "2024-01-18T12:00:00Z",
            "2024-01-18T12:00:00+00:00",
            "2024-01-18T12:00:00",
        ]

        expected_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)

        for iso_string in test_cases:
            epoch = PendleEpoch(iso_string)
            assert epoch.start_datetime == expected_start

    def test_init_with_invalid_timestamp(self):
        """Test initialization with invalid timestamp raises ValidationError."""
        # Use a timestamp that's actually invalid (too large)
        with pytest.raises(ValidationError) as exc_info:
            PendleEpoch(999999999999999)  # Year 33658, way beyond valid range

        assert "Invalid timestamp" in str(exc_info.value)
        assert exc_info.value.field == "time_input"

    def test_init_with_invalid_string(self):
        """Test initialization with invalid string raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PendleEpoch("not-a-date")

        assert "Invalid datetime string format" in str(exc_info.value)
        assert exc_info.value.field == "time_input"

    def test_init_with_invalid_type(self):
        """Test initialization with invalid type raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PendleEpoch([1, 2, 3])  # type: ignore

        assert "Unsupported time input type" in str(exc_info.value)

    def test_epoch_boundaries_for_different_weekdays(self):
        """Test epoch boundary calculation for different days of the week."""
        # Test cases: (input_date, expected_epoch_start)
        test_cases = [
            # Monday -> previous Thursday
            (
                datetime(2024, 1, 15, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 11, 0, 0, tzinfo=UTC),
            ),
            # Tuesday -> previous Thursday
            (
                datetime(2024, 1, 16, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 11, 0, 0, tzinfo=UTC),
            ),
            # Wednesday -> previous Thursday
            (
                datetime(2024, 1, 17, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 11, 0, 0, tzinfo=UTC),
            ),
            # Thursday -> same Thursday
            (
                datetime(2024, 1, 18, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 18, 0, 0, tzinfo=UTC),
            ),
            # Friday -> same Thursday
            (
                datetime(2024, 1, 19, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 18, 0, 0, tzinfo=UTC),
            ),
            # Saturday -> same Thursday
            (
                datetime(2024, 1, 20, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 18, 0, 0, tzinfo=UTC),
            ),
            # Sunday -> same Thursday
            (
                datetime(2024, 1, 21, 12, 0, tzinfo=UTC),
                datetime(2024, 1, 18, 0, 0, tzinfo=UTC),
            ),
        ]

        for input_date, expected_start in test_cases:
            epoch = PendleEpoch(input_date)
            assert epoch.start_datetime == expected_start, (
                f"Failed for {input_date.strftime('%A')}"
            )
            assert epoch.end_datetime == expected_start + timedelta(days=7)

    def test_properties(self):
        """Test epoch properties return correct values."""
        test_time = datetime(2024, 1, 18, 12, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(test_time)

        expected_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        expected_end = expected_start + timedelta(days=7)

        # Test datetime properties
        assert epoch.start_datetime == expected_start
        assert epoch.end_datetime == expected_end

    def test_status_properties_past_epoch(self):
        """Test status properties for a past epoch."""
        # Create an epoch from 2023 (definitely in the past)
        past_time = datetime(2023, 1, 18, 12, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(past_time)

        assert epoch.is_past is True
        assert epoch.is_current is False
        assert epoch.is_future is False

    def test_status_properties_future_epoch(self):
        """Test status properties for a future epoch."""
        # Create an epoch far in the future
        future_time = datetime.now(UTC) + timedelta(days=365)  # One year from now
        epoch = PendleEpoch(future_time)

        assert epoch.is_past is False
        assert epoch.is_current is False
        assert epoch.is_future is True

    def test_status_properties_current_epoch(self):
        """Test status properties for the current epoch."""
        # Create epoch for current time
        current_epoch = PendleEpoch()

        # At least one of these should be true, and they should be mutually exclusive
        status_count = sum([current_epoch.is_past, current_epoch.is_current, current_epoch.is_future])
        assert status_count == 1, "Exactly one status should be true"

        # If we're in the current epoch, verify the logic
        if current_epoch.is_current:
            now = datetime.now(UTC)
            assert current_epoch.start_datetime <= now < current_epoch.end_datetime

    def test_get_block_range_future_epoch_raises_error(self):
        """Test that get_block_range raises ValidationError for future epochs."""
        # Create a future epoch
        future_time = datetime.now(UTC) + timedelta(days=365)
        future_epoch = PendleEpoch(future_time)

        # Mock client (shouldn't be called)
        mock_client = Mock()

        with pytest.raises(ValidationError) as exc_info:
            future_epoch.get_block_range(mock_client)

        assert "Cannot get block range for future epoch" in str(exc_info.value)
        assert exc_info.value.field == "epoch_status"
        assert exc_info.value.value == "future"

        # Verify no API calls were made
        assert mock_client.get_block_number_by_timestamp.call_count == 0

    def test_get_block_range_past_epoch(self):
        """Test get_block_range for past epochs (existing behavior)."""
        # Create a past epoch
        past_time = datetime(2023, 1, 18, 12, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(past_time)

        # Mock client
        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.side_effect = [19000000, 19010000]

        start_block, end_block = epoch.get_block_range(mock_client)

        assert start_block == 19000000
        assert end_block == 19010000

        # Verify both API calls were made
        assert mock_client.get_block_number_by_timestamp.call_count == 2

    def test_get_block_range_current_epoch_default(self):
        """Test get_block_range for current epoch with default behavior."""
        # Create current epoch
        current_epoch = PendleEpoch()

        # Skip test if not actually current
        if not current_epoch.is_current:
            pytest.skip("Test requires current epoch")

        # Mock client
        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.return_value = 19000000

        start_block, end_block = current_epoch.get_block_range(mock_client)

        assert start_block == 19000000
        assert end_block is None

        # Verify only start block API call was made
        assert mock_client.get_block_number_by_timestamp.call_count == 1

    def test_get_block_range_current_epoch_with_latest(self):
        """Test get_block_range for current epoch with use_latest_for_current=True."""
        # Create current epoch
        current_epoch = PendleEpoch()

        # Skip test if not actually current
        if not current_epoch.is_current:
            pytest.skip("Test requires current epoch")

        # Mock client
        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.side_effect = [19000000, 19020000]

        start_block, end_block = current_epoch.get_block_range(
            mock_client, use_latest_for_current=True
        )

        assert start_block == 19000000
        assert end_block == 19020000

        # Verify both API calls were made
        assert mock_client.get_block_number_by_timestamp.call_count == 2

    def test_get_block_range_use_latest_for_current_parameter(self):
        """Test the use_latest_for_current parameter with different epoch types."""
        # Test with past epoch - parameter should be ignored
        past_time = datetime(2023, 1, 18, 12, 0, 0, tzinfo=UTC)
        past_epoch = PendleEpoch(past_time)

        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.side_effect = [19000000, 19010000]

        start_block, end_block = past_epoch.get_block_range(
            mock_client, use_latest_for_current=True
        )

        assert start_block == 19000000
        assert end_block == 19010000

        # Should not call get_latest_block_number for past epochs
        assert mock_client.get_latest_block_number.call_count == 0

    def test_status_properties_are_mutually_exclusive(self):
        """Test that status properties are mutually exclusive."""
        test_times = [
            datetime(2023, 1, 18, tzinfo=UTC),  # Past
            datetime.now(UTC),  # Current
            datetime.now(UTC) + timedelta(days=365),  # Future
        ]

        for test_time in test_times:
            epoch = PendleEpoch(test_time)
            status_count = sum([epoch.is_past, epoch.is_current, epoch.is_future])
            assert status_count == 1, f"Exactly one status should be true for {test_time}"

    def test_get_block_range_return_type_annotation(self):
        """Test that get_block_range returns the correct types."""
        # Test with past epoch
        past_time = datetime(2023, 1, 18, 12, 0, 0, tzinfo=UTC)
        past_epoch = PendleEpoch(past_time)

        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.side_effect = [19000000, 19010000]

        start_block, end_block = past_epoch.get_block_range(mock_client)

        assert isinstance(start_block, int)
        assert isinstance(end_block, int)

        # Test with current epoch (if available)
        current_epoch = PendleEpoch()
        if current_epoch.is_current:
            # Create a new mock client for current epoch tests
            current_mock_client = Mock()
            current_mock_client.get_block_number_by_timestamp.return_value = 19000000

            start_block, end_block = current_epoch.get_block_range(current_mock_client)

            assert isinstance(start_block, int)
            assert end_block is None

            # Test with use_latest_for_current=True
            current_mock_client.get_latest_block_number.return_value = 19020000

            start_block, end_block = current_epoch.get_block_range(
                current_mock_client, use_latest_for_current=True
            )

            assert isinstance(start_block, int)
            assert isinstance(end_block, int)

    def test_contains_method(self):
        """Test the contains method with various input types."""
        # Create epoch for January 18-25, 2024
        epoch_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(epoch_start)

        # Test datetime inputs
        assert epoch.contains(datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC))  # Start
        assert epoch.contains(datetime(2024, 1, 20, 12, 0, 0, tzinfo=UTC))  # Middle
        assert epoch.contains(
            datetime(2024, 1, 24, 23, 59, 59, tzinfo=UTC)
        )  # Almost end
        assert not epoch.contains(
            datetime(2024, 1, 25, 0, 0, 0, tzinfo=UTC)
        )  # End (exclusive)
        assert not epoch.contains(
            datetime(2024, 1, 17, 23, 59, 59, tzinfo=UTC)
        )  # Before

        # Test timestamp inputs
        assert epoch.contains(int(epoch_start.timestamp()))
        assert not epoch.contains(int(epoch.end_datetime.timestamp()))

        # Test string inputs
        assert epoch.contains("2024-01-20T12:00:00Z")
        assert not epoch.contains("2024-01-25T00:00:00Z")

    def test_contains_with_invalid_input(self):
        """Test contains method with invalid input raises ValidationError."""
        epoch = PendleEpoch(datetime(2024, 1, 18, tzinfo=UTC))

        with pytest.raises(ValidationError):
            epoch.contains("invalid-date")

        with pytest.raises(ValidationError):
            epoch.contains([1, 2, 3])  # type: ignore

    def test_get_block_range(self):
        """Test get_block_range method with mocked EtherscanClient."""
        epoch = PendleEpoch(datetime(2024, 1, 18, tzinfo=UTC))

        # Mock EtherscanClient
        mock_client = Mock()
        mock_client.get_block_number_by_timestamp.side_effect = [19000000, 19010000]

        start_block, end_block = epoch.get_block_range(mock_client)

        assert start_block == 19000000
        assert end_block == 19010000

        # Verify the client was called with correct parameters
        assert mock_client.get_block_number_by_timestamp.call_count == 2
        calls = mock_client.get_block_number_by_timestamp.call_args_list

        # First call should be for start timestamp with "after"
        assert calls[0][0][0] == epoch.start_timestamp  # First positional arg
        assert calls[0][1]["closest"] == "after"  # Keyword arg
        # Second call should be for end timestamp with "before"
        assert calls[1][0][0] == epoch.end_timestamp  # First positional arg
        assert calls[1][1]["closest"] == "before"  # Keyword arg

    def test_equality_comparison(self):
        """Test epoch equality comparison."""
        time1 = datetime(2024, 1, 18, 12, 0, 0, tzinfo=UTC)
        time2 = datetime(2024, 1, 19, 8, 0, 0, tzinfo=UTC)  # Same epoch
        time3 = datetime(2024, 1, 25, 12, 0, 0, tzinfo=UTC)  # Different epoch

        epoch1 = PendleEpoch(time1)
        epoch2 = PendleEpoch(time2)
        epoch3 = PendleEpoch(time3)

        # Same epoch
        assert epoch1 == epoch2
        assert not epoch1 != epoch2

        # Different epochs
        assert epoch1 != epoch3
        assert not epoch1 == epoch3

        # Comparison with non-PendleEpoch
        assert epoch1 != "not-an-epoch"
        assert not epoch1 == "not-an-epoch"

    def test_less_than_comparison(self):
        """Test epoch less than comparison."""
        earlier_time = datetime(2024, 1, 18, 12, 0, 0, tzinfo=UTC)
        later_time = datetime(2024, 1, 25, 12, 0, 0, tzinfo=UTC)

        earlier_epoch = PendleEpoch(earlier_time)
        later_epoch = PendleEpoch(later_time)

        assert earlier_epoch < later_epoch
        assert not later_epoch < earlier_epoch
        assert not earlier_epoch < earlier_epoch  # Not less than itself

    def test_string_representations(self):
        """Test string and repr methods."""
        test_time = datetime(2024, 1, 18, 12, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(test_time)

        # Test __str__
        str_repr = str(epoch)
        assert "Epoch" in str_repr
        assert "Jan 18" in str_repr
        assert "Jan 24, 2024" in str_repr

        # Test __repr__
        repr_str = repr(epoch)
        assert "PendleEpoch" in repr_str
        assert "2024-01-18T00:00:00+00:00" in repr_str

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test epoch boundary (exactly at Thursday 00:00 UTC)
        thursday_start = datetime(2024, 1, 18, 0, 0, 0, tzinfo=UTC)
        epoch = PendleEpoch(thursday_start)

        assert epoch.start_datetime == thursday_start
        assert epoch.contains(thursday_start)

        # Test just before epoch boundary
        wednesday_end = datetime(2024, 1, 17, 23, 59, 59, tzinfo=UTC)
        epoch_before = PendleEpoch(wednesday_end)

        # Should be in the previous epoch
        expected_previous_start = datetime(2024, 1, 11, 0, 0, 0, tzinfo=UTC)
        assert epoch_before.start_datetime == expected_previous_start

    def test_month_boundary_handling(self):
        """Test epoch calculation across month boundaries."""
        # Test case where epoch spans across months
        end_of_month = datetime(2024, 1, 31, 12, 0, 0, tzinfo=UTC)  # Wednesday
        epoch = PendleEpoch(end_of_month)

        # Should start on the previous Thursday (January 25)
        expected_start = datetime(2024, 1, 25, 0, 0, 0, tzinfo=UTC)
        expected_end = datetime(2024, 2, 1, 0, 0, 0, tzinfo=UTC)  # February 1

        assert epoch.start_datetime == expected_start
        assert epoch.end_datetime == expected_end

    def test_year_boundary_handling(self):
        """Test epoch calculation across year boundaries."""
        # Test case where epoch spans across years
        new_years = datetime(2024, 1, 3, 12, 0, 0, tzinfo=UTC)  # Wednesday
        epoch = PendleEpoch(new_years)

        # Should start on the previous Thursday (December 28, 2023)
        expected_start = datetime(2023, 12, 28, 0, 0, 0, tzinfo=UTC)
        expected_end = datetime(2024, 1, 4, 0, 0, 0, tzinfo=UTC)

        assert epoch.start_datetime == expected_start
        assert epoch.end_datetime == expected_end
