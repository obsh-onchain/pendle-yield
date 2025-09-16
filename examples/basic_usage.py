#!/usr/bin/env python3
"""
Basic usage example for the pendle-yield package.

This script demonstrates how to use the PendleYieldClient to fetch
enriched vote data from Pendle Finance using the get_votes method.
"""

import os
from pendle_yield import PendleYieldClient, APIError, ValidationError


def main():
    """
    Example demonstrating the main functionality of PendleYieldClient.

    This example shows how to use the get_votes method to fetch enriched
    vote events for a specific block number.
    """
    print("🚀 Pendle Yield SDK - Basic Usage Example")
    print("=" * 50)

    # Get API key from environment or use the provided test key
    api_key = os.getenv("ETHERSCAN_API_KEY")

    if not api_key:
        print("❌ No Etherscan API key found!")
        print("   Please set ETHERSCAN_API_KEY environment variable")
        return

    print(f"📡 Using Etherscan API key: {api_key[:8]}...")
    print()

    try:
        # Initialize the PendleYieldClient
        print("🔧 Initializing PendleYieldClient...")
        client = PendleYieldClient(etherscan_api_key=api_key)

        # Example block number - you can change this to test different blocks
        # Using a block that contains vote events
        block_number = 23251350

        print(f"🔍 Fetching enriched vote events for block {block_number:,}...")
        print("   This combines Etherscan vote data with Pendle pool information")
        print()

        # Get enriched vote events using the main method
        votes = client.get_votes(block_number)

        if votes:
            print(f"✅ Found {len(votes)} enriched vote events!")
            print()

            # Display detailed information for each vote
            for i, vote in enumerate(votes, 1):
                print(f"📊 Vote #{i}:")
                print(f"   Voter Address: {vote.voter_address}")
                print(f"   Pool: {vote.pool_name} ({vote.pool_symbol})")
                print(f"   Protocol: {vote.protocol}")
                print(f"   Chain ID: {vote.chain_id}")
                print(f"   Vote Bias: {vote.bias:,}")
                print(f"   Vote Slope: {vote.slope:,}")
                print(f"   VePendle Value: {vote.ve_pendle_value:.4f}")
                print(f"   Voter APY: {vote.voter_apy * 100:.2f}%")
                print(f"   Pool Expiry: {vote.expiry.strftime('%Y-%m-%d')}")
                print(f"   Transaction: {vote.transaction_hash}")
                print(f"   Block: {vote.block_number:,}")
                if vote.timestamp:
                    print(f"   Timestamp: {vote.timestamp}")
                print("-" * 60)

            # Summary statistics
            total_bias = sum(vote.bias for vote in votes)
            total_slope = sum(vote.slope for vote in votes)
            total_ve_pendle = sum(vote.ve_pendle_value for vote in votes)
            avg_apy = sum(vote.voter_apy for vote in votes) / len(votes)
            avg_ve_pendle = total_ve_pendle / len(votes)
            unique_voters = len(set(vote.voter_address for vote in votes))
            unique_pools = len(set(vote.pool_address for vote in votes))

            print(f"📈 Summary Statistics:")
            print(f"   Total Votes: {len(votes)}")
            print(f"   Unique Voters: {unique_voters}")
            print(f"   Unique Pools: {unique_pools}")
            print(f"   Total Bias: {total_bias:,}")
            print(f"   Total Slope: {total_slope:,}")
            print(f"   Total VePendle Value: {total_ve_pendle:.4f}")
            print(f"   Average VePendle Value: {avg_ve_pendle:.4f}")
            print(f"   Average Voter APY: {avg_apy * 100:.2f}%")

        else:
            print("ℹ️  No vote events found for this block")
            print(
                "   Try a different block number or check if there were votes in this block"
            )

    except ValidationError as e:
        print(f"❌ Validation Error: {e}")
        print("   Check that the block number is valid and the API key is correct")
    except APIError as e:
        print(f"❌ API Error: {e}")
        print(
            "   This could be due to rate limiting, network issues, or invalid parameters"
        )
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        print("   Please check your internet connection and try again")
    finally:
        # Clean up the client
        if "client" in locals():
            client.close()
            print("\n🔒 Client connection closed")

    print("\n✨ Example completed!")
    print("\n💡 Next steps:")
    print("1. Try different block numbers to see various vote events")
    print("2. Explore the EnrichedVoteEvent model for more data fields")
    print("3. Check out the documentation in docs/index.md")
    print("4. Use the data for your own analysis and applications")


if __name__ == "__main__":
    main()
