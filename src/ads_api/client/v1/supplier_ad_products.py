"""SupplierAdProducts resource operations.

Generated from OpenAPI spec (tag: SupplierAdProducts).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_ad_products.general import (
    QuerySupplierAdProductRequest,
    SupplierAdProductSuccessResponse,
)


class SupplierAdProducts(BaseResource):

    @overload
    async def query_supplier_ad_product(
        self, body: QuerySupplierAdProductRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierAdProductSuccessResponse: ...
    @overload
    async def query_supplier_ad_product(
        self, body: QuerySupplierAdProductRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_ad_product(
        self, body: QuerySupplierAdProductRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_ad_product(
        self, body: QuerySupplierAdProductRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierAdProductSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier ad products"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierAdProducts", json=self.dump_json(body))
        return self._response(SupplierAdProductSuccessResponse, resp, mode=mode)
