#!/usr/bin/env python3
"""
Pendle Voter Leaderboard for August 2025

This example reproduces the Pendle voter leaderboard for August 2025,
calculating rewards based on vote distribution and pool fees.

The leaderboard format:
#
User, Total Rewards, USDT per 1000 vePENDLE, vePENDLE Balance
1, 0x025...b604, 496 USDT, 337.60, 1,480
2, 0xacc...0c0b, 1,809 USDT, 308.44, 5,867
"""

import os
from collections import defaultdict

from pendle_yield import PendleEpoch, PendleYieldClient
from pendle_yield.models import EnrichedVoteEvent


def format_address(address: str) -> str:
    """Format address for display (first 6 and last 4 characters)."""
    return f"{address[:6]}...{address[-4:]}"


def get_august_2025_epochs() -> tuple[list[PendleEpoch], list[PendleEpoch]]:
    """
    Get the Pendle epochs for August 2025.

    According to the task, we need epochs that ended in August:
    - July 31 epoch (ends Aug 7) - uses votes from July 24 epoch
    - Aug 7 epoch (ends Aug 14) - uses votes from July 31 epoch
    - Aug 14 epoch (ends Aug 21) - uses votes from Aug 7 epoch
    - Aug 21 epoch (ends Aug 28) - uses votes from Aug 14 epoch

    We exclude the Aug 28 epoch as specified.

    Returns:
        Tuple of (fee_epochs, vote_epochs) where vote_epochs[i] determines
        rewards for fee_epochs[i]
    """
    # Epochs where we collect fees (August 2025)
    fee_epoch_dates = [
        "2025-07-31",  # Epoch ending Aug 7
        "2025-08-07",  # Epoch ending Aug 14
        "2025-08-14",  # Epoch ending Aug 21
        "2025-08-21",  # Epoch ending Aug 28
    ]

    # Previous epochs where votes were cast that determine August rewards
    vote_epoch_dates = [
        "2025-07-24",  # Votes for July 31 epoch
        "2025-07-31",  # Votes for Aug 7 epoch
        "2025-08-07",  # Votes for Aug 14 epoch
        "2025-08-14",  # Votes for Aug 21 epoch
    ]

    fee_epochs = [PendleEpoch(date_str) for date_str in fee_epoch_dates]
    vote_epochs = [PendleEpoch(date_str) for date_str in vote_epoch_dates]

    return fee_epochs, vote_epochs


def calculate_epoch_end_ve_pendle_per_pool(
    votes: list[EnrichedVoteEvent], epoch: PendleEpoch
) -> dict[tuple[str, str], float]:
    """
    Calculate VePendle values at the end of an epoch for each voter per pool.

    For each voter-pool combination, we use their latest vote for that specific pool
    in the epoch and calculate the VePendle value at the epoch end time.

    Returns:
        Dict mapping (voter_address, pool_address) -> ve_pendle_value
    """
    voter_pool_latest_vote = {}

    # Find the latest vote for each voter-pool combination in this epoch
    for vote in votes:
        voter_addr = vote.voter_address.lower()
        pool_addr = vote.pool_address.lower()
        key = (voter_addr, pool_addr)

        if (
            key not in voter_pool_latest_vote
            or vote.timestamp > voter_pool_latest_vote[key].timestamp
        ):
            voter_pool_latest_vote[key] = vote

    # Calculate VePendle at epoch end for each voter-pool combination
    voter_pool_ve_pendle = {}
    epoch_end_time = epoch.end_datetime

    for (voter_addr, pool_addr), vote in voter_pool_latest_vote.items():
        # Calculate VePendle at epoch end using the vote's bias and slope
        ve_pendle_at_end = EnrichedVoteEvent.calculate_ve_pendle_value(
            vote.bias, vote.slope, epoch_end_time
        )
        voter_pool_ve_pendle[(voter_addr, pool_addr)] = ve_pendle_at_end

    return voter_pool_ve_pendle


def calculate_total_ve_pendle_per_voter(
    voter_pool_ve_pendle: dict[tuple[str, str], float],
) -> dict[str, float]:
    """
    Calculate total VePendle for each voter across all pools.

    Args:
        voter_pool_ve_pendle: Dict mapping (voter_address, pool_address) -> ve_pendle_value

    Returns:
        Dict mapping voter_address -> total_ve_pendle_value
    """
    voter_total_ve_pendle = defaultdict(float)

    for (voter_addr, _pool_addr), ve_pendle in voter_pool_ve_pendle.items():
        voter_total_ve_pendle[voter_addr] += ve_pendle

    return dict(voter_total_ve_pendle)


def calculate_pool_rewards(
    votes: list[EnrichedVoteEvent], epoch: PendleEpoch, pool_fees: dict[str, float]
) -> dict[str, float]:
    """
    Calculate rewards for each voter based on their vote distribution.

    For each pool:
    1. Calculate VePendle voting power at epoch end for each voter-pool combination
    2. Calculate each user's share of that specific pool
    3. Distribute pool fees proportionally
    """
    # Get VePendle values at epoch end per voter-pool combination
    voter_pool_ve_pendle = calculate_epoch_end_ve_pendle_per_pool(votes, epoch)

    # Calculate rewards for each voter
    voter_rewards = defaultdict(float)

    # Group by pool to calculate rewards
    pools_with_voters = defaultdict(list)
    for (voter_addr, pool_addr), ve_pendle in voter_pool_ve_pendle.items():
        if ve_pendle > 0:  # Only include voters with positive VePendle
            pools_with_voters[pool_addr].append((voter_addr, ve_pendle))

    for pool_address, voter_ve_list in pools_with_voters.items():
        # Get pool fees for this pool
        pool_fee = pool_fees.get(pool_address, 0.0)
        if pool_fee <= 0:
            continue

        # Calculate total VePendle for this specific pool
        total_pool_ve_pendle = sum(ve_pendle for _, ve_pendle in voter_ve_list)

        if total_pool_ve_pendle <= 0:
            continue

        # Distribute fees proportionally based on VePendle voting power for this pool
        for voter_addr, voter_ve_pendle in voter_ve_list:
            voter_share = voter_ve_pendle / total_pool_ve_pendle
            voter_reward = pool_fee * voter_share
            voter_rewards[voter_addr] += voter_reward

    return dict(voter_rewards)


def main():
    """Main function to generate the Pendle voter leaderboard."""
    # Check for required environment variable
    api_key = os.getenv("ETHERSCAN_API_KEY")
    if not api_key:
        print("❌ ETHERSCAN_API_KEY environment variable is required")
        print("Please set your Etherscan API key and try again.")
        return

    print("=== Pendle Voter Leaderboard for August 2025 ===")
    print()

    # Get August 2025 epochs
    fee_epochs, vote_epochs = get_august_2025_epochs()
    print(f"📅 Processing {len(fee_epochs)} epochs for August 2025:")
    print("   Note: Rewards are based on votes from the PREVIOUS epoch")
    for i, (fee_epoch, vote_epoch) in enumerate(
        zip(fee_epochs, vote_epochs, strict=True), 1
    ):
        print(f"   {i}. {fee_epoch} (using votes from {vote_epoch})")
    print()

    # Initialize the client
    try:
        with PendleYieldClient(etherscan_api_key=api_key) as client:
            print("🔍 Fetching market fees data...")

            # Fetch market fees for the period
            try:
                market_fees_response = client.get_market_fees_for_period(
                    "2025-07-30", "2025-09-01"
                )
                print(
                    f"   Found fee data for {len(market_fees_response.results)} markets"
                )
            except Exception as e:
                print(f"❌ Error fetching market fees: {e}")
                return

            # Process each epoch
            total_user_rewards = defaultdict(float)
            total_user_ve_pendle = defaultdict(float)

            for epoch_num, (fee_epoch, vote_epoch) in enumerate(
                zip(fee_epochs, vote_epochs, strict=True), 1
            ):
                print(f"\n📊 Processing Epoch {epoch_num}: {fee_epoch}")
                print(f"   Using votes from: {vote_epoch}")

                # Fetch votes from the PREVIOUS epoch (vote_epoch)
                # These votes determine rewards for the current fee_epoch
                try:
                    votes = client.get_votes_by_epoch(vote_epoch)
                    print(f"   Found {len(votes)} vote events")
                except Exception as e:
                    print(f"   ❌ Error fetching votes: {e}")
                    continue

                if not votes:
                    print("   ⚠️  No votes found for this epoch")
                    continue

                # Extract pool fees for the FEE epoch (not the vote epoch)
                epoch_pool_fees = {}
                fee_epoch_start_str = fee_epoch.start_datetime.strftime("%Y-%m-%d")

                for market_data in market_fees_response.results:
                    market_id = market_data.market.id
                    # Extract pool address from market ID (format: "1-0x...")
                    if "-" in market_id:
                        pool_address = market_id.split("-", 1)[1].lower()
                    else:
                        continue

                    # Find fees for the FEE epoch
                    for fee_value in market_data.values:
                        fee_date_str = fee_value.time.strftime("%Y-%m-%d")
                        if fee_date_str == fee_epoch_start_str:
                            epoch_pool_fees[pool_address] = fee_value.total_fees
                            break

                print(f"   Found fees for {len(epoch_pool_fees)} pools")

                # Calculate rewards using votes from vote_epoch and fees from fee_epoch
                # Use vote_epoch for calculating VePendle values at the end of voting
                epoch_rewards = calculate_pool_rewards(
                    votes, vote_epoch, epoch_pool_fees
                )

                # Calculate VePendle balances at the end of the vote epoch
                epoch_voter_pool_ve_pendle = calculate_epoch_end_ve_pendle_per_pool(
                    votes, vote_epoch
                )

                # Calculate total VePendle per voter for this epoch
                epoch_ve_pendle = calculate_total_ve_pendle_per_voter(
                    epoch_voter_pool_ve_pendle
                )

                # Add to totals
                for voter_addr, reward in epoch_rewards.items():
                    total_user_rewards[voter_addr] += reward

                # Update VePendle balances (use the latest epoch's values)
                for voter_addr, ve_pendle in epoch_ve_pendle.items():
                    total_user_ve_pendle[voter_addr] = ve_pendle

                print(f"   Calculated rewards for {len(epoch_rewards)} voters")

            print("\n💰 Final Results Summary")
            print(f"   Total unique voters: {len(total_user_rewards)}")
            print(
                f"   Total rewards distributed: {sum(total_user_rewards.values()):.2f} USDT"
            )
            print()

            # Filter users with >= 1000 vePENDLE
            MIN_VE_PENDLE = 1000.0
            eligible_users = []

            for voter_addr in total_user_rewards:
                ve_pendle_balance = total_user_ve_pendle.get(voter_addr, 0.0)
                if ve_pendle_balance >= MIN_VE_PENDLE:
                    # Calculate basic portion: 32.5 USDT per 1000 VePendle per month
                    basic_portion = (ve_pendle_balance / 1000) * 32.5

                    # Add basic portion to total rewards
                    pool_rewards = total_user_rewards[voter_addr]
                    total_reward = pool_rewards + basic_portion

                    # Calculate USDT per 1000 vePENDLE
                    usdt_per_1000_ve = (
                        (total_reward / ve_pendle_balance) * 1000
                        if ve_pendle_balance > 0
                        else 0
                    )

                    eligible_users.append(
                        {
                            "address": voter_addr,
                            "total_rewards": total_reward,
                            "usdt_per_1000_ve": usdt_per_1000_ve,
                            "ve_pendle_balance": ve_pendle_balance,
                        }
                    )

            # Sort by USDT per 1000 vePENDLE descending
            eligible_users.sort(key=lambda x: x["usdt_per_1000_ve"], reverse=True)

            print("🏆 Pendle Voter Leaderboard (August 2025)")
            print(f"   Showing users with ≥{MIN_VE_PENDLE:.0f} vePENDLE")
            print("=" * 80)
            print("#")
            print("User, Total Rewards, USDT per 1000 vePENDLE, vePENDLE Balance")

            for rank, user in enumerate(eligible_users, 1):
                formatted_addr = format_address(user["address"])
                total_rewards = user["total_rewards"]
                usdt_per_1000 = user["usdt_per_1000_ve"]
                ve_balance = user["ve_pendle_balance"]

                print(
                    f"{rank}, {formatted_addr}, {total_rewards:.0f} USDT, "
                    f"{usdt_per_1000:.2f}, {ve_balance:,.0f}"
                )

            print()
            print("✅ Leaderboard generation complete!")

    except Exception as e:
        print(f"❌ Error initializing client: {e}")
        return


if __name__ == "__main__":
    main()
