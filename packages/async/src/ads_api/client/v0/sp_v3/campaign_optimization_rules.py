"""CampaignOptimizationRules resource operations.

Generated from OpenAPI spec (tag: Campaign Optimization Rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.campaign_optimization_rules import (
    CreateSPCampaignOptimizationRulesRequest,
    CreateSPCampaignOptimizationRulesResult,
    DeleteSPCampaignOptimizationRuleResult,
    GetSPCampaignOptimizationRuleResponse,
    SPCampaignOptimizationNotificationAPIRequest,
    SPCampaignOptimizationNotificationAPIResponse,
    SPCampaignOptimizationRecommendationAPIResponse,
    SPCampaignOptimizationRecommendationsAPIRequest,
    UpdateSPCampaignOptimizationRuleResult,
    UpdateSPCampaignOptimizationRulesRequest,
)


class CampaignOptimizationRules(BaseResource):

    @overload
    async def create_optimization_rule(
        self, body: CreateSPCampaignOptimizationRulesRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_optimization_rule(
        self, body: CreateSPCampaignOptimizationRulesRequest, *, mode: Literal["pydantic"]
    ) -> CreateSPCampaignOptimizationRulesResult: ...
    @overload
    async def create_optimization_rule(
        self, body: CreateSPCampaignOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rule(
        self, body: CreateSPCampaignOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateSPCampaignOptimizationRulesResult | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/rules/campaignOptimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.optimizationrules.v1+json",
                "Accept": "application/vnd.optimizationrules.v1+json",
            },
        )
        return self._response(CreateSPCampaignOptimizationRulesResult, resp, mode=mode)

    @overload
    async def delete_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def delete_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["pydantic"]
    ) -> DeleteSPCampaignOptimizationRuleResult: ...
    @overload
    async def delete_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def delete_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DeleteSPCampaignOptimizationRuleResult | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "DELETE",
            f"/sp/rules/campaignOptimization/{campaign_optimization_id}",
            headers={"Accept": "application/vnd.optimizationrules.v1+json"},
        )
        return self._response(DeleteSPCampaignOptimizationRuleResult, resp, mode=mode)

    @overload
    async def get_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["pydantic"]
    ) -> GetSPCampaignOptimizationRuleResponse: ...
    @overload
    async def get_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_campaign_optimization_rule(
        self, campaign_optimization_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetSPCampaignOptimizationRuleResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "GET",
            f"/sp/rules/campaignOptimization/{campaign_optimization_id}",
            headers={"Accept": "application/vnd.optimizationrules.v1+json"},
        )
        return self._response(GetSPCampaignOptimizationRuleResponse, resp, mode=mode)

    @overload
    async def get_optimization_rule_eligibility(
        self, body: SPCampaignOptimizationRecommendationsAPIRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_optimization_rule_eligibility(
        self, body: SPCampaignOptimizationRecommendationsAPIRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignOptimizationRecommendationAPIResponse: ...
    @overload
    async def get_optimization_rule_eligibility(
        self, body: SPCampaignOptimizationRecommendationsAPIRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_optimization_rule_eligibility(
        self,
        body: SPCampaignOptimizationRecommendationsAPIRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> SPCampaignOptimizationRecommendationAPIResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/rules/campaignOptimization/eligibility",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.optimizationrules.v1+json",
                "Accept": "application/vnd.optimizationrules.v1+json",
            },
        )
        return self._response(SPCampaignOptimizationRecommendationAPIResponse, resp, mode=mode)

    @overload
    async def get_rule_notification(
        self, body: SPCampaignOptimizationNotificationAPIRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_rule_notification(
        self, body: SPCampaignOptimizationNotificationAPIRequest, *, mode: Literal["pydantic"]
    ) -> SPCampaignOptimizationNotificationAPIResponse: ...
    @overload
    async def get_rule_notification(
        self, body: SPCampaignOptimizationNotificationAPIRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_rule_notification(
        self, body: SPCampaignOptimizationNotificationAPIRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPCampaignOptimizationNotificationAPIResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/rules/campaignOptimization/state",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.optimizationrules.v1+json",
                "Accept": "application/vnd.optimizationrules.v1+json",
            },
        )
        return self._response(SPCampaignOptimizationNotificationAPIResponse, resp, mode=mode)

    @overload
    async def update_optimization_rule(
        self, body: UpdateSPCampaignOptimizationRulesRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_optimization_rule(
        self, body: UpdateSPCampaignOptimizationRulesRequest, *, mode: Literal["pydantic"]
    ) -> UpdateSPCampaignOptimizationRuleResult: ...
    @overload
    async def update_optimization_rule(
        self, body: UpdateSPCampaignOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rule(
        self, body: UpdateSPCampaignOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UpdateSPCampaignOptimizationRuleResult | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sp/rules/campaignOptimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.optimizationrules.v1+json",
                "Accept": "application/vnd.optimizationrules.v1+json",
            },
        )
        return self._response(UpdateSPCampaignOptimizationRuleResult, resp, mode=mode)
