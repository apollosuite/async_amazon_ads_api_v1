# amazon-ads-api-v1

[![PyPI version](https://img.shields.io/pypi/v/amazon-ads-api-v1)](https://pypi.org/project/amazon-ads-api-v1/)
[![Python versions](https://img.shields.io/pypi/pyversions/amazon-ads-api-v1)](https://pypi.org/project/amazon-ads-api-v1/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

纯同步 Amazon Ads API 客户端。PyPI 安装名为 **`amazon-ads-api-v1`**，导入名为 **`ads_api`**。统一覆盖 v0 与 v1（SP、SB、SD、DSP、ST、SP Global、Accounts、Reporting、Ads Data Manager、Exports 等）。原生基于 `httpx.Client`，支持直接调用，无事件循环冲突。

## Installation

```bash
pip install amazon-ads-api-v1
# 或
uv add amazon-ads-api-v1
```

Redis 缓存支持：

```bash
pip install "amazon-ads-api-v1[redis]"
# 或
uv add "amazon-ads-api-v1[redis]"
```

## Quick Start

所有 API 方法仅接受 Pydantic model 实例，不支持 dict。默认 `mode="dict"`，需要模型对象时传 `mode="pydantic"`。

### 使用 Access Token

```python
from ads_api import AdsClient, AmazonAdsConfig, Region
from ads_api.models.v1.campaigns.sp import SPQueryCampaignRequest


def main() -> None:
    config = AmazonAdsConfig(
        access_token="your-access-token",
        client_id="your-client-id",
        region=Region.NA,
    )
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )

    with AdsClient(config) as ads:
        resp = ads.v1.sp.campaigns.query_campaign(body)
        print(resp)


if __name__ == "__main__":
    main()
```

### 使用 Refresh Token（自动续期）

```python
from ads_api import AdsClient, AmazonAdsConfig, Region
from ads_api.models.v1.campaigns.sp import SPQueryCampaignRequest


def main() -> None:
    config = AmazonAdsConfig(
        client_id="your-client-id",
        refresh_token="your-refresh-token",
        client_secret="your-client-secret",
        region=Region.NA,
    )
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )

    with AdsClient(config) as ads:
        resp = ads.v1.sp.campaigns.query_campaign(body, mode="pydantic")
        print(resp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
```

## Token Management

SDK 内置 OAuth token 生命周期管理。提供 `refresh_token` 与 `client_secret` 后会自动续期；缓存按字段推断：

```python
from ads_api import AmazonAdsConfig, Region

# 自动续期，不使用磁盘 / Redis 缓存
config = AmazonAdsConfig(
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token",
    region=Region.NA,
)

# 文件缓存
config = AmazonAdsConfig(
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token",
    region=Region.NA,
    token_cache_dir="~/.cache/ads_api",
)

# Redis 缓存
config = AmazonAdsConfig(
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token",
    region=Region.NA,
    redis_url="redis://localhost:6379",
)
```

## API 入口

```python
with AdsClient(config) as ads:
    # v1
    ads.v1.sp.campaigns.query_campaign(body)
    ads.v1.sb.campaigns.query_campaign(body)
    ads.v1.sd.campaigns.query_campaign(body)
    ads.v1.selling_accounts.query_selling_account(body)
    ads.v1.reports.create_report(body)

    # v0
    ads.v0.accounts.profiles.list_profiles()
    ads.v0.portfolios.list_portfolios()
    ads.v0.sp_v3.campaigns.create_sponsored_products_campaigns(body)
    ads.v0.sb_v4.budget_rules.create_budget_rules_for_sb_campaigns(body)
    ads.v0.sd.creatives.create_creatives(body)
```

## License

[MIT](LICENSE)
