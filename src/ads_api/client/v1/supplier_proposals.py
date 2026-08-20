"""SupplierProposals resource operations.

Generated from OpenAPI spec (tag: SupplierProposals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposals.general import (
    CreateSupplierProposalRequest,
    QuerySupplierProposalRequest,
    SupplierProposalMultiStatusResponse,
    SupplierProposalSuccessResponse,
    UpdateSupplierProposalRequest,
)


class SupplierProposals(BaseResource):

    @overload
    async def create_supplier_proposal(
        self, body: CreateSupplierProposalRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposalMultiStatusResponse: ...
    @overload
    async def create_supplier_proposal(
        self, body: CreateSupplierProposalRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposal(
        self, body: CreateSupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposal(
        self, body: CreateSupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposalMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposals", json=self.dump_json(body))
        return self._response(SupplierProposalMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_supplier_proposal(
        self, body: QuerySupplierProposalRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposalSuccessResponse: ...
    @overload
    async def query_supplier_proposal(
        self, body: QuerySupplierProposalRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposal(
        self, body: QuerySupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposal(
        self, body: QuerySupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposalSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposals", json=self.dump_json(body))
        return self._response(SupplierProposalSuccessResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposal(
        self, body: UpdateSupplierProposalRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposalMultiStatusResponse: ...
    @overload
    async def update_supplier_proposal(
        self, body: UpdateSupplierProposalRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposal(
        self, body: UpdateSupplierProposalRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposal(
        self, body: UpdateSupplierProposalRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposalMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposal"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposals", json=self.dump_json(body))
        return self._response(SupplierProposalMultiStatusResponse, resp, mode=mode)
