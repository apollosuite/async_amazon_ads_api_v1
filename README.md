# Amazon Ads Python SDK (v0 & v1)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python versions](https://img.shields.io/pypi/pyversions/async-amazon-ads-api-v1)](https://pypi.org/project/async-amazon-ads-api-v1/)

Amazon Ads API Python SDK，提供**纯异步（Async）**与**原生纯同步（Sync）**两套物理隔离的独立分发包。统一覆盖 v0 与 v1（SP、SB、SD、DSP、ST、SP Global、Accounts、Reporting、Ads Data Manager、Exports 等）。

## Packages

| Package | PyPI 安装名 | Python 导入名 | 底层 I/O | 适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **异步包 (Async)** | [`async-amazon-ads-api-v1`](https://pypi.org/project/async-amazon-ads-api-v1/) | `ads_api` | `httpx.AsyncClient` | FastAPI, Tornado, 高并发微服务 |
| **同步包 (Sync)** | [`amazon-ads-api-v1`](https://pypi.org/project/amazon-ads-api-v1/) | `ads_api` | `httpx.Client` | Jupyter, Pandas, Django/Flask, Celery, 自动化脚本 |

两套包的模型、参数结构及调用体验完全一致，同步版本直接调用方法（无需 `async/await`），无事件循环冲突。

## Installation

### 异步版本 (Async)
```bash
pip install async-amazon-ads-api-v1
# 或
uv add async-amazon-ads-api-v1
```

### 同步版本 (Sync)
```bash
pip install amazon-ads-api-v1
# 或
uv add amazon-ads-api-v1
```

## Quick Start 对比

### 异步调用 (Async)
```python
import asyncio
from ads_api import AdsClient, AmazonAdsConfig, Region
from ads_api.models.v1.campaigns.sp import SPQueryCampaignRequest

async def main() -> None:
    config = AmazonAdsConfig(client_id="...", access_token="...", region=Region.NA)
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )
    async with AdsClient(config) as ads:
        resp = await ads.v1.sp.campaigns.query_campaign(body)
        print(resp)

asyncio.run(main())
```

### 同步调用 (Sync)
```python
from ads_api import AdsClient, AmazonAdsConfig, Region
from ads_api.models.v1.campaigns.sp import SPQueryCampaignRequest

def main() -> None:
    config = AmazonAdsConfig(client_id="...", access_token="...", region=Region.NA)
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

## License

[MIT](LICENSE)
