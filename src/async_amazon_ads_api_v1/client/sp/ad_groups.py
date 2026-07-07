"""AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp.ad_groups import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
    SPQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    """AdGroup 广告组资源操作。"""

    _spec = _ResourceSpec(
        name="adGroups",
        create_model=SPAdGroupCreate,
        update_model=SPAdGroupUpdate,
        delete_key="adGroupIds",
    )

    async def create(self, ad_groups: list[SPAdGroupCreate]) -> SPAdGroupMultiStatusResponse:
        return await self._create(ad_groups, self._spec, SPAdGroupMultiStatusResponse)

    async def query(self, body: SPQueryAdGroupRequest) -> SPAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SPAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SPAdGroupUpdate]) -> SPAdGroupMultiStatusResponse:
        return await self._update(ad_groups, self._spec, SPAdGroupMultiStatusResponse)

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        return await self._delete(ad_group_ids, self._spec, SPAdGroupMultiStatusResponse)
