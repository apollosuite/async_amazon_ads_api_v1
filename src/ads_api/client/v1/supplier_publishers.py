"""SupplierPublishers resource operations.

Generated from OpenAPI spec (tag: SupplierPublishers).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.supplier_publishers.general import (
    QuerySupplierPublisherRequest,
    SupplierPublisherSuccessResponse,
)


class SupplierPublishers(BaseResource):

    @overload
    async def query_supplier_publisher(
        self, body: QuerySupplierPublisherRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SupplierPublisherSuccessResponse: ...
    @overload
    async def query_supplier_publisher(
        self, body: QuerySupplierPublisherRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_supplier_publisher(
        self, body: QuerySupplierPublisherRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_supplier_publisher(
        self, body: QuerySupplierPublisherRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SupplierPublisherSuccessResponse | dict[str, Any] | httpx.Response:
        """Query supplier publishers"""

        resp = await self._request("POST", "/adsApi/v1/query/supplierPublishers", json=self.dump_json(body))
        return self._response(SupplierPublisherSuccessResponse, resp, mode=mode)
