"""Ads resource operations.

Generated from OpenAPI spec (tag: Ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.ads import (
    CreateSponsoredBrandsAutoCollectionAdsRequestContent,
    CreateSponsoredBrandsAutoCollectionAdsResponseContent,
    CreateSponsoredBrandsBrandVideoAdsRequestContent,
    CreateSponsoredBrandsBrandVideoAdsResponseContent,
    CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent,
    CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent,
    CreateSponsoredBrandsManualCollectionAdsRequestContent,
    CreateSponsoredBrandsManualCollectionAdsResponseContent,
    CreateSponsoredBrandsProductCollectionAdsRequestContent,
    CreateSponsoredBrandsProductCollectionAdsResponseContent,
    CreateSponsoredBrandStoreSpotlightAdsRequestContent,
    CreateSponsoredBrandStoreSpotlightAdsResponseContent,
    CreateSponsoredBrandsVideoAdsRequestContent,
    CreateSponsoredBrandsVideoAdsResponseContent,
    DeleteSponsoredBrandsAdsRequestContent,
    DeleteSponsoredBrandsAdsResponseContent,
    ListSponsoredBrandsAdsRequestContent,
    ListSponsoredBrandsAdsResponseContent,
    UpdateSponsoredBrandsAdsRequestContent,
    UpdateSponsoredBrandsAdsResponseContent,
    UpdateSponsoredBrandsAutoCollectionAdsRequestContent,
    UpdateSponsoredBrandsAutoCollectionAdsResponseContent,
    UpdateSponsoredBrandsManualCollectionAdsRequestContent,
    UpdateSponsoredBrandsManualCollectionAdsResponseContent,
)


class Ads(BaseResource):

    @overload
    async def create_sponsored_brand_store_spotlight_ads(
        self, body: CreateSponsoredBrandStoreSpotlightAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brand_store_spotlight_ads(
        self, body: CreateSponsoredBrandStoreSpotlightAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandStoreSpotlightAdsResponseContent: ...
    @overload
    async def create_sponsored_brand_store_spotlight_ads(
        self, body: CreateSponsoredBrandStoreSpotlightAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brand_store_spotlight_ads(
        self,
        body: CreateSponsoredBrandStoreSpotlightAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandStoreSpotlightAdsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands store spotlight ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/storeSpotlight",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandStoreSpotlightAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_auto_collection_ads(
        self, body: CreateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_auto_collection_ads(
        self, body: CreateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsAutoCollectionAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_auto_collection_ads(
        self, body: CreateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_auto_collection_ads(
        self,
        body: CreateSponsoredBrandsAutoCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandsAutoCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands automatic collection ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/autoCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsAutoCollectionAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_brand_video_ads(
        self, body: CreateSponsoredBrandsBrandVideoAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_brand_video_ads(
        self, body: CreateSponsoredBrandsBrandVideoAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsBrandVideoAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_brand_video_ads(
        self, body: CreateSponsoredBrandsBrandVideoAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_brand_video_ads(
        self,
        body: CreateSponsoredBrandsBrandVideoAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandsBrandVideoAdsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands brand video ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/brandVideo",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsBrandVideoAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_extended_product_collection_ads(
        self, body: CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_extended_product_collection_ads(
        self, body: CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_extended_product_collection_ads(
        self, body: CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_extended_product_collection_ads(
        self,
        body: CreateSponsoredBrandsExtendedProductCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """[DEPRECATED - Do not use] Refer to the [Product Collection Deprecation Notice](https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations#deprecation-of-sponsored-brands-product-collection-ad-type) for more details. Use [/sb/v4/ads/manualCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ads/operation/CreateSponsoredBrandsManualCollectionAds) or [/sb/v4/ads/autoCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ads/operation/CreateSponsoredBrandsAutoCollectionAds) instead."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/productCollectionExtended",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsExtendedProductCollectionAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_manual_collection_ads(
        self, body: CreateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_manual_collection_ads(
        self, body: CreateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsManualCollectionAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_manual_collection_ads(
        self, body: CreateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_manual_collection_ads(
        self,
        body: CreateSponsoredBrandsManualCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandsManualCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands manual collection ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/manualCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsManualCollectionAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_product_collection_ads(
        self, body: CreateSponsoredBrandsProductCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_product_collection_ads(
        self, body: CreateSponsoredBrandsProductCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsProductCollectionAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_product_collection_ads(
        self, body: CreateSponsoredBrandsProductCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_product_collection_ads(
        self,
        body: CreateSponsoredBrandsProductCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateSponsoredBrandsProductCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """[DEPRECATED - Do not use] Refer to the [Product Collection Deprecation Notice](https://advertising.amazon.com/API/docs/en-us/release-notes/deprecations#deprecation-of-sponsored-brands-product-collection-ad-type) for more details. Use [/sb/v4/ads/manualCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ads/operation/CreateSponsoredBrandsManualCollectionAds) or [/sb/v4/ads/autoCollection](https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi/prod#tag/Ads/operation/CreateSponsoredBrandsAutoCollectionAds) instead."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/productCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsProductCollectionAdsResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_video_ads(
        self, body: CreateSponsoredBrandsVideoAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_video_ads(
        self, body: CreateSponsoredBrandsVideoAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> CreateSponsoredBrandsVideoAdsResponseContent: ...
    @overload
    async def create_sponsored_brands_video_ads(
        self, body: CreateSponsoredBrandsVideoAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_video_ads(
        self, body: CreateSponsoredBrandsVideoAdsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateSponsoredBrandsVideoAdsResponseContent | dict[str, Any] | httpx.Response:
        """Creates Sponsored Brands video ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/video",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsVideoAdsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_brands_ads(
        self, body: DeleteSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_brands_ads(
        self, body: DeleteSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> DeleteSponsoredBrandsAdsResponseContent: ...
    @overload
    async def delete_sponsored_brands_ads(
        self, body: DeleteSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_brands_ads(
        self,
        body: DeleteSponsoredBrandsAdsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> DeleteSponsoredBrandsAdsResponseContent | dict[str, Any] | httpx.Response:
        """Deletes Sponsored Brands ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(DeleteSponsoredBrandsAdsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_brands_ads(
        self, body: ListSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_brands_ads(
        self, body: ListSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["pydantic"]
    ) -> ListSponsoredBrandsAdsResponseContent: ...
    @overload
    async def list_sponsored_brands_ads(
        self, body: ListSponsoredBrandsAdsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_brands_ads(
        self,
        body: ListSponsoredBrandsAdsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> ListSponsoredBrandsAdsResponseContent | dict[str, Any] | httpx.Response:
        """Lists Sponsored Brands ads."""

        resp = await self._request(
            "POST",
            "/sb/v4/ads/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(ListSponsoredBrandsAdsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_ads(
        self, body: UpdateSponsoredBrandsAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_ads(
        self, body: UpdateSponsoredBrandsAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> UpdateSponsoredBrandsAdsResponseContent: ...
    @overload
    async def update_sponsored_brands_ads(
        self, body: UpdateSponsoredBrandsAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_ads(
        self, body: UpdateSponsoredBrandsAdsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UpdateSponsoredBrandsAdsResponseContent | dict[str, Any] | httpx.Response:
        """Updates Sponsored Brands ads."""

        resp = await self._request(
            "PUT",
            "/sb/v4/ads",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsAdsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_auto_collection_ads(
        self, body: UpdateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_auto_collection_ads(
        self, body: UpdateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> UpdateSponsoredBrandsAutoCollectionAdsResponseContent: ...
    @overload
    async def update_sponsored_brands_auto_collection_ads(
        self, body: UpdateSponsoredBrandsAutoCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_auto_collection_ads(
        self,
        body: UpdateSponsoredBrandsAutoCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> UpdateSponsoredBrandsAutoCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """Updates the ad settings for an automatic collection by creating a new version"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/autoCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsAutoCollectionAdsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_manual_collection_ads(
        self, body: UpdateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_manual_collection_ads(
        self, body: UpdateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> UpdateSponsoredBrandsManualCollectionAdsResponseContent: ...
    @overload
    async def update_sponsored_brands_manual_collection_ads(
        self, body: UpdateSponsoredBrandsManualCollectionAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_manual_collection_ads(
        self,
        body: UpdateSponsoredBrandsManualCollectionAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> UpdateSponsoredBrandsManualCollectionAdsResponseContent | dict[str, Any] | httpx.Response:
        """Updates the ad settings for a manual collection by creating a new version"""

        resp = await self._request(
            "POST",
            "/sb/ads/creatives/manualCollection",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbadresource.v4+json",
                "Accept": "application/vnd.sbadresource.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsManualCollectionAdsResponseContent, resp, mode=mode)
