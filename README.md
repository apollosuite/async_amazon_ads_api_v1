# async-amazon-ads-api-v1

[![PyPI version](https://img.shields.io/pypi/v/async-amazon-ads-api-v1)](https://pypi.org/project/async-amazon-ads-api-v1/)
[![Python versions](https://img.shields.io/pypi/pyversions/async-amazon-ads-api-v1)](https://pypi.org/project/async-amazon-ads-api-v1/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Pure async Amazon Ads API v1 client — Sponsored Products, Sponsored Brands, Sponsored Display.

## Installation

```bash
pip install async-amazon-ads-api-v1
# 或
uv add async-amazon-ads-api-v1
```

Redis 缓存支持：

```bash
pip install "async-amazon-ads-api-v1[redis]"
# 或
uv add "async-amazon-ads-api-v1[redis]"
```

## Quick Start

所有 API 方法仅接受 Pydantic model 实例，不支持 dict。

### 使用 Access Token（直接提供）

```python
import asyncio
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient
from async_amazon_ads_api_v1.models.sp import SPQueryCampaignRequest


async def main() -> None:
    config = AmazonAdsConfig(
        access_token="your-access-token",
        client_id="your-client-id",
        region=Region.NA,
    )
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )

    async with SPClient(config) as sp:
        resp = await sp.campaigns.query(body)
        print(resp.model_dump_json(indent=2))


asyncio.run(main())
```

### 使用 Refresh Token（自动续期）

```python
import asyncio
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient
from async_amazon_ads_api_v1.models.sp import SPQueryCampaignRequest


async def main() -> None:
    config = AmazonAdsConfig(
        access_token="your-access-token",   # 可选，提供后直接使用
        client_id="your-client-id",
        refresh_token="your-refresh-token", # access_token 过期后自动刷新
        client_secret="your-client-secret",
        region=Region.NA,
    )
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )

    async with SPClient(config) as sp:
        resp = await sp.campaigns.query(body)
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
from async_amazon_ads_api_v1.config.loader import from_toml

config = from_toml()
```

## Environment Variables

| 变量 | 必填 | 说明 |
|---|---|---|
| `AMAZON_ACCESS_TOKEN` | 条件 | OAuth bearer token（或使用 refresh_token 自动获取） |
| `AMAZON_CLIENT_ID` | 条件 | OAuth client ID（使用 refresh_token 时必填） |
| `AMAZON_REFRESH_TOKEN` | 否 | OAuth refresh token，用于自动续期 |
| `AMAZON_CLIENT_SECRET` | 条件 | OAuth client secret（使用 refresh_token 时必填） |
| `AMAZON_REGION` | 否 | `na` \| `eu` \| `fe`，默认 `na` |
| `AMAZON_PROFILE_ID` | 否 | 广告主 profile ID |
| `AMAZON_TOKEN_URL` | 否 | 自定义 token 端点 |
| `AMAZON_TOKEN_CACHE_DIR` | 否 | 文件缓存目录（默认系统临时目录） |
| `AMAZON_CACHE_BACKEND` | 否 | `file` \| `redis`，默认 `file` |
| `AMAZON_REDIS_URL` | 否 | Redis 连接 URL（使用 redis 缓存时需要） |
| `AMAZON_ENDPOINT_NA` | 否 | 覆盖 NA 端点 |
| `AMAZON_ENDPOINT_EU` | 否 | 覆盖 EU 端点 |
| `AMAZON_ENDPOINT_FE` | 否 | 覆盖 FE 端点 |

## Token Management

SDK 内置 OAuth token 生命周期管理，支持自动续期和缓存：

```python
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region

# 自动续期 + 文件缓存（默认）
config = AmazonAdsConfig(
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token",
    region=Region.NA,
)

# 自动续期 + Redis 缓存
config = AmazonAdsConfig(
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token",
    region=Region.NA,
    cache_backend="redis",
    redis_url="redis://localhost:6379",
)
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

## Legacy / 非标准 API

以下资源类不遵循 `/adsApi/v1` 通用 CRUD 模式，需要单独实例化：

### BudgetRules — 预算规则关联

SP、SB、SD 共用同一接口结构，通过 `product` 参数切换：

```python
from async_amazon_ads_api_v1.client.legacy import BudgetRules

rules = BudgetRules(ctx, product="sp")  # "sp" | "sb" | "sd"
await rules.get_associated_rules("campaign-id")
await rules.associate_to_campaign("campaign-id", ["rule-id-1"])
await rules.disassociate_from_campaign("campaign-id", "rule-id-1")
```

### Portfolios — 投资组合

```python
from async_amazon_ads_api_v1.client.legacy import Portfolios

pf = Portfolios(ctx)
await pf.list()
await pf.update([portfolio])
```

### SBOptimizationRules — SB 优化规则 (Beta)

```python
from async_amazon_ads_api_v1.client.legacy import SBOptimizationRules
from async_amazon_ads_api_v1.models.legacy import SBEntityFilter, SBListOptimizationRulesRequest

rules = SBOptimizationRules(ctx)
request = SBListOptimizationRulesRequest(
    entityFilter=SBEntityFilter(entityType="CAMPAIGN", entityId="..."),
)
await rules.list_optimization_rules(request)
await rules.disassociate_optimization_rules(request)
```

### SDOptimizationRules — SD 优化规则 (Beta)

```python
from async_amazon_ads_api_v1.client.legacy import SDOptimizationRules

rules = SDOptimizationRules(ctx)
await rules.list_optimization_rules("ad-group-id")
await rules.disassociate_optimization_rules("ad-group-id", request)
```

### SDCreatives — SD 创意

```python
from async_amazon_ads_api_v1.client.legacy import SDCreatives

creatives = SDCreatives(ctx)
await creatives.create([{...}])
```

## License

[MIT](LICENSE)
