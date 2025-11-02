"""
Vote Distribution Example

This example demonstrates how to:
1. Create a Pendle epoch for a specific date range (2025-09-11 to 2025-09-18)
2. Fetch all vote events during that epoch
3. Calculate final vote distribution for a specific pool
4. Show voting power distribution across voters
"""

import os
from collections import defaultdict
from datetime import datetime

from pendle_yield import PendleEpoch, PendleYieldClient


def format_wei_to_readable(wei_value: int, decimals: int = 18) -> float:
    """Convert wei value to readable format."""
    return wei_value / (10 ** decimals)


def format_address(address: str) -> str:
    """Format address for display (first 6 and last 4 characters)."""
    return f"{address[:6]}...{address[-4:]}"


def main():
    """Main function to demonstrate vote distribution calculation."""
    # Configuration
    TARGET_POOL = "0xb6ac3d5da138918ac4e84441e924a20daa60dbdd"
    EPOCH_START_DATE = "2025-09-11"
    
    # Check for required environment variable
    api_key = os.getenv('ETHERSCAN_API_KEY')
    if not api_key:
        print("❌ ETHERSCAN_API_KEY environment variable is required")
        print("Please set your Etherscan API key and try again.")
        return
    
    print("=== Pendle Vote Distribution Analysis ===")
    print(f"Target Pool: {TARGET_POOL}")
    print(f"Epoch Start: {EPOCH_START_DATE}")
    print()
    
    # Create epoch for the specified date range
    try:
        epoch = PendleEpoch(EPOCH_START_DATE)
        print(f"📅 Epoch: {epoch}")
        print(f"   Start: {epoch.start_datetime}")
        print(f"   End: {epoch.end_datetime}")
        print(f"   Status: {'Past' if epoch.is_past else 'Current' if epoch.is_current else 'Future'}")
        print()
    except Exception as e:
        print(f"❌ Error creating epoch: {e}")
        return
    
    # Initialize the client
    try:
        with PendleYieldClient(etherscan_api_key=api_key) as client:
            print("🔍 Fetching vote events...")
            
            # Fetch all votes for the epoch
            try:
                all_votes = client.get_votes_by_epoch(epoch)
                print(f"   Found {len(all_votes)} total vote events")
            except Exception as e:
                print(f"❌ Error fetching votes: {e}")
                return
            
            # Filter votes for the target pool
            pool_votes = [vote for vote in all_votes if vote.pool_address.lower() == TARGET_POOL.lower()]
            print(f"   Found {len(pool_votes)} votes for target pool")
            
            if not pool_votes:
                print("⚠️  No votes found for the target pool in this epoch")
                return
            
            print()
            
            # Calculate vote distribution
            print("📊 Calculating vote distribution...")
            
            # Group votes by voter and sum their VePendle values
            voter_voting_power = defaultdict(float)
            voter_latest_vote = {}  # Track the latest vote for each voter
            
            for vote in pool_votes:
                voter_addr = vote.voter_address.lower()
                # Use the VePendle value calculated in the enriched vote event
                voter_voting_power[voter_addr] = vote.ve_pendle_value
                
                # Keep track of the latest vote for each voter (for display purposes)
                if (voter_addr not in voter_latest_vote or 
                    vote.timestamp > voter_latest_vote[voter_addr].timestamp):
                    voter_latest_vote[voter_addr] = vote
            
            total_voting_power = sum(voter_voting_power.values())
            
            if total_voting_power == 0:
                print("⚠️  No voting power found (all votes may have expired)")
                return
            
            print(f"   Total voting power: {total_voting_power:.2f} VePendle")
            print(f"   Number of unique voters: {len(voter_voting_power)}")
            print()
            
            # Show vote distribution
            print("🎯 Vote Distribution Results")
            print("=" * 70)
            print(f"{'Voter Address':<20} {'Voting Power':<15} {'Share %':<10}")
            print("-" * 70)
            
            for voter_addr, voting_power in sorted(voter_voting_power.items(), 
                                                 key=lambda x: x[1], reverse=True):
                # Calculate percentage of total voting power
                vote_percentage = (voting_power / total_voting_power) * 100
                
                # Format for display
                formatted_addr = format_address(voter_addr)
                
                print(f"{formatted_addr:<20} {voting_power:>10.2f} VePendle {vote_percentage:>6.2f}%")
            
            print("-" * 70)
            print(f"{'TOTAL':<20} {total_voting_power:>10.2f} VePendle {'100.00%':>6}")
            print()
            
            # Summary statistics
            print("📈 Summary Statistics")
            print(f"   • Epoch: {epoch}")
            print(f"   • Target Pool: {TARGET_POOL}")
            print(f"   • Total Votes: {len(pool_votes)}")
            print(f"   • Unique Voters: {len(voter_voting_power)}")
            print(f"   • Total Voting Power: {total_voting_power:.2f} VePendle")
            
            # Additional insights
            if pool_votes:
                print()
                print("🔍 Additional Insights")
                
                # Pool information from the first vote
                sample_vote = pool_votes[0]
                print(f"   • Pool Name: {sample_vote.pool_name}")
                print(f"   • Pool Symbol: {sample_vote.pool_symbol}")
                print(f"   • Protocol: {sample_vote.protocol}")
                print(f"   • Voter APY: {sample_vote.voter_apy:.2f}%")
                print(f"   • Pool Expiry: {sample_vote.expiry}")
                
                # Voting timeline
                vote_timestamps = [vote.timestamp for vote in pool_votes if vote.timestamp]
                if vote_timestamps:
                    earliest_vote = min(vote_timestamps)
                    latest_vote = max(vote_timestamps)
                    print(f"   • First Vote: {earliest_vote}")
                    print(f"   • Last Vote: {latest_vote}")
            
            print()
            print("✅ Analysis complete!")
            
    except Exception as e:
        print(f"❌ Error initializing client: {e}")
        return


if __name__ == "__main__":
    main()
