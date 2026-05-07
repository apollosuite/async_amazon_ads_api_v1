# Amazon Ads SDK

Pure async Python SDK for Amazon Advertising API — Sponsored Products.

## Installation

```bash
uv sync
```

## Quick Start

```python
import asyncio
from amazon_ads_sdk import AmazonAdsClient, Region
from amazon_ads_sdk.config import AmazonAdsConfig

async def main():
    config = AmazonAdsConfig(
        access_token="YOUR_ACCESS_TOKEN",
        region=Region.NA,
    )
    async with AmazonAdsClient(config) as client:
        resp = await client.query_campaigns({"stateFilter": {"include": ["enabled"]}})
        print(resp.json())

asyncio.run(main())
```