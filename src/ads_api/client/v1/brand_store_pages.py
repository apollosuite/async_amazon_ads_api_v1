"""BrandStorePages resource operations.

Generated from OpenAPI spec (tag: BrandStorePages).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v1.brand_store_pages.general import (
    BrandStorePageSuccessResponse,
    QueryBrandStorePageRequest,
)


class BrandStorePages(BaseResource):

    @overload
    async def query_brand_store_page(
        self, body: QueryBrandStorePageRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BrandStorePageSuccessResponse: ...
    @overload
    async def query_brand_store_page(
        self, body: QueryBrandStorePageRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_brand_store_page(
        self, body: QueryBrandStorePageRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_brand_store_page(
        self, body: QueryBrandStorePageRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BrandStorePageSuccessResponse | dict[str, Any] | httpx.Response:
        """Retrieve brand store page content"""

        resp = await self._request("POST", "/adsApi/v1/query/brandStorePages", json=self.dump_json(body))
        return self._response(BrandStorePageSuccessResponse, resp, mode=mode)
