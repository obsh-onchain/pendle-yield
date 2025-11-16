#!/usr/bin/env python3
"""
Example demonstrating how to fetch historical market data using the Pendle V2 API.

This script shows how to use the markets_controller_market_historical_data_v_2 API
to retrieve time-series data for a specific market, including APY metrics, TVL,
prices, and fee breakdowns.
"""

from pendle_v2 import Client
from pendle_v2.api.markets import markets_controller_market_historical_data_v_2
from pendle_v2.models.markets_controller_market_historical_data_v2_time_frame import (
    MarketsControllerMarketHistoricalDataV2TimeFrame,
)


def main():
    """
    Fetch historical market data for the USDe market on Ethereum mainnet.
    
    This example demonstrates:
    - How to initialize the Pendle V2 API client
    - How to fetch daily historical data for a specific market
    - How to request all available fields including fee breakdown
    - How to process and display the response data
    """
    print("📊 Pendle V2 API - Market Historical Data Example")
    print("=" * 60)
    print()

    # ========================================================================
    # Step 1: Initialize the Pendle V2 API Client
    # ========================================================================
    # The Client class is used for unauthenticated API access.
    # For authenticated endpoints, use AuthenticatedClient instead.
    
    base_url = "https://api-v2.pendle.finance/core"
    client = Client(base_url=base_url)
    
    print(f"✅ Initialized Pendle V2 API client")
    print(f"   Base URL: {base_url}")
    print()

    # ========================================================================
    # Step 2: Define Market Parameters
    # ========================================================================
    # Market: USDe on Ethereum mainnet
    # You can find market addresses on the Pendle Finance website or API
    
    chain_id = 1  # Ethereum mainnet
    market_address = "0xb4460e76d99ecad95030204d3c25fb33c4833997"
    market_name = "USDe"  # For reference only
    
    print(f"🎯 Target Market:")
    print(f"   Name: {market_name}")
    print(f"   Address: {market_address}")
    print(f"   Chain ID: {chain_id} (Ethereum mainnet)")
    print()

    # ========================================================================
    # Step 3: Configure Request Parameters
    # ========================================================================
    
    # Resolution: Use daily data points
    # Available options: HOUR, DAY, WEEK
    time_frame = MarketsControllerMarketHistoricalDataV2TimeFrame.DAY
    
    # Fields: Request all available fields
    # Available fields include: timestamp, maxApy, baseApy, underlyingApy,
    # impliedApy, tvl, totalTvl, underlyingInterestApy, underlyingRewardApy,
    # ytFloatingApy, swapFeeApy, voterApr, pendleApy, lpRewardApy, totalPt,
    # totalSy, totalSupply, ptPrice, ytPrice, syPrice, lpPrice,
    # lastEpochVotes, tradingVolume
    fields = (
        "timestamp,maxApy,baseApy,underlyingApy,impliedApy,tvl,totalTvl,"
        "underlyingInterestApy,underlyingRewardApy,ytFloatingApy,swapFeeApy,"
        "voterApr,pendleApy,lpRewardApy,totalPt,totalSy,totalSupply,ptPrice,"
        "ytPrice,syPrice,lpPrice,lastEpochVotes,tradingVolume"
    )
    
    # Include fee breakdown: Get detailed fee information
    # This adds explicitSwapFee, implicitSwapFee, and limitOrderFee fields
    # (only available for daily and weekly timeframes)
    include_fee_breakdown = True
    
    print(f"⚙️  Request Configuration:")
    print(f"   Time Frame: {time_frame.value} (daily resolution)")
    print(f"   Include Fee Breakdown: {include_fee_breakdown}")
    print(f"   Fields: All available fields requested")
    print()

    # ========================================================================
    # Step 4: Fetch Historical Data
    # ========================================================================
    
    print(f"🔄 Fetching historical market data...")
    print()
    
    try:
        # Call the sync function to get historical data
        # Note: Use sync_detailed() if you need access to HTTP response details
        response = markets_controller_market_historical_data_v_2.sync(
            chain_id=chain_id,
            address=market_address,
            client=client,
            time_frame=time_frame,
            fields=fields,
            include_fee_breakdown=include_fee_breakdown,
            # Optional: You can also specify timestamp_start and timestamp_end
            # to limit the date range:
            # timestamp_start=datetime(2024, 1, 1),
            # timestamp_end=datetime(2024, 12, 31),
        )
        
        if response is None:
            print("❌ No data returned from API")
            return
        
        # ====================================================================
        # Step 5: Process and Display Results
        # ====================================================================
        
        print(f"✅ Successfully retrieved historical data!")
        print()
        print(f"📈 Response Summary:")
        print(f"   Total data points: {int(response.total)}")
        print(f"   Date range: {response.timestamp_start.date()} to {response.timestamp_end.date()}")
        print(f"   Number of results: {len(response.results)}")
        print()
        
        # Display the first few data points as examples
        print(f"📊 Sample Data Points (showing first 3):")
        print("-" * 60)
        
        for i, data_point in enumerate(response.results[:3]):
            print(f"\n🕐 Data Point {i + 1}:")
            print(f"   Timestamp: {data_point.timestamp}")
            
            # APY metrics
            if data_point.max_apy is not None:
                print(f"   Max APY: {data_point.max_apy * 100:.2f}%")
            if data_point.base_apy is not None:
                print(f"   Base APY: {data_point.base_apy * 100:.2f}%")
            if data_point.underlying_apy is not None:
                print(f"   Underlying APY: {data_point.underlying_apy * 100:.2f}%")
            if data_point.implied_apy is not None:
                print(f"   Implied APY: {data_point.implied_apy * 100:.2f}%")
            
            # TVL
            if data_point.tvl is not None:
                print(f"   TVL: ${data_point.tvl:,.2f}")
            if data_point.total_tvl is not None:
                print(f"   Total TVL: ${data_point.total_tvl:,.2f}")
            
            # Fee breakdown (only available with include_fee_breakdown=True)
            if data_point.explicit_swap_fee is not None:
                print(f"   Explicit Swap Fee: ${data_point.explicit_swap_fee:,.2f}")
            if data_point.implicit_swap_fee is not None:
                print(f"   Implicit Swap Fee: ${data_point.implicit_swap_fee:,.2f}")
            if data_point.limit_order_fee is not None:
                print(f"   Limit Order Fee: ${data_point.limit_order_fee:,.2f}")
        
        print()
        print("-" * 60)
        print(f"✨ Example completed successfully!")
        
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        raise


if __name__ == "__main__":
    main()

