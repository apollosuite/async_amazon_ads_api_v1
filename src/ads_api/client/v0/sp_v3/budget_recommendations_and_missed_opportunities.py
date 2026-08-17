"""BudgetRecommendationsAndMissedOpportunities resource operations.

Generated from OpenAPI spec (tag: Budget recommendations and missed opportunities).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.budget_recommendations_and_missed_opportunities import (
    BudgetRecommendationRequest,
    BudgetRecommendationResponse,
)


class BudgetRecommendationsAndMissedOpportunities(BaseResource):

    @overload
    async def get_budget_recommendations(
        self, body: BudgetRecommendationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> BudgetRecommendationResponse: ...
    @overload
    async def get_budget_recommendations(
        self, body: BudgetRecommendationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_recommendations(
        self, body: BudgetRecommendationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_recommendations(
        self, body: BudgetRecommendationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> BudgetRecommendationResponse | dict[str, Any] | httpx.Response:
        """Given a list of campaigns as input, this API provides the following metrics -  <br> <b>1. Recommended daily budget - </b> Estimated daily budget needed to keep the campaign in budget for the full 24-hour period in a day. Consider this daily budget to minimize your campaign's chances of running out of budget. <br> <b>2. Percent time in budget </b> - Actual average percentage of time the campaign was in budget between the start and end date specified in the response. Note: value -1 means we don’t have enough information to compute the campaign’s percent time in budget. <br> <b>3. Estimated missed impressions, clicks and sales </b> - These are the estimated range of additional impressions, clicks and sales the campaign might have generated between the start and end date specified in the response had it been in budget 100% of the time. These are estimates based on historical traffic and the campaign's past performance (e.g. impressions & clicks generated) but not guaranteed."""

        resp = await self._request(
            "POST",
            "/sp/campaigns/budgetRecommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.budgetrecommendation.v3+json",
                "Accept": "application/vnd.budgetrecommendation.v3+json",
            },
        )
        return self._response(BudgetRecommendationResponse, resp, mode=mode)
