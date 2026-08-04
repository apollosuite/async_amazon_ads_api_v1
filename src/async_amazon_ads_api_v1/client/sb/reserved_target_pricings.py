"""ReservedTargetPricings resource operations.

Generated from OpenAPI spec (tag: ReservedTargetPricings).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.reserved_target_pricings import (
    SBCreateReservedTargetPricingRequest,
    SBReservedTargetPricingMultiStatusResponse,
)


class ReservedTargetPricings(BaseResource):

    async def sb_ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest
    ) -> SBReservedTargetPricingMultiStatusResponse:
        """Create reservedTarget pricing"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/reservedTargetPricings/sb",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBReservedTargetPricingMultiStatusResponse, resp)
