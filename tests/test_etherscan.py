"""
Unit tests for the EtherscanClient class.
"""

from unittest.mock import Mock, patch

import httpx
import pytest

from pendle_yield.etherscan import EtherscanClient
from pendle_yield.exceptions import APIError, RateLimitError, ValidationError
from pendle_yield.models import VoteEvent


class TestEtherscanClient:
    """Test cases for EtherscanClient."""

    @pytest.fixture
    def client(self):
        """Create a test client instance."""
        return EtherscanClient(api_key="test_key")

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
        )

    def test_init_valid_api_key(self):
        """Test client initialization with valid API key."""
        client = EtherscanClient(api_key="test_key")
        assert client.api_key == "test_key"
        assert client.base_url == "https://api.etherscan.io/v2/api"

    def test_init_empty_api_key(self):
        """Test client initialization with empty API key raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            EtherscanClient(api_key="")

        assert "Etherscan API key is required" in str(exc_info.value)
        assert exc_info.value.field == "api_key"

    def test_init_custom_url(self):
        """Test client initialization with custom URL."""
        client = EtherscanClient(
            api_key="test_key",
            base_url="https://custom-etherscan.com",
        )
        assert client.base_url == "https://custom-etherscan.com"

    def test_context_manager(self):
        """Test client as context manager."""
        with EtherscanClient(api_key="test_key") as client:
            assert isinstance(client, EtherscanClient)
        # Client should be closed after context exit

    def test_make_request_success(self, client):
        """Test successful HTTP request."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "1", "result": []}

        with patch.object(client._client, "get", return_value=mock_response):
            result = client._make_request("https://test.com")
            assert result == {"status": "1", "result": []}

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

    def test_get_vote_events_invalid_block(self, client):
        """Test get_vote_events with invalid block numbers."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_vote_events(-1, 1000)

        assert "Block numbers must be positive" in str(exc_info.value)
        assert exc_info.value.field == "block_numbers"

    def test_get_vote_events_invalid_block_range(self, client):
        """Test get_vote_events with invalid block range."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_vote_events(2000, 1000)

        assert "from_block must be less than or equal to to_block" in str(
            exc_info.value
        )
        assert exc_info.value.field == "block_range"

    def test_get_vote_events_success(self, client):
        """Test successful vote events retrieval with real Etherscan API response format."""
        # Using real Etherscan API response structure
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                },
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x00000000000000000000000061e4a41853550dc09dc296088ac83d770cd45c5a",
                    ],
                    "data": "0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x92",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                },
            ],
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            vote_events = client.get_vote_events(
                23251350, 23251350
            )  # Using real block number

            assert len(vote_events) == 2

            # Test first vote event (with actual data)
            vote1 = vote_events[0]
            assert vote1.block_number == 23251350  # 0x162c996 in decimal
            assert (
                vote1.transaction_hash
                == "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043"
            )
            assert vote1.voter_address == "0x23ce39c9ab29d00fca9b83a50f64a67837c757c5"
            assert vote1.pool_address == "0x6d98a2b6cdbf44939362a3e99793339ba2016af4"
            # The weight should be parsed from the first 64 hex chars of data
            assert vote1.weight == int(
                "0000000000000000000000000000000000000000000000000de0b6b3a7640000", 16
            )
            # The bias and slope values should be parsed from the data field
            assert vote1.bias > 0  # Should have parsed some positive value
            assert vote1.slope > 0  # Should have parsed some positive value
            # Check timestamp is properly converted (0x68b273eb = 1756525547 in decimal)
            assert vote1.timestamp is not None
            assert vote1.timestamp.timestamp() == 1756525547

            # Test second vote event (with zero data)
            vote2 = vote_events[1]
            assert vote2.block_number == 23251350
            assert (
                vote2.transaction_hash
                == "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043"
            )
            assert vote2.voter_address == "0x23ce39c9ab29d00fca9b83a50f64a67837c757c5"
            assert vote2.pool_address == "0x61e4a41853550dc09dc296088ac83d770cd45c5a"
            assert vote2.weight == 0  # Zero data should result in zero values
            assert vote2.bias == 0  # Zero data should result in zero values
            assert vote2.slope == 0
            # Both events should have the same timestamp
            assert vote2.timestamp is not None
            assert vote2.timestamp.timestamp() == 1756525547

    def test_get_vote_events_api_error(self, client):
        """Test API error handling."""
        mock_response = {
            "status": "0",
            "message": "NOTOK",
            "result": "Error! Invalid address format",
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            with pytest.raises(APIError) as exc_info:
                client.get_vote_events(12345, 12345)

            assert "Etherscan API error: NOTOK" in str(exc_info.value)

    def test_get_vote_events_empty_result(self, client):
        """Test handling of empty results."""
        mock_response = {"status": "1", "message": "OK", "result": []}

        with patch.object(client, "_make_request", return_value=mock_response):
            vote_events = client.get_vote_events(12345, 12345)
            assert len(vote_events) == 0

    def test_get_vote_events_malformed_log(self, client):
        """Test handling of malformed log entries."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1"
                    ],  # Missing required topics
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000",
                    "blockNumber": "0x162c996",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "logIndex": "0x90",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                }
            ],
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            vote_events = client.get_vote_events(12345, 12345)
            # Should skip malformed entries and return empty list
            assert len(vote_events) == 0

    # Tests for get_block_number_by_timestamp method

    def test_get_block_number_by_timestamp_success(self, client):
        """Test successful block number retrieval by timestamp."""
        mock_response = {"status": "1", "message": "OK", "result": "23403509"}

        with patch.object(client, "_make_request", return_value=mock_response):
            block_number = client.get_block_number_by_timestamp(1758361967, "after")
            assert block_number == 23403509

    def test_get_block_number_by_timestamp_before(self, client):
        """Test block number retrieval with 'before' parameter."""
        mock_response = {"status": "1", "message": "OK", "result": "23403508"}

        with patch.object(client, "_make_request", return_value=mock_response):
            block_number = client.get_block_number_by_timestamp(1758361967, "before")
            assert block_number == 23403508

    def test_get_block_number_by_timestamp_default_closest(self, client):
        """Test block number retrieval with default 'before' parameter."""
        mock_response = {"status": "1", "message": "OK", "result": "23403508"}

        with patch.object(client, "_make_request", return_value=mock_response):
            block_number = client.get_block_number_by_timestamp(1758361967)
            assert block_number == 23403508

    def test_get_block_number_by_timestamp_invalid_timestamp(self, client):
        """Test get_block_number_by_timestamp with invalid timestamp."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_block_number_by_timestamp(-1, "after")

        assert "Timestamp must be positive" in str(exc_info.value)
        assert exc_info.value.field == "timestamp"
        assert exc_info.value.value == "-1"

    def test_get_block_number_by_timestamp_zero_timestamp(self, client):
        """Test get_block_number_by_timestamp with zero timestamp."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_block_number_by_timestamp(0, "after")

        assert "Timestamp must be positive" in str(exc_info.value)
        assert exc_info.value.field == "timestamp"

    def test_get_block_number_by_timestamp_invalid_closest(self, client):
        """Test get_block_number_by_timestamp with invalid closest parameter."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_block_number_by_timestamp(1758361967, "invalid")

        assert "closest parameter must be 'before' or 'after'" in str(exc_info.value)
        assert exc_info.value.field == "closest"
        assert exc_info.value.value == "invalid"

    def test_get_block_number_by_timestamp_api_error(self, client):
        """Test API error handling for get_block_number_by_timestamp."""
        mock_response = {
            "status": "0",
            "message": "NOTOK",
            "result": "Error! Invalid timestamp",
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            with pytest.raises(APIError) as exc_info:
                client.get_block_number_by_timestamp(1758361967, "after")

            assert "Etherscan API error: NOTOK" in str(exc_info.value)

    def test_get_block_number_by_timestamp_pydantic_validation_error(self, client):
        """Test handling of Pydantic validation errors."""
        # Test with invalid response that will fail Pydantic validation
        mock_response = {"status": "1", "message": "OK", "result": 12345}

        with patch.object(client, "_make_request", return_value=mock_response):
            with pytest.raises(ValidationError) as exc_info:
                client.get_block_number_by_timestamp(1758361967, "after")

            # Should get a Pydantic validation error wrapped in our ValidationError
            assert "Invalid response format" in str(exc_info.value)

    def test_get_block_number_by_timestamp_invalid_block_number(self, client):
        """Test handling of invalid block number in result."""
        mock_response = {"status": "1", "message": "OK", "result": "not_a_number"}

        with patch.object(client, "_make_request", return_value=mock_response):
            with pytest.raises(ValidationError) as exc_info:
                client.get_block_number_by_timestamp(1758361967, "after")

            assert "Invalid block number format: not_a_number" in str(exc_info.value)

    # Tests for pagination functionality

    def test_get_vote_events_pagination_single_page(self, client):
        """Test pagination with single page (less than 1000 results)."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ],
        }

        with patch.object(
            client, "_make_request", return_value=mock_response
        ) as mock_request:
            vote_events = client.get_vote_events(12345, 12345)

            # Should only make one request since we got less than 1000 results
            assert mock_request.call_count == 1
            assert len(vote_events) == 1

            # Check that pagination parameters were included
            # The parameters are passed as the second positional argument to _make_request
            call_args = mock_request.call_args
            assert call_args is not None
            # _make_request is called with (url, params)
            params = call_args[0][1]  # Second positional argument
            assert "page" in params
            assert "offset" in params
            assert params["page"] == "1"
            assert params["offset"] == "1000"

    def test_get_vote_events_pagination_multiple_pages(self, client):
        """Test pagination with multiple pages."""
        # Mock responses for multiple pages
        page1_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ]
            * 1000,  # Exactly 1000 results to trigger next page
        }

        page2_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ]
            * 500,  # 500 results (less than 1000) to end pagination
        }

        with patch.object(
            client, "_make_request", side_effect=[page1_response, page2_response]
        ) as mock_request:
            vote_events = client.get_vote_events(12345, 12345)

            # Should make two requests
            assert mock_request.call_count == 2
            assert len(vote_events) == 1500  # 1000 + 500

            # Check pagination parameters for both calls
            first_call_params = mock_request.call_args_list[0][0][
                1
            ]  # Second positional arg of first call
            assert first_call_params["page"] == "1"
            assert first_call_params["offset"] == "1000"

            second_call_params = mock_request.call_args_list[1][0][
                1
            ]  # Second positional arg of second call
            assert second_call_params["page"] == "2"
            assert second_call_params["offset"] == "1000"

    def test_get_vote_events_pagination_max_pages(self, client):
        """Test pagination with max_pages limit."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ]
            * 1000,  # Always return 1000 results to test max_pages limit
        }

        with patch.object(
            client, "_make_request", return_value=mock_response
        ) as mock_request:
            vote_events = client.get_vote_events(12345, 12345, max_pages=2)

            # Should stop after 2 pages due to max_pages limit
            assert mock_request.call_count == 2
            assert len(vote_events) == 2000  # 2 pages * 1000 results each

    def test_rate_limiting_initialization(self):
        """Test rate limiting configuration during initialization."""
        # Test default rate limiting (5 req/sec)
        client = EtherscanClient(api_key="test_key")
        assert client._requests_per_second == 5.0
        assert client._min_request_interval == 0.2  # 1/5 = 0.2 seconds

        # Test custom rate limiting
        client_custom = EtherscanClient(api_key="test_key", requests_per_second=10.0)
        assert client_custom._requests_per_second == 10.0
        assert client_custom._min_request_interval == 0.1  # 1/10 = 0.1 seconds

    def test_rate_limiting_enforcement(self, client):
        """Test that rate limiting is enforced."""

        # Mock time.time() and time.sleep to control timing
        with (
            patch("pendle_yield.etherscan.time.time") as mock_time,
            patch("pendle_yield.etherscan.time.sleep") as mock_sleep,
        ):
            # Reset the client's last request time to simulate a fresh start
            client._last_request_time = 0.0

            # Set up time progression: first call at 1.0, second call at 1.1 (only 0.1s later)
            mock_time.side_effect = [
                1.0,
                1.1,
                1.1,
                1.3,
            ]  # First call, check, sleep, final time

            # First call should not sleep (enough time has passed since last request)
            client._enforce_rate_limit()
            assert mock_sleep.call_count == 0

            # Second call should sleep because only 0.1 seconds have passed (need 0.2)
            client._enforce_rate_limit()
            # The sleep time should be 0.2 - 0.1 = 0.1 seconds
            # Use pytest.approx to handle floating-point precision issues
            mock_sleep.assert_called_once()
            actual_sleep_time = mock_sleep.call_args[0][0]
            assert actual_sleep_time == pytest.approx(0.2, abs=1e-10)

    # Tests for block range batching functionality

    def test_get_vote_events_block_batching_single_batch(self, client):
        """Test block range batching with a range that fits in a single batch."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ],
        }

        with patch.object(
            client, "_make_request", return_value=mock_response
        ) as mock_request:
            # Test with a range smaller than BLOCK_BATCH_SIZE (1000)
            vote_events = client.get_vote_events(1000, 1500)

            # Should only make one request since range is within single batch
            assert mock_request.call_count == 1
            assert len(vote_events) == 1

            # Check that the request was made with correct block range
            call_args = mock_request.call_args
            params = call_args[0][1]
            assert params["fromBlock"] == "1000"
            assert params["toBlock"] == "1500"

    def test_get_vote_events_block_batching_multiple_batches(self, client):
        """Test block range batching with a range that requires multiple batches."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ],
        }

        with patch.object(
            client, "_make_request", return_value=mock_response
        ) as mock_request:
            # Test with a range that spans multiple batches (2500 blocks = 3 batches)
            vote_events = client.get_vote_events(1000, 3500)

            # Should make 3 requests for 3 batches
            assert mock_request.call_count == 3
            assert len(vote_events) == 3  # One event per batch

            # Check that requests were made with correct block ranges
            call_args_list = mock_request.call_args_list

            # First batch: 1000-1999
            first_params = call_args_list[0][0][1]
            assert first_params["fromBlock"] == "1000"
            assert first_params["toBlock"] == "1999"

            # Second batch: 2000-2999
            second_params = call_args_list[1][0][1]
            assert second_params["fromBlock"] == "2000"
            assert second_params["toBlock"] == "2999"

            # Third batch: 3000-3500
            third_params = call_args_list[2][0][1]
            assert third_params["fromBlock"] == "3000"
            assert third_params["toBlock"] == "3500"

    def test_batch_pagination_limit_enforcement(self, client):
        """Test that pagination stops at page 10 to avoid API limit."""
        # Mock response that always returns 1000 results to trigger pagination
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0x44087e105137a5095c008aab6a6530182821f2f0",
                    "topics": [
                        "0xc71e393f1527f71ce01b78ea87c9bd4fca84f1482359ce7ac9b73f358c61b1e1",
                        "0x00000000000000000000000023ce39c9ab29d00fca9b83a50f64a67837c757c5",
                        "0x0000000000000000000000006d98a2b6cdbf44939362a3e99793339ba2016af4",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000000000000000000000000000000000000000000000079206cec12fc1322fd7000000000000000000000000000000000000000000000000000011e0ee61f4b64a",
                    "blockNumber": "0x162c996",
                    "blockHash": "0x2bcf153ff39a252324c3049a528d4571793d68bb64b50d10e193005e8d58a7d7",
                    "timeStamp": "0x68b273eb",
                    "gasPrice": "0x43efee42",
                    "gasUsed": "0x19514",
                    "logIndex": "0x90",
                    "transactionHash": "0x4010dca56ab072d9c8b56f877025ba155ad1b9c0cfe609b571e3567f8d879043",
                    "transactionIndex": "0x26",
                }
            ]
            * 1000,  # Always return 1000 results
        }

        with patch.object(
            client, "_make_request", return_value=mock_response
        ) as mock_request:
            # Test with a small range that should trigger pagination limit
            vote_events = client.get_vote_events(1000, 1100)

            # Should stop at page 10 (10,000 results max)
            assert mock_request.call_count == 10
            assert len(vote_events) == 10000  # 10 pages * 1000 results each

            # Check that pagination went from page 1 to page 10
            call_args_list = mock_request.call_args_list
            for i, call_args in enumerate(call_args_list):
                params = call_args[0][1]
                assert params["page"] == str(i + 1)  # Pages 1-10

    def test_block_batch_size_constant(self):
        """Test that BLOCK_BATCH_SIZE constant is properly defined."""
        from pendle_yield.etherscan import BLOCK_BATCH_SIZE

        assert BLOCK_BATCH_SIZE == 1000
        assert isinstance(BLOCK_BATCH_SIZE, int)
