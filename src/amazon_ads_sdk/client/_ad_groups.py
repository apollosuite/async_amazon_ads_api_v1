"""AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
)

from ._base import _RequestMethod, _ResponseMethod, resource


class AdGroups:
    """AdGroup 广告组资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    @resource(
        "POST",
        "/adsApi/v1/create/adGroups",
        response=SPAdGroupSuccessResponse,
        wrap="adGroups",
        request_model=SPAdGroupCreate,
        accept_async=True,
    )
    async def create(
        self, ad_groups: list[dict[str, Any] | SPAdGroupCreate]
    ) -> SPAdGroupSuccessResponse:
        """创建广告组。"""
        return ad_groups  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/query/adGroups",
        response=SPAdGroupSuccessResponse,
    )
    async def query(self, body: dict[str, Any]) -> SPAdGroupSuccessResponse:
        """查询广告组，支持 nextToken 分页。"""
        return body  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/update/adGroups",
        response=SPAdGroupMultiStatusResponse,
        wrap="adGroups",
        request_model=SPAdGroupUpdate,
        accept_async=True,
    )
    async def update(
        self, ad_groups: list[dict[str, Any] | SPAdGroupUpdate]
    ) -> SPAdGroupMultiStatusResponse:
        """更新广告组。"""
        return ad_groups  # type: ignore[return-value]

    @resource(
        "POST",
        "/adsApi/v1/delete/adGroups",
        response=SPAdGroupMultiStatusResponse,
        wrap="adGroupIds",
        accept_async=True,
    )
    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        """删除广告组。"""
        return ad_group_ids  # type: ignore[return-value]
