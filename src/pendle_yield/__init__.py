"""
pendle-yield: Python SDK for interacting with Pendle Finance data.

This package provides a high-level, developer-friendly interface to fetch,
analyze, and work with on-chain data from sources like the Etherscan and
Pendle Finance APIs.
"""

__version__ = "0.1.0"
__author__ = "obsh-onchain"

# Import main classes for easy access
from .client import PendleYieldClient
from .epoch import PendleEpoch
from .etherscan import EtherscanClient
from .etherscan_cached import CachedEtherscanClient
from .exceptions import (
    APIError,
    PendleYieldError,
    RateLimitError,
    ValidationError,
)
from .models import EpochMarketFee

__all__ = [
    "PendleYieldClient",
    "PendleEpoch",
    "EtherscanClient",
    "CachedEtherscanClient",
    "PendleYieldError",
    "APIError",
    "ValidationError",
    "RateLimitError",
    "EpochMarketFee",
    "__version__",
]
