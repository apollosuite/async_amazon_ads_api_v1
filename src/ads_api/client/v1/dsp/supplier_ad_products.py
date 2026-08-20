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
    async def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPSupplierAdProductSuccessResponse: ...
    @overload
    async def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_ad_product(
        self, body: DSPQuerySupplierAdProductRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPSupplierAdProductSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier ad products"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierAdProducts", json=self.dump_json(body))
        return self._response(DSPSupplierAdProductSuccessResponse, resp, mode=mode)
