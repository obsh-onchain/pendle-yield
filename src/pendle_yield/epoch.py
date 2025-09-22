"""
Pendle epoch management for the pendle-yield package.

This module provides the PendleEpoch class for handling Pendle's 7-day voting epochs
that start on Thursday 00:00 UTC.
"""

from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING

from .exceptions import ValidationError

if TYPE_CHECKING:
    from .etherscan import EtherscanClient


class PendleEpoch:
    """
    Represents a Pendle epoch - a 7-day voting period starting Thursday 00:00 UTC.

    This class encapsulates the time-related logic for Pendle epochs, providing:
    - Flexible input handling (datetime, timestamp, string)
    - Automatic calculation of epoch boundaries
    - Easy access to start/end times in multiple formats
    - Integration with blockchain block number lookups
    """

    def __init__(self, time_input: datetime | int | str | None = None) -> None:
        """
        Initialize a PendleEpoch from various input formats.

        Args:
            time_input: Can be:
                - datetime object (will be converted to UTC)
                - Unix timestamp (int)
                - ISO format string
                - None (uses current time)

        Raises:
            ValidationError: If the input format is invalid
        """
        # Parse input to datetime using shared conversion logic
        reference_time = self._convert_to_utc_datetime(time_input)

        # Calculate epoch boundaries
        self._start_datetime = self._calculate_epoch_start(reference_time)
        self._end_datetime = self._start_datetime + timedelta(days=7)

    def _convert_to_utc_datetime(
        self, time_input: datetime | int | str | None
    ) -> datetime:
        """
        Convert various time input formats to UTC datetime.

        Args:
            time_input: Time input in various formats

        Returns:
            UTC datetime object

        Raises:
            ValidationError: If the input format is invalid
        """
        if time_input is None:
            return datetime.now(UTC)
        elif isinstance(time_input, datetime):
            # Ensure timezone awareness
            if time_input.tzinfo is None:
                return time_input.replace(tzinfo=UTC)
            else:
                return time_input.astimezone(UTC)
        elif isinstance(time_input, int):
            try:
                return datetime.fromtimestamp(time_input, tz=UTC)
            except (ValueError, OSError) as e:
                raise ValidationError(
                    f"Invalid timestamp: {time_input}",
                    field="time_input",
                    value=time_input,
                ) from e
        elif isinstance(time_input, str):
            try:
                # Try parsing as ISO format
                parsed_dt = datetime.fromisoformat(time_input.replace("Z", "+00:00"))
                if parsed_dt.tzinfo is None:
                    return parsed_dt.replace(tzinfo=UTC)
                else:
                    return parsed_dt.astimezone(UTC)
            except ValueError as e:
                raise ValidationError(
                    f"Invalid datetime string format: {time_input}",
                    field="time_input",
                    value=time_input,
                ) from e
        else:
            raise ValidationError(
                f"Unsupported time input type: {type(time_input)}",
                field="time_input",
                value=time_input,
            )

    def _calculate_epoch_start(self, reference_time: datetime) -> datetime:
        """
        Calculate the start of the epoch containing the reference time.

        Pendle epochs start on Thursday 00:00 UTC and last for 7 days.

        Args:
            reference_time: UTC datetime to find the epoch for

        Returns:
            Start of the epoch as UTC datetime
        """
        # Get the date of the reference time
        ref_date = reference_time.date()

        # Find the Thursday of this week or the previous week
        # Monday = 0, Tuesday = 1, ..., Sunday = 6
        # Thursday = 3
        days_since_thursday = (ref_date.weekday() - 3) % 7

        # If it's Thursday and we're at or after 00:00 UTC, use this Thursday
        # Otherwise, use the previous Thursday
        if ref_date.weekday() == 3 and reference_time.time() >= datetime.min.time():
            epoch_start_date = ref_date
        else:
            # Go back to the most recent Thursday
            epoch_start_date = ref_date - timedelta(days=days_since_thursday)

        # Create datetime at 00:00 UTC
        return datetime.combine(epoch_start_date, datetime.min.time(), UTC)

    @property
    def start_datetime(self) -> datetime:
        """Start of the epoch as datetime (Thursday 00:00 UTC)."""
        return self._start_datetime

    @property
    def end_datetime(self) -> datetime:
        """End of the epoch as datetime (next Thursday 00:00 UTC)."""
        return self._end_datetime

    @property
    def start_timestamp(self) -> int:
        """Start of the epoch as Unix timestamp."""
        return int(self._start_datetime.timestamp())

    @property
    def end_timestamp(self) -> int:
        """End of the epoch as Unix timestamp."""
        return int(self._end_datetime.timestamp())

    @property
    def is_past(self) -> bool:
        """Check if this epoch has completely ended."""
        return datetime.now(UTC) >= self._end_datetime

    @property
    def is_current(self) -> bool:
        """Check if we are currently in this epoch."""
        now = datetime.now(UTC)
        return self._start_datetime <= now < self._end_datetime

    @property
    def is_future(self) -> bool:
        """Check if this epoch hasn't started yet."""
        return datetime.now(UTC) < self._start_datetime

    def contains(self, time_input: datetime | int | str) -> bool:
        """
        Check if a given time falls within this epoch.

        Args:
            time_input: Time to check (datetime, timestamp, or string)

        Returns:
            True if the time is within this epoch, False otherwise

        Raises:
            ValidationError: If the input format is invalid
        """
        # Convert input to datetime using shared conversion logic
        check_time = self._convert_to_utc_datetime(time_input)
        return self._start_datetime <= check_time < self._end_datetime

    def get_block_range(
        self, etherscan_client: "EtherscanClient", use_latest_for_current: bool = False
    ) -> tuple[int, int | None]:
        """
        Get the block number range for this epoch using Etherscan.

        Args:
            etherscan_client: EtherscanClient instance to use for block lookups
            use_latest_for_current: If True, use the latest block number for current epochs.
                                  If False, return None for the end block of current epochs.

        Returns:
            Tuple of (start_block, end_block). For current epochs, end_block may be None
            or the latest block number depending on use_latest_for_current parameter.

        Raises:
            ValidationError: If this is a future epoch (hasn't started yet)
            APIError: If the Etherscan API requests fail
        """
        # Check if this is a future epoch
        if self.is_future:
            raise ValidationError(
                f"Cannot get block range for future epoch. Epoch starts at {self.start_datetime.isoformat()}",
                field="epoch_status",
                value="future",
            )

        # Get start block (always available for current and past epochs)
        start_block = etherscan_client.get_block_number_by_timestamp(
            self.start_timestamp, closest="after"
        )

        # Handle end block based on epoch status
        if self.is_past:
            # For past epochs, get the actual end block
            end_block = etherscan_client.get_block_number_by_timestamp(
                self.end_timestamp, closest="before"
            )
        elif self.is_current:
            # For current epochs, handle based on user preference
            if use_latest_for_current:
                # Get the latest block number
                end_block = etherscan_client.get_block_number_by_timestamp(
                    int(datetime.now().timestamp()), closest="before"
                )
            else:
                # Return None to indicate the epoch is still ongoing
                end_block = None
        else:
            # This should not happen due to the future epoch check above,
            # but included for completeness
            end_block = None

        return start_block, end_block

    def __eq__(self, other: object) -> bool:
        """Check if two epochs are the same."""
        if not isinstance(other, PendleEpoch):
            return False
        return self._start_datetime == other._start_datetime

    def __lt__(self, other: "PendleEpoch") -> bool:
        """Check if this epoch is before another."""
        return self._start_datetime < other._start_datetime

    def __str__(self) -> str:
        """Human-readable string representation."""
        start_str = self._start_datetime.strftime("%b %d")
        end_str = (self._end_datetime - timedelta(days=1)).strftime("%b %d, %Y")
        return f"Epoch {start_str} - {end_str}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"PendleEpoch(start={self._start_datetime.isoformat()}, end={self._end_datetime.isoformat()})"
