"""
Integration tests for the PendleYieldClient class.
"""

from datetime import datetime
from unittest.mock import patch

import pytest

from pendle_yield.client import PendleYieldClient
from pendle_yield.exceptions import ValidationError
from pendle_yield.models import EnrichedVoteEvent, VoteEvent, PoolInfo


class TestPendleYieldClient:
    """Integration test cases for PendleYieldClient."""

    @pytest.fixture
    def client(self):
        """Create a test client instance."""
        return PendleYieldClient(etherscan_api_key="test_key")

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

    @pytest.fixture
    def mock_pool_info(self):
        """Create mock pool info."""
        return PoolInfo(
            id="1-0x0987654321098765432109876543210987654321",
            chainId=1,
            address="0x0987654321098765432109876543210987654321",
            symbol="PENDLE-LPT",
            expiry=datetime(2024, 12, 31),
            protocol="Test Protocol",
            voterApy=0.055,
            accentColor="#A8A8A8",
            name="Test Pool",
            farmSimpleName="Test Pool",
            farmSimpleIcon="https://example.com/icon.svg",
            farmProName="Test Pool Pro",
            farmProIcon="https://example.com/pro-icon.svg",
        )

    def test_init_valid_api_key(self):
        """Test client initialization with valid API key."""
        client = PendleYieldClient(etherscan_api_key="test_key")
        assert client.etherscan_api_key == "test_key"
        assert client.etherscan_base_url == "https://api.etherscan.io/api"
        assert client.pendle_base_url == "https://api-v2.pendle.finance/core"

    def test_init_empty_api_key(self):
        """Test client initialization with empty API key raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PendleYieldClient(etherscan_api_key="")

        assert "Etherscan API key is required" in str(exc_info.value)
        assert exc_info.value.field == "etherscan_api_key"

    def test_init_custom_urls(self):
        """Test client initialization with custom URLs."""
        client = PendleYieldClient(
            etherscan_api_key="test_key",
            etherscan_base_url="https://custom-etherscan.com",
            pendle_base_url="https://custom-pendle.com",
        )
        assert client.etherscan_base_url == "https://custom-etherscan.com"
        assert client.pendle_base_url == "https://custom-pendle.com"

    def test_context_manager(self):
        """Test client as context manager."""
        with PendleYieldClient(etherscan_api_key="test_key") as client:
            assert isinstance(client, PendleYieldClient)
        # Client should be closed after context exit

    def test_get_vote_events_delegation(self, client):
        """Test that get_vote_events delegates to EtherscanClient."""
        mock_vote_events = [
            VoteEvent(
                block_number=12345,
                transaction_hash="0xabc123",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                bias=1000,
                slope=500,
            )
        ]

        with patch.object(
            client._etherscan_client, "get_vote_events", return_value=mock_vote_events
        ):
            result = client.get_vote_events(12345)
            assert result == mock_vote_events
            client._etherscan_client.get_vote_events.assert_called_once_with(12345)

    def test_get_votes_integration(self, client, mock_vote_event, mock_pool_info):
        """Test the integrated get_votes method using voter APR data."""
        from pendle_yield.models import VoterAprResponse, PoolVoterData

        # Create mock voter APR response
        mock_voter_apr_response = VoterAprResponse(
            results=[
                PoolVoterData(
                    pool=mock_pool_info,
                    currentVoterApr=0.055,
                    lastEpochVoterApr=0.050,
                    currentSwapFee=1000.0,
                    lastEpochSwapFee=950.0,
                    projectedVoterApr=0.060,
                )
            ],
            totalPools=1,
            totalFee=1000.0,
            timestamp=datetime.now(),
        )

        with patch.object(client, "get_vote_events", return_value=[mock_vote_event]):
            with patch.object(
                client._pendle_client,
                "get_pool_voter_apr_data",
                return_value=mock_voter_apr_response,
            ):
                enriched_votes = client.get_votes(12345)

                assert len(enriched_votes) == 1
                vote = enriched_votes[0]
                assert isinstance(vote, EnrichedVoteEvent)
                assert vote.block_number == 12345
                assert vote.pool_name == "Test Pool"
                assert vote.protocol == "Test Protocol"
                assert vote.voter_apy == 0.055


class TestValidationEdgeCases:
    """Test edge cases for validation."""

    def test_ethereum_address_validation(self):
        """Test Ethereum address validation in models."""
        # Valid address
        vote = VoteEvent(
            block_number=1,
            transaction_hash="0xabc",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            bias=100,
            slope=50,
        )
        assert vote.voter_address == "0x1234567890123456789012345678901234567890"

        # Invalid address format
        with pytest.raises(ValueError):
            VoteEvent(
                block_number=1,
                transaction_hash="0xabc",
                voter_address="invalid_address",
                pool_address="0x0987654321098765432109876543210987654321",
                bias=100,
                slope=50,
            )

    def test_negative_values_validation(self):
        """Test validation of negative values."""
        with pytest.raises(ValueError):
            VoteEvent(
                block_number=1,
                transaction_hash="0xabc",
                voter_address="0x1234567890123456789012345678901234567890",
                pool_address="0x0987654321098765432109876543210987654321",
                bias=-100,  # Invalid negative bias
                slope=50,
            )

    def test_enriched_vote_creation(self):
        """Test EnrichedVoteEvent creation from separate objects."""
        vote = VoteEvent(
            block_number=1,
            transaction_hash="0xabc",
            voter_address="0x1234567890123456789012345678901234567890",
            pool_address="0x0987654321098765432109876543210987654321",
            bias=100,
            slope=50,
        )

        pool_info = PoolInfo(
            id="1-0x0987654321098765432109876543210987654321",
            chainId=1,
            address="0x0987654321098765432109876543210987654321",
            symbol="PENDLE-LPT",
            expiry=datetime(2024, 12, 31),
            protocol="Test Protocol",
            voterApy=0.055,
            accentColor="#A8A8A8",
            name="Test Pool",
            farmSimpleName="Test Pool",
            farmSimpleIcon="https://example.com/icon.svg",
            farmProName="Test Pool Pro",
            farmProIcon="https://example.com/pro-icon.svg",
        )

        enriched = EnrichedVoteEvent.from_vote_and_pool(vote, pool_info)
        assert enriched.block_number == 1
        assert enriched.pool_name == "Test Pool"
        assert enriched.bias == 100
        assert enriched.protocol == "Test Protocol"
        assert enriched.voter_apy == 0.055
