"""BrandStores resource operations.

Generated from OpenAPI spec (tag: BrandStores).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.brand_stores.general import (
    BrandStoreSuccessResponse,
    QueryBrandStoreRequest,
)


class BrandStores(BaseResource):

    @overload
    async def query_brand_store(
        self, body: QueryBrandStoreRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def query_brand_store(
        self, body: QueryBrandStoreRequest, *, mode: Literal["pydantic"]
    ) -> BrandStoreSuccessResponse: ...
    @overload
    async def query_brand_store(self, body: QueryBrandStoreRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_brand_store(
        self, body: QueryBrandStoreRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BrandStoreSuccessResponse | dict[str, Any] | httpx.Response:
        """Query brand store content"""

        resp = await self._request("POST", "/adsApi/v1/query/brandStores", json=self.dump_json(body))
        return self._response(BrandStoreSuccessResponse, resp, mode=mode)
