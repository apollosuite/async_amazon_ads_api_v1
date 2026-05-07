"""Ad resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
)

from ._resource import _ResourceBase

if TYPE_CHECKING:
    from ._context import ClientContext


class Ads(_ResourceBase):
    """Ad 广告资源操作。"""

    def __init__(self, ctx: ClientContext) -> None:
        super().__init__(ctx)

    async def create(self, ads: list[dict[str, Any] | SPAdCreate]) -> SPAdSuccessResponse:
        """创建广告。"""
        validated = self._validate(ads, SPAdCreate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json={"ads": validated},
            accept_async=True,
        )
        return self._response(SPAdSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdSuccessResponse:
        """查询广告，支持 nextToken 分页。"""
        resp = await self._request("POST", "/adsApi/v1/query/ads", json=body)
        return self._response(SPAdSuccessResponse, resp)

    async def update(self, ads: list[dict[str, Any] | SPAdUpdate]) -> SPAdMultiStatusResponse:
        """更新广告。"""
        validated = self._validate(ads, SPAdUpdate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json={"ads": validated},
            accept_async=True,
        )
        return self._response(SPAdMultiStatusResponse, resp)

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        """删除广告。"""
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json={"adIds": ad_ids},
            accept_async=True,
        )
        return self._response(SPAdMultiStatusResponse, resp)
