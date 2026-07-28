"""BrandStoreEditionPublishVersions resource operations.

Generated from OpenAPI spec (tag: BrandStoreEditionPublishVersions).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.general.brand_store_edition_publish_versions import (
    BrandStoreEditionPublishVersionMultiStatusResponse,
    BrandStoreEditionPublishVersionSuccessResponse,
    QueryBrandStoreEditionPublishVersionRequest,
    UpdateBrandStoreEditionPublishVersionRequest,
)


class BrandStoreEditionPublishVersions(_ResourceBase):

    async def query_brand_store_edition_publish_version(
        self, body: QueryBrandStoreEditionPublishVersionRequest
    ) -> BrandStoreEditionPublishVersionSuccessResponse:
        """Query store edition publish versions"""

        return await self._query(
            body, "/adsApi/v1/query/brandStoreEditionPublishVersions", BrandStoreEditionPublishVersionSuccessResponse
        )

    async def update_brand_store_edition_publish_version(
        self, body: UpdateBrandStoreEditionPublishVersionRequest
    ) -> BrandStoreEditionPublishVersionMultiStatusResponse:
        """Update store edition publish versions"""

        return await self._query(
            body,
            "/adsApi/v1/update/brandStoreEditionPublishVersions",
            BrandStoreEditionPublishVersionMultiStatusResponse,
        )
