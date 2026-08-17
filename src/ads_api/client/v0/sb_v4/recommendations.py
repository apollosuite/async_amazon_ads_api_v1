"""Recommendations resource operations.

Generated from OpenAPI spec (tag: Recommendations).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sb_v4.recommendations import (
    GetBudgetRecommendationsRequestContent,
    GetBudgetRecommendationsResponseContent,
    HeadlineSuggestionRequest,
    HeadlineSuggestionResponse,
    SBOptimizationRecommendationRequestContent,
    SBOptimizationRecommendationResponseContent,
    SBTargetingGetNegativeBrandsResponseContent,
)


class Recommendations(BaseResource):

    @overload
    async def get_budget_recommendations(
        self, body: GetBudgetRecommendationsRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetBudgetRecommendationsResponseContent: ...
    @overload
    async def get_budget_recommendations(
        self, body: GetBudgetRecommendationsRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_recommendations(
        self, body: GetBudgetRecommendationsRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_recommendations(
        self, body: GetBudgetRecommendationsRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetBudgetRecommendationsResponseContent | dict[str, Any] | httpx.Response:
        """Provides daily budget recommendations for a list of requested Sponsored Brands campaigns, with context on estimated historical missed opportunities."""

        resp = await self._request(
            "POST",
            "/sb/campaigns/budgetRecommendations",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbbudgetrecommendation.v4+json",
                "Accept": "application/vnd.sbbudgetrecommendation.v4+json",
            },
        )
        return self._response(GetBudgetRecommendationsResponseContent, resp, mode=mode)

    @overload
    async def get_headline_recommendations(
        self, body: HeadlineSuggestionRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> HeadlineSuggestionResponse: ...
    @overload
    async def get_headline_recommendations(
        self, body: HeadlineSuggestionRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_headline_recommendations(
        self, body: HeadlineSuggestionRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_headline_recommendations(
        self, body: HeadlineSuggestionRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> HeadlineSuggestionResponse | dict[str, Any] | httpx.Response:
        """API to receive creative headline suggestions."""

        resp = await self._request("POST", "/sb/recommendations/creative/headline", json=self.dump_json(body))
        return self._response(HeadlineSuggestionResponse, resp, mode=mode)

    @overload
    async def optimization_recommendation(
        self, body: SBOptimizationRecommendationRequestContent, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBOptimizationRecommendationResponseContent: ...
    @overload
    async def optimization_recommendation(
        self, body: SBOptimizationRecommendationRequestContent, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def optimization_recommendation(
        self, body: SBOptimizationRecommendationRequestContent, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def optimization_recommendation(
        self, body: SBOptimizationRecommendationRequestContent, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBOptimizationRecommendationResponseContent | dict[str, Any] | httpx.Response:
        """Returns recommended bid value for optimization rule enable campaigns. Recommendations are generated based landing page, page type and ASINs provided in request. Only available for Sellers and Vendors."""

        resp = await self._request(
            "POST",
            "/sb/recommendations/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sboptimizationrecommendationresource.v4+json",
                "Accept": "application/vnd.sboptimizationrecommendationresource.v4+json",
            },
        )
        return self._response(SBOptimizationRecommendationResponseContent, resp, mode=mode)

    @overload
    async def targeting_get_negative_brands(
        self, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None
    ) -> SBTargetingGetNegativeBrandsResponseContent: ...
    @overload
    async def targeting_get_negative_brands(
        self, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def targeting_get_negative_brands(
        self, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def targeting_get_negative_brands(
        self, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic", next_token: str | None = None
    ) -> SBTargetingGetNegativeBrandsResponseContent | dict[str, Any] | httpx.Response:
        """Returns brands recommended for negative targeting. Only available for Sellers and Vendors. These recommendations include your own brands because targeting your own brands usually results in lower performance than targeting competitors' brands."""

        params = {
            "nextToken": next_token,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request(
            "GET",
            "/sb/negativeTargets/brands/recommendations",
            params=params,
            headers={"Accept": "application/vnd.sbtargeting.v4+json"},
        )
        return self._response(SBTargetingGetNegativeBrandsResponseContent, resp, mode=mode)
