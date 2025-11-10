"""
Data models for the pendle-yield package.

This module defines Pydantic models for API responses and data structures
used throughout the package.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


class VoteEvent(BaseModel):
    """Represents a vote event from the Etherscan API."""

    block_number: int = Field(..., description="Block number where the vote occurred")
    transaction_hash: str = Field(..., description="Transaction hash of the vote")
    voter_address: str = Field(..., description="Address of the voter")
    pool_address: str = Field(..., description="Address of the pool being voted for")
    weight: int = Field(..., description="Vote weight value")
    bias: int = Field(..., description="Vote bias value")
    slope: int = Field(..., description="Vote slope value")
    timestamp: datetime | None = Field(None, description="Timestamp of the vote")

    @field_validator("voter_address", "pool_address")
    @classmethod
    def validate_ethereum_address(cls, v: str) -> str:
        """Validate that the address is a valid Ethereum address format."""
        if not v.startswith("0x") or len(v) != 42:
            raise ValueError("Invalid Ethereum address format")
        return v.lower()

    @field_validator("weight", "bias", "slope")
    @classmethod
    def validate_non_negative(cls, v: int) -> int:
        """Validate that weight, bias and slope are non-negative."""
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v


class EnrichedVoteEvent(BaseModel):
    """Represents a vote event enriched with pool information."""

    # Vote event data
    block_number: int = Field(..., description="Block number where the vote occurred")
    transaction_hash: str = Field(..., description="Transaction hash of the vote")
    voter_address: str = Field(..., description="Address of the voter")
    pool_address: str = Field(..., description="Address of the pool being voted for")
    weight: int = Field(..., description="Vote weight value")
    bias: int = Field(..., description="Vote bias value")
    slope: int = Field(..., description="Vote slope value")
    timestamp: datetime | None = Field(None, description="Timestamp of the vote")

    # Pool information from PoolInfo
    pool_name: str = Field(..., description="Human-readable name of the pool")
    pool_symbol: str = Field(..., description="Pool symbol")
    protocol: str = Field(..., description="Protocol name")
    expiry: datetime = Field(..., description="Pool expiry date")
    chain_id: int = Field(..., description="Blockchain chain ID")
    voter_apy: float = Field(..., description="Voter APY")

    # VePendle calculation
    ve_pendle_value: float = Field(
        ..., description="Calculated VePendle value at vote time"
    )

    @field_validator("ve_pendle_value")
    @classmethod
    def validate_ve_pendle_non_negative(cls, v: float) -> float:
        """Validate that VePendle value is non-negative."""
        if v < 0:
            raise ValueError("VePendle value must be non-negative")
        return v

    @staticmethod
    def calculate_ve_pendle_value(
        bias: int, slope: int, timestamp: datetime | None
    ) -> float:
        """
        Calculate VePendle value using bias, slope, and timestamp.

        Based on the VeBalanceLib.sol contract:
        VePendle = bias - slope * timestamp

        Args:
            bias: Vote bias value (in wei units)
            slope: Vote slope value (in wei units)
            timestamp: Block timestamp of the vote

        Returns:
            VePendle value scaled to readable units (divided by 10^18)
        """
        if timestamp is None:
            return 0.0

        # Convert datetime to Unix timestamp
        unix_timestamp = int(timestamp.timestamp())

        # VePendle = bias - slope * timestamp
        # If result is negative or zero, the vote has expired
        ve_value_wei = bias - slope * unix_timestamp

        # Convert from wei to readable units and ensure non-negative
        ve_value = max(0.0, float(ve_value_wei) / 10**18)

        return ve_value

    @classmethod
    def from_vote_and_pool(
        cls, vote_event: VoteEvent, pool_info: "PoolInfo"
    ) -> "EnrichedVoteEvent":
        """Create an enriched vote event from separate vote and pool data."""
        # Calculate VePendle value
        ve_pendle_value = cls.calculate_ve_pendle_value(
            vote_event.bias, vote_event.slope, vote_event.timestamp
        )

        return cls(
            # Vote data
            block_number=vote_event.block_number,
            transaction_hash=vote_event.transaction_hash,
            voter_address=vote_event.voter_address,
            pool_address=vote_event.pool_address,
            weight=vote_event.weight,
            bias=vote_event.bias,
            slope=vote_event.slope,
            timestamp=vote_event.timestamp,
            # Pool data from PoolInfo
            pool_name=pool_info.name,
            pool_symbol=pool_info.symbol,
            protocol=pool_info.protocol,
            expiry=pool_info.expiry,
            chain_id=pool_info.chain_id,
            voter_apy=pool_info.voter_apy,
            # VePendle calculation
            ve_pendle_value=ve_pendle_value,
        )


class EtherscanLogEntry(BaseModel):
    """Raw log entry from Etherscan API response."""

    address: str
    topics: list[str]
    data: str
    block_number: str = Field(alias="blockNumber")
    transaction_hash: str = Field(alias="transactionHash")
    transaction_index: str = Field(alias="transactionIndex")
    block_hash: str = Field(alias="blockHash")
    log_index: str = Field(alias="logIndex")
    time_stamp: str = Field(alias="timeStamp")
    gas_price: str = Field(alias="gasPrice")
    gas_used: str = Field(alias="gasUsed")
    removed: bool = Field(default=False)

    model_config = ConfigDict(populate_by_name=True)


class EtherscanResponse(BaseModel):
    """Response structure from Etherscan API."""

    status: str
    message: str
    result: list[EtherscanLogEntry] | str


class PendlePoolResponse(BaseModel):
    """Response structure from Pendle API for pool data."""

    pools: list[dict[str, Any]]
    total: int
    page: int
    limit: int


class PoolInfo(BaseModel):
    """Pool information from the voter APR API response."""

    id: str = Field(..., description="Pool ID")
    chain_id: int = Field(..., alias="chainId", description="Blockchain chain ID")
    address: str = Field(..., description="Pool contract address")
    symbol: str = Field(..., description="Pool symbol")
    expiry: datetime = Field(..., description="Pool expiry date")
    protocol: str = Field(..., description="Protocol name")
    underlying_pool: str = Field(
        "", alias="underlyingPool", description="Underlying pool address"
    )
    voter_apy: float = Field(..., alias="voterApy", description="Voter APY")
    accent_color: str = Field(..., alias="accentColor", description="UI accent color")
    name: str = Field(..., description="Pool name")
    farm_simple_name: str = Field(
        ..., alias="farmSimpleName", description="Simple farm name"
    )
    farm_simple_icon: str = Field(
        ..., alias="farmSimpleIcon", description="Simple farm icon URL"
    )
    farm_pro_name: str = Field(..., alias="farmProName", description="Pro farm name")
    farm_pro_icon: str = Field(
        ..., alias="farmProIcon", description="Pro farm icon URL"
    )

    @field_validator("address")
    @classmethod
    def validate_ethereum_address(cls, v: str) -> str:
        """Validate that the address is a valid Ethereum address format."""
        if not v.startswith("0x") or len(v) != 42:
            raise ValueError("Invalid Ethereum address format")
        return v.lower()


class PoolVoterData(BaseModel):
    """Pool voter data including APR metrics."""

    pool: PoolInfo = Field(..., description="Pool information")
    current_voter_apr: float = Field(
        ..., alias="currentVoterApr", description="Current voter APR"
    )
    last_epoch_voter_apr: float = Field(
        ..., alias="lastEpochVoterApr", description="Last epoch voter APR"
    )
    current_swap_fee: float = Field(
        ..., alias="currentSwapFee", description="Current swap fee"
    )
    last_epoch_swap_fee: float = Field(
        ..., alias="lastEpochSwapFee", description="Last epoch swap fee"
    )
    projected_voter_apr: float = Field(
        ..., alias="projectedVoterApr", description="Projected voter APR"
    )


class VoterAprResponse(BaseModel):
    """Response from the voter APR API endpoint."""

    results: list[PoolVoterData] = Field(..., description="List of pool voter data")
    total_pools: int = Field(
        ..., alias="totalPools", description="Total number of pools"
    )
    total_fee: float = Field(
        ..., alias="totalFee", description="Total fee across all pools"
    )
    timestamp: datetime = Field(..., description="Response timestamp")


class MarketInfo(BaseModel):
    """Market information for market fees API."""

    id: str = Field(..., description="Market ID")


class MarketFeeValue(BaseModel):
    """Individual fee data point for a market."""

    time: datetime = Field(..., description="Timestamp of the fee data")
    total_fees: float = Field(
        ..., alias="totalFees", description="Total fees for this period"
    )

    @field_validator("total_fees")
    @classmethod
    def validate_total_fees_non_negative(cls, v: float) -> float:
        """Validate that total fees are non-negative."""
        if v < 0:
            raise ValueError("Total fees must be non-negative")
        return v


class MarketFeeData(BaseModel):
    """Market fee data containing market info and fee values."""

    market: MarketInfo = Field(..., description="Market information")
    values: list[MarketFeeValue] = Field(
        ..., description="List of fee values over time"
    )


class MarketFeesResponse(BaseModel):
    """Response from the market fees chart API endpoint."""

    results: list[MarketFeeData] = Field(..., description="List of market fee data")


class EpochMarketFee(BaseModel):
    """Represents market fees for a specific epoch."""

    chain_id: int = Field(..., description="Blockchain chain ID")
    market_address: str = Field(..., description="Market contract address")
    total_fee: float = Field(..., description="Total fees accumulated in the epoch")
    epoch_start: datetime = Field(..., description="Epoch start timestamp")
    epoch_end: datetime = Field(..., description="Epoch end timestamp")

    @field_validator("market_address")
    @classmethod
    def validate_ethereum_address(cls, v: str) -> str:
        """Validate that the address is a valid Ethereum address format."""
        if not v.startswith("0x") or len(v) != 42:
            raise ValueError("Invalid Ethereum address format")
        return v.lower()

    @field_validator("total_fee")
    @classmethod
    def validate_total_fee_non_negative(cls, v: float) -> float:
        """Validate that total fee is non-negative."""
        if v < 0:
            raise ValueError("Total fee must be non-negative")
        return v

    @staticmethod
    def parse_market_id(market_id: str) -> tuple[int, str]:
        """
        Parse market ID into chain_id and address.

        Market IDs are in the format "chainId-address", e.g. "1-0x123..."

        Args:
            market_id: Market ID string

        Returns:
            Tuple of (chain_id, address)

        Raises:
            ValueError: If market ID format is invalid
        """
        parts = market_id.split("-", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid market ID format: {market_id}")

        try:
            chain_id = int(parts[0])
        except ValueError as e:
            raise ValueError(f"Invalid chain ID in market ID: {market_id}") from e

        address = parts[1]
        if not address.startswith("0x"):
            address = f"0x{address}"

        return chain_id, address


class VoteSnapshot(BaseModel):
    """Represents a single vote in an epoch snapshot."""

    voter_address: str = Field(..., description="Address of the voter")
    pool_address: str = Field(..., description="Address of the pool being voted for")
    bias: int = Field(..., description="Vote bias value")
    slope: int = Field(..., description="Vote slope value")
    ve_pendle_value: float = Field(
        ..., description="Calculated VePendle value at snapshot time"
    )
    last_vote_block: int = Field(
        ..., description="Block number of the last vote that affected this state"
    )
    last_vote_timestamp: datetime = Field(
        ..., description="Timestamp of the last vote that affected this state"
    )

    @field_validator("voter_address", "pool_address")
    @classmethod
    def validate_ethereum_address(cls, v: str) -> str:
        """Validate that the address is a valid Ethereum address format."""
        if not v.startswith("0x") or len(v) != 42:
            raise ValueError("Invalid Ethereum address format")
        return v.lower()

    @field_validator("bias", "slope")
    @classmethod
    def validate_non_negative(cls, v: int) -> int:
        """Validate that bias and slope are non-negative."""
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v

    @field_validator("ve_pendle_value")
    @classmethod
    def validate_ve_pendle_non_negative(cls, v: float) -> float:
        """Validate that VePendle value is non-negative."""
        if v < 0:
            raise ValueError("VePendle value must be non-negative")
        return v


class EpochVotesSnapshot(BaseModel):
    """Represents the complete votes snapshot for an epoch."""

    epoch_start: datetime = Field(..., description="Epoch start timestamp")
    epoch_end: datetime = Field(..., description="Epoch end timestamp")
    snapshot_timestamp: datetime = Field(
        ..., description="Timestamp when snapshot was taken (always epoch start)"
    )
    votes: list[VoteSnapshot] = Field(
        ..., description="List of active votes in the snapshot"
    )
    total_ve_pendle: float = Field(
        ..., description="Sum of all vePendle values in the snapshot"
    )

    @field_validator("total_ve_pendle")
    @classmethod
    def validate_total_ve_pendle_non_negative(cls, v: float) -> float:
        """Validate that total vePendle is non-negative."""
        if v < 0:
            raise ValueError("Total vePendle must be non-negative")
        return v
