"""SD AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sd.ad_groups import (
    SDAdGroupCreate,
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDAdGroupUpdate,
    SDQueryAdGroupRequest,
)


class AdGroups(BaseResource):

    async def create(self, ad_groups: list[SDAdGroupCreate]) -> SDAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json={"adGroups": self._dump(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)

    async def query(self, body: SDQueryAdGroupRequest) -> SDAdGroupSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDAdGroupSuccessResponse, resp)

    async def update(self, ad_groups: list[SDAdGroupUpdate]) -> SDAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json={"adGroups": self._dump(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)

    async def delete(self, ad_group_ids: list[str]) -> SDAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json={"adGroupIds": ad_group_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdGroupMultiStatusResponse, resp)
