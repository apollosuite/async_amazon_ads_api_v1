"""SupplierProposedDeals resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDeals).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deals.general import (
    CreateSupplierProposedDealRequest,
    QuerySupplierProposedDealRequest,
    SupplierProposedDealMultiStatusResponse,
    SupplierProposedDealSuccessResponse,
    UpdateSupplierProposedDealRequest,
)


class SupplierProposedDeals(BaseResource):

    @overload
    async def create_supplier_proposed_deal(
        self, body: CreateSupplierProposedDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealMultiStatusResponse: ...
    @overload
    async def create_supplier_proposed_deal(
        self, body: CreateSupplierProposedDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_supplier_proposed_deal(
        self, body: CreateSupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_supplier_proposed_deal(
        self, body: CreateSupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposedDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Create supplier proposed deal"""

        resp = await self._request("POST", "/adsApi/v1/create/supplierProposedDeals", json=self.dump_json(body))
        return self._response(SupplierProposedDealMultiStatusResponse, resp, mode=mode)

    @overload
    async def query_supplier_proposed_deal(
        self, body: QuerySupplierProposedDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealSuccessResponse: ...
    @overload
    async def query_supplier_proposed_deal(
        self, body: QuerySupplierProposedDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposed_deal(
        self, body: QuerySupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposed_deal(
        self, body: QuerySupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposedDealSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposed deals"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierProposedDeals", json=self.dump_json(body))
        return self._response(SupplierProposedDealSuccessResponse, resp, mode=mode)

    @overload
    async def update_supplier_proposed_deal(
        self, body: UpdateSupplierProposedDealRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealMultiStatusResponse: ...
    @overload
    async def update_supplier_proposed_deal(
        self, body: UpdateSupplierProposedDealRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_supplier_proposed_deal(
        self, body: UpdateSupplierProposedDealRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_supplier_proposed_deal(
        self, body: UpdateSupplierProposedDealRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierProposedDealMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update supplier proposed deal"""

        resp = await self._request("POST", "/adsApi/v1/update/supplierProposedDeals", json=self.dump_json(body))
        return self._response(SupplierProposedDealMultiStatusResponse, resp, mode=mode)
