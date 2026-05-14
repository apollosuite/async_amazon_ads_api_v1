# Amazon Ads SDK

Pure async Python SDK for Amazon Advertising API — Sponsored Products, Sponsored Brands, and Sponsored Display.

## Installation

```bash
uv sync
```

## Quick Start

```python
import asyncio
from amazon_ads_sdk import AmazonAdsConfig, Region, SPClient, SBClient, SDClient

async def main():
    config = AmazonAdsConfig(access_token="...", region=Region.NA)

    # Sponsored Products
    async with SPClient(config) as sp:
        resp = await sp.campaigns.query({"stateFilter": {"include": ["enabled"]}})
        print(resp.model_dump_json(indent=2))

    # Sponsored Brands
    async with SBClient(config) as sb:
        resp = await sb.campaigns.query({...})
        resp = await sb.advertising_deals.query({...})  # SB-exclusive

    # Sponsored Display
    async with SDClient(config) as sd:
        resp = await sd.campaigns.query({...})

asyncio.run(main())
```

## API Reference

### `SPClient` — Sponsored Products

| 资源 | 方法 |
|---|---|
| `client.campaigns` | `create()`, `query()`, `update()`, `delete()` |
| `client.ad_groups` | `create()`, `query()`, `update()`, `delete()` |
| `client.ads` | `create()`, `query()`, `update()`, `delete()` |
| `client.targets` | `create()`, `query()`, `update()`, `delete()` |
| `client.ad_extensions` | `create()`, `query()`, `update()` |

### `SBClient` — Sponsored Brands

| 资源 | 方法 |
|---|---|
| `client.campaigns` | `create()`, `query()`, `update()`, `delete()` |
| `client.ad_groups` | `create()`, `query()`, `update()`, `delete()` |
| `client.ads` | `create()`, `query()`, `update()`, `delete()` |
| `client.targets` | `create()`, `query()`, `update()`, `delete()` |
| `client.ad_extensions` | `create()`, `query()`, `update()` |
| `client.advertising_deals` | `create()`, `query()`, `update()`, `delete()` |
| `client.advertising_deal_targets` | `create()`, `query()`, `delete()` |
| `client.branded_keywords_pricings` | `create()` |
| `client.keyword_reservation_validations` | `create()` |
| `client.recommendations` | `create()` |
| `client.recommendation_types` | `query()` |

### `SDClient` — Sponsored Display

| 资源 | 方法 |
|---|---|
| `client.campaigns` | `create()`, `query()`, `update()`, `delete()` |
| `client.ad_groups` | `create()`, `query()`, `update()`, `delete()` |
| `client.ads` | `create()`, `query()`, `update()`, `delete()` |
| `client.targets` | `create()`, `query()`, `update()`, `delete()` |
