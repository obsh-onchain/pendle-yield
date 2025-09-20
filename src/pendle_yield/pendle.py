"""
Pendle API client for the pendle-yield package.

This module provides functionality to interact with the Pendle Finance API
to fetch pool metadata and other DeFi-related data.
"""

import time
from typing import Any

import httpx
from pydantic import ValidationError as PydanticValidationError

from .exceptions import APIError, RateLimitError, ValidationError
from .models import VoterAprResponse


class PendleClient:
    """
    Client for interacting with the Pendle Finance API.

    This client provides methods to fetch pool metadata and other DeFi data
    from the Pendle API.
    """

    def __init__(
        self,
        base_url: str = "https://api-v2.pendle.finance/core",
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        """
        Initialize the PendleClient.

        Args:
            base_url: Base URL for Pendle API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
        """
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries

        # HTTP client configuration
        self._client = httpx.Client(
            timeout=httpx.Timeout(timeout),
            limits=httpx.Limits(max_keepalive_connections=10, max_connections=20),
        )

    def __enter__(self) -> "PendleClient":
        """Context manager entry."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def _make_request(
        self, url: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Make an HTTP request with retry logic.

        Args:
            url: URL to request
            params: Query parameters

        Returns:
            JSON response data

        Raises:
            APIError: If the request fails
            RateLimitError: If rate limit is exceeded
        """
        last_exception = None

        for attempt in range(self.max_retries + 1):
            try:
                response = self._client.get(url, params=params)

                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 60))
                    raise RateLimitError(
                        "Rate limit exceeded",
                        retry_after=retry_after,
                        status_code=response.status_code,
                        url=url,
                    )

                response.raise_for_status()
                json_response: dict[str, Any] = response.json()
                return json_response

            except httpx.HTTPStatusError as e:
                last_exception = APIError(
                    f"HTTP {e.response.status_code}: {e.response.text}",
                    status_code=e.response.status_code,
                    response_text=e.response.text,
                    url=url,
                )
            except httpx.RequestError as e:
                last_exception = APIError(f"Request failed: {str(e)}", url=url)
            except RateLimitError:
                # Re-raise RateLimitError as-is
                raise
            except Exception as e:
                last_exception = APIError(f"Unexpected error: {str(e)}", url=url)

            if attempt < self.max_retries:
                time.sleep(2**attempt)  # Exponential backoff

        # This should never be reached due to the loop logic, but mypy needs this
        if last_exception is not None:
            raise last_exception
        raise APIError("All retry attempts failed", url=url)

    def get_pool_voter_apr_data(self) -> VoterAprResponse:
        """
        Fetch pool voter APR data from the Pendle API.

        Returns:
            Voter APR response containing pool data with APR metrics

        Raises:
            APIError: If the API request fails
            ValidationError: If the response format is invalid
        """
        url = f"{self.base_url}/v1/ve-pendle/pool-voter-apr-swap-fee"
        params = {"order_by": "voterApr:-1"}

        response_data = self._make_request(url, params)

        try:
            return VoterAprResponse(**response_data)
        except PydanticValidationError as e:
            raise ValidationError(f"Invalid voter APR response format: {str(e)}") from e
