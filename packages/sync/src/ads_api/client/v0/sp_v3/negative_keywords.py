"""NegativeKeywords resource operations.

Generated from OpenAPI spec (tag: Negative keywords).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.negative_keywords import (
    SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent,
    SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent,
    SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent,
    SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent,
    SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent,
    SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent,
    SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent,
    SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent,
)


class NegativeKeywords(BaseResource):

    @overload
    def create_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def create_sponsored_products_negative_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    def create_sponsored_products_negative_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Create negative keywords"""

        resp = self._request(
            "POST",
            "/sp/negativeKeywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeKeyword.v3+json",
                "Accept": "application/vnd.spNegativeKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent, resp, mode=mode)

    @overload
    def delete_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def delete_sponsored_products_negative_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    def delete_sponsored_products_negative_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Delete negative keywords"""

        resp = self._request(
            "POST",
            "/sp/negativeKeywords/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeKeyword.v3+json",
                "Accept": "application/vnd.spNegativeKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent, resp, mode=mode)

    @overload
    def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """List negative keywords"""

        resp = self._request(
            "POST",
            "/sp/negativeKeywords/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeKeyword.v3+json",
                "Accept": "application/vnd.spNegativeKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent, resp, mode=mode)

    @overload
    def update_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def update_sponsored_products_negative_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    def update_sponsored_products_negative_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Update negative keywords"""

        resp = self._request(
            "PUT",
            "/sp/negativeKeywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeKeyword.v3+json",
                "Accept": "application/vnd.spNegativeKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent, resp, mode=mode)
