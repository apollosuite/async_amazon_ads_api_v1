"""Ad resource operations."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import _RequestMethod


class Ads:
    """Ad 广告资源操作。"""

    def __init__(self, request: _RequestMethod) -> None:
        self._request = request

    async def create(self, ads: list[dict[str, Any]]) -> httpx.Response:
        """创建广告。

        参数
        -----
        ads : list[dict[str, Any]]
            广告列表，每项包含 adGroupId、adProduct、creative、state 等字段。
        """
        return await self._request(
            "POST", "/adsApi/v1/create/ads", json={"ads": ads}
        )

    async def query(self, body: dict[str, Any]) -> httpx.Response:
        """查询广告。

        参数
        -----
        body : dict[str, Any]
            查询条件，包含 adIdFilter、adGroupIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        return await self._request("POST", "/adsApi/v1/query/ads", json=body)

    async def update(self, ads: list[dict[str, Any]]) -> httpx.Response:
        """更新广告。

        参数
        -----
        ads : list[dict[str, Any]]
            广告更新列表，每项需包含 adId。
        """
        return await self._request(
            "POST", "/adsApi/v1/update/ads", json={"ads": ads}
        )

    async def delete(self, ad_ids: list[str]) -> httpx.Response:
        """删除广告。

        参数
        -----
        ad_ids : list[str]
            要删除的广告 ID 列表。
        """
        return await self._request(
            "POST", "/adsApi/v1/delete/ads", json={"adIds": ad_ids}
        )
