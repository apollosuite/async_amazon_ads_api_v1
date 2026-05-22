"""Download Amazon Ads API OpenAPI specification JSON from a remote URL.

Usage:
    uv run python scripts/download_spec.py
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx

HERE = Path(__file__).parent

SP_URL: str = (
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISPMerged_prod_3p.json"
)
SB_URL: str = (
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISBMerged_prod_3p.json"
)
SD_URL: str = (
    "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISDMerged_prod_3p.json"
)


def download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    with httpx.Client(follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()
    data = resp.json()
    content = json.dumps(data, indent=2, ensure_ascii=False).encode()
    dest.write_bytes(content)
    print(f"  -> saved {dest}  ({len(content)} bytes)")


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
