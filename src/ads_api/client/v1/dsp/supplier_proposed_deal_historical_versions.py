"""DSPSupplierProposedDealHistoricalVersions resource operations.

Generated from OpenAPI spec (tag: SupplierProposedDealHistoricalVersions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_proposed_deal_historical_versions.dsp import (
    DSPQuerySupplierProposedDealHistoricalVersionRequest,
    DSPSupplierProposedDealHistoricalVersionSuccessResponse,
)


class DSPSupplierProposedDealHistoricalVersions(BaseResource):

    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: DSPQuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPSupplierProposedDealHistoricalVersionSuccessResponse: ...
    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: DSPQuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_proposed_deal_historical_version(
        self, body: DSPQuerySupplierProposedDealHistoricalVersionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_proposed_deal_historical_version(
        self,
        body: DSPQuerySupplierProposedDealHistoricalVersionRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> DSPSupplierProposedDealHistoricalVersionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier proposed deal historical versions"""

        resp = await self._request(
            "POST", "/adsApi/v1/query/supplierProposedDealHistoricalVersions", json=self.dump_json(body)
        )
        return self._response(DSPSupplierProposedDealHistoricalVersionSuccessResponse, resp, mode=mode)
