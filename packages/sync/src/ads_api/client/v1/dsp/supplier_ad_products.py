"""DSPSupplierAdProducts resource operations.

Generated from OpenAPI spec (tag: SupplierAdProducts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_ad_products.dsp import (
    DSPQuerySupplierAdProductRequest,
    DSPSupplierAdProductSuccessResponse,
)


class DSPSupplierAdProducts(BaseResource):

    @overload
    def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierAdProductSuccessResponse: ...
    @overload
    def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierAdProductSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier ad products"""

        resp = self._request("POST", "/adsApi/v1/query/supplierAdProducts", json=self.dump_json(body))
        return self._response(DSPSupplierAdProductSuccessResponse, resp, mode=mode)
