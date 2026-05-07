"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdExtensionCreate,
    SPAdExtensionSuccessResponse,
    SPAdExtensionUpdate,
)

from ._base import _RequestMethod, _ResponseMethod, resource


class AdExtensions:
    """AdExtension 广告扩展资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    @resource(
        "POST",
        "/adsApi/v1/create/adExtensions",
        response=SPAdExtensionSuccessResponse,
        wrap="adExtensions",
        request_model=SPAdExtensionCreate,
    )
    async def create(
        self,
        ad_extensions: list[dict[str, Any] | SPAdExtensionCreate],
    ) -> SPAdExtensionSuccessResponse:
        """创建广告扩展。"""
        return ad_extensions  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/query/adExtensions",
        response=SPAdExtensionSuccessResponse,
    )
    async def query(self, body: dict[str, Any]) -> SPAdExtensionSuccessResponse:
        """查询广告扩展，支持 nextToken 分页。"""
        return body  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/update/adExtensions",
        response=SPAdExtensionSuccessResponse,
        wrap="adExtensions",
        request_model=SPAdExtensionUpdate,
    )
    async def update(
        self,
        ad_extensions: list[dict[str, Any] | SPAdExtensionUpdate],
    ) -> SPAdExtensionSuccessResponse:
        """更新广告扩展。"""
        return ad_extensions  # type: ignore[return-value]
