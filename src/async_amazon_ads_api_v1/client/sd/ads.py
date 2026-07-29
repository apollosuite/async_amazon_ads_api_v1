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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/ads",
            json={"ads": self._dump(ads)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdMultiStatusResponse, resp)

    async def query(self, body: SDQueryAdRequest) -> SDAdSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/ads",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDAdSuccessResponse, resp)

    async def update(self, ads: list[SDAdUpdate]) -> SDAdMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/update/ads",
            json={"ads": self._dump(ads)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdMultiStatusResponse, resp)

    async def delete(self, ad_ids: list[str]) -> SDAdMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/ads",
            json={"adIds": ad_ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SDAdMultiStatusResponse, resp)
