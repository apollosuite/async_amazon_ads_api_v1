"""AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
)

from ._context import ClientContext
from ._resource import _ResourceBase


class AdGroups(_ResourceBase):
    """AdGroup 广告组资源操作。"""

    def __init__(self, ctx: ClientContext) -> None:
        super().__init__(ctx)

    async def create(
        self, ad_groups: list[dict[str, Any] | SPAdGroupCreate]
    ) -> SPAdGroupSuccessResponse:
        """创建广告组。"""
        validated = self._validate(ad_groups, SPAdGroupCreate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json={"adGroups": validated},
            accept_async=True,
        )
        return self._response(SPAdGroupSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdGroupSuccessResponse:
        """查询广告组，支持 nextToken 分页。"""
        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=body)
        return self._response(SPAdGroupSuccessResponse, resp)

    async def update(
        self, ad_groups: list[dict[str, Any] | SPAdGroupUpdate]
    ) -> SPAdGroupMultiStatusResponse:
        """更新广告组。"""
        validated = self._validate(ad_groups, SPAdGroupUpdate)
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json={"adGroups": validated},
            accept_async=True,
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        """删除广告组。"""
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json={"adGroupIds": ad_group_ids},
            accept_async=True,
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)
