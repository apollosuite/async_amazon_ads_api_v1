"""SB AdvertisingDeal resource operations."""

from __future__ import annotations

from typing import Any

from amazon_ads_sdk._base import _ResourceBase, _ResourceSpec
from amazon_ads_sdk.models.sb import (
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
        query_model=SBQueryAdvertisingDealRequest,
        delete_key="advertisingDealIds",
        path_suffix="/sb",
    )

    async def create(
        self, items: list[dict[str, Any] | SBAdvertisingDealCreate]
    ) -> SBAdvertisingDealSuccessResponse:
        return await self._create(items, self._spec, SBAdvertisingDealSuccessResponse)

    async def query(
        self, body: dict[str, Any] | SBQueryAdvertisingDealRequest
    ) -> SBAdvertisingDealSuccessResponse:
        return await self._query(body, self._spec, SBAdvertisingDealSuccessResponse)

    async def update(
        self, items: list[dict[str, Any] | SBAdvertisingDealUpdate]
    ) -> SBAdvertisingDealMultiStatusResponse:
        return await self._update(items, self._spec, SBAdvertisingDealMultiStatusResponse)

    async def delete(self, ids: list[str]) -> SBAdvertisingDealMultiStatusResponse:
        return await self._delete(ids, self._spec, SBAdvertisingDealMultiStatusResponse)
