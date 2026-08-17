"""OptimizationRules resource operations.

Generated from OpenAPI spec (tag: Optimization rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.optimization_rules import (
    AssociateSponsoredBrandsOptimizationRulesRequestContent,
    AssociateSponsoredBrandsOptimizationRulesResponseContent,
    CreateSponsoredBrandsOptimizationRulesRequestContent,
    CreateSponsoredBrandsOptimizationRulesResponseContent,
    DisassociateSponsoredBrandsOptimizationRulesRequestContent,
    DisassociateSponsoredBrandsOptimizationRulesResponseContent,
    ListSponsoredBrandsOptimizationRulesRequestContent,
    ListSponsoredBrandsOptimizationRulesResponseContent,
    UpdateSponsoredBrandsOptimizationRulesRequestContent,
    UpdateSponsoredBrandsOptimizationRulesResponseContent,
)


class OptimizationRules(BaseResource):

    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: AssociateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> AssociateSponsoredBrandsOptimizationRulesResponseContent: ...
    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: AssociateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: AssociateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def associate_sponsored_brands_optimization_rules(
        self,
        body: AssociateSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> AssociateSponsoredBrandsOptimizationRulesResponseContent | dict[str, Any] | httpx.Response:
        """Currently available in beta. Associate one or more optimization rules by providing combinations of entityId-ruleId that require association."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/associate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(AssociateSponsoredBrandsOptimizationRulesResponseContent, resp, mode=mode)

    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: CreateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateSponsoredBrandsOptimizationRulesResponseContent: ...
    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: CreateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: CreateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_optimization_rules(
        self,
        body: CreateSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> CreateSponsoredBrandsOptimizationRulesResponseContent | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(CreateSponsoredBrandsOptimizationRulesResponseContent, resp, mode=mode)

    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self,
        body: DisassociateSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> DisassociateSponsoredBrandsOptimizationRulesResponseContent: ...
    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: DisassociateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: DisassociateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_sponsored_brands_optimization_rules(
        self,
        body: DisassociateSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> DisassociateSponsoredBrandsOptimizationRulesResponseContent | dict[str, Any] | httpx.Response:
        """Currently available in beta. Disassociate one or more optimization rules by providing combinations of entityId-ruleId that require disassociation"""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/disassociate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(DisassociateSponsoredBrandsOptimizationRulesResponseContent, resp, mode=mode)

    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: ListSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> ListSponsoredBrandsOptimizationRulesResponseContent: ...
    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: ListSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: ListSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_brands_optimization_rules(
        self,
        body: ListSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> ListSponsoredBrandsOptimizationRulesResponseContent | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(ListSponsoredBrandsOptimizationRulesResponseContent, resp, mode=mode)

    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: UpdateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> UpdateSponsoredBrandsOptimizationRulesResponseContent: ...
    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: UpdateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: UpdateSponsoredBrandsOptimizationRulesRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_optimization_rules(
        self,
        body: UpdateSponsoredBrandsOptimizationRulesRequestContent,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> UpdateSponsoredBrandsOptimizationRulesResponseContent | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "PUT",
            "/sb/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(UpdateSponsoredBrandsOptimizationRulesResponseContent, resp, mode=mode)
