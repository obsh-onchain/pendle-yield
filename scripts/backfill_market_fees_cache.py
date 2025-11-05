"""
Backfill script to populate market fees cache from November 2022 to present.

This script iterates through all Pendle epochs from the start date (2022-11-23)
until now and fetches market fees for each epoch using the cached client.
Finished epochs will be cached permanently in the database.
"""

import os
from datetime import UTC, datetime, timedelta

from pendle_yield import CachedPendleYieldClient, PendleEpoch


def main() -> None:
    """Backfill the market fees cache from November 2022 to present."""
    # Get API key from environment
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
    if not etherscan_api_key:
        raise ValueError("ETHERSCAN_API_KEY environment variable not set")

    # Start date: November 23, 2022 00:00 UTC
    start_date = datetime(2022, 11, 23, 0, 0, 0, tzinfo=UTC)
    current_date = datetime.now(UTC)

    print("=" * 80)
    print("Market Fees Cache Backfill Script")
    print("=" * 80)
    print(f"Start date: {start_date.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"End date:   {current_date.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Database:   cache.db")
    print("=" * 80)

    # Initialize the cached client
    with CachedPendleYieldClient(
        etherscan_api_key=etherscan_api_key, db_path="cache.db"
    ) as client:
        # Calculate total epochs to process
        total_days = (current_date - start_date).days
        total_epochs = total_days // 7 + 1

        print(f"\nEstimated epochs to process: ~{total_epochs}")
        print("\nStarting backfill process...\n")

        # Track statistics
        epochs_processed = 0
        epochs_cached = 0
        epochs_skipped = 0
        total_markets = 0

        # Iterate through epochs
        current_epoch_date = start_date

        while current_epoch_date < current_date:
            # Create epoch for this date
            epoch = PendleEpoch(current_epoch_date)

            # Skip if this is the current epoch (don't cache it)
            if epoch.is_current:
                print(
                    f"Skipping current epoch: {epoch} (not caching current epochs)"
                )
                epochs_skipped += 1
                break

            try:
                # Fetch market fees (will cache if not already cached)
                fees = client.get_market_fees_by_epoch(epoch)

                epochs_processed += 1
                total_markets += len(fees)

                # Calculate total fees for this epoch
                total_fees = sum(fee.total_fee for fee in fees)

                # Print progress
                status = "CACHED" if epoch.is_past else "FETCHED"
                print(
                    f"[{epochs_processed:3d}/{total_epochs}] {epoch} - "
                    f"{status} - {len(fees):3d} markets - "
                    f"${total_fees:12,.2f} total fees"
                )

                if epoch.is_past:
                    epochs_cached += 1

            except Exception as e:
                print(f"ERROR processing {epoch}: {str(e)}")
                # Continue with next epoch even if this one fails
                pass

            # Move to next epoch (add 7 days)
            current_epoch_date += timedelta(days=7)

        # Print summary
        print("\n" + "=" * 80)
        print("Backfill Complete!")
        print("=" * 80)
        print(f"Total epochs processed:  {epochs_processed}")
        print(f"Epochs cached:           {epochs_cached}")
        print(f"Epochs skipped:          {epochs_skipped}")
        print(f"Total market records:    {total_markets}")
        print(f"Average markets/epoch:   {total_markets / max(epochs_processed, 1):.1f}")
        print("=" * 80)
        print(
            "\nCache database 'cache.db' has been populated with historical market fees."
        )
        print("Subsequent queries for these epochs will be instant (no API calls).")


if __name__ == "__main__":
    main()
