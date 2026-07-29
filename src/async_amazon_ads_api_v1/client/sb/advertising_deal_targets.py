"""SB AdvertisingDealTarget resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.sb.advertising_deal_targets import (
    SBAdvertisingDealTargetCreate,
    SBAdvertisingDealTargetMultiStatusResponse,
    SBAdvertisingDealTargetSuccessResponse,
    SBQueryAdvertisingDealTargetRequest,
)


class AdvertisingDealTargets(_ResourceBase):

    async def create(self, items: list[SBAdvertisingDealTargetCreate]) -> SBAdvertisingDealTargetSuccessResponse:
        return await self._post(
            "/adsApi/v1/create/advertisingDealTargets/sb",
            SBAdvertisingDealTargetSuccessResponse,
            json={"advertisingDealTargets": self._validate(items)},
        )

    async def query(self, body: SBQueryAdvertisingDealTargetRequest) -> SBAdvertisingDealTargetSuccessResponse:
        return await self._query(
            body,
            "/adsApi/v1/query/advertisingDealTargets/sb",
            SBAdvertisingDealTargetSuccessResponse,
        )

    async def delete(self, ids: list[str]) -> SBAdvertisingDealTargetMultiStatusResponse:
        return await self._post(
            "/adsApi/v1/delete/advertisingDealTargets/sb",
            SBAdvertisingDealTargetMultiStatusResponse,
            json={"advertisingDealTargetIds": ids},
        )
