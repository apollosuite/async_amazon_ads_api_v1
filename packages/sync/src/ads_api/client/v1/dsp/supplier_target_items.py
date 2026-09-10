"""DSPSupplierTargetItems resource operations.

Generated from OpenAPI spec (tag: SupplierTargetItems).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_target_items.dsp import (
    DSPQuerySupplierTargetItemRequest,
    DSPSupplierTargetItemSuccessResponse,
)


class DSPSupplierTargetItems(BaseResource):

    @overload
    def query_supplier_target_item(
        self, body: DSPQuerySupplierTargetItemRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def query_supplier_target_item(
        self, body: DSPQuerySupplierTargetItemRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierTargetItemSuccessResponse: ...
    @overload
    def query_supplier_target_item(
        self, body: DSPQuerySupplierTargetItemRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def query_supplier_target_item(
        self, body: DSPQuerySupplierTargetItemRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierTargetItemSuccessResponse | dict[str, Any] | httpx.Response:
        """Fetch supplier target items"""

        resp = self._request("POST", "/adsApi/v1/query/supplierTargetItems", json=self.dump_json(body))
        return self._response(DSPSupplierTargetItemSuccessResponse, resp, mode=mode)
