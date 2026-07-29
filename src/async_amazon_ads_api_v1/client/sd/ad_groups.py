"""SD AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sd.ad_groups import (
    SDAdGroupCreate,
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDAdGroupUpdate,
    SDQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):

    async def create(self, ad_groups: list[SDAdGroupCreate]) -> SDAdGroupMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/adGroups",
            SDAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def query(self, body: SDQueryAdGroupRequest) -> SDAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SDAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SDAdGroupUpdate]) -> SDAdGroupMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/adGroups",
            SDAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def delete(self, ad_group_ids: list[str]) -> SDAdGroupMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/adGroups",
            SDAdGroupMultiStatusResponse,
            json={"adGroupIds": ad_group_ids},
        )
