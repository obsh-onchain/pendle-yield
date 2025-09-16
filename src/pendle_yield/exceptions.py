"""
Custom exceptions for the pendle-yield package.

This module defines all custom exceptions that can be raised by the package,
providing clear error handling and debugging information.
"""

from typing import Any


class PendleYieldError(Exception):
    """Base exception class for all pendle-yield related errors."""

    def __init__(self, message: str, details: dict[str, Any] | None = None) -> None:
        """
        Initialize the exception.

        Args:
            message: Human-readable error message
            details: Optional dictionary with additional error context
        """
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        """Return string representation of the error."""
        if self.details:
            return f"{self.message} (Details: {self.details})"
        return self.message


class APIError(PendleYieldError):
    """Raised when an API request fails."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_text: str | None = None,
        url: str | None = None,
    ) -> None:
        """
        Initialize the API error.

        Args:
            message: Human-readable error message
            status_code: HTTP status code from the failed request
            response_text: Raw response text from the API
            url: URL that was requested
        """
        details: dict[str, Any] = {}
        if status_code is not None:
            details["status_code"] = status_code
        if response_text is not None:
            details["response_text"] = response_text
        if url is not None:
            details["url"] = url

        super().__init__(message, details)
        self.status_code = status_code
        self.response_text = response_text
        self.url = url


class ValidationError(PendleYieldError):
    """Raised when input validation fails."""

    def __init__(
        self, message: str, field: str | None = None, value: Any = None
    ) -> None:
        """
        Initialize the validation error.

        Args:
            message: Human-readable error message
            field: Name of the field that failed validation
            value: Value that failed validation
        """
        details: dict[str, Any] = {}
        if field is not None:
            details["field"] = field
        if value is not None:
            details["value"] = value

        super().__init__(message, details)
        self.field = field
        self.value = value


class RateLimitError(APIError):
    """Raised when API rate limits are exceeded."""

    def __init__(
        self,
        message: str = "API rate limit exceeded",
        retry_after: int | None = None,
        status_code: int | None = None,
        response_text: str | None = None,
        url: str | None = None,
    ) -> None:
        """
        Initialize the rate limit error.

        Args:
            message: Human-readable error message
            retry_after: Number of seconds to wait before retrying
            status_code: HTTP status code from the failed request
            response_text: Raw response text from the API
            url: URL that was requested
        """
        super().__init__(message, status_code, response_text, url)
        self.retry_after = retry_after
        if retry_after is not None:
            self.details["retry_after"] = retry_after
