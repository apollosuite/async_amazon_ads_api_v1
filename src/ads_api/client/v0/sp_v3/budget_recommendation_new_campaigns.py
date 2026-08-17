"""BudgetRecommendationNewCampaigns resource operations.

Generated from OpenAPI spec (tag: Budget Recommendation New Campaigns).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.budget_recommendation_new_campaigns import (
    InitialBudgetRecommendationRequest,
    InitialBudgetRecommendationResponse,
)


class BudgetRecommendationNewCampaigns(BaseResource):

    @overload
    async def get_budget_recommendation(
        self, body: InitialBudgetRecommendationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> InitialBudgetRecommendationResponse: ...
    @overload
    async def get_budget_recommendation(
        self, body: InitialBudgetRecommendationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_recommendation(
        self, body: InitialBudgetRecommendationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_recommendation(
        self, body: InitialBudgetRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> InitialBudgetRecommendationResponse | dict[str, Any] | httpx.Response:
        """Creates daily budget recommendation along with benchmark metrics when creating a new campaign."""

        resp = await self._request(
            "POST",
            "/sp/campaigns/initialBudgetRecommendation",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.spinitialbudgetrecommendation.v3.4+json",
                "Accept": "application/vnd.spinitialbudgetrecommendation.v3.4+json",
            },
        )
        return self._response(InitialBudgetRecommendationResponse, resp, mode=mode)
