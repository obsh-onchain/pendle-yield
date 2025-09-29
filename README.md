# pendle-yield

`pendle-yield` is a Python SDK for interacting with Pendle Finance data. It provides a high-level, developer-friendly interface to fetch, analyze, and work with on-chain data from sources like the Etherscan and Pendle Finance APIs.

The primary goal is to simplify data access for developers, analysts, and enthusiasts building tools and strategies around the Pendle ecosystem.

## Installation

```bash
pip install pendle-yield
```

## Quick Start

```python
from pendle_yield import PendleEpoch, PendleYieldClient

# Initialize with your Etherscan API key
client = PendleYieldClient(etherscan_api_key="your_api_key_here")

# Create epoch object, epoch starts on Th 00:00:00 and ends on Wd 23:59:59
epoch = PendleEpoch("2025-08-21")

# Get enriched vote events for the epoch
votes = client.get_votes_by_epoch(epoch)

# Display vote information
for vote in votes:
    print(f"Voter: {vote.voter_address}")
    print(f"Pool: {vote.pool_name} ({vote.protocol})")
    print(f"APY: {vote.voter_apy*100:.2f}%")
    print(f"Bias: {vote.bias:,}")
    print(f"Slope: {vote.slope:,}")
    print(f"VePendle Value: {vote.ve_pendle_value:.4f}")
```

## What it does now

The `get_votes_by_epoch()` method:
1. Fetches vote events from Etherscan for the specified Pendle epoch
2. Enriches them with pool metadata from Pendle Finance API
3. Returns structured data combining both sources

Each vote event includes:
- Voter address and transaction details
- Pool information (name, address, protocol, expiry, current voter APY)
- Vote parameters (bias, slope)
- **VePendle value**: Calculated voting power at the time of the vote using the formula `VePendle = max(0, (bias - slope × timestamp) / 10^18)`

## Requirements

- Python 3.11+
- Etherscan API key (get one at [etherscan.io/apis](https://etherscan.io/apis))

## Development

This project uses [PDM](https://pdm.fming.dev/) for dependency management:

```bash
# Install dependencies
pdm install

# Run tests
pdm run pytest

# Run the example
pdm run python examples/basic_usage.py
