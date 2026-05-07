"""AdGroup resource operations."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import _RequestMethod


class AdGroups:
    """AdGroup 广告组资源操作。"""

    def __init__(self, request: _RequestMethod) -> None:
        self._request = request

    async def create(self, ad_groups: list[dict[str, Any]]) -> httpx.Response:
        """创建广告组。

        参数
        -----
        ad_groups : list[dict[str, Any]]
            广告组列表，每项包含 campaignId、name、bid、state 等字段。
        """
        return await self._request(
            "POST", "/adsApi/v1/create/adGroups", json={"adGroups": ad_groups}
        )

    async def query(self, body: dict[str, Any]) -> httpx.Response:
        """查询广告组。

        参数
        -----
        body : dict[str, Any]
            查询条件，包含 adGroupIdFilter、campaignIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        return await self._request("POST", "/adsApi/v1/query/adGroups", json=body)

    async def update(self, ad_groups: list[dict[str, Any]]) -> httpx.Response:
        """更新广告组。

        参数
        -----
        ad_groups : list[dict[str, Any]]
            广告组更新列表，每项需包含 adGroupId。
        """
        return await self._request(
            "POST", "/adsApi/v1/update/adGroups", json={"adGroups": ad_groups}
        )

    async def delete(self, ad_group_ids: list[str]) -> httpx.Response:
        """删除广告组。

        参数
        -----
        ad_group_ids : list[str]
            要删除的广告组 ID 列表。
        """
        return await self._request(
            "POST", "/adsApi/v1/delete/adGroups", json={"adGroupIds": ad_group_ids}
        )
