"""Auto-generated models for Budget Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from datetime import date

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class SDBudgetRecommendation(LenientModel):
    index: int = Field(description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    campaignId: str = Field(description="Campaign id.")
    suggestedBudget: float = Field(description="Recommended budget for the campaign. This will be in local currency.")
    sevenDaysMissedOpportunities: SDSevenDaysMissedOpportunities


class SDBudgetRecommendationErrorResult(LenientModel):
    index: int = Field(description="Correlate the recommendation to the campaign index in the request. Zero-based.")
    campaignId: str = Field(description="Campaign id.")
    code: str = Field(description="The HTTP status code of the response.")
    details: str = Field(description="A human-readable description of the response.")


class SDBudgetRecommendationsRequest(StrictModel):
    """Request for budget recommendations."""

    campaignIds: list[str] = Field(
        min_length=1,
        max_length=100,
        description="A list of campaign ids for which to get budget recommendations and missed opportunities.",
    )


class SDBudgetRecommendationsResponse(LenientModel):
    budgetRecommendationsSuccessResults: list[SDBudgetRecommendation] = Field(
        min_length=0, max_length=100, description="List of successful budget recommendation for campaigns."
    )
    budgetRecommendationsErrorResults: list[SDBudgetRecommendationErrorResult] = Field(
        min_length=0, max_length=100, description="List of errors that occurred when generating budget recommendation."
    )


class SDSevenDaysMissedOpportunities(LenientModel):
    startDate: date | None = Field(
        default=None, description="Start date of the missed opportunities date range (YYYY-MM-DD)."
    )
    endDate: date | None = Field(
        default=None, description="End date of the missed opportunities date range (YYYY-MM-DD)."
    )
    percentTimeInBudget: float | None = Field(
        default=None, description="Percentage of time the campaign is active with a budget."
    )
    estimatedMissedSalesLower: float | None = Field(
        default=None, description="Lower bound of the estimated missed sales. This will be in local currency."
    )
    estimatedMissedSalesUpper: float | None = Field(
        default=None, description="Upper bound of the estimated missed sales. This will be in local currency."
    )
    estimatedMissedClicksLower: int | None = Field(
        default=None, description="Lower bound of the estimated missed clicks."
    )
    estimatedMissedClicksUpper: int | None = Field(
        default=None, description="Upper bound of the estimated missed clicks."
    )
    estimatedMissedImpressionsLower: int | None = Field(
        default=None, description="Lower bound of the estimated missed impressions."
    )
    estimatedMissedImpressionsUpper: int | None = Field(
        default=None, description="Upper bound of the estimated missed impressions."
    )
    estimatedMissedViewableImpressionsLower: int | None = Field(
        default=None, description="Lower bound of the estimated missed viewable impressions for vCPM campaigns."
    )
    estimatedMissedViewableImpressionsUpper: int | None = Field(
        default=None, description="Upper bound of the estimated missed viewable impressions for vCPM campaigns."
    )


__all__ = [
    "SDBudgetRecommendation",
    "SDBudgetRecommendationErrorResult",
    "SDBudgetRecommendationsRequest",
    "SDBudgetRecommendationsResponse",
    "SDSevenDaysMissedOpportunities",
]
