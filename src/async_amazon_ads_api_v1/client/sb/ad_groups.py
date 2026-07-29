"""SB AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.ad_groups import (
    SBAdGroupCreate,
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBAdGroupUpdate,
    SBQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):

    async def create(self, ad_groups: list[SBAdGroupCreate]) -> SBAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json={"adGroups": self._dump(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)

    async def query(self, body: SBQueryAdGroupRequest) -> SBAdGroupSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBAdGroupSuccessResponse, resp)

    async def update(self, ad_groups: list[SBAdGroupUpdate]) -> SBAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json={"adGroups": self._dump(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)

    async def delete(self, ad_group_ids: list[str]) -> SBAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json={"adGroupIds": ad_group_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdGroupMultiStatusResponse, resp)
