"""SupplierProposedDealHistoricalVersions resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDealHistoricalVersions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deal_historical_versions.general import (
    QuerySupplierProposedDealHistoricalVersionRequest,
    SupplierProposedDealHistoricalVersionSuccessResponse,
)


class SupplierProposedDealHistoricalVersions(BaseResource):

    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: QuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierProposedDealHistoricalVersionSuccessResponse: ...
    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: QuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: QuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposed_deal_historical_version(
        self,
        body: QuerySupplierProposedDealHistoricalVersionRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SupplierProposedDealHistoricalVersionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposed deal historical versions"""

        resp = await self._request(
            "POST", "/adsApi/v1/query/supplierProposedDealHistoricalVersions", json=self.dump_json(body)
        )
        return self._response(SupplierProposedDealHistoricalVersionSuccessResponse, resp, mode=mode)
