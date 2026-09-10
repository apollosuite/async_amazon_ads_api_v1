"""Keywords resource operations.

Generated from OpenAPI spec (tag: Keywords).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.keywords import (
    SponsoredProductsCreateSponsoredProductsKeywordsRequestContent,
    SponsoredProductsCreateSponsoredProductsKeywordsResponseContent,
    SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent,
    SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent,
    SponsoredProductsListSponsoredProductsKeywordsRequestContent,
    SponsoredProductsListSponsoredProductsKeywordsResponseContent,
    SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent,
    SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent,
)


class Keywords(BaseResource):

    @overload
    def create_sponsored_products_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsKeywordsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def create_sponsored_products_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsKeywordsResponseContent: ...
    @overload
    def create_sponsored_products_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_sponsored_products_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Create keywords"""

        resp = self._request(
            "POST",
            "/sp/keywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spKeyword.v3+json",
                "Accept": "application/vnd.spKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsKeywordsResponseContent, resp, mode=mode)

    @overload
    def delete_sponsored_products_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def delete_sponsored_products_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent: ...
    @overload
    def delete_sponsored_products_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_sponsored_products_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Delete keywords"""

        resp = self._request(
            "POST",
            "/sp/keywords/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spKeyword.v3+json",
                "Accept": "application/vnd.spKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsKeywordsResponseContent, resp, mode=mode)

    @overload
    def list_sponsored_products_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsKeywordsRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def list_sponsored_products_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsKeywordsResponseContent: ...
    @overload
    def list_sponsored_products_keywords(
        self, body: SponsoredProductsListSponsoredProductsKeywordsRequestContent | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def list_sponsored_products_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsKeywordsRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """List keywords"""

        resp = self._request(
            "POST",
            "/sp/keywords/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spKeyword.v3+json",
                "Accept": "application/vnd.spKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsKeywordsResponseContent, resp, mode=mode)

    @overload
    def update_sponsored_products_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    def update_sponsored_products_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent: ...
    @overload
    def update_sponsored_products_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_sponsored_products_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Update keywords"""

        resp = self._request(
            "PUT",
            "/sp/keywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spKeyword.v3+json",
                "Accept": "application/vnd.spKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsKeywordsResponseContent, resp, mode=mode)
