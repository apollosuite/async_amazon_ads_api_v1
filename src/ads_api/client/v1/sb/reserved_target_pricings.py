"""SBReservedTargetPricings resource operations.

Generated from OpenAPI spec (tag: ReservedTargetPricings).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.reserved_target_pricings.sb import (
    SBCreateReservedTargetPricingRequest,
    SBReservedTargetPricingMultiStatusResponse,
)


class SBReservedTargetPricings(BaseResource):

    @overload
    async def ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["pydantic"]
    ) -> SBReservedTargetPricingMultiStatusResponse: ...
    @overload
    async def ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def ads_apiv1create_reserved_target_pricing(
        self, body: SBCreateReservedTargetPricingRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SBReservedTargetPricingMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create reservedTarget pricing"""

        resp = await self._request("POST", "/adsApi/v1/create/reservedTargetPricings/sb", json=self.dump_json(body))
        return self._response(SBReservedTargetPricingMultiStatusResponse, resp, mode=mode)
