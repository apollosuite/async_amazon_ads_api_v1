"""Ad resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk.models import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
)

from ._base import _RequestMethod, _ResponseMethod


class Ads:
    """Ad 广告资源操作。"""

    def __init__(self, request: _RequestMethod, response: _ResponseMethod) -> None:
        self._request = request
        self._response = response

    async def create(self, ads: list[dict[str, Any] | SPAdCreate]) -> SPAdSuccessResponse:
        """创建广告。

        参数
        -----
        ads : list[dict | SPAdCreate]
            广告列表，每项包含 adGroupId、adProduct、creative、state 等字段。
        """
        validated = [
            a.model_dump() if isinstance(a, SPAdCreate) else SPAdCreate(**a).model_dump()
            for a in ads
        ]
        resp = await self._request("POST", "/adsApi/v1/create/ads", json={"ads": validated})
        return self._response(SPAdSuccessResponse, resp)  # type: ignore[return-value]

    async def query(self, body: dict[str, Any]) -> SPAdSuccessResponse:
        """查询广告。

        参数
        -----
        body : dict
            查询条件，包含 adIdFilter、adGroupIdFilter 等过滤条件。
            支持 nextToken 分页。
        """
        resp = await self._request("POST", "/adsApi/v1/query/ads", json=body)
        return self._response(SPAdSuccessResponse, resp)  # type: ignore[return-value]

    async def update(self, ads: list[dict[str, Any] | SPAdUpdate]) -> SPAdMultiStatusResponse:
        """更新广告。

        参数
        -----
        ads : list[dict | SPAdUpdate]
            广告更新列表，每项需包含 adId。
        """
        validated = [
            a.model_dump() if isinstance(a, SPAdUpdate) else SPAdUpdate(**a).model_dump()
            for a in ads
        ]
        resp = await self._request("POST", "/adsApi/v1/update/ads", json={"ads": validated})
        return self._response(SPAdMultiStatusResponse, resp)  # type: ignore[return-value]

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        """删除广告。

        参数
        -----
        ad_ids : list[str]
            要删除的广告 ID 列表。
        """
        resp = await self._request("POST", "/adsApi/v1/delete/ads", json={"adIds": ad_ids})
        return self._response(SPAdMultiStatusResponse, resp)  # type: ignore[return-value]
