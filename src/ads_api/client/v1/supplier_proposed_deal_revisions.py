"""SupplierProposedDealRevisions resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDealRevisions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deal_revisions.general import (
    CreateSupplierProposedDealRevisionRequest,
    SupplierProposedDealRevisionMultiStatusResponse,
    UpdateSupplierProposedDealRevisionRequest,
)


class SupplierProposedDealRevisions(BaseResource):

    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: CreateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealRevisionMultiStatusResponse: ...
    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: CreateSupplierProposedDealRevisionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: CreateSupplierProposedDealRevisionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposed_deal_revision(
        self, body: CreateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposedDealRevisionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposed deal revision"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposedDealRevisions", json=self.dump_json(body))
        return self._response(SupplierProposedDealRevisionMultiStatusResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: UpdateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealRevisionMultiStatusResponse: ...
    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: UpdateSupplierProposedDealRevisionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: UpdateSupplierProposedDealRevisionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposed_deal_revision(
        self, body: UpdateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposedDealRevisionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposed deal revision"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposedDealRevisions", json=self.dump_json(body))
        return self._response(SupplierProposedDealRevisionMultiStatusResponse, resp, mode=mode)
