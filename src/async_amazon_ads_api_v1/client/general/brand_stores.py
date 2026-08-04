"""BrandStores resource operations.

Generated from OpenAPI spec (tag: BrandStores).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.general.brand_stores import (
    BrandStoreSuccessResponse,
    QueryBrandStoreRequest,
)


class BrandStores(BaseResource):

    async def query_brand_store(self, body: QueryBrandStoreRequest) -> BrandStoreSuccessResponse:
        """Query brand store content"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/brandStores",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(BrandStoreSuccessResponse, resp)
