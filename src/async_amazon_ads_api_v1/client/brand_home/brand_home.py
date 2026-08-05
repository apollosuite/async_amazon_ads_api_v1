"""BrandHome resource operations.

Generated from OpenAPI spec (tag: BrandHomeAPIService).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.brand_home.brand_home import (
    ListPagesRequest,
    ListPagesResponse,
    ListStoresRequest,
    ListStoresResponse,
)


class BrandHome(BaseResource):

    @overload
    async def list_pages(
        self, body: ListPagesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListPagesResponse: ...
    @overload
    async def list_pages(self, body: ListPagesRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def list_pages(self, body: ListPagesRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_pages(
        self, body: ListPagesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListPagesResponse | dict[str, Any] | httpx.Response:
        """List all Store pages for Advertiser"""

        resp = await self._request(
            "POST",
            "/brand/stores/v1/storePages/list",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={"Content-Type": "application/brandStore.ListPages.v1+json"},
        )
        return self._response(ListPagesResponse, resp, mode=mode)

    @overload
    async def list_stores(
        self, body: ListStoresRequest | None = None, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListStoresResponse: ...
    @overload
    async def list_stores(self, body: ListStoresRequest | None = None, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def list_stores(self, body: ListStoresRequest | None = None, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_stores(
        self, body: ListStoresRequest | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListStoresResponse | dict[str, Any] | httpx.Response:
        """Lists all Stores for Advertiser"""

        body = body or ListStoresRequest()
        resp = await self._request(
            "POST",
            "/brand/stores/v1/stores/list",
            json=body.model_dump(mode="json", exclude_unset=True),
            headers={"Content-Type": "application/brandStores.ListStores.v1+json"},
        )
        return self._response(ListStoresResponse, resp, mode=mode)
