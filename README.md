# async-amazon-ads-api-v1

Pure async Amazon Ads API v1 client — Sponsored Products, Sponsored Brands, Sponsored Display.

## Installation

```bash
pip install async-amazon-ads-api-v1
# 或
uv add async-amazon-ads-api-v1
```

## Quick Start

### 使用 Access Token（直接提供）

```python
import asyncio
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient

async def main():
    config = AmazonAdsConfig(
        access_token="your-access-token",
        client_id="your-client-id",
        region=Region.NA,
    )

    async with SPClient(config) as sp:
        resp = await sp.campaigns.query({"stateFilter": {"include": ["enabled"]}})
        print(resp.model_dump_json(indent=2))

asyncio.run(main())
```

### 使用 Refresh Token（自动续期）

```python
import asyncio
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient

async def main():
    config = AmazonAdsConfig(
        access_token="your-access-token",   # 可选，提供后直接使用
        client_id="your-client-id",
        refresh_token="your-refresh-token", # access_token 过期后自动刷新
        client_secret="your-client-secret",
        region=Region.NA,
    )

    async with SPClient(config) as sp:
        resp = await sp.campaigns.query({"stateFilter": {"include": ["enabled"]}})
        print(resp.model_dump_json(indent=2))

asyncio.run(main())
```

### 从环境变量加载

```bash
export AMAZON_ACCESS_TOKEN=...
export AMAZON_CLIENT_ID=...
export AMAZON_REFRESH_TOKEN=...     # 可选，用于自动续期
export AMAZON_CLIENT_SECRET=...     # 可选，refresh_token 时需要
export AMAZON_REGION=na             # na | eu | fe，默认 na
export AMAZON_PROFILE_ID=...        # 可选
```

```python
from async_amazon_ads_api_v1 import AmazonAdsConfig, SPClient

config = AmazonAdsConfig.from_env()
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
