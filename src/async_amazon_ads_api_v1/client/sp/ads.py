"""Ad resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sp.ads import (
    SPAdCreate,
    SPAdMultiStatusResponse,
    SPAdSuccessResponse,
    SPAdUpdate,
    SPQueryAdRequest,
)


class Ads(_ResourceBase):
    """Ad 广告资源操作。"""

    async def create(self, ads: list[SPAdCreate]) -> SPAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/create/ads",
            SPAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def query(self, body: SPQueryAdRequest) -> SPAdSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/ads", SPAdSuccessResponse)

    async def update(self, ads: list[SPAdUpdate]) -> SPAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/ads",
            SPAdMultiStatusResponse,
            json={"ads": self._validate(ads)},
        )

    async def delete(self, ad_ids: list[str]) -> SPAdMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/ads",
            SPAdMultiStatusResponse,
            json={"adIds": ad_ids},
        )
