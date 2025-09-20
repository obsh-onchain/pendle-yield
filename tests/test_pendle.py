"""
Unit tests for the PendleClient class.
"""

from datetime import datetime
from unittest.mock import Mock, patch

import httpx
import pytest

from pendle_yield.exceptions import APIError, RateLimitError, ValidationError
from pendle_yield.models import PoolInfo, PoolVoterData, VoterAprResponse
from pendle_yield.pendle import PendleClient


class TestPendleClient:
    """Test cases for PendleClient."""

    @pytest.fixture
    def client(self):
        """Create a test client instance."""
        return PendleClient()

    def test_init_default_url(self):
        """Test client initialization with default URL."""
        client = PendleClient()
        assert client.base_url == "https://api-v2.pendle.finance/core"

    def test_init_custom_url(self):
        """Test client initialization with custom URL."""
        client = PendleClient(base_url="https://custom-pendle.com")
        assert client.base_url == "https://custom-pendle.com"

    def test_context_manager(self):
        """Test client as context manager."""
        with PendleClient() as client:
            assert isinstance(client, PendleClient)
        # Client should be closed after context exit

    def test_make_request_success(self, client):
        """Test successful HTTP request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"pool": {"name": "Test Pool"}}

        with patch.object(client._client, "get", return_value=mock_response):
            result = client._make_request("https://test.com")
            assert result == {"pool": {"name": "Test Pool"}}

    def test_make_request_rate_limit(self, client):
        """Test rate limit handling."""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_response.headers = {"Retry-After": "60"}

        with patch.object(client._client, "get", return_value=mock_response):
            with pytest.raises(RateLimitError) as exc_info:
                client._make_request("https://test.com")

            assert exc_info.value.retry_after == 60
            assert exc_info.value.status_code == 429

    def test_make_request_http_error(self, client):
        """Test HTTP error handling."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "500 Server Error", request=Mock(), response=mock_response
        )

        with patch.object(client._client, "get", return_value=mock_response):
            with pytest.raises(APIError) as exc_info:
                client._make_request("https://test.com")

            assert exc_info.value.status_code == 500
            assert "Internal Server Error" in exc_info.value.response_text

    @pytest.fixture
    def mock_voter_apr_response(self):
        """Create mock voter APR response data."""
        return {
            "results": [
                {
                    "pool": {
                        "id": "1-0x6d98a2b6cdbf44939362a3e99793339ba2016af4",
                        "chainId": 1,
                        "address": "0x6d98a2b6cdbf44939362a3e99793339ba2016af4",
                        "symbol": "PENDLE-LPT",
                        "expiry": "2025-09-25T00:00:00.000Z",
                        "protocol": "Ethena",
                        "underlyingPool": "",
                        "voterApy": 0.10724758541692492,
                        "accentColor": "#A8A8A8",
                        "name": "USDe",
                        "farmSimpleName": "USDe",
                        "farmSimpleIcon": "https://storage.googleapis.com/prod-pendle-bucket-a/images/uploads/d268798b-a558-4ebe-9b62-eab24a82ce02.svg",
                        "farmProName": "USDe",
                        "farmProIcon": "https://storage.googleapis.com/prod-pendle-bucket-a/images/uploads/d268798b-a558-4ebe-9b62-eab24a82ce02.svg",
                    },
                    "currentVoterApr": 0.10724758541692492,
                    "lastEpochVoterApr": 0.09961876528176773,
                    "currentSwapFee": 38856.289778318336,
                    "lastEpochSwapFee": 55721.30130835859,
                    "projectedVoterApr": 0.12129753519813753,
                },
                {
                    "pool": {
                        "id": "999-0x61e4a41853550dc09dc296088ac83d770cd45c5a",
                        "chainId": 999,
                        "address": "0x61e4a41853550dc09dc296088ac83d770cd45c5a",
                        "symbol": "PENDLE-LPT",
                        "expiry": "2025-11-13T00:00:00.000Z",
                        "protocol": "Kinetiq",
                        "underlyingPool": "",
                        "voterApy": 0.1677583798820081,
                        "accentColor": "#4842D9",
                        "name": "vkHYPE",
                        "farmSimpleName": "vkHYPE",
                        "farmSimpleIcon": "https://storage.googleapis.com/prod-pendle-bucket-a/images/uploads/3d37b93d-2929-4bc1-b79b-ed50e4480b0c.svg",
                        "farmProName": "vkHYPE",
                        "farmProIcon": "https://storage.googleapis.com/prod-pendle-bucket-a/images/uploads/3d37b93d-2929-4bc1-b79b-ed50e4480b0c.svg",
                    },
                    "currentVoterApr": 0.1677583798820081,
                    "lastEpochVoterApr": 0.1700306677061001,
                    "currentSwapFee": 19200.588106544223,
                    "lastEpochSwapFee": 19147.897015689836,
                    "projectedVoterApr": 0.1542172234284484,
                },
            ],
            "totalPools": 188,
            "totalFee": 358705.6949107315,
            "timestamp": "2025-09-16T19:49:26.593Z",
        }

    def test_get_pool_voter_apr_data_success(self, client, mock_voter_apr_response):
        """Test successful voter APR data retrieval."""
        with patch.object(
            client, "_make_request", return_value=mock_voter_apr_response
        ):
            voter_apr_data = client.get_pool_voter_apr_data()

            # Verify response structure
            assert isinstance(voter_apr_data, VoterAprResponse)
            assert len(voter_apr_data.results) == 2
            assert voter_apr_data.total_pools == 188
            assert voter_apr_data.total_fee == 358705.6949107315
            assert voter_apr_data.timestamp == datetime.fromisoformat(
                "2025-09-16T19:49:26.593Z"
            )

            # Verify first pool data
            first_pool = voter_apr_data.results[0]
            assert isinstance(first_pool, PoolVoterData)
            assert first_pool.current_voter_apr == 0.10724758541692492
            assert first_pool.last_epoch_voter_apr == 0.09961876528176773
            assert first_pool.current_swap_fee == 38856.289778318336
            assert first_pool.projected_voter_apr == 0.12129753519813753

            # Verify pool info
            pool_info = first_pool.pool
            assert isinstance(pool_info, PoolInfo)
            assert pool_info.id == "1-0x6d98a2b6cdbf44939362a3e99793339ba2016af4"
            assert pool_info.chain_id == 1
            assert pool_info.address == "0x6d98a2b6cdbf44939362a3e99793339ba2016af4"
            assert pool_info.symbol == "PENDLE-LPT"
            assert pool_info.protocol == "Ethena"
            assert pool_info.name == "USDe"
            assert pool_info.voter_apy == 0.10724758541692492

    def test_get_pool_voter_apr_data_api_error(self, client):
        """Test voter APR data retrieval with API error."""
        with patch.object(
            client, "_make_request", side_effect=APIError("API Error", url="test")
        ):
            with pytest.raises(APIError):
                client.get_pool_voter_apr_data()

    def test_get_pool_voter_apr_data_validation_error(self, client):
        """Test voter APR data retrieval with invalid response format."""
        invalid_response = {"invalid": "data"}

        with patch.object(client, "_make_request", return_value=invalid_response):
            with pytest.raises(ValidationError) as exc_info:
                client.get_pool_voter_apr_data()

            assert "Invalid voter APR response format" in str(exc_info.value)

    def test_get_pool_voter_apr_data_request_params(
        self, client, mock_voter_apr_response
    ):
        """Test that correct URL and parameters are used for voter APR request."""
        with patch.object(
            client, "_make_request", return_value=mock_voter_apr_response
        ) as mock_request:
            client.get_pool_voter_apr_data()

            # Verify the correct URL and parameters were used
            expected_url = f"{client.base_url}/v1/ve-pendle/pool-voter-apr-swap-fee"
            expected_params = {"order_by": "voterApr:-1"}

            mock_request.assert_called_once_with(expected_url, expected_params)
