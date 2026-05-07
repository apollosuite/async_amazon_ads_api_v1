"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
)

from ._context import ClientContext
from ._resource import _ResourceBase


class AdExtensions(_ResourceBase):
    """AdExtension 广告扩展资源操作。"""

    def __init__(self, ctx: ClientContext) -> None:
        super().__init__(ctx)

    async def create(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionCreate]
    ) -> SPAdExtensionSuccessResponse:
        """创建广告扩展。"""
        validated = self._validate(ad_extensions, SPAdExtensionCreate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": validated},
            accept_async=True,
        )
        return self._response(SPAdExtensionSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdExtensionSuccessResponse:
        """查询广告扩展，支持 nextToken 分页。"""
        resp = await self._request("POST", "/adsApi/v1/query/adExtensions", json=body)
        return self._response(SPAdExtensionSuccessResponse, resp)

    async def update(
        self, ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate]
    ) -> SPAdExtensionSuccessResponse:
        """更新广告扩展。"""
        validated = self._validate(ad_extensions, SPAdExtensionUpdate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": validated},
            accept_async=True,
        )
        return self._response(SPAdExtensionSuccessResponse, resp)
