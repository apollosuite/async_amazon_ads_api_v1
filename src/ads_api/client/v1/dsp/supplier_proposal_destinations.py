"""DSPSupplierProposalDestinations resource operations.

Generated from OpenAPI spec (tag: SupplierProposalDestinations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposal_destinations.dsp import (
    DSPQuerySupplierProposalDestinationRequest,
    DSPSupplierProposalDestinationSuccessResponse,
)


class DSPSupplierProposalDestinations(BaseResource):

    @overload
    async def query_supplier_proposal_destination(
        self, body: DSPQuerySupplierProposalDestinationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPSupplierProposalDestinationSuccessResponse: ...
    @overload
    async def query_supplier_proposal_destination(
        self, body: DSPQuerySupplierProposalDestinationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposal_destination(
        self, body: DSPQuerySupplierProposalDestinationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposal_destination(
        self, body: DSPQuerySupplierProposalDestinationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPSupplierProposalDestinationSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposal destinations"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposalDestinations", json=self.dump_json(body))
        return self._response(DSPSupplierProposalDestinationSuccessResponse, resp, mode=mode)
