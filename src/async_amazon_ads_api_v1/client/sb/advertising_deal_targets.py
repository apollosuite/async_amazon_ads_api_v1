"""SB AdvertisingDealTarget resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.advertising_deal_targets import (
    SBAdvertisingDealTargetCreate,
    SBAdvertisingDealTargetMultiStatusResponse,
    SBAdvertisingDealTargetSuccessResponse,
    SBQueryAdvertisingDealTargetRequest,
)


class AdvertisingDealTargets(_ResourceBase):
    _spec = _ResourceSpec(
        name="advertisingDealTargets",
        create_model=SBAdvertisingDealTargetCreate,
        delete_key="advertisingDealTargetIds",
        path_suffix="/sb",
    )

    async def create(self, items: list[SBAdvertisingDealTargetCreate]) -> SBAdvertisingDealTargetSuccessResponse:
        return await self._create(items, self._spec, SBAdvertisingDealTargetSuccessResponse)

    async def query(self, body: SBQueryAdvertisingDealTargetRequest) -> SBAdvertisingDealTargetSuccessResponse:
        return await self._query(
            body,
            "/adsApi/v1/query/advertisingDealTargets/sb",
            SBAdvertisingDealTargetSuccessResponse,
        )

    async def delete(self, ids: list[str]) -> SBAdvertisingDealTargetMultiStatusResponse:
        return await self._delete(ids, self._spec, SBAdvertisingDealTargetMultiStatusResponse)
