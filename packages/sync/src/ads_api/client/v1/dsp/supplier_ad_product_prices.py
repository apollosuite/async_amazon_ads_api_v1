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
    def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierAdProductPriceMultiStatusResponse: ...
    @overload
    def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_supplier_ad_product_price(
        self, body: DSPCreateSupplierAdProductPriceRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierAdProductPriceMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier ad product price"""

        resp = self._request("POST", "/adsApi/v1/create/supplierAdProductPrices", json=self.dump_json(body))
        return self._response(DSPSupplierAdProductPriceMultiStatusResponse, resp, mode=mode)
