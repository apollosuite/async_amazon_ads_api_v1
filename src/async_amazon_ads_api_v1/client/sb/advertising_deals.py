"""SB AdvertisingDeal resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.models.sb import (
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

    async def create(
        self, items: list[dict[str, Any] | SBAdvertisingDealCreate]
    ) -> SBAdvertisingDealSuccessResponse | dict[str, Any]:
        return await self._create(items, self._spec, SBAdvertisingDealSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SBQueryAdvertisingDealRequest
    ) -> SBAdvertisingDealSuccessResponse | dict[str, Any]:
        if isinstance(body, dict):
            body = SBQueryAdvertisingDealRequest(**body)
        return await self._query(body, "/adsApi/v1/query/advertisingDeals/sb", SBAdvertisingDealSuccessResponse)

    async def update(
        self, items: list[dict[str, Any] | SBAdvertisingDealUpdate]
    ) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any]:
        return await self._update(items, self._spec, SBAdvertisingDealMultiStatusResponse)

    async def delete(self, ids: list[str]) -> SBAdvertisingDealMultiStatusResponse | dict[str, Any]:
        return await self._delete(ids, self._spec, SBAdvertisingDealMultiStatusResponse)
