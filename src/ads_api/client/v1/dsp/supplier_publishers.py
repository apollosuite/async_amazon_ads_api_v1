"""DSPSupplierPublishers resource operations.

Generated from OpenAPI spec (tag: SupplierPublishers).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_publishers.dsp import (
    DSPQuerySupplierPublisherRequest,
    DSPSupplierPublisherSuccessResponse,
)


class DSPSupplierPublishers(BaseResource):

    @overload
    async def query_supplier_publisher(
        self, body: DSPQuerySupplierPublisherRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DSPSupplierPublisherSuccessResponse: ...
    @overload
    async def query_supplier_publisher(
        self, body: DSPQuerySupplierPublisherRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_publisher(
        self, body: DSPQuerySupplierPublisherRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_publisher(
        self, body: DSPQuerySupplierPublisherRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DSPSupplierPublisherSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier publishers"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierPublishers", json=self.dump_json(body))
        return self._response(DSPSupplierPublisherSuccessResponse, resp, mode=mode)
