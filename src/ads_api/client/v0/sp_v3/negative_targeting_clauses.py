"""NegativeTargetingClauses resource operations.

Generated from OpenAPI spec (tag: Negative targeting clauses).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.negative_targeting_clauses import (
    SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent,
    SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesResponseContent,
    SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent,
    SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesResponseContent,
    SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent,
    SponsoredProductsListSponsoredProductsNegativeTargetingClausesResponseContent,
    SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent,
    SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesResponseContent,
)


class NegativeTargetingClauses(BaseResource):

    @overload
    async def create_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesResponseContent: ...
    @overload
    async def create_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def create_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Create negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/negativeTargets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsCreateSponsoredProductsNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def delete_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesResponseContent: ...
    @overload
    async def delete_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def delete_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Delete negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/negativeTargets/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsDeleteSponsoredProductsNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def list_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsNegativeTargetingClausesResponseContent: ...
    @overload
    async def list_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def list_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsNegativeTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsListSponsoredProductsNegativeTargetingClausesResponseContent | dict[str, Any] | httpx.Response
    ):
        """List negative targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/negativeTargets/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsListSponsoredProductsNegativeTargetingClausesResponseContent, resp, mode=mode
        )

    @overload
    async def update_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesResponseContent: ...
    @overload
    async def update_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def update_sponsored_products_negative_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> (
        SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesResponseContent
        | dict[str, Any]
        | httpx.Response
    ):
        """Update negative targeting clauses"""

        resp = await self._request(
            "PUT",
            "/sp/negativeTargets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spNegativeTargetingClause.v3+json",
                "Accept": "application/vnd.spNegativeTargetingClause.v3+json",
            },
        )
        return self._response(
            SponsoredProductsUpdateSponsoredProductsNegativeTargetingClausesResponseContent, resp, mode=mode
        )
