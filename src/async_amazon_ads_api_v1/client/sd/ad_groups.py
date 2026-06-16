"""SD AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sd import (
    SDAdGroupCreate,
    SDAdGroupMultiStatusResponse,
    SDAdGroupSuccessResponse,
    SDAdGroupUpdate,
    SDQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SDAdGroupCreate,
        update_model=SDAdGroupUpdate,
        delete_key="adGroupIds",
    )

    async def create(self, ad_groups: list[SDAdGroupCreate]) -> SDAdGroupMultiStatusResponse:
        return await self._create(ad_groups, self._spec, SDAdGroupMultiStatusResponse)

    async def query(self, body: SDQueryAdGroupRequest) -> SDAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SDAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SDAdGroupUpdate]) -> SDAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SDAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SDAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SDAdGroupMultiStatusResponse)
