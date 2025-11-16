"""
Script to download and fix the Pendle V2 OpenAPI specification.

This script:
1. Downloads the OpenAPI spec from the Pendle API
2. Fixes the TotalFeesWithTimestamp schema by removing 'totalFees' from required fields
3. Saves the corrected spec to a local file

The upstream API incorrectly marks 'totalFees' as required, but it's sometimes
missing in actual responses. This script corrects that issue so the generated
client can handle missing values (as UNSET).

Usage:
    python scripts/fix_openapi_spec.py
"""

import json
import sys
from pathlib import Path
from typing import Any

import httpx


def download_openapi_spec(url: str) -> dict[str, Any]:
    """
    Download the OpenAPI specification from the given URL.

    Args:
        url: The URL to download the spec from

    Returns:
        The OpenAPI spec as a dictionary

    Raises:
        httpx.HTTPError: If the download fails
    """
    print(f"Downloading OpenAPI spec from: {url}")
    response = httpx.get(url, timeout=30.0)
    response.raise_for_status()
    print("✓ Download successful")
    return response.json()


def fix_total_fees_schema(spec: dict[str, Any]) -> dict[str, Any]:
    """
    Fix the TotalFeesWithTimestamp schema to make 'totalFees' optional.

    Args:
        spec: The OpenAPI specification dictionary

    Returns:
        The modified specification
    """
    print("\nApplying fixes to OpenAPI spec...")

    # Navigate to the TotalFeesWithTimestamp schema
    schemas = spec.get("components", {}).get("schemas", {})

    if "TotalFeesWithTimestamp" not in schemas:
        print("⚠ Warning: TotalFeesWithTimestamp schema not found in spec")
        return spec

    schema = schemas["TotalFeesWithTimestamp"]

    # Remove 'totalFees' from required fields
    required = schema.get("required", [])

    if "totalFees" in required:
        schema["required"] = [field for field in required if field != "totalFees"]
        print("✓ Removed 'totalFees' from required fields in TotalFeesWithTimestamp")
        print(f"  Before: {required}")
        print(f"  After:  {schema['required']}")
    else:
        print("ℹ 'totalFees' was not in required fields (already fixed or schema changed)")

    return spec


def save_spec(spec: dict[str, Any], output_path: Path) -> None:
    """
    Save the OpenAPI spec to a JSON file.

    Args:
        spec: The OpenAPI specification dictionary
        output_path: Path where to save the file
    """
    print(f"\nSaving corrected spec to: {output_path}")

    # Ensure the directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save with pretty formatting
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved successfully ({output_path.stat().st_size:,} bytes)")


def main() -> None:
    """Main function to download, fix, and save the OpenAPI spec."""
    # Configuration
    api_url = "https://api-v2.pendle.finance/core/docs-json"
    output_file = Path("corrected-openapi.json")

    print("=" * 80)
    print("Pendle V2 OpenAPI Specification Fix Script")
    print("=" * 80)

    try:
        # Download the spec
        spec = download_openapi_spec(api_url)

        # Apply fixes
        fixed_spec = fix_total_fees_schema(spec)

        # Save to file
        save_spec(fixed_spec, output_file)

        print("\n" + "=" * 80)
        print("✓ Success! OpenAPI spec has been downloaded and fixed.")
        print("=" * 80)
        print(f"\nYou can now use the corrected spec with:")
        print(
            f"  openapi-python-client generate --path {output_file} "
            "--meta pdm --output-path src --config openapi.yaml --overwrite"
        )

    except httpx.HTTPError as e:
        print(f"\n✗ Error downloading spec: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

