"""SupplierProposalDestinations resource operations.

Generated from OpenAPI spec (tag: SupplierProposalDestinations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposal_destinations.general import (
    QuerySupplierProposalDestinationRequest,
    SupplierProposalDestinationSuccessResponse,
)


class SupplierProposalDestinations(BaseResource):

    @overload
    async def query_supplier_proposal_destination(
        self, body: QuerySupplierProposalDestinationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposalDestinationSuccessResponse: ...
    @overload
    async def query_supplier_proposal_destination(
        self, body: QuerySupplierProposalDestinationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposal_destination(
        self, body: QuerySupplierProposalDestinationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposal_destination(
        self, body: QuerySupplierProposalDestinationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposalDestinationSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposal destinations"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposalDestinations", json=self.dump_json(body))
        return self._response(SupplierProposalDestinationSuccessResponse, resp, mode=mode)
