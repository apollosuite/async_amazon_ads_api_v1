"""ReservedTargetPricings resource operations.

Generated from OpenAPI spec (tag: ReservedTargetPricings).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sb.reserved_target_pricings import (
    SBCreateReservedTargetPricingRequest,
    SBReservedTargetPricingMultiStatusResponse,
)


class ReservedTargetPricings(BaseResource):

    @overload
    async def sb_ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBReservedTargetPricingMultiStatusResponse: ...
    @overload
    async def sb_ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def sb_ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def sb_ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBReservedTargetPricingMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create reservedTarget pricing"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/create/reservedTargetPricings/sb",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SBReservedTargetPricingMultiStatusResponse, resp, mode=mode)
