#!/usr/bin/env python3
"""
Backfill script to populate market historical data cache.

This script fetches all markets (both active and inactive) from the Pendle API
and backfills their historical data into the SQLite cache database. The script:
- Fetches all markets across all chains
- For each market, determines the date range (creation to expiry or yesterday)
- Uses the caching method to fetch and store daily historical data
- Implements retry logic with exponential backoff
- Provides detailed progress logging
- Supports resuming from interruptions
"""

import argparse
import logging
import os
import sys
import time
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Optional

from dateutil.parser import isoparse

from pendle_v2 import Client as PendleV2Client
from pendle_v2.api.markets import markets_cross_chain_controller_get_all_markets
from pendle_yield import PendleYieldClient


def setup_logging(log_file: Optional[str] = None) -> logging.Logger:
    """Set up logging configuration."""
    # Set up root logger to capture all logs
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger("backfill_historical_data")
    logger.setLevel(logging.INFO)

    # Also enable cache logger
    cache_logger = logging.getLogger("pendle_yield.cache")
    cache_logger.setLevel(logging.INFO)

    # File handler for errors
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.ERROR)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


def fetch_all_markets(
    pendle_client: PendleV2Client, logger: logging.Logger, chain_id: Optional[int] = None
) -> list[dict]:
    """
    Fetch all markets (active and inactive) from the Pendle API.

    Args:
        pendle_client: Pendle V2 API client
        logger: Logger instance
        chain_id: Optional chain ID to filter markets (None = all chains)

    Returns:
        List of market dictionaries with address, chain_id, name, timestamp, and expiry
    """
    logger.info("Fetching all markets from Pendle API...")

    try:
        # Fetch all markets (don't filter by is_active to get both active and inactive)
        response = markets_cross_chain_controller_get_all_markets.sync(
            client=pendle_client,
            chain_id=float(chain_id) if chain_id else None,
        )

        if response is None or not response.markets:
            logger.warning("No markets returned from API")
            return []

        markets = []
        for market in response.markets:
            markets.append(
                {
                    "address": market.address.lower(),
                    "chain_id": int(market.chain_id),
                    "name": market.name,
                    "timestamp": market.timestamp,  # Creation timestamp
                    "expiry": market.expiry,  # Expiry date string
                }
            )

        logger.info(f"Found {len(markets)} markets")
        return markets

    except Exception as e:
        logger.error(f"Failed to fetch markets: {e}")
        raise


def calculate_date_range(
    market: dict, logger: logging.Logger
) -> tuple[date, date] | None:
    """
    Calculate the date range to backfill for a market.

    Args:
        market: Market dictionary with timestamp and expiry
        logger: Logger instance

    Returns:
        Tuple of (start_date, end_date) or None if no data to fetch
    """
    try:
        # Start date: market creation date
        creation_datetime = market["timestamp"]
        start_date = creation_datetime.date()

        # End date: earlier of (expiry date OR yesterday)
        # We exclude today since it changes throughout the day
        yesterday = (datetime.now(UTC) - timedelta(days=1)).date()

        # Parse expiry date (format: "2024-03-28T00:00:00.000Z")
        expiry_datetime = isoparse(market["expiry"])
        expiry_date = expiry_datetime.date()

        # Use the earlier of expiry or yesterday
        end_date = min(expiry_date, yesterday)

        # If start_date is after end_date, no data to fetch
        if start_date > end_date:
            return None

        return (start_date, end_date)

    except Exception as e:
        logger.error(f"Error calculating date range for market {market['address']}: {e}")
        return None


def backfill_market(
    client: PendleYieldClient,
    market: dict,
    logger: logging.Logger,
    max_retries: int = 3,
    dry_run: bool = False,
) -> tuple[int, int]:
    """
    Backfill historical data for a single market.

    Args:
        client: PendleYieldClient instance with caching enabled
        market: Market dictionary
        logger: Logger instance
        max_retries: Maximum number of retry attempts
        dry_run: If True, don't actually fetch data

    Returns:
        Tuple of (days_processed, days_cached)
    """
    market_address = market["address"]
    chain_id = market["chain_id"]
    market_name = market["name"]

    # Calculate date range
    date_range = calculate_date_range(market, logger)
    if date_range is None:
        logger.info(
            f"  [{market_name}] No historical data to fetch (market not yet active or expired)"
        )
        return (0, 0)

    start_date, end_date = date_range
    total_days = (end_date - start_date).days + 1

    logger.info(
        f"  [{market_name}] Date range: {start_date} to {end_date} ({total_days} days)"
    )

    if dry_run:
        logger.info(f"  [{market_name}] DRY RUN - skipping actual fetch")
        return (total_days, 0)

    # Retry logic with exponential backoff
    for attempt in range(max_retries):
        try:
            logger.info(f"  [{market_name}] Calling get_market_historical_data_cached...")

            # Use the caching method - it will handle cache lookups and storage
            response = client.get_market_historical_data_cached(
                chain_id=chain_id,
                market_address=market_address,
                start_date=start_date,
                end_date=end_date,
            )

            days_fetched = len(response.results)
            logger.info(
                f"  [{market_name}] ✓ Successfully retrieved {days_fetched} data points"
            )
            return (days_fetched, days_fetched)

        except Exception as e:
            if attempt < max_retries - 1:
                # Exponential backoff: 2^attempt seconds
                wait_time = 2**attempt
                logger.warning(
                    f"  [{market_name}] Attempt {attempt + 1}/{max_retries} failed: {e}. "
                    f"Retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"  [{market_name}] ✗ Failed after {max_retries} attempts: {e}"
                )
                return (0, 0)

    return (0, 0)


def main() -> None:
    """Main backfill function."""
    parser = argparse.ArgumentParser(
        description="Backfill historical market data into cache database"
    )
    parser.add_argument(
        "--db-path",
        type=str,
        default="./cache.db",
        help="Path to SQLite database file (default: ./cache.db)",
    )
    parser.add_argument(
        "--chain-id",
        type=int,
        help="Filter to specific chain ID (e.g., 1 for Ethereum mainnet)",
    )
    parser.add_argument(
        "--markets",
        type=str,
        help="Comma-separated list of market addresses to backfill (default: all markets)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retry attempts per market (default: 3)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay in seconds between market requests (default: 0.5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be fetched without actually fetching",
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default="backfill_errors.log",
        help="Path to error log file (default: backfill_errors.log)",
    )

    args = parser.parse_args()

    # Set up logging
    logger = setup_logging(args.log_file)

    # Get Etherscan API key from environment
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
    if not etherscan_api_key:
        logger.error("ETHERSCAN_API_KEY environment variable not set")
        sys.exit(1)

    # Print configuration
    logger.info("=" * 80)
    logger.info("Market Historical Data Backfill Script")
    logger.info("=" * 80)
    logger.info(f"Database path:    {args.db_path}")
    logger.info(f"Chain ID filter:  {args.chain_id or 'All chains'}")
    logger.info(f"Market filter:    {args.markets or 'All markets'}")
    logger.info(f"Max retries:      {args.max_retries}")
    logger.info(f"Delay:            {args.delay}s")
    logger.info(f"Dry run:          {args.dry_run}")
    logger.info(f"Error log:        {args.log_file}")
    logger.info("=" * 80)

    # Create database directory if it doesn't exist
    db_path = Path(args.db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Initialize clients
    logger.info("\nInitializing clients...")

    pendle_client = PendleV2Client(base_url="https://api-v2.pendle.finance/core")

    with PendleYieldClient(
        etherscan_api_key=etherscan_api_key, db_path=str(args.db_path)
    ) as client:
        # Fetch all markets
        all_markets = fetch_all_markets(pendle_client, logger, args.chain_id)

        # Filter markets if specific addresses provided
        if args.markets:
            market_addresses = set(addr.strip().lower() for addr in args.markets.split(","))
            markets_to_process = [
                m for m in all_markets if m["address"] in market_addresses
            ]
            logger.info(
                f"\nFiltered to {len(markets_to_process)} markets from {len(all_markets)} total"
            )
        else:
            markets_to_process = all_markets

        if not markets_to_process:
            logger.warning("No markets to process")
            sys.exit(0)

        # Process markets
        logger.info(f"\nProcessing {len(markets_to_process)} markets...")
        logger.info("=" * 80)

        total_days_processed = 0
        total_days_cached = 0
        markets_succeeded = 0
        markets_failed = 0
        markets_skipped = 0

        start_time = time.time()

        for i, market in enumerate(markets_to_process, 1):
            logger.info(
                f"\n[{i}/{len(markets_to_process)}] Processing {market['name']} "
                f"(Chain {market['chain_id']}, {market['address']})"
            )

            try:
                days_processed, days_cached = backfill_market(
                    client, market, logger, args.max_retries, args.dry_run
                )

                if days_processed > 0:
                    total_days_processed += days_processed
                    total_days_cached += days_cached
                    markets_succeeded += 1
                else:
                    markets_skipped += 1

                # Add delay between markets to avoid rate limiting
                if i < len(markets_to_process) and args.delay > 0:
                    time.sleep(args.delay)

            except KeyboardInterrupt:
                logger.warning("\n\nBackfill interrupted by user")
                logger.info(
                    f"Progress: {i}/{len(markets_to_process)} markets processed"
                )
                break
            except Exception as e:
                logger.error(f"Unexpected error processing market: {e}")
                markets_failed += 1
                continue

        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        elapsed_minutes = elapsed_time / 60

        # Print summary
        logger.info("\n" + "=" * 80)
        logger.info("Backfill Complete!")
        logger.info("=" * 80)
        logger.info(f"Total markets processed:     {markets_succeeded}")
        logger.info(f"Markets skipped (no data):   {markets_skipped}")
        logger.info(f"Markets failed:              {markets_failed}")
        logger.info(f"Total data points processed: {total_days_processed}")
        logger.info(f"Total data points cached:    {total_days_cached}")
        logger.info(f"Elapsed time:                {elapsed_minutes:.1f} minutes")
        if markets_succeeded > 0:
            logger.info(
                f"Average time per market:     {elapsed_time / markets_succeeded:.1f} seconds"
            )
        logger.info("=" * 80)

        if not args.dry_run:
            logger.info(
                f"\nCache database '{args.db_path}' has been populated with historical data."
            )
            logger.info(
                "Subsequent queries for cached dates will be instant (no API calls)."
            )

        if markets_failed > 0:
            logger.warning(
                f"\n⚠️  {markets_failed} markets failed. Check {args.log_file} for details."
            )


if __name__ == "__main__":
    main()


