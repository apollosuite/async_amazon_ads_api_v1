"""AdCreatives resource operations.

Generated from OpenAPI spec (tag: Ad creatives).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.ad_creatives import (
    CreateBrandVideoCreativeRequestContent,
    CreateBrandVideoCreativeResponseContent,
    CreateExtendedProductCollectionCreativeRequestContent,
    CreateExtendedProductCollectionCreativeResponseContent,
    CreateProductCollectionCreativeRequestContent,
    CreateProductCollectionCreativeResponseContent,
    CreateStoreSpotlightCreativeRequestContent,
    CreateStoreSpotlightCreativeResponseContent,
    CreateVideoCreativeRequestContent,
    CreateVideoCreativeResponseContent,
    ListCreativesRequestContent,
    ListCreativesResponseContent,
)


class AdCreatives(BaseResource):

    @overload
    async def create_brand_video_creative(
        self, body: CreateBrandVideoCreativeRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateBrandVideoCreativeResponseContent: ...
    @overload
    async def create_brand_video_creative(
        self, body: CreateBrandVideoCreativeRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_brand_video_creative(
        self, body: CreateBrandVideoCreativeRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_brand_video_creative(
        self, body: CreateBrandVideoCreativeRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateBrandVideoCreativeResponseContent | dict[str, Any] | httpx.Response:
        """This API creates a new version of an existing creative for given Sponsored Brands Ad by supplying brand video creative content"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/brandVideo",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(CreateBrandVideoCreativeResponseContent, resp, mode=mode)

    @overload
    async def create_extended_product_collection_creative(
        self, body: CreateExtendedProductCollectionCreativeRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateExtendedProductCollectionCreativeResponseContent: ...
    @overload
    async def create_extended_product_collection_creative(
        self, body: CreateExtendedProductCollectionCreativeRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_extended_product_collection_creative(
        self, body: CreateExtendedProductCollectionCreativeRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_extended_product_collection_creative(
        self,
        body: CreateExtendedProductCollectionCreativeRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> CreateExtendedProductCollectionCreativeResponseContent | dict[str, Any] | httpx.Response:
        """[DEPRECATED - Do not use] Refer to the [Product Collection Deprecation Notice](https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations#deprecation-of-sponsored-brands-product-collection-ad-type) for more details. Use [/sb/ads/creatives/manualCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ad-creatives/operation/UpdateSponsoredBrandsManualCollectionAds) instead."""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/productCollectionExtended",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(CreateExtendedProductCollectionCreativeResponseContent, resp, mode=mode)

    @overload
    async def create_product_collection_creative(
        self, body: CreateProductCollectionCreativeRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateProductCollectionCreativeResponseContent: ...
    @overload
    async def create_product_collection_creative(
        self, body: CreateProductCollectionCreativeRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_product_collection_creative(
        self, body: CreateProductCollectionCreativeRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_product_collection_creative(
        self,
        body: CreateProductCollectionCreativeRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> CreateProductCollectionCreativeResponseContent | dict[str, Any] | httpx.Response:
        """[DEPRECATED - Do not use] Refer to the [Product Collection Deprecation Notice](https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations#deprecation-of-sponsored-brands-product-collection-ad-type) for more details. Use [/sb/ads/creatives/manualCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ad-creatives/operation/UpdateSponsoredBrandsManualCollectionAds) instead."""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/productCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(CreateProductCollectionCreativeResponseContent, resp, mode=mode)

    @overload
    async def create_store_spotlight_creative(
        self, body: CreateStoreSpotlightCreativeRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateStoreSpotlightCreativeResponseContent: ...
    @overload
    async def create_store_spotlight_creative(
        self, body: CreateStoreSpotlightCreativeRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_store_spotlight_creative(
        self, body: CreateStoreSpotlightCreativeRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_store_spotlight_creative(
        self, body: CreateStoreSpotlightCreativeRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateStoreSpotlightCreativeResponseContent | dict[str, Any] | httpx.Response:
        """This API creates a new version of creative for given Sponsored Brands ad by supplying store spotlight creative content"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/storeSpotlight",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(CreateStoreSpotlightCreativeResponseContent, resp, mode=mode)

    @overload
    async def create_video_creative(
        self, body: CreateVideoCreativeRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateVideoCreativeResponseContent: ...
    @overload
    async def create_video_creative(
        self, body: CreateVideoCreativeRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_video_creative(
        self, body: CreateVideoCreativeRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_video_creative(
        self, body: CreateVideoCreativeRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateVideoCreativeResponseContent | dict[str, Any] | httpx.Response:
        """This API creates a new version of an existing creative for given Sponsored Brands ad by supplying video creative content"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/video",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(CreateVideoCreativeResponseContent, resp, mode=mode)

    @overload
    async def list_creatives(
        self, body: ListCreativesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListCreativesResponseContent: ...
    @overload
    async def list_creatives(self, body: ListCreativesRequestContent, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def list_creatives(self, body: ListCreativesRequestContent, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def list_creatives(
        self, body: ListCreativesRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> ListCreativesResponseContent | dict[str, Any] | httpx.Response:
        """This API gets an array of all Sponsored Brands creatives that qualify the given resource identifiers and filters"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbAdCreativeResource.v4+json",
                "Accept": "application/vnd.sbAdCreativeResource.v4+json",
            },
        )
        return self._response(ListCreativesResponseContent, resp, mode=mode)
