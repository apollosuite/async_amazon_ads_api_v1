"""Ad resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
)

from ._base import _RequestMethod, _ResponseMethod, resource


class Ads:
    """Ad 广告资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    @resource(
        "POST",
        "/adsApi/v1/create/ads",
        response=SPAdSuccessResponse,
        wrap="ads",
        request_model=SPAdCreate,
    )
    async def create(self, ads: list[dict[str, Any] | SPAdCreate]) -> SPAdSuccessResponse:
        """创建广告。"""
        return ads  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/query/ads",
        response=SPAdSuccessResponse,
    )
    async def query(self, body: dict[str, Any]) -> SPAdSuccessResponse:
        """查询广告，支持 nextToken 分页。"""
        return body  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/update/ads",
        response=SPAdMultiStatusResponse,
        wrap="ads",
        request_model=SPAdUpdate,
    )
    async def update(self, ads: list[dict[str, Any] | SPAdUpdate]) -> SPAdMultiStatusResponse:
        """更新广告。"""
        return ads  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/delete/ads",
        response=SPAdMultiStatusResponse,
        wrap="adIds",
    )
    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        """删除广告。"""
        return ad_ids  # type: ignore[return-value]
