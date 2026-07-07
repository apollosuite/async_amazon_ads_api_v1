"""SD Ad resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sd.ads import (
    SDAdCreate,
    SDAdMultiStatusResponse,
    SDAdSuccessResponse,
    SDAdUpdate,
    SDQueryAdRequest,
)


class Ads(_ResourceBase):
    _spec = _ResourceSpec(
        name="ads",
        create_model=SDAdCreate,
        update_model=SDAdUpdate,
        delete_key="adIds",
    )

    async def create(self, ads: list[SDAdCreate]) -> SDAdMultiStatusResponse:
        return await self._create(ads, self._spec, SDAdMultiStatusResponse)

    async def query(self, body: SDQueryAdRequest) -> SDAdSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/ads", SDAdSuccessResponse)

    async def update(self, ads: list[SDAdUpdate]) -> SDAdMultiStatusResponse:
        return await self._update(ads, self._spec, SDAdMultiStatusResponse)

    async def delete(self, ad_ids: list[str]) -> SDAdMultiStatusResponse:
        return await self._delete(ad_ids, self._spec, SDAdMultiStatusResponse)
