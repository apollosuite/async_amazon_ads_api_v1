"""Async HTTP client wrapping httpx."""

from __future__ import annotations

import asyncio
from typing import Any

import httpx

from amazon_ads_sdk.config import AmazonAdsConfig


class AmazonAdsClient:
    """Async HTTP client for the Amazon Ads API.

    Parameters
    ----------
    config : AmazonAdsConfig
        Client configuration (auth, region, timeouts, retries).
    """

    BASE_URL: str = "https://advertising-api.amazon.com"
    API_VERSION: str = "v1"

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config = config
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.config.region.value,
                timeout=httpx.Timeout(self.config.timeout),
                headers={
                    "Authorization": f"Bearer {self.config.access_token}",
                    "Content-Type": "application/json",
                    "Accept": "application/vnd.createasyncrequestresults.v3+json",
                },
            )
        return self._client

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> AmazonAdsClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    def _profile_header(self) -> dict[str, str]:
        if self.config.profile_id is not None:
            return {"Amazon-Advertising-API-ProfileId": str(self.config.profile_id)}
        return {}

    # ─── Internal request helper with retry ─────────────────────────────────

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> httpx.Response:
        client = await self._get_client()
        headers = self._profile_header()
        for attempt in range(self.config.max_retries):
            try:
                resp = await client.request(
                    method=method,
                    url=path,
                    params=params,
                    json=json,
                    headers=headers,
                )
                resp.raise_for_status()
                return resp
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self.config.max_retries - 1:
                        await asyncio.sleep(2 ** attempt)
                        continue
                raise
            except httpx.ConnectError:
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise
        # satisfy mypy — should not reach here
        raise RuntimeError("Retry loop exited unexpectedly")

    # ─── Campaigns ────────────────────────────────────────────────────────────

    async def create_campaigns(self, campaigns: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/create/campaigns", json={"campaigns": campaigns})

    async def query_campaigns(self, body: dict[str, Any]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/query/campaigns", json=body)

    async def update_campaigns(self, campaigns: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/update/campaigns", json={"campaigns": campaigns})

    async def delete_campaigns(self, campaign_ids: list[str]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/delete/campaigns", json={"campaignIds": campaign_ids})

    # ─── AdGroups ─────────────────────────────────────────────────────────────

    async def create_ad_groups(self, ad_groups: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/create/adGroups", json={"adGroups": ad_groups})

    async def query_ad_groups(self, body: dict[str, Any]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/query/adGroups", json=body)

    async def update_ad_groups(self, ad_groups: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/update/adGroups", json={"adGroups": ad_groups})

    async def delete_ad_groups(self, ad_group_ids: list[str]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/delete/adGroups", json={"adGroupIds": ad_group_ids})

    # ─── Ads ─────────────────────────────────────────────────────────────────

    async def create_ads(self, ads: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/create/ads", json={"ads": ads})

    async def query_ads(self, body: dict[str, Any]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/query/ads", json=body)

    async def update_ads(self, ads: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/update/ads", json={"ads": ads})

    async def delete_ads(self, ad_ids: list[str]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/delete/ads", json={"adIds": ad_ids})

    # ─── Targets ─────────────────────────────────────────────────────────────

    async def create_targets(self, targets: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/create/targets", json={"targets": targets})

    async def query_targets(self, body: dict[str, Any]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/query/targets", json=body)

    async def update_targets(self, targets: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/update/targets", json={"targets": targets})

    async def delete_targets(self, target_ids: list[str]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/delete/targets", json={"targetIds": target_ids})

    # ─── AdExtensions ────────────────────────────────────────────────────────

    async def create_ad_extensions(self, ad_extensions: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/create/adExtensions", json={"adExtensions": ad_extensions})

    async def query_ad_extensions(self, body: dict[str, Any]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/query/adExtensions", json=body)

    async def update_ad_extensions(self, ad_extensions: list[dict[str, Any]]) -> httpx.Response:
        return await self._request("POST", "/adsApi/v1/update/adExtensions", json={"adExtensions": ad_extensions})
