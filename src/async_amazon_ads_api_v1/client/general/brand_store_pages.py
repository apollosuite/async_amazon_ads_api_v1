"""BrandStorePages resource operations.

Generated from OpenAPI spec (tag: BrandStorePages).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.brand_store_pages import (
    BrandStorePageSuccessResponse,
    QueryBrandStorePageRequest,
)


class BrandStorePages(_ResourceBase):

    async def query_brand_store_page(self, body: QueryBrandStorePageRequest) -> BrandStorePageSuccessResponse:
        """Retrieve brand store page content"""

        return await self._query(body, "/adsApi/v1/query/brandStorePages", BrandStorePageSuccessResponse)
