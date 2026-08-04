"""AdvertisingDeals resource operations.

Generated from OpenAPI spec (tag: AdvertisingDeals).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.advertising_deals import (
    SBAdvertisingDealMultiStatusResponse,
    SBAdvertisingDealSuccessResponse,
    SBCreateAdvertisingDealRequest,
    SBDeleteAdvertisingDealRequest,
    SBQueryAdvertisingDealRequest,
    SBUpdateAdvertisingDealRequest,
)


class AdvertisingDeals(BaseResource):

    async def sb_create_advertising_deal(
        self, body: SBCreateAdvertisingDealRequest
    ) -> SBAdvertisingDealMultiStatusResponse:
        """Create advertisingDeal"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertisingDeals/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealMultiStatusResponse, resp)

    async def sb_delete_advertising_deal(
        self, body: SBDeleteAdvertisingDealRequest
    ) -> SBAdvertisingDealMultiStatusResponse:
        """Delete advertisingDeal"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/advertisingDeals/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealMultiStatusResponse, resp)

    async def sb_query_advertising_deal(self, body: SBQueryAdvertisingDealRequest) -> SBAdvertisingDealSuccessResponse:
        """Query advertisingDeal"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertisingDeals/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealSuccessResponse, resp)

    async def sb_update_advertising_deal(
        self, body: SBUpdateAdvertisingDealRequest
    ) -> SBAdvertisingDealMultiStatusResponse:
        """Update advertisingDeal"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/advertisingDeals/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealMultiStatusResponse, resp)
