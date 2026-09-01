"""DSPSupplierProposedDealForecasts resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDealForecasts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deal_forecasts.dsp import (
    DSPCreateSupplierProposedDealForecastRequest,
    DSPSupplierProposedDealForecastMultiStatusResponse,
)


class DSPSupplierProposedDealForecasts(BaseResource):

    @overload
    async def create_supplier_proposed_deal_forecast(
        self, body: DSPCreateSupplierProposedDealForecastRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposed_deal_forecast(
        self, body: DSPCreateSupplierProposedDealForecastRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealForecastMultiStatusResponse: ...
    @overload
    async def create_supplier_proposed_deal_forecast(
        self, body: DSPCreateSupplierProposedDealForecastRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposed_deal_forecast(
        self, body: DSPCreateSupplierProposedDealForecastRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealForecastMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposed deal forecast"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposedDealForecasts", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealForecastMultiStatusResponse, resp, mode=mode)
