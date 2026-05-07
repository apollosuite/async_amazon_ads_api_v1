"""Campaign resource operations."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import _RequestMethod


class Campaigns:
    """Campaign 广告活动资源操作。"""

    def __init__(self, request: _RequestMethod) -> None:
        self._request = request

    async def create(self, campaigns: list[dict[str, Any]]) -> httpx.Response:
        """创建广告活动。

        参数
        -----
        campaigns : list[dict[str, Any]]
            广告活动列表，每项包含 name、state、budgets 等字段。
        """
        return await self._request(
            "POST", "/adsApi/v1/create/campaigns", json={"campaigns": campaigns}
        )

    async def query(self, body: dict[str, Any]) -> httpx.Response:
        """查询广告活动。

        参数
        -----
        body : dict[str, Any]
            查询条件，包含 stateFilter、campaignIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        return await self._request("POST", "/adsApi/v1/query/campaigns", json=body)

    async def update(self, campaigns: list[dict[str, Any]]) -> httpx.Response:
        """更新广告活动。

        参数
        -----
        campaigns : list[dict[str, Any]]
            广告活动更新列表，每项需包含 campaignId。
        """
        return await self._request(
            "POST", "/adsApi/v1/update/campaigns", json={"campaigns": campaigns}
        )

    async def delete(self, campaign_ids: list[str]) -> httpx.Response:
        """删除广告活动。

        参数
        -----
        campaign_ids : list[str]
            要删除的广告活动 ID 列表。
        """
        return await self._request(
            "POST", "/adsApi/v1/delete/campaigns", json={"campaignIds": campaign_ids}
        )
