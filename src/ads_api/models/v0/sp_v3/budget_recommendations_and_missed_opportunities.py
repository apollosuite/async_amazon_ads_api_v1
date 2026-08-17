"""Auto-generated models for Budget recommendations and missed opportunities from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class BudgetRecommendationError(LenientModel):
    Error: SPTORBudgetRecommendationErrorResult
    campaignId: str = Field(description="encrypted campaignId")
    index: int = Field(description="Correlate the recommendation to the campaign index in the request. Zero-based")


class BudgetRecommendationForExistingCampaign(LenientModel):
    budgetRuleRecommendation: BudgetRuleRecommendation
    campaignId: str = Field(description="encrypted campaignId")
    index: int = Field(description="Correlate the recommendation to the campaign index in the request. Zero-based")
    sevenDaysMissedOpportunities: SevenDaysMissedOpportunities
    suggestedBudget: float = Field(description="recommended budget for the campaign.")


class BudgetRecommendationRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=100, description="List of campaigns.")


class BudgetRecommendationResponse(LenientModel):
    budgetRecommendationsErrorResults: list[BudgetRecommendationError] = Field(
        description="List of errors that occured when generating bduget recommendation."
    )
    budgetRecommendationsSuccessResults: list[BudgetRecommendationForExistingCampaign] = Field(
        description="List of successful budget recomendation for campagins."
    )


class BudgetRuleRecommendation(LenientModel):
    ruleId: str | None = Field(default=None, description="rule id for the recomemendation")
    ruleName: str | None = Field(default=None, description="rule name for the recomemendation")
    suggestedBudgetIncreasePercent: float | None = Field(default=None, description="suggested increase percent")


class SPTORBudgetRecommendationErrorResult(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")


class SevenDaysMissedOpportunities(LenientModel):
    endDate: str | None = Field(
        default=None,
        description="End date of the date range for which missed opportunity metrics are provided (YYYYMMDD). Local time",
    )
    estimatedMissedClicksLower: int | None = Field(
        default=None,
        description="Lower bound estimate of the additional clicks the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period.",
    )
    estimatedMissedClicksUpper: int | None = Field(
        default=None,
        description="Upper bound estimate of the additional clicks the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period.",
    )
    estimatedMissedImpressionsLower: int | None = Field(
        default=None,
        description="Lower bound estimate of the additional impressions the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period.",
    )
    estimatedMissedImpressionsUpper: int | None = Field(
        default=None,
        description="Upper bound estimate of the additional impressions the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period.",
    )
    estimatedMissedSalesLower: float | None = Field(
        default=None,
        description="Lower bound estimate of the additional sales the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period. Provided in local currency.",
    )
    estimatedMissedSalesUpper: float | None = Field(
        default=None,
        description="Upper bound estimate of the additional sales the campaign might have generated if it had not run out of budget during the {startDate} to {endDate} period. Provided in local currency.",
    )
    percentTimeInBudget: float | None = Field(
        default=None,
        description="percentage of time the campaign is active with a budget. Provided as a decimal ranging from 0 to 1 (e.g. 0.76 means the campaign was in budget for 76% of the time between the startDate and endDate period)",
    )
    startDate: str | None = Field(
        default=None,
        description="Starting date of the date range for which missed opportunity metrics are provided (YYYYMMDD). Local time",
    )


__all__ = [
    "BudgetRecommendationError",
    "BudgetRecommendationForExistingCampaign",
    "BudgetRecommendationRequest",
    "BudgetRecommendationResponse",
    "BudgetRuleRecommendation",
    "SPTORBudgetRecommendationErrorResult",
    "SevenDaysMissedOpportunities",
]
