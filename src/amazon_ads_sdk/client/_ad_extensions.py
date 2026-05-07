"""AdExtension resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
)

if TYPE_CHECKING:
    from amazon_ads_sdk.client import AmazonAdsClient


class AdExtensions:
    """AdExtension 广告扩展资源操作。"""

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

    async def create(
        self,
        ad_extensions: list[dict[str, Any] | SPAdExtensionCreate],
    ) -> SPAdExtensionSuccessResponse:
        """创建广告扩展。"""
        validated = self._validate(ad_extensions, SPAdExtensionCreate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": validated},
            accept_async=True,
        )
        return self._client._response(SPAdExtensionSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdExtensionSuccessResponse:
        """查询广告扩展，支持 nextToken 分页。"""
        resp = await self._client._request("POST", "/adsApi/v1/query/adExtensions", json=body)
        return self._client._response(SPAdExtensionSuccessResponse, resp)

    async def update(
        self,
        ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate],
    ) -> SPAdExtensionSuccessResponse:
        """更新广告扩展。"""
        validated = self._validate(ad_extensions, SPAdExtensionUpdate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": validated},
            accept_async=True,
        )
        return self._client._response(SPAdExtensionSuccessResponse, resp)
