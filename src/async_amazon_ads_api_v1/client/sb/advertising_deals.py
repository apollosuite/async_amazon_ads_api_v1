"""SB AdvertisingDeal resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb.advertising_deals import (
    SBAdvertisingDealCreate,
    SBAdvertisingDealMultiStatusResponse,
    SBAdvertisingDealSuccessResponse,
    SBAdvertisingDealUpdate,
    SBQueryAdvertisingDealRequest,
)


class AdvertisingDeals(_ResourceBase):
    _spec = _ResourceSpec(
        name="advertisingDeals",
        create_model=SBAdvertisingDealCreate,
        update_model=SBAdvertisingDealUpdate,
        delete_key="advertisingDealIds",
        path_suffix="/sb",
    )

    async def create(self, items: list[SBAdvertisingDealCreate]) -> SBAdvertisingDealSuccessResponse:
        return await self._create(items, self._spec, SBAdvertisingDealSuccessResponse)

    async def query(self, body: SBQueryAdvertisingDealRequest) -> SBAdvertisingDealSuccessResponse:
        return await self._query(body, "/adsApi/v1/query/advertisingDeals/sb", SBAdvertisingDealSuccessResponse)

    async def update(self, items: list[SBAdvertisingDealUpdate]) -> SBAdvertisingDealMultiStatusResponse:
        return await self._update(items, self._spec, SBAdvertisingDealMultiStatusResponse)

    async def delete(self, ids: list[str]) -> SBAdvertisingDealMultiStatusResponse:
        return await self._delete(ids, self._spec, SBAdvertisingDealMultiStatusResponse)
