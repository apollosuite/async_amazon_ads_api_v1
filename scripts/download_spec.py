"""Download Amazon Ads API OpenAPI specification JSON from a remote URL.

Usage:
    uv run python scripts/download_spec.py
"""

from __future__ import annotations

from pathlib import Path

import httpx

HERE = Path(__file__).parent

# TODO: Fill in the actual URL(s) to download.
# Example:
#   SP_URL = "https://example.com/path/to/AmazonAdsAPISPMerged_prod_3p.json"
#   SB_URL = "https://example.com/path/to/AmazonAdsAPISBMerged_prod_3p.json"
#   SD_URL = "https://example.com/path/to/AmazonAdsAPISDMerged_prod_3p.json"

SP_URL: str = ""
SB_URL: str = ""
SD_URL: str = ""


def download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    with httpx.Client(follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()
    dest.write_bytes(resp.content)
    print(f"  -> saved {dest}  ({len(resp.content)} bytes)")


def main() -> None:
    specs: dict[str, str] = {
        "sp": SP_URL,
        "sb": SB_URL,
        "sd": SD_URL,
    }

    for name, url in specs.items():
        if not url:
            print(f"Skipping {name}: URL not configured")
            continue
        download(url, HERE / f"AmazonAdsAPI{name.upper()}Merged_prod_3p.json")


if __name__ == "__main__":
    main()
