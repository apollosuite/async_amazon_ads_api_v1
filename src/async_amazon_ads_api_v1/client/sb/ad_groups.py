"""SB AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.ad_groups import (
    SBAdGroupCreate,
    SBAdGroupMultiStatusResponse,
    SBAdGroupSuccessResponse,
    SBAdGroupUpdate,
    SBQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SBAdGroupCreate,
        update_model=SBAdGroupUpdate,
        delete_key="adGroupIds",
    )

    async def create(self, ad_groups: list[SBAdGroupCreate]) -> SBAdGroupMultiStatusResponse:
        return await self._create(ad_groups, self._spec, SBAdGroupMultiStatusResponse)

    async def query(self, body: SBQueryAdGroupRequest) -> SBAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SBAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SBAdGroupUpdate]) -> SBAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SBAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SBAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SBAdGroupMultiStatusResponse)
