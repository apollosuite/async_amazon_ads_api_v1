"""DSPSupplierProposedDeals resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDeals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deals.dsp import (
    DSPCreateSupplierProposedDealRequest,
    DSPQuerySupplierProposedDealRequest,
    DSPSupplierProposedDealMultiStatusResponse,
    DSPSupplierProposedDealSuccessResponse,
    DSPUpdateSupplierProposedDealRequest,
)


class DSPSupplierProposedDeals(BaseResource):

    @overload
    async def create_supplier_proposed_deal(
        self, body: DSPCreateSupplierProposedDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposed_deal(
        self, body: DSPCreateSupplierProposedDealRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealMultiStatusResponse: ...
    @overload
    async def create_supplier_proposed_deal(
        self, body: DSPCreateSupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposed_deal(
        self, body: DSPCreateSupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposed deal"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposedDeals", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_supplier_proposed_deal(
        self, body: DSPQuerySupplierProposedDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposed_deal(
        self, body: DSPQuerySupplierProposedDealRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealSuccessResponse: ...
    @overload
    async def query_supplier_proposed_deal(
        self, body: DSPQuerySupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposed_deal(
        self, body: DSPQuerySupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposed deals"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposedDeals", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealSuccessResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposed_deal(
        self, body: DSPUpdateSupplierProposedDealRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposed_deal(
        self, body: DSPUpdateSupplierProposedDealRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealMultiStatusResponse: ...
    @overload
    async def update_supplier_proposed_deal(
        self, body: DSPUpdateSupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposed_deal(
        self, body: DSPUpdateSupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposed deal"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposedDeals", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealMultiStatusResponse, resp, mode=mode)
