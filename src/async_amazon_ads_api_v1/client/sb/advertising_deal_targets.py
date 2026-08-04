"""AdvertisingDealTargets resource operations.

Generated from OpenAPI spec (tag: AdvertisingDealTargets).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.advertising_deal_targets import (
    SBAdvertisingDealTargetMultiStatusResponse,
    SBAdvertisingDealTargetSuccessResponse,
    SBCreateAdvertisingDealTargetRequest,
    SBDeleteAdvertisingDealTargetRequest,
    SBQueryAdvertisingDealTargetRequest,
)


class AdvertisingDealTargets(BaseResource):

    async def sb_create_advertising_deal_target(
        self, body: SBCreateAdvertisingDealTargetRequest
    ) -> SBAdvertisingDealTargetMultiStatusResponse:
        """Create advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp)

    async def sb_delete_advertising_deal_target(
        self, body: SBDeleteAdvertisingDealTargetRequest
    ) -> SBAdvertisingDealTargetMultiStatusResponse:
        """Delete advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/delete/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetMultiStatusResponse, resp)

    async def sb_query_advertising_deal_target(
        self, body: SBQueryAdvertisingDealTargetRequest
    ) -> SBAdvertisingDealTargetSuccessResponse:
        """Query advertisingDealTarget"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/advertisingDealTargets/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBAdvertisingDealTargetSuccessResponse, resp)
