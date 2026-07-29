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
        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertisingDealTargets/sb",
            json={"advertisingDealTargets": self._dump(items)},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdvertisingDealTargetSuccessResponse, resp)

    async def query(self, body: SBQueryAdvertisingDealTargetRequest) -> SBAdvertisingDealTargetSuccessResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertisingDealTargets/sb",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetSuccessResponse, resp)

    async def delete(self, ids: list[str]) -> SBAdvertisingDealTargetMultiStatusResponse:
        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/advertisingDealTargets/sb",
            json={"advertisingDealTargetIds": ids},
            headers=self.ASYNC_ACCEPT,
        )
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp)
