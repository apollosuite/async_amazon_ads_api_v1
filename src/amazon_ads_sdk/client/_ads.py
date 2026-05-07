"""Ad resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
)

if TYPE_CHECKING:
    from amazon_ads_sdk.client import AmazonAdsClient


class Ads:
    """Ad 广告资源操作。"""

    def __init__(self, client: AmazonAdsClient) -> None:
        self._client = client

    def _validate(self, items: list[Any], model_cls: type[Any]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for item in items:
            if isinstance(item, model_cls):
                result.append(item.model_dump())
            else:
                result.append(model_cls(**item).model_dump())
        return result

    async def create(self, ads: list[dict[str, Any] | SPAdCreate]) -> SPAdSuccessResponse:
        """创建广告。"""
        validated = self._validate(ads, SPAdCreate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/create/ads",
            json={"ads": validated},
            accept_async=True,
        )
        return self._client._response(SPAdSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdSuccessResponse:
        """查询广告，支持 nextToken 分页。"""
        resp = await self._client._request("POST", "/adsApi/v1/query/ads", json=body)
        return self._client._response(SPAdSuccessResponse, resp)

    async def update(self, ads: list[dict[str, Any] | SPAdUpdate]) -> SPAdMultiStatusResponse:
        """更新广告。"""
        validated = self._validate(ads, SPAdUpdate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/update/ads",
            json={"ads": validated},
            accept_async=True,
        )
        return self._client._response(SPAdMultiStatusResponse, resp)

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        """删除广告。"""
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json={"adIds": ad_ids},
            accept_async=True,
        )
        return self._client._response(SPAdMultiStatusResponse, resp)
