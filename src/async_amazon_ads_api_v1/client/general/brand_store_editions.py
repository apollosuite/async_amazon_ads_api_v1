"""BrandStoreEditions resource operations.

Generated from OpenAPI spec (tag: BrandStoreEditions).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.brand_store_editions import (
    BrandStoreEditionSuccessResponse,
)


class BrandStoreEditions(_ResourceBase):

    async def list_brand_store_edition(
        self, brand_store_id: str, next_token: str | None = None, max_results: int | None = None
    ) -> BrandStoreEditionSuccessResponse:
        """Retrieve brand store page content"""

        params = {
            "brandStoreId": brand_store_id,
            "nextToken": next_token,
            "maxResults": max_results,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/adsApi/v1/brandStoreEditions", params=params)
        return self._response(BrandStoreEditionSuccessResponse, resp)
