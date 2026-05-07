"""AdGroup resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
)

from ._base import _RequestMethod, _ResponseMethod


class AdGroups:
    """AdGroup 广告组资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    async def create(
        self, ad_groups: list[dict[str, Any] | SPAdGroupCreate]
    ) -> SPAdGroupSuccessResponse:
        """创建广告组。

        参数
        -----
        ad_groups : list[dict | SPAdGroupCreate]
            广告组列表，每项包含 campaignId、name、bid、state 等字段。
        """
        validated = [
            g.model_dump() if isinstance(g, SPAdGroupCreate) else SPAdGroupCreate(**g).model_dump()
            for g in ad_groups
        ]
        resp = await self._request(
            "POST", "/adsApi/v1/create/adGroups", json={"adGroups": validated}
        )
        return self._response(SPAdGroupSuccessResponse, resp)  # type: ignore[return-value]

    async def query(self, body: dict[str, Any]) -> SPAdGroupSuccessResponse:
        """查询广告组。

        参数
        -----
        body : dict
            查询条件，包含 adGroupIdFilter、campaignIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        resp = await self._request("POST", "/adsApi/v1/query/adGroups", json=body)
        return self._response(SPAdGroupSuccessResponse, resp)  # type: ignore[return-value]

    async def update(
        self, ad_groups: list[dict[str, Any] | SPAdGroupUpdate]
    ) -> SPAdGroupMultiStatusResponse:
        """更新广告组。

        参数
        -----
        ad_groups : list[dict | SPAdGroupUpdate]
            广告组更新列表，每项需包含 adGroupId。
        """
        validated = [
            g.model_dump() if isinstance(g, SPAdGroupUpdate) else SPAdGroupUpdate(**g).model_dump()
            for g in ad_groups
        ]
        resp = await self._request(
            "POST", "/adsApi/v1/update/adGroups", json={"adGroups": validated}
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)  # type: ignore[return-value]

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        """删除广告组。

        参数
        -----
        ad_group_ids : list[str]
            要删除的广告组 ID 列表。
        """
        resp = await self._request(
            "POST", "/adsApi/v1/delete/adGroups", json={"adGroupIds": ad_group_ids}
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)  # type: ignore[return-value]
