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
    def create_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def create_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    def create_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def create_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsCreateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsCreateSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Create targeting clauses"""

        resp = self._request(
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
    def delete_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def delete_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    def delete_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def delete_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsDeleteSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsDeleteSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Delete targeting clauses"""

        resp = self._request(
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
    def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> SponsoredProductsListSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    def list_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsListSponsoredProductsTargetingClausesRequestContent | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsListSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """List targeting clauses"""

        resp = self._request(
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
    def update_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    def update_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["pydantic"]
    ) -> SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent: ...
    @overload
    def update_sponsored_products_targeting_clauses(
        self, body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def update_sponsored_products_targeting_clauses(
        self,
        body: SponsoredProductsUpdateSponsoredProductsTargetingClausesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent | dict[str, Any] | httpx.Response:
        """Update targeting clauses"""

        resp = self._request(
            "PUT",
            "/sp/targets",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spTargetingClause.v3+json",
                "Accept": "application/vnd.spTargetingClause.v3+json",
            },
        )
        return self._response(SponsoredProductsUpdateSponsoredProductsTargetingClausesResponseContent, resp, mode=mode)
