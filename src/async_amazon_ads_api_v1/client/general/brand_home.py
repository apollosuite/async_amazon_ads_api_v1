"""BrandHome resource operations.

Generated from OpenAPI spec (tag: BrandHomeAPIService).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.brand_home import (
    ListPagesRequest,
    ListPagesResponse,
    ListStoresRequest,
    ListStoresResponse,
)


class BrandHome(BaseResource):

    async def list_pages(self, body: ListPagesRequest) -> ListPagesResponse:
        """List all Store pages for Advertiser"""

        resp = await self._request(
            "POST",
            "/brand/stores/v1/storePages/list",
            json=body.model_dump(exclude_none=True),
            headers={"Content-Type": "application/brandStore.ListPages.v1+json"},
        )
        return self._response(ListPagesResponse, resp)

    async def list_stores(self, body: ListStoresRequest | None = None) -> ListStoresResponse:
        """Lists all Stores for Advertiser"""

        body = body or ListStoresRequest()
        resp = await self._request(
            "POST",
            "/brand/stores/v1/stores/list",
            json=body.model_dump(exclude_none=True),
            headers={"Content-Type": "application/brandStores.ListStores.v1+json"},
        )
        return self._response(ListStoresResponse, resp)
