"""
Backfill script to populate vote snapshots cache from first epoch to current.

This script iterates through all Pendle epochs from the first voting epoch
(2022-11-23 00:00 UTC) until the current epoch and fetches vote snapshots
using the cached client. All snapshots will be cached permanently in the
database to avoid redundant API calls.

The script efficiently builds snapshots by:
1. Starting from the first epoch (empty state)
2. Recursively building each snapshot from the previous one
3. Caching each snapshot as it's computed
4. Leveraging the cache for subsequent epochs
"""

import os
from datetime import UTC, datetime, timedelta

from pendle_yield import PendleEpoch, PendleYieldClient
from pendle_yield.client import FIRST_EPOCH_START


def main() -> None:
    """Backfill the vote snapshots cache from first epoch to current epoch."""
    # Get API key from environment
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
    if not etherscan_api_key:
        raise ValueError("ETHERSCAN_API_KEY environment variable not set")

    # Initialize the client with caching enabled
    with PendleYieldClient(
        etherscan_api_key=etherscan_api_key,
        db_path="cache.db",
    ) as client:
        # Get current epoch
        current_epoch = PendleEpoch()

        # Calculate total epochs to process
        first_epoch = PendleEpoch(FIRST_EPOCH_START)
        total_epochs = int(
            (current_epoch.start_datetime - first_epoch.start_datetime).days / 7
        ) + 1

        print("=" * 80)
        print("Vote Snapshots Cache Backfill Script")
        print("=" * 80)
        print(f"First epoch:    {first_epoch} ({first_epoch.start_datetime.strftime('%Y-%m-%d')})")
        print(f"Current epoch:  {current_epoch} ({current_epoch.start_datetime.strftime('%Y-%m-%d')})")
        print(f"Total epochs:   {total_epochs}")
        print("Database:       cache.db")
        print("=" * 80)
        print("\nNote: Snapshots are built recursively from previous epochs.")
        print("The first few epochs will be slower, then it speeds up significantly!")
        print("\nStarting backfill process...\n")

        # Track statistics
        epochs_processed = 0
        total_votes = 0
        total_ve_pendle = 0.0
        epoch_start_time = datetime.now()

        # Iterate through all epochs
        current_epoch_iter = PendleEpoch(FIRST_EPOCH_START)

        while current_epoch_iter.start_datetime <= current_epoch.start_datetime:
            try:
                batch_start = datetime.now()

                # Fetch snapshot (will cache if not already cached)
                snapshot = client.get_epoch_votes_snapshot(current_epoch_iter)

                batch_duration = (datetime.now() - batch_start).total_seconds()
                epochs_processed += 1
                total_votes += len(snapshot.votes)
                total_ve_pendle += snapshot.total_ve_pendle

                # Calculate progress
                progress_pct = (epochs_processed / total_epochs) * 100

                # Print progress
                print(
                    f"[{epochs_processed:3d}/{total_epochs}] "
                    f"{current_epoch_iter.start_datetime.strftime('%Y-%m-%d')} - "
                    f"{len(snapshot.votes):5d} votes - "
                    f"{snapshot.total_ve_pendle:12,.2f} vePendle - "
                    f"{batch_duration:5.2f}s - "
                    f"{progress_pct:5.1f}% complete"
                )

            except Exception as e:
                print(
                    f"ERROR processing epoch {current_epoch_iter.start_datetime.strftime('%Y-%m-%d')}: {str(e)}"
                )
                # Continue with next epoch even if this one fails
                pass

            # Move to next epoch (7 days later)
            next_epoch_start = current_epoch_iter.start_datetime + timedelta(days=7)
            current_epoch_iter = PendleEpoch(next_epoch_start)

        # Calculate total duration
        total_duration = (datetime.now() - epoch_start_time).total_seconds()

        # Print summary
        print("\n" + "=" * 80)
        print("Backfill Complete!")
        print("=" * 80)
        print(f"Total epochs processed:   {epochs_processed}")
        print(f"Total votes cached:       {total_votes:,}")
        print(f"Average votes/epoch:      {total_votes / max(epochs_processed, 1):.1f}")
        print(f"Total vePendle (current): {total_ve_pendle:,.2f}")
        print(f"Total duration:           {total_duration:.1f}s ({total_duration/60:.1f} min)")
        print(f"Average time/epoch:       {total_duration / max(epochs_processed, 1):.2f}s")
        print("=" * 80)
        print("\nCache database 'cache.db' has been populated with vote snapshots.")
        print("Subsequent queries for these epochs will be instant (no API calls).")
        print("\nYou can now:")
        print("  • Analyze historical voting patterns")
        print("  • Track vePendle distribution over time")
        print("  • Compare snapshots across epochs")
        print("  • Build voting analytics dashboards")


if __name__ == "__main__":
    main()

