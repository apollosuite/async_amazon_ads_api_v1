"""BudgetRecommendations resource operations.

Generated from OpenAPI spec (tag: Budget Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.budget_recommendations import (
    SDBudgetRecommendationsRequest,
    SDBudgetRecommendationsResponse,
)


class BudgetRecommendations(BaseResource):

    @overload
    async def get_sd_budget_recommendations(
        self, body: SDBudgetRecommendationsRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDBudgetRecommendationsResponse: ...
    @overload
    async def get_sd_budget_recommendations(
        self, body: SDBudgetRecommendationsRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_sd_budget_recommendations(
        self, body: SDBudgetRecommendationsRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_sd_budget_recommendations(
        self, body: SDBudgetRecommendationsRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDBudgetRecommendationsResponse | dict[str, Any] | httpx.Response:
        """Given a list of campaigns as input, this API provides the following metrics:"""

        resp = await self._request(
            "POST",
            "/sd/campaigns/budgetRecommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sdbudgetrecommendations.v3+json",
                "Accept": "application/vnd.sdbudgetrecommendations.v3+json",
            },
        )
        return self._response(SDBudgetRecommendationsResponse, resp, mode=mode)
