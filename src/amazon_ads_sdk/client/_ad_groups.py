"""AdGroup resource operations."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from amazon_ads_sdk.models import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
)

if TYPE_CHECKING:
    from amazon_ads_sdk.client import AmazonAdsClient


class AdGroups:
    """AdGroup 广告组资源操作。"""

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
        self, ad_groups: list[dict[str, Any] | SPAdGroupCreate]
    ) -> SPAdGroupSuccessResponse:
        """创建广告组。"""
        validated = self._validate(ad_groups, SPAdGroupCreate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json={"adGroups": validated},
            accept_async=True,
        )
        return self._client._response(SPAdGroupSuccessResponse, resp)

    async def query(self, body: dict[str, Any]) -> SPAdGroupSuccessResponse:
        """查询广告组，支持 nextToken 分页。"""
        resp = await self._client._request("POST", "/adsApi/v1/query/adGroups", json=body)
        return self._client._response(SPAdGroupSuccessResponse, resp)

    async def update(
        self, ad_groups: list[dict[str, Any] | SPAdGroupUpdate]
    ) -> SPAdGroupMultiStatusResponse:
        """更新广告组。"""
        validated = self._validate(ad_groups, SPAdGroupUpdate)
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json={"adGroups": validated},
            accept_async=True,
        )
        return self._client._response(SPAdGroupMultiStatusResponse, resp)

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        """删除广告组。"""
        resp = await self._client._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json={"adGroupIds": ad_group_ids},
            accept_async=True,
        )
        return self._client._response(SPAdGroupMultiStatusResponse, resp)
