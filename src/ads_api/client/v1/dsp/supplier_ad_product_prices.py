"""DSPSupplierAdProductPrices resource operations.

Generated from OpenAPI spec (tag: SupplierAdProductPrices).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_ad_product_prices.dsp import (
    DSPCreateSupplierAdProductPriceRequest,
    DSPSupplierAdProductPriceMultiStatusResponse,
)


class DSPSupplierAdProductPrices(BaseResource):

    @overload
    async def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPSupplierAdProductPriceMultiStatusResponse: ...
    @overload
    async def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPSupplierAdProductPriceMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier ad product price"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierAdProductPrices", json=self.dump_json(body))
        return self._response(DSPSupplierAdProductPriceMultiStatusResponse, resp, mode=mode)
