import os
from datetime import datetime, timedelta
from pendle_yield import PendleEpoch, EtherscanClient

# Create epochs for testing
past_epoch = PendleEpoch('2024-01-15')  # Past epoch
current_epoch = PendleEpoch()  # Current epoch
future_epoch = PendleEpoch(datetime.now() + timedelta(days=7))  # Future epoch

print("=== Epoch Status ===")
print(f"Past epoch: {past_epoch} (is_past: {past_epoch.is_past})")
print(f"Current epoch: {current_epoch} (is_current: {current_epoch.is_current})")
print(f"Future epoch: {future_epoch} (is_future: {future_epoch.is_future})")

# Only proceed with API calls if we have an API key
api_key = os.getenv('ETHERSCAN_API_KEY')
if not api_key:
    print("\n⚠️  ETHERSCAN_API_KEY not set. Skipping API calls.")
    print("Set the environment variable to test the improved block range functionality.")
    exit(0)

es_client = EtherscanClient(api_key=api_key)

print("\n=== Testing Improved Block Range Functionality ===")

# Test past epoch - should work normally
try:
    st_block, end_block = past_epoch.get_block_range(es_client)
    print(f"✅ Past epoch blocks: {st_block} - {end_block}")
except Exception as e:
    print(f"❌ Past epoch error: {e}")

# Test current epoch without use_latest_for_current - should return None for end_block
try:
    st_block, end_block = current_epoch.get_block_range(es_client)
    print(f"✅ Current epoch blocks (default): {st_block} - {end_block}")
except Exception as e:
    print(f"❌ Current epoch error: {e}")

# Test current epoch with use_latest_for_current=True - should return latest block
try:
    st_block, end_block = current_epoch.get_block_range(es_client, use_latest_for_current=True)
    print(f"✅ Current epoch blocks (with latest): {st_block} - {end_block}")
except Exception as e:
    print(f"❌ Current epoch with latest error: {e}")

# Test future epoch - should raise ValidationError immediately (no API call)
try:
    st_block, end_block = future_epoch.get_block_range(es_client)
    print(f"❌ Future epoch blocks: {st_block} - {end_block}")  # This shouldn't happen
except Exception as e:
    print(f"✅ Future epoch error (expected): {e}")
