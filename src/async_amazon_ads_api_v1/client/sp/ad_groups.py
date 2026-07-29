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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/adGroups",
            json={"adGroups": self._validate(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)

    async def query(self, body: SPQueryAdGroupRequest) -> SPAdGroupSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/adGroups",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SPAdGroupSuccessResponse, resp)

    async def update(self, ad_groups: list[SPAdGroupUpdate]) -> SPAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/adGroups",
            json={"adGroups": self._validate(ad_groups)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)

    async def delete(self, ad_group_ids: list[str]) -> SPAdGroupMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/adGroups",
            json={"adGroupIds": ad_group_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SPAdGroupMultiStatusResponse, resp)
