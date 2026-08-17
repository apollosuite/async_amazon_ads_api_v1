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
    async def create_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    async def create_sponsored_products_negative_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_negative_keywords(
        self, body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Create negative keywords"""

        resp = await self._request(
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
    async def delete_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    async def delete_sponsored_products_negative_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_negative_keywords(
        self, body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Delete negative keywords"""

        resp = await self._request(
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
    async def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    async def list_sponsored_products_negative_keywords(
        self, body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_negative_keywords(
        self, body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """List negative keywords"""

        resp = await self._request(
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
    async def update_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent: ...
    @overload
    async def update_sponsored_products_negative_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_negative_keywords(
        self, body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_products_negative_keywords(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeKeywordsRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent | dict[str, Any] | httpx.Response:
        """Update negative keywords"""

        resp = await self._request(
            "PUT",
            "/sp/negativeKeywords",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeKeyword.v3+json",
                "Accept": "application/vnd.spNegativeKeyword.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsNegativeKeywordsResponseContent, resp, mode=mode)
