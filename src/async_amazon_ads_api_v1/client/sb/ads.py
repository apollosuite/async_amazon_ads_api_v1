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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json={"ads": self._dump(ads)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdMultiStatusResponse, resp)

    async def query(self, body: SBQueryAdRequest) -> SBAdSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBAdSuccessResponse, resp)

    async def update(self, ads: list[SBAdUpdate]) -> SBAdMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json={"ads": self._dump(ads)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdMultiStatusResponse, resp)

    async def delete(self, ad_ids: list[str]) -> SBAdMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json={"adIds": ad_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdMultiStatusResponse, resp)
