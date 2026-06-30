"""Download Amazon Ads API OpenAPI specs (JSON / YAML)."""

import json
from pathlib import Path

import httpx

HERE = Path(__file__).parent

specs: dict[str, str] = {
    "AmazonAdsAPISPMerged_prod_3p.json": "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISPMerged_prod_3p.json",
    "AmazonAdsAPISBMerged_prod_3p.json": "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISBMerged_prod_3p.json",
    "AmazonAdsAPISDMerged_prod_3p.json": "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/AmazonAdsAPISDMerged_prod_3p.json",
    "SponsoredProducts_prod_3p.json": "https://d1y2lf8k3vrkfu.cloudfront.net/openapi/en-us/dest/SponsoredProducts_prod_3p.json",
    "sponsoredBrands_40_openapi.json": "https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-brands/4-0/openapi.json",
    "sponsoredDisplay_30_openapi.yaml": "https://d3a0d0y2hgofx6.cloudfront.net/openapi/en-us/sponsored-display/3-0/openapi.yaml",
}


def download(url: str, dest: Path) -> None:
    print(f"Downloading {url} ...")
    with httpx.Client(follow_redirects=True) as client:
        resp = client.get(url)
        resp.raise_for_status()

    if url.endswith(".yaml"):
        dest = dest.with_suffix(".yaml")
        content = resp.text.encode()
    else:
        content = json.dumps(resp.json(), indent=2, ensure_ascii=False).encode()

    dest.write_bytes(content)
    print(f"  -> saved {dest}  ({len(content)} bytes)")


def main() -> None:
    for filename, url in specs.items():
        download(url, HERE / filename)


if __name__ == "__main__":
    main()
