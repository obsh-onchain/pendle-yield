"""
Example: Getting Epoch Votes Snapshot

This example demonstrates how to get the votes snapshot for a Pendle epoch.
The snapshot represents the state of all active votes at the START of the epoch
(Thursday 00:00 UTC), which is when incentive rates are adjusted.

Key concepts:
- Snapshots are calculated at epoch start (Thursday 00:00 UTC)
- Votes cast DURING an epoch affect the NEXT epoch's snapshot
- VePendle values decay over time based on bias and slope
- Expired votes (vePendle <= 0) are filtered out
- Snapshots are cached for both past and current epochs
"""

import os
from datetime import timedelta

from pendle_yield import PendleEpoch, PendleYieldClient


def main():
    # Get API key from environment
    api_key = os.getenv("ETHERSCAN_API_KEY")
    if not api_key:
        print("Error: ETHERSCAN_API_KEY environment variable not set")
        return

    # Initialize client with caching enabled
    with PendleYieldClient(
        etherscan_api_key=api_key,
        db_path="cache.db",
    ) as client:
        # Get current epoch
        current_epoch = PendleEpoch()
        print(f"\n{'='*80}")
        print(f"Current Epoch: {current_epoch}")
        print(f"Start: {current_epoch.start_datetime}")
        print(f"End: {current_epoch.end_datetime}")
        print(f"{'='*80}\n")

        # Get snapshot for current epoch
        # This snapshot was taken at the START of the current epoch
        print("Fetching votes snapshot for current epoch...")
        snapshot = client.get_epoch_votes_snapshot(current_epoch)

        print(f"\nSnapshot Details:")
        print(f"  Snapshot Time: {snapshot.snapshot_timestamp}")
        print(f"  Total Active Votes: {len(snapshot.votes)}")
        print(f"  Total vePendle: {snapshot.total_ve_pendle:,.2f}")

        # Show top 10 votes by vePendle value
        if snapshot.votes:
            print(f"\nTop 10 Votes by vePendle Value:")
            print(f"{'Voter':<44} {'Pool':<44} {'vePendle':>15}")
            print("-" * 105)

            sorted_votes = sorted(
                snapshot.votes, key=lambda v: v.ve_pendle_value, reverse=True
            )
            for vote in sorted_votes[:10]:
                print(
                    f"{vote.voter_address:<44} {vote.pool_address:<44} {vote.ve_pendle_value:>15,.2f}"
                )

        # Get snapshot for previous epoch
        previous_epoch_start = current_epoch.start_datetime - timedelta(days=7)
        previous_epoch = PendleEpoch(previous_epoch_start)

        print(f"\n{'='*80}")
        print(f"Previous Epoch: {previous_epoch}")
        print(f"{'='*80}\n")

        print("Fetching votes snapshot for previous epoch...")
        previous_snapshot = client.get_epoch_votes_snapshot(previous_epoch)

        print(f"\nSnapshot Details:")
        print(f"  Snapshot Time: {previous_snapshot.snapshot_timestamp}")
        print(f"  Total Active Votes: {len(previous_snapshot.votes)}")
        print(f"  Total vePendle: {previous_snapshot.total_ve_pendle:,.2f}")

        # Compare snapshots
        print(f"\n{'='*80}")
        print("Snapshot Comparison")
        print(f"{'='*80}\n")

        vote_change = len(snapshot.votes) - len(previous_snapshot.votes)
        ve_pendle_change = snapshot.total_ve_pendle - previous_snapshot.total_ve_pendle

        print(f"Vote Count Change: {vote_change:+d}")
        print(f"Total vePendle Change: {ve_pendle_change:+,.2f}")

        # Analyze vote changes
        current_voters = {
            (v.voter_address, v.pool_address) for v in snapshot.votes
        }
        previous_voters = {
            (v.voter_address, v.pool_address) for v in previous_snapshot.votes
        }

        new_votes = current_voters - previous_voters
        removed_votes = previous_voters - current_voters

        print(f"\nNew Votes: {len(new_votes)}")
        print(f"Removed Votes: {len(removed_votes)}")
        print(f"Continuing Votes: {len(current_voters & previous_voters)}")

        # Note about caching
        print(f"\n{'='*80}")
        print("Caching Information")
        print(f"{'='*80}\n")
        print("Both snapshots are now cached in the database.")
        print("Subsequent calls will be instant and won't require API calls.")
        print("\nNote: Snapshots are immutable even for current epochs because")
        print("they represent the state at epoch START, which is in the past.")


if __name__ == "__main__":
    main()

