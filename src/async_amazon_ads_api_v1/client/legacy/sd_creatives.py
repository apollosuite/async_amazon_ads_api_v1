"""SD Creatives resource operations — from sponsoredDisplay_30_openapi.yaml."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sd_creatives import (
    SDCreateCreative,
    SDCreative,
    SDCreativeModeration,
    SDCreativePreviewRequest,
    SDCreativePreviewResponse,
    SDCreativeResponse,
    SDCreativeUpdate,
)


class SDCreatives(_ResourceBase):
    """Sponsored Display Creatives API."""

    async def list_creatives(
        self,
    ) -> list[SDCreative]:
        """获取创意列表。"""
        resp = await self._request("GET", "/sd/creatives")
        return [SDCreative.model_construct(**item) for item in resp.json()]

    async def create_creatives(
        self,
        creatives: list[SDCreateCreative],
    ) -> list[SDCreativeResponse]:
        """批量创建创意。"""
        resp = await self._request(
            "POST",
            "/sd/creatives",
            json=[c.model_dump(exclude_none=True) for c in creatives],
        )
        return [SDCreativeResponse.model_construct(**item) for item in resp.json()]

    async def update_creatives(
        self,
        creatives: list[SDCreativeUpdate],
    ) -> list[SDCreativeResponse]:
        """批量更新创意。"""
        resp = await self._request(
            "PUT",
            "/sd/creatives",
            json=[c.model_dump(exclude_none=True) for c in creatives],
        )
        return [SDCreativeResponse.model_construct(**item) for item in resp.json()]

    async def preview_creative(
        self,
        request: SDCreativePreviewRequest,
    ) -> SDCreativePreviewResponse:
        """获取创意预览 HTML。"""
        resp = await self._request(
            "POST",
            "/sd/creatives/preview",
            json=request.model_dump(),
        )
        return self._response(SDCreativePreviewResponse, resp)

    async def list_creative_moderations(
        self,
    ) -> list[SDCreativeModeration]:
        """获取创意审核列表。"""
        resp = await self._request("GET", "/sd/moderation/creatives")
        return [SDCreativeModeration.model_construct(**item) for item in resp.json()]
