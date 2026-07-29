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
        return await self._create(
            "/adsApi/v1/create/adGroups",
            SBAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def query(self, body: SBQueryAdGroupRequest) -> SBAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SBAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SBAdGroupUpdate]) -> SBAdGroupMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/adGroups",
            SBAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def delete(self, ad_group_ids: list[str]) -> SBAdGroupMultiStatusResponse:
        return await self._delete(
            "/adsApi/v1/delete/adGroups",
            SBAdGroupMultiStatusResponse,
            json={"adGroupIds": ad_group_ids},
        )
