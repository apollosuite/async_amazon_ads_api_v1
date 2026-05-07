"""Target resource operations."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import _RequestMethod


class Targets:
    """Target 投放目标资源操作。"""

    def __init__(self, request: _RequestMethod) -> None:
        self._request = request

    async def create(self, targets: list[dict[str, Any]]) -> httpx.Response:
        """创建投放目标（关键词、商品投放等）。

        参数
        -----
        targets : list[dict[str, Any]]
            目标列表，每项包含 adGroupId、targetType、bid、state 等字段。
        """
        return await self._request("POST", "/adsApi/v1/create/targets", json={"targets": targets})

    async def query(self, body: dict[str, Any]) -> httpx.Response:
        """查询投放目标。

        参数
        -----
        body : dict[str, Any]
            查询条件，包含 targetIdFilter、adGroupIdFilter、campaignIdFilter 等。
            支持 nextToken 分页。
        """
        return await self._request("POST", "/adsApi/v1/query/targets", json=body)

    async def update(self, targets: list[dict[str, Any]]) -> httpx.Response:
        """更新投放目标。

        参数
        -----
        targets : list[dict[str, Any]]
            目标更新列表，每项需包含 targetId。
        """
        return await self._request("POST", "/adsApi/v1/update/targets", json={"targets": targets})

    async def delete(self, target_ids: list[str]) -> httpx.Response:
        """删除投放目标。

        参数
        -----
        target_ids : list[str]
            要删除的目标 ID 列表。
        """
        return await self._request(
            "POST", "/adsApi/v1/delete/targets", json={"targetIds": target_ids}
        )
