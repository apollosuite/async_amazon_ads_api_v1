"""AdExtension resource operations."""

from __future__ import annotations

from typing import Any

import httpx

from ._base import _RequestMethod


class AdExtensions:
    """AdExtension 广告扩展资源操作。"""

    def __init__(self, request: _RequestMethod) -> None:
        self._request = request

    async def create(self, ad_extensions: list[dict[str, Any]]) -> httpx.Response:
        """创建广告扩展（Prompts、Video 等类型）。

        参数
        -----
        ad_extensions : list[dict[str, Any]]
            广告扩展列表，每项包含 adExtensionType、adExtensionSettings 等字段。
        """
        return await self._request(
            "POST",
            "/adsApi/v1/create/adExtensions",
            json={"adExtensions": ad_extensions},
        )

    async def query(self, body: dict[str, Any]) -> httpx.Response:
        """查询广告扩展。

        参数
        -----
        body : dict[str, Any]
            查询条件，包含 adExtensionIdFilter、adExtensionTypeFilter 等。
            支持 nextToken 分页。
        """
        return await self._request("POST", "/adsApi/v1/query/adExtensions", json=body)

    async def update(self, ad_extensions: list[dict[str, Any]]) -> httpx.Response:
        """更新广告扩展。

        参数
        -----
        ad_extensions : list[dict[str, Any]]
            广告扩展更新列表，每项需包含 adExtensionId。
        """
        return await self._request(
            "POST",
            "/adsApi/v1/update/adExtensions",
            json={"adExtensions": ad_extensions},
        )
