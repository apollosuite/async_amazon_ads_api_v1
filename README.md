# Amazon Ads SDK

Pure async Python SDK for Amazon Advertising API — Sponsored Products.

## Installation

```bash
uv sync
```

## Quick Start

```python
import asyncio
from amazon_ads_sdk import AmazonAdsClient, AmazonAdsConfig, Region

async def main():
    config = AmazonAdsConfig(
        access_token="YOUR_ACCESS_TOKEN",
        region=Region.NA,
    )
    async with AmazonAdsClient(config) as client:
        resp = await client.campaign.query({"stateFilter": {"include": ["enabled"]}})
        print(resp.model_dump_json(indent=2))

asyncio.run(main())
```

## API Reference

`AmazonAdsClient` 通过嵌套 property 暴露各资源：

| 资源 | 方法 | 响应类型 |
|---|---|---|
| `client.campaign` | `create()`, `query()`, `update()`, `delete()` | `SPCampaignSuccessResponse` / `SPCampaignMultiStatusResponse` |
| `client.ad_group` | `create()`, `query()`, `update()`, `delete()` | `SPAdGroupSuccessResponse` / `SPAdGroupMultiStatusResponse` |
| `client.ad` | `create()`, `query()`, `update()`, `delete()` | `SPAdSuccessResponse` / `SPAdMultiStatusResponse` |
| `client.target` | `create()`, `query()`, `update()`, `delete()` | `SPTargetSuccessResponse` / `SPTargetMultiStatusResponse` |
| `client.ad_extension` | `create()`, `query()`, `update()` | `SPAdExtensionSuccessResponse` / `SPAdExtensionMultiStatusResponse` |
