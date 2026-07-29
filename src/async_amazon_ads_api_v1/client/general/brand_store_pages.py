"""BrandStorePages resource operations.

Generated from OpenAPI spec (tag: BrandStorePages).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.brand_store_pages import (
    BrandStorePageSuccessResponse,
    QueryBrandStorePageRequest,
)


class BrandStorePages(BaseResource):

    async def query_brand_store_page(self, body: QueryBrandStorePageRequest) -> BrandStorePageSuccessResponse:
        """Retrieve brand store page content"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/brandStorePages",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(BrandStorePageSuccessResponse, resp)
