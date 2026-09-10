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
    def create_sponsored_products_product_ads(
        self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_sponsored_products_product_ads(
        self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsProductAdsResponseContent: ...
    @overload
    def create_sponsored_products_product_ads(
        self, body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_sponsored_products_product_ads(
        self,
        body: SponsoredProductsCreateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Create product ads"""

        resp = self._request(
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
    def delete_sponsored_products_product_ads(
        self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_sponsored_products_product_ads(
        self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent: ...
    @overload
    def delete_sponsored_products_product_ads(
        self, body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_sponsored_products_product_ads(
        self,
        body: SponsoredProductsDeleteSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Delete product ads"""

        resp = self._request(
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
    def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsProductAdsResponseContent: ...
    @overload
    def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    def list_sponsored_products_product_ads(
        self,
        body: SponsoredProductsListSponsoredProductsProductAdsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """List product ads"""

        resp = self._request(
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
    def update_sponsored_products_product_ads(
        self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_sponsored_products_product_ads(
        self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent: ...
    @overload
    def update_sponsored_products_product_ads(
        self, body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_sponsored_products_product_ads(
        self,
        body: SponsoredProductsUpdateSponsoredProductsProductAdsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent | dict[str, Any] | httpx.Response:
        """Update product ads"""

        resp = self._request(
            "PUT",
            "/sp/productAds",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spProductAd.v3+json",
                "Accept": "application/vnd.spProductAd.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsProductAdsResponseContent, resp, mode=mode)
