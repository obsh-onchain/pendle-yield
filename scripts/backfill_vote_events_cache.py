"""
Backfill script to populate vote events cache from November 2022 to present.

This script iterates through block ranges from the first vote event (block 16033191)
until the latest finished block and fetches vote events using the cached Etherscan client.
All blocks will be cached permanently in the database to avoid redundant API calls.
"""

import os
from datetime import datetime

from pendle_yield import CachedEtherscanClient


def main() -> None:
    """Backfill the vote events cache from block 16,033,191 to the latest finished block."""
    # Get API key from environment
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
    if not etherscan_api_key:
        raise ValueError("ETHERSCAN_API_KEY environment variable not set")

    # Define block range
    start_block = 16_033_191  # First block with vote events
    batch_size = 100_000      # Blocks per batch for progress visibility

    # Initialize the cached Etherscan client
    with CachedEtherscanClient(
        api_key=etherscan_api_key, db_path="cache.db"
    ) as client:
        # Get the latest finished block using current timestamp
        current_timestamp = int(datetime.now().timestamp())
        end_block = client.get_block_number_by_timestamp(current_timestamp, "before")

        print("=" * 80)
        print("Vote Events Cache Backfill Script")
        print("=" * 80)
        print(f"Start block:    {start_block:,}")
        print(f"End block:      {end_block:,} (latest finished)")
        print(f"Batch size:     {batch_size:,} blocks")
        print("Database:       cache.db")
        print("=" * 80)
        # Calculate total batches to process
        total_blocks = end_block - start_block + 1
        total_batches = (total_blocks + batch_size - 1) // batch_size

        print(f"\nTotal blocks:   {total_blocks:,}")
        print(f"Total batches:  {total_batches}")
        print("\nStarting backfill process...\n")

        # Track statistics
        batches_processed = 0
        total_events = 0
        current_block = start_block

        while current_block <= end_block:
            # Calculate batch range
            batch_end = min(current_block + batch_size - 1, end_block)

            try:
                # Fetch vote events (will cache if not already cached)
                events = client.get_vote_events(current_block, batch_end)

                batches_processed += 1
                total_events += len(events)

                # Calculate progress
                blocks_processed = batch_end - start_block + 1
                progress_pct = (blocks_processed / total_blocks) * 100

                # Print progress
                print(
                    f"[{batches_processed:3d}/{total_batches}] "
                    f"Blocks {current_block:,} - {batch_end:,} - "
                    f"{len(events):4d} events - "
                    f"{progress_pct:5.1f}% complete - "
                    f"{total_events:,} total events"
                )

            except Exception as e:
                print(f"ERROR processing blocks {current_block:,} - {batch_end:,}: {str(e)}")
                # Continue with next batch even if this one fails
                pass

            # Move to next batch
            current_block = batch_end + 1

        # Print summary
        print("\n" + "=" * 80)
        print("Backfill Complete!")
        print("=" * 80)
        print(f"Total batches processed:  {batches_processed}")
        print(f"Total vote events found:  {total_events:,}")
        print(f"Average events/batch:     {total_events / max(batches_processed, 1):.1f}")
        print("=" * 80)
        print(
            "\nCache database 'cache.db' has been populated with historical vote events."
        )
        print("Subsequent queries for these blocks will be instant (no API calls).")


if __name__ == "__main__":
    main()
