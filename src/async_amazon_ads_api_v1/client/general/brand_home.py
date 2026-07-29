"""BrandHome resource operations.

Generated from OpenAPI spec (tag: BrandHomeAPIService).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.brand_home import (
    ListPagesRequest,
    ListPagesResponse,
    ListStoresRequest,
    ListStoresResponse,
)


class BrandHome(_ResourceBase):

    async def list_pages(self, body: ListPagesRequest) -> ListPagesResponse:
        """List all Store pages for Advertiser"""

        return await self._query(
            body,
            "/brand/stores/v1/storePages/list",
            ListPagesResponse,
            headers={"Content-Type": "application/brandStore.ListPages.v1+json"},
        )

    async def list_stores(self, body: ListStoresRequest | None = None) -> ListStoresResponse:
        """Lists all Stores for Advertiser"""

        body = body or ListStoresRequest()
        return await self._query(
            body,
            "/brand/stores/v1/stores/list",
            ListStoresResponse,
            headers={"Content-Type": "application/brandStores.ListStores.v1+json"},
        )
