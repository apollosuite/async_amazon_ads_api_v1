"""Ad resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sp import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
    SPQueryAdRequest,
)


class Ads(_ResourceBase):
    """Ad 广告资源操作。"""

    _spec = _ResourceSpec(
        name="ads",
        create_model=SPAdCreate,
        update_model=SPAdUpdate,
        delete_key="adIds",
    )

    async def create(self, ads: list[SPAdCreate]) -> SPAdMultiStatusResponse:
        return await self._create(ads, self._spec, SPAdMultiStatusResponse)

    async def query(self, body: SPQueryAdRequest) -> SPAdSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/ads", SPAdSuccessResponse)

    async def update(self, ads: list[SPAdUpdate]) -> SPAdMultiStatusResponse:
        return await self._update(ads, self._spec, SPAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        return await self._delete(ad_ids, self._spec, SPAdMultiStatusResponse)
