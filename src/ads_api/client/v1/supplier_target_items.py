"""SupplierTargetItems resource operations.

Generated from OpenAPI spec (tag: SupplierTargetItems).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_target_items.general import (
    QuerySupplierTargetItemRequest,
    SupplierTargetItemSuccessResponse,
)


class SupplierTargetItems(BaseResource):

    @overload
    async def query_supplier_target_item(
        self, body: QuerySupplierTargetItemRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierTargetItemSuccessResponse: ...
    @overload
    async def query_supplier_target_item(
        self, body: QuerySupplierTargetItemRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_target_item(
        self, body: QuerySupplierTargetItemRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_target_item(
        self, body: QuerySupplierTargetItemRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierTargetItemSuccessResponse | dict[str, Any] | httpx.Response:
        """Fetch supplier target items"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierTargetItems", json=self.dump_json(body))
        return self._response(SupplierTargetItemSuccessResponse, resp, mode=mode)
