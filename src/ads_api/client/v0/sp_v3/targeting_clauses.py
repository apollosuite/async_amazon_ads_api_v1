"""TargetingClauses resource operations.

Generated from OpenAPI spec (tag: Targeting clauses).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.targeting_clauses import (
    SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent,
    SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent,
    SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent,
    SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent,
    SponsoredProductsListSponsoredProductsTargetingClausesRequestContent,
    SponsoredProductsListSponsoredProductsTargetingClausesResponseContent,
    SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent,
    SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent,
)


class TargetingClauses(BaseResource):

    @overload
    async def create_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    async def create_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Create targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/targets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetingClause.v3+json",
                "Accept": "application/vnd.spTargetingClause.v3+json",
            },
        )
        return self._response(SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent, resp, mode=mode)

    @overload
    async def delete_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    async def delete_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def delete_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Delete targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/targets/delete",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetingClause.v3+json",
                "Accept": "application/vnd.spTargetingClause.v3+json",
            },
        )
        return self._response(SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    async def list_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsListSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """List targeting clauses"""

        resp = await self._request(
            "POST",
            "/sp/targets/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetingClause.v3+json",
                "Accept": "application/vnd.spTargetingClause.v3+json",
            },
        )
        return self._response(SponsoredProductsListSponsoredProductsTargetingClausesResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    async def update_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Update targeting clauses"""

        resp = await self._request(
            "PUT",
            "/sp/targets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetingClause.v3+json",
                "Accept": "application/vnd.spTargetingClause.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent, resp, mode=mode)
