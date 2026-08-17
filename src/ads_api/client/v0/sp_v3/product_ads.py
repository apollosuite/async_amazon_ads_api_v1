"""ProductAds resource operations.

Generated from OpenAPI spec (tag: Product ads).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.product_ads import (
    SponsoredProductsCreateSponsoredProductsProductAdsRequestContent,
    SponsoredProductsCreateSponsoredProductsProductAdsResponseContent,
    SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent,
    SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent,
    SponsoredProductsListSponsoredProductsProductAdsRequestContent,
    SponsoredProductsListSponsoredProductsProductAdsResponseContent,
    SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent,
    SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent,
)


class ProductAds(BaseResource):

    @overload
    async def create_sponsored_products_product_ads(
        self,
        body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsProductAdsResponseContent: ...
    @overload
    async def create_sponsored_products_product_ads(
        self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_product_ads(
        self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_products_product_ads(
        self,
        body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Create product ads"""

        resp = await self._request(
            "POST",
            "/sp/productAds",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spProductAd.v3+json",
                "Accept": "application/vnd.spProductAd.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsProductAdsResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_products_product_ads(
        self,
        body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent: ...
    @overload
    async def delete_sponsored_products_product_ads(
        self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_product_ads(
        self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_products_product_ads(
        self,
        body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Delete product ads"""

        resp = await self._request(
            "POST",
            "/sp/productAds/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spProductAd.v3+json",
                "Accept": "application/vnd.spProductAd.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsProductAdsResponseContent: ...
    @overload
    async def list_sponsored_products_product_ads(
        self, body: SponsoredProductsListSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_product_ads(
        self, body: SponsoredProductsListSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """List product ads"""

        resp = await self._request(
            "POST",
            "/sp/productAds/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spProductAd.v3+json",
                "Accept": "application/vnd.spProductAd.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsProductAdsResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_products_product_ads(
        self,
        body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent: ...
    @overload
    async def update_sponsored_products_product_ads(
        self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_product_ads(
        self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_products_product_ads(
        self,
        body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Update product ads"""

        resp = await self._request(
            "PUT",
            "/sp/productAds",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spProductAd.v3+json",
                "Accept": "application/vnd.spProductAd.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent, resp, mode=mode)
