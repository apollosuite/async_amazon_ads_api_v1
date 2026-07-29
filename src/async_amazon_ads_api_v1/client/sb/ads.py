"""SB Ad resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.ads import (
    SBAdCreate,
    SBAdMultiStatusResponse,
    SBAdSuccessResponse,
    SBAdUpdate,
    SBQueryAdRequest,
)


class Ads(_ResourceBase):

    async def create(self, ads: list[SBAdCreate]) -> SBAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/ads",
            SBAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def query(self, body: SBQueryAdRequest) -> SBAdSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/ads", SBAdSuccessResponse)

    async def update(self, ads: list[SBAdUpdate]) -> SBAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/ads",
            SBAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def delete(self, ad_ids: list[str]) -> SBAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/ads",
            SBAdMultiStatusResponse,
            json={"adIds": ad_ids},
        )
