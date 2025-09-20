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
        """Test get_vote_events with invalid block number."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_vote_events(-1)

        assert "Block number must be positive" in str(exc_info.value)
        assert exc_info.value.field == "block_number"
        assert exc_info.value.value == -1

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
            vote_events = client.get_vote_events(23251350)  # Using real block number

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
                client.get_vote_events(12345)

            assert "Etherscan API error: NOTOK" in str(exc_info.value)

    def test_get_vote_events_empty_result(self, client):
        """Test handling of empty results."""
        mock_response = {"status": "1", "message": "OK", "result": []}

        with patch.object(client, "_make_request", return_value=mock_response):
            vote_events = client.get_vote_events(12345)
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
            vote_events = client.get_vote_events(12345)
            # Should skip malformed entries and return empty list
            assert len(vote_events) == 0

    # Tests for get_swap_events method

    def test_get_swap_events_invalid_pool_address(self, client):
        """Test get_swap_events with invalid pool address."""
        with pytest.raises(ValidationError) as exc_info:
            client.get_swap_events("invalid_address", 1000, 2000)

        assert "Invalid pool address format" in str(exc_info.value)
        assert exc_info.value.field == "pool_address"

    def test_get_swap_events_negative_blocks(self, client):
        """Test get_swap_events with negative block numbers."""
        pool_address = "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e"

        with pytest.raises(ValidationError) as exc_info:
            client.get_swap_events(pool_address, -1, 1000)

        assert "Block numbers must be positive" in str(exc_info.value)
        assert exc_info.value.field == "block_numbers"

    def test_get_swap_events_invalid_block_range(self, client):
        """Test get_swap_events with invalid block range."""
        pool_address = "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e"

        with pytest.raises(ValidationError) as exc_info:
            client.get_swap_events(pool_address, 2000, 1000)

        assert "from_block must be less than or equal to to_block" in str(
            exc_info.value
        )
        assert exc_info.value.field == "block_range"

    def test_get_swap_events_success(self, client):
        """Test successful swap events retrieval with provided API response data."""
        # Using the provided API response data
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                    "topics": [
                        "0x829000a5bc6a12d46e30cdcecd7c56b1efd88f6d7d059da6734a04f3764557c4",
                        "0x000000000000000000000000888888888889758f76e7103c6cbf23abbf58f946",
                        "0x000000000000000000000000f342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000003f40b86776a39724665fffffffffffffffffffffffffffffffffffffffffffffc2579eb7e7520d31f9f0000000000000000000000000000000000000000000000005bdbb3b4910deb5d000000000000000000000000000000000000000000000000497c8fc3a73e55e4",
                    "blockNumber": "0x1651bf5",
                    "blockHash": "0x286a4b662389390eef4704b04cf45e9c81e5b30157e9eb55f5097f6a9976e676",
                    "timeStamp": "0x68ce796f",
                    "gasPrice": "0x11b7b899",
                    "gasUsed": "0x74418",
                    "logIndex": "0x6a",
                    "transactionHash": "0x89b0acd3f493951473feb23034a290ce54e362c5f1859a467d749d6e5e5b237b",
                    "transactionIndex": "0x1a",
                }
            ],
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            swap_events = client.get_swap_events(
                "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                23403509,  # 0x1651bf5 in decimal
                23403509,
            )

            assert len(swap_events) == 1

            swap_event = swap_events[0]
            assert swap_event.block_number == 23403509  # 0x1651bf5 in decimal
            assert (
                swap_event.transaction_hash
                == "0x89b0acd3f493951473feb23034a290ce54e362c5f1859a467d749d6e5e5b237b"
            )
            assert (
                swap_event.pool_address == "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e"
            )
            assert swap_event.caller == "0x888888888889758f76e7103c6cbf23abbf58f946"
            assert swap_event.receiver == "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e"

            # Test parsed data values
            # netPtOut: 0x0000000000000000000000000000000000000000000003f40b86776a39724665 = 18,668,935,485,073,476,699,749 (positive)
            assert swap_event.net_pt_out == 18668935485073476699749

            # netSyOut: 0xfffffffffffffffffffffffffffffffffffffffffffffc2579eb7e7520d31f9f (negative int256)
            # This is a negative number in two's complement
            expected_net_sy_out = (
                -18198151146211684180065
            )  # Calculated from the hex value
            assert swap_event.net_sy_out == expected_net_sy_out

            # netSyFee: 0x0000000000000000000000000000000000000000000000005bdbb3b4910deb5d = 6,619,081,665,460,169,565
            assert swap_event.net_sy_fee == 6619081665460169565

            # netSyToReserve: 0x000000000000000000000000000000000000000000000000497c8fc3a73e55e4 = 5,295,265,332,368,135,652
            assert swap_event.net_sy_to_reserve == 5295265332368135652

            # Check timestamp is properly converted (0x68ce796f = 1758361967 in decimal)
            assert swap_event.timestamp is not None
            assert swap_event.timestamp.timestamp() == 1758361967

    def test_get_swap_events_api_error(self, client):
        """Test API error handling for swap events."""
        mock_response = {
            "status": "0",
            "message": "NOTOK",
            "result": "Error! Invalid address format",
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            with pytest.raises(APIError) as exc_info:
                client.get_swap_events(
                    "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e", 1000, 2000
                )

            assert "Etherscan API error: NOTOK" in str(exc_info.value)

    def test_get_swap_events_empty_result(self, client):
        """Test handling of empty swap events results."""
        mock_response = {"status": "1", "message": "OK", "result": []}

        with patch.object(client, "_make_request", return_value=mock_response):
            swap_events = client.get_swap_events(
                "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e", 1000, 2000
            )
            assert len(swap_events) == 0

    def test_get_swap_events_malformed_log(self, client):
        """Test handling of malformed swap event log entries."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                    "topics": [
                        "0x829000a5bc6a12d46e30cdcecd7c56b1efd88f6d7d059da6734a04f3764557c4"
                    ],  # Missing required topics
                    "data": "0x0000000000000000000000000000000000000000000003f40b86776a39724665",
                    "blockNumber": "0x1651bf5",
                    "transactionHash": "0x89b0acd3f493951473feb23034a290ce54e362c5f1859a467d749d6e5e5b237b",
                    "transactionIndex": "0x1a",
                    "blockHash": "0x286a4b662389390eef4704b04cf45e9c81e5b30157e9eb55f5097f6a9976e676",
                    "logIndex": "0x6a",
                    "timeStamp": "0x68ce796f",
                    "gasPrice": "0x11b7b899",
                    "gasUsed": "0x74418",
                }
            ],
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            swap_events = client.get_swap_events(
                "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e", 1000, 2000
            )
            # Should skip malformed entries and return empty list
            assert len(swap_events) == 0

    def test_get_swap_events_short_data(self, client):
        """Test handling of swap events with insufficient data."""
        mock_response = {
            "status": "1",
            "message": "OK",
            "result": [
                {
                    "address": "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                    "topics": [
                        "0x829000a5bc6a12d46e30cdcecd7c56b1efd88f6d7d059da6734a04f3764557c4",
                        "0x000000000000000000000000888888888889758f76e7103c6cbf23abbf58f946",
                        "0x000000000000000000000000f342d4bde4ec5b4bba94c17ab4c92ee3792abd5e",
                    ],
                    "data": "0x0000000000000000000000000000000000000000000003f40b86776a39724665",  # Too short
                    "blockNumber": "0x1651bf5",
                    "blockHash": "0x286a4b662389390eef4704b04cf45e9c81e5b30157e9eb55f5097f6a9976e676",
                    "timeStamp": "0x68ce796f",
                    "gasPrice": "0x11b7b899",
                    "gasUsed": "0x74418",
                    "logIndex": "0x6a",
                    "transactionHash": "0x89b0acd3f493951473feb23034a290ce54e362c5f1859a467d749d6e5e5b237b",
                    "transactionIndex": "0x1a",
                }
            ],
        }

        with patch.object(client, "_make_request", return_value=mock_response):
            swap_events = client.get_swap_events(
                "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e", 1000, 2000
            )

            assert len(swap_events) == 1
            swap_event = swap_events[0]

            # Should have zero values for all data fields when data is too short
            assert swap_event.net_pt_out == 0
            assert swap_event.net_sy_out == 0
            assert swap_event.net_sy_fee == 0
            assert swap_event.net_sy_to_reserve == 0

            # But addresses should still be parsed correctly
            assert swap_event.caller == "0x888888888889758f76e7103c6cbf23abbf58f946"
            assert swap_event.receiver == "0xf342d4bde4ec5b4bba94c17ab4c92ee3792abd5e"
