"""BrandStoreEditionPublishVersions resource operations.

Generated from OpenAPI spec (tag: BrandStoreEditionPublishVersions).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.general.brand_store_edition_publish_versions import (
    BrandStoreEditionPublishVersionMultiStatusResponse,
    BrandStoreEditionPublishVersionSuccessResponse,
    QueryBrandStoreEditionPublishVersionRequest,
    UpdateBrandStoreEditionPublishVersionRequest,
)


class BrandStoreEditionPublishVersions(BaseResource):

    @overload
    async def query_brand_store_edition_publish_version(
        self, body: QueryBrandStoreEditionPublishVersionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BrandStoreEditionPublishVersionSuccessResponse: ...
    @overload
    async def query_brand_store_edition_publish_version(
        self, body: QueryBrandStoreEditionPublishVersionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def query_brand_store_edition_publish_version(
        self, body: QueryBrandStoreEditionPublishVersionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def query_brand_store_edition_publish_version(
        self,
        body: QueryBrandStoreEditionPublishVersionRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> BrandStoreEditionPublishVersionSuccessResponse | dict[str, Any] | httpx.Response:
        """Query store edition publish versions"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/query/brandStoreEditionPublishVersions",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(BrandStoreEditionPublishVersionSuccessResponse, resp, mode=mode)

    @overload
    async def update_brand_store_edition_publish_version(
        self, body: UpdateBrandStoreEditionPublishVersionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BrandStoreEditionPublishVersionMultiStatusResponse: ...
    @overload
    async def update_brand_store_edition_publish_version(
        self, body: UpdateBrandStoreEditionPublishVersionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_brand_store_edition_publish_version(
        self, body: UpdateBrandStoreEditionPublishVersionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_brand_store_edition_publish_version(
        self,
        body: UpdateBrandStoreEditionPublishVersionRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> BrandStoreEditionPublishVersionMultiStatusResponse | dict[str, Any] | httpx.Response:
        """Update store edition publish versions"""

        resp = await self._request(
            "POST",
            "/adsApi/v1/update/brandStoreEditionPublishVersions",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(BrandStoreEditionPublishVersionMultiStatusResponse, resp, mode=mode)
