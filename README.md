# pendle-yield

`pendle-yield` is a Python SDK for interacting with Pendle Finance data. It provides a high-level, developer-friendly interface to fetch, analyze, and work with on-chain data from sources like the Etherscan and Pendle Finance APIs.

The primary goal is to simplify data access for developers, analysts, and enthusiasts building tools and strategies around the Pendle ecosystem.

## Installation

> ⚠️ **Alpha Version**: This package is under active development. APIs may change between releases.

Install from PyPI:
```bash
pip install pendle-yield
```

## Quick Start

```python
from pendle_yield import PendleEpoch, PendleYieldClient

# Initialize with your Etherscan API key and optional caching
client = PendleYieldClient(
    etherscan_api_key="your_api_key_here",
    db_path="cache.db"  # Optional: enables caching for better performance
)

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

### Caching

The client supports optional SQLite caching to avoid redundant API calls:

```python
# With caching (recommended for production)
client = PendleYieldClient(
    etherscan_api_key="your_key",
    db_path="cache.db"  # Caches market fees and vote snapshots
)

# Without caching (always fetches fresh data)
client = PendleYieldClient(
    etherscan_api_key="your_key"
)
```

**Caching behavior:**
- **Vote events**: Cached per block range (automatically uses `CachedEtherscanClient`)
- **Market fees**: Cached permanently for past epochs (immutable data)
- **Vote snapshots**: Cached for past and current epochs (snapshot is at epoch start)

## Features

### Vote Events by Epoch

The `get_votes_by_epoch()` method:
1. Fetches vote events from Etherscan for the specified Pendle epoch
2. Enriches them with pool metadata from Pendle Finance API
3. Returns structured data combining both sources

Each vote event includes:
- Voter address and transaction details
- Pool information (name, address, protocol, expiry, current voter APY)
- Vote parameters (bias, slope)
- **VePendle value**: Calculated voting power at the time of the vote using the formula `VePendle = max(0, (bias - slope × timestamp) / 10^18)`

### Epoch Votes Snapshot

The `get_epoch_votes_snapshot()` method provides the state of all active votes at the **start** of an epoch (Thursday 00:00 UTC):

```python
from pendle_yield import PendleEpoch, PendleYieldClient

# Initialize client with caching for better performance
client = PendleYieldClient(
    etherscan_api_key="your_api_key_here",
    db_path="data/cache.db"
)

# Get current epoch
epoch = PendleEpoch()

# Get snapshot at epoch start
snapshot = client.get_epoch_votes_snapshot(epoch)

print(f"Total Active Votes: {len(snapshot.votes)}")
print(f"Total vePendle: {snapshot.total_ve_pendle:,.2f}")

# Analyze individual votes
for vote in snapshot.votes:
    print(f"Voter: {vote.voter_address}")
    print(f"Pool: {vote.pool_address}")
    print(f"vePendle: {vote.ve_pendle_value:,.2f}")
```

**Key concepts:**
- Snapshots are taken at epoch start (Thursday 00:00 UTC) when incentive rates are adjusted
- Votes cast **during** an epoch affect the **next** epoch's snapshot
- VePendle values decay over time based on bias and slope
- Expired votes (vePendle ≤ 0) are automatically filtered out
- Votes persist across epochs unless explicitly removed (weight = 0)
- Snapshots are cached in SQLite for instant retrieval

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
```

### Regenerating the Pendle V2 Client

The Pendle V2 client is auto-generated from the OpenAPI specification. However, the upstream spec has some issues that need to be corrected before generation.

**Step 1: Download and fix the OpenAPI spec**

Run the fix script to download the latest spec and apply necessary corrections:

```bash
pdm run python scripts/fix_openapi_spec.py
```

This script:
- Downloads the OpenAPI spec from `https://api-v2.pendle.finance/core/docs-json`
- Fixes the `TotalFeesWithTimestamp` schema by removing `totalFees` from required fields (it's sometimes missing in API responses)
- Saves the corrected spec to `corrected-openapi.json`

**Step 2: Generate the client code**

Use the corrected spec to generate the client:

```bash
openapi-python-client generate --path corrected-openapi.json --meta pdm --output-path src --config openapi.yaml --overwrite
```

**Note:** Always run the fix script first when regenerating the client to ensure the spec is up-to-date and corrected.
