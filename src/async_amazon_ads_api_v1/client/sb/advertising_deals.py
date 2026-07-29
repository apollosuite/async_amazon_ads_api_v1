"""SB AdvertisingDeal resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.advertising_deals import (
    SBAdvertisingDealCreate,
    SBAdvertisingDealMultiStatusResponse,
    SBAdvertisingDealSuccessResponse,
    SBAdvertisingDealUpdate,
    SBQueryAdvertisingDealRequest,
)


class AdvertisingDeals(_ResourceBase):

    async def create(self, items: list[SBAdvertisingDealCreate]) -> SBAdvertisingDealSuccessResponse:
        return await self._post(
            "/adsApi/v1/create/advertisingDeals/sb",
            SBAdvertisingDealSuccessResponse,
            json={"advertisingDeals": self._validate(items)},
        )

    async def query(self, body: SBQueryAdvertisingDealRequest) -> SBAdvertisingDealSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/advertisingDeals/sb", SBAdvertisingDealSuccessResponse)

    async def update(self, items: list[SBAdvertisingDealUpdate]) -> SBAdvertisingDealMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/update/advertisingDeals/sb",
            SBAdvertisingDealMultiStatusResponse,
            json={"advertisingDeals": self._validate(items)},
        )

    async def delete(self, ids: list[str]) -> SBAdvertisingDealMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/advertisingDeals/sb",
            SBAdvertisingDealMultiStatusResponse,
            json={"advertisingDealIds": ids},
        )
