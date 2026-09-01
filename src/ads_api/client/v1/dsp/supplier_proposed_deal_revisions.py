"""DSPSupplierProposedDealRevisions resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDealRevisions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deal_revisions.dsp import (
    DSPCreateSupplierProposedDealRevisionRequest,
    DSPSupplierProposedDealRevisionMultiStatusResponse,
    DSPUpdateSupplierProposedDealRevisionRequest,
)


class DSPSupplierProposedDealRevisions(BaseResource):

    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: DSPCreateSupplierProposedDealRevisionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: DSPCreateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealRevisionMultiStatusResponse: ...
    @overload
    async def create_supplier_proposed_deal_revision(
        self, body: DSPCreateSupplierProposedDealRevisionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposed_deal_revision(
        self, body: DSPCreateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealRevisionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposed deal revision"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposedDealRevisions", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealRevisionMultiStatusResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: DSPUpdateSupplierProposedDealRevisionRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: DSPUpdateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic"]
    ) -> DSPSupplierProposedDealRevisionMultiStatusResponse: ...
    @overload
    async def update_supplier_proposed_deal_revision(
        self, body: DSPUpdateSupplierProposedDealRevisionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposed_deal_revision(
        self, body: DSPUpdateSupplierProposedDealRevisionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DSPSupplierProposedDealRevisionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposed deal revision"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposedDealRevisions", json=self.dump_json(body))
        return self._response(DSPSupplierProposedDealRevisionMultiStatusResponse, resp, mode=mode)
