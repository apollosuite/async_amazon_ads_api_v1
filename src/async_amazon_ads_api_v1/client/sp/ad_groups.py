"""AdGroup resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sp.ad_groups import (
    SPAdGroupCreate,
    SPAdGroupMultiStatusResponse,
    SPAdGroupSuccessResponse,
    SPAdGroupUpdate,
    SPQueryAdGroupRequest,
)


class AdGroups(_ResourceBase):
    """AdGroup 广告组资源操作。"""

    async def create(self, ad_groups: list[SPAdGroupCreate]) -> SPAdGroupMultiStatusResponse:
        return await self._create(
            "/adsApi/v1/create/adGroups",
            SPAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def query(self, body: SPQueryAdGroupRequest) -> SPAdGroupSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/adGroups", SPAdGroupSuccessResponse)

    async def update(self, ad_groups: list[SPAdGroupUpdate]) -> SPAdGroupMultiStatusResponse:
        return await self._update(
            "/adsApi/v1/update/adGroups",
            SPAdGroupMultiStatusResponse,
            json={"adGroups": self._validate(ad_groups)},
        )

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        return await self._delete(
            "/adsApi/v1/delete/adGroups",
            SPAdGroupMultiStatusResponse,
            json={"adGroupIds": ad_group_ids},
        )
