"""OptimizationRules resource operations.

Generated from OpenAPI spec (tag: Optimization Rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.optimization_rules import (
    OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest,
    OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse,
    OptimizationRulesAPISwaggerCreateOptimizationRulesRequest,
    OptimizationRulesAPISwaggerOptimizationRulesResponse,
    OptimizationRulesAPISwaggerSearchOptimizationRulesRequest,
    OptimizationRulesAPISwaggerSearchOptimizationRulesResponse,
    OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest,
)


class OptimizationRules(BaseResource):

    @overload
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse: ...
    @overload
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest | None = None,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            f"/sp/campaigns/{campaign_id}/optimizationRules",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spoptimizationrules.v1+json",
                "Accept": "application/vnd.spoptimizationrules.v1+json",
            },
        )
        return self._response(OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse, resp, mode=mode)

    @overload
    async def create_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def create_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse: ...
    @overload
    async def create_optimization_rules(
        self, body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spoptimizationrules.v1+json",
                "Accept": "application/vnd.spoptimizationrules.v1+json",
            },
        )
        return self._response(OptimizationRulesAPISwaggerOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def search_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def search_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> OptimizationRulesAPISwaggerSearchOptimizationRulesResponse: ...
    @overload
    async def search_optimization_rules(
        self, body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def search_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> OptimizationRulesAPISwaggerSearchOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/rules/optimization/search",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spoptimizationrules.v1+json",
                "Accept": "application/vnd.spoptimizationrules.v1+json",
            },
        )
        return self._response(OptimizationRulesAPISwaggerSearchOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def update_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def update_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse: ...
    @overload
    async def update_optimization_rules(
        self, body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sp/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spoptimizationrules.v1+json",
                "Accept": "application/vnd.spoptimizationrules.v1+json",
            },
        )
        return self._response(OptimizationRulesAPISwaggerOptimizationRulesResponse, resp, mode=mode)
