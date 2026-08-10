"""BrandStores resource operations.

Generated from OpenAPI spec (tag: BrandStores).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.general.brand_stores import (
    BrandStoreSuccessResponse,
    QueryBrandStoreRequest,
)


class BrandStores(BaseResource):

    @overload
    async def query_brand_store(
        self, body: QueryBrandStoreRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BrandStoreSuccessResponse: ...
    @overload
    async def query_brand_store(self, body: QueryBrandStoreRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def query_brand_store(self, body: QueryBrandStoreRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def query_brand_store(
        self, body: QueryBrandStoreRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BrandStoreSuccessResponse | dict[str, Any] | httpx.Response:
        """Query brand store content"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/brandStores",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(BrandStoreSuccessResponse, resp, mode=mode)
