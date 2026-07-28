"""BrandStores resource operations.

Generated from OpenAPI spec (tag: BrandStores).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.brand_stores import (
    BrandStoreSuccessResponse,
    QueryBrandStoreRequest,
)


class BrandStores(_ResourceBase):

    async def query_brand_store(self, body: QueryBrandStoreRequest) -> BrandStoreSuccessResponse:
        """Query brand store content"""

        return await self._query(body, "/adsApi/v1/query/brandStores", BrandStoreSuccessResponse)
