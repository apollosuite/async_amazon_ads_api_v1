"""DSPSupplierProposals resource operations.

Generated from OpenAPI spec (tag: SupplierProposals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposals.dsp import (
    DSPCreateSupplierProposalRequest,
    DSPQuerySupplierProposalRequest,
    DSPSupplierProposalMultiStatusResponse,
    DSPSupplierProposalSuccessResponse,
    DSPUpdateSupplierProposalRequest,
)


class DSPSupplierProposals(BaseResource):

    @overload
    async def create_supplier_proposal(
        self, body: DSPCreateSupplierProposalRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposal(
        self, body: DSPCreateSupplierProposalRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposalMultiStatusResponse: ...
    @overload
    async def create_supplier_proposal(
        self, body: DSPCreateSupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposal(
        self, body: DSPCreateSupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposalMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposals", json=self.dump_json(body))
        return self._response(DSPSupplierProposalMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_supplier_proposal(
        self, body: DSPQuerySupplierProposalRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposal(
        self, body: DSPQuerySupplierProposalRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposalSuccessResponse: ...
    @overload
    async def query_supplier_proposal(
        self, body: DSPQuerySupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposal(
        self, body: DSPQuerySupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposalSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposals", json=self.dump_json(body))
        return self._response(DSPSupplierProposalSuccessResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposal(
        self, body: DSPUpdateSupplierProposalRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposal(
        self, body: DSPUpdateSupplierProposalRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposalMultiStatusResponse: ...
    @overload
    async def update_supplier_proposal(
        self, body: DSPUpdateSupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposal(
        self, body: DSPUpdateSupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposalMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposals", json=self.dump_json(body))
        return self._response(DSPSupplierProposalMultiStatusResponse, resp, mode=mode)
