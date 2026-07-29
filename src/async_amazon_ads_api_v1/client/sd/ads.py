"""SD Ad resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sd.ads import (
    SDAdCreate,
    SDAdMultiStatusResponse,
    SDAdSuccessResponse,
    SDAdUpdate,
    SDQueryAdRequest,
)


class Ads(_ResourceBase):

    async def create(self, ads: list[SDAdCreate]) -> SDAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/ads",
            SDAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def query(self, body: SDQueryAdRequest) -> SDAdSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/ads", SDAdSuccessResponse)

    async def update(self, ads: list[SDAdUpdate]) -> SDAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/ads",
            SDAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def delete(self, ad_ids: list[str]) -> SDAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/ads",
            SDAdMultiStatusResponse,
            json={"adIds": ad_ids},
        )
