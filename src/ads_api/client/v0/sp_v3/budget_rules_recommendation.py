"""BudgetRulesRecommendation resource operations.

Generated from OpenAPI spec (tag: BudgetRulesRecommendation).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.budget_rules_recommendation import (
    SPBudgetRulesRecommendationEventResponse,
    SPGetAllRuleEventRequest,
    SPGetAllRuleEventResponse,
)


class BudgetRulesRecommendation(BaseResource):

    @overload
    async def get_all_rule_events(
        self, body: SPGetAllRuleEventRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGetAllRuleEventResponse: ...
    @overload
    async def get_all_rule_events(self, body: SPGetAllRuleEventRequest, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_all_rule_events(self, body: SPGetAllRuleEventRequest, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_all_rule_events(
        self, body: SPGetAllRuleEventRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGetAllRuleEventResponse | dict[str, Any] | httpx.Response:
        """A rule enables an automatic budget increase for a specified date range or for a special event. The response includes the suggested date range for each special event."""

        resp = await self._request("POST", "/sp/v1/events", json=self.dump_json(body))
        return self._response(SPGetAllRuleEventResponse, resp, mode=mode)

    @overload
    async def get_budget_rules_recommendation(
        self, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPBudgetRulesRecommendationEventResponse: ...
    @overload
    async def get_budget_rules_recommendation(self, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_budget_rules_recommendation(self, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_budget_rules_recommendation(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPBudgetRulesRecommendationEventResponse | dict[str, Any] | httpx.Response:
        """A rule enables an automatic budget increase for a specified date range or for a special event. The response also includes a suggested budget increase for each special event."""

        resp = await self._request(
            "POST",
            "/sp/campaigns/budgetRules/recommendations",
            headers={
                "Content-Type": "application/vnd.spbudgetrulesrecommendation.v3+json",
                "Accept": "application/vnd.spbudgetrulesrecommendation.v3+json",
            },
        )
        return self._response(SPBudgetRulesRecommendationEventResponse, resp, mode=mode)
