"""Async HTTP client wrapping httpx."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.config import AmazonAdsConfig

from ._base import _AmazonAdsClientBase


class AmazonAdsClient(_AmazonAdsClientBase):
    """Async HTTP client for the Amazon Ads API.

    Parameters
    ----------
    config : AmazonAdsConfig
        Client configuration (auth, region, timeouts, retries).
    """

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config = config
        self._client: Any = None

    async def __aenter__(self) -> AmazonAdsClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    # ─── Campaigns ────────────────────────────────────────────────────────────

    async def create_campaigns(self, campaigns: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/create/campaigns", json={"campaigns": campaigns})

    async def query_campaigns(self, body: dict[str, Any]) -> Any:
        return await self._request("POST", "/adsApi/v1/query/campaigns", json=body)

    async def update_campaigns(self, campaigns: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/update/campaigns", json={"campaigns": campaigns})

    async def delete_campaigns(self, campaign_ids: list[str]) -> Any:
        return await self._request("POST", "/adsApi/v1/delete/campaigns", json={"campaignIds": campaign_ids})

    # ─── AdGroups ─────────────────────────────────────────────────────────────

    async def create_ad_groups(self, ad_groups: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/create/adGroups", json={"adGroups": ad_groups})

    async def query_ad_groups(self, body: dict[str, Any]) -> Any:
        return await self._request("POST", "/adsApi/v1/query/adGroups", json=body)

    async def update_ad_groups(self, ad_groups: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/update/adGroups", json={"adGroups": ad_groups})

    async def delete_ad_groups(self, ad_group_ids: list[str]) -> Any:
        return await self._request("POST", "/adsApi/v1/delete/adGroups", json={"adGroupIds": ad_group_ids})

    # ─── Ads ─────────────────────────────────────────────────────────────────

    async def create_ads(self, ads: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/create/ads", json={"ads": ads})

    async def query_ads(self, body: dict[str, Any]) -> Any:
        return await self._request("POST", "/adsApi/v1/query/ads", json=body)

    async def update_ads(self, ads: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/update/ads", json={"ads": ads})

    async def delete_ads(self, ad_ids: list[str]) -> Any:
        return await self._request("POST", "/adsApi/v1/delete/ads", json={"adIds": ad_ids})

    # ─── Targets ─────────────────────────────────────────────────────────────

    async def create_targets(self, targets: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/create/targets", json={"targets": targets})

    async def query_targets(self, body: dict[str, Any]) -> Any:
        return await self._request("POST", "/adsApi/v1/query/targets", json=body)

    async def update_targets(self, targets: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/update/targets", json={"targets": targets})

    async def delete_targets(self, target_ids: list[str]) -> Any:
        return await self._request("POST", "/adsApi/v1/delete/targets", json={"targetIds": target_ids})

    # ─── AdExtensions ────────────────────────────────────────────────────────

    async def create_ad_extensions(self, ad_extensions: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/create/adExtensions", json={"adExtensions": ad_extensions})

    async def query_ad_extensions(self, body: dict[str, Any]) -> Any:
        return await self._request("POST", "/adsApi/v1/query/adExtensions", json=body)

    async def update_ad_extensions(self, ad_extensions: list[dict[str, Any]]) -> Any:
        return await self._request("POST", "/adsApi/v1/update/adExtensions", json={"adExtensions": ad_extensions})
