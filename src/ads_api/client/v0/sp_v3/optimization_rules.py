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
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignResponse: ...
    @overload
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...
    @overload
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...
    async def associate_optimization_rules_to_campaign(
        self,
        campaign_id: str,
        body: OptimizationRulesAPISwaggerAssociateOptimizationRulesToCampaignRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
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
        self, body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse: ...
    @overload
    async def create_optimization_rules(
        self, body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_optimization_rules(
        self, body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerCreateOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
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
        self, body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> OptimizationRulesAPISwaggerSearchOptimizationRulesResponse: ...
    @overload
    async def search_optimization_rules(
        self, body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def search_optimization_rules(
        self, body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def search_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerSearchOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
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
        self, body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> OptimizationRulesAPISwaggerOptimizationRulesResponse: ...
    @overload
    async def update_optimization_rules(
        self, body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_optimization_rules(
        self, body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rules(
        self,
        body: OptimizationRulesAPISwaggerUpdateOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
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
