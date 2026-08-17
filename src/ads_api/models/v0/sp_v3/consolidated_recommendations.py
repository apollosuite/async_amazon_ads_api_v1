"""Auto-generated models for Consolidated Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class RecommendationType(StrEnum):
    """
    Type of recommendations requested.
    """

    BIDDING_STRATEGY = "BIDDING_STRATEGY"  # Recommendation for the campaign bidding strategy.
    BUDGET_STRATEGY = "BUDGET_STRATEGY"  # Recommendation for the campaign budget.
    KEYWORD = "KEYWORD"  # Recommendations related to campaign keywords targeting.
    KEYWORD_GROUP = "KEYWORD_GROUP"  # Recommendation related to Keyword groups. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords.
    PLACEMENT_BIDDING = (
        "PLACEMENT_BIDDING"  # Bid recommendations for campaign placements such as top of search, rest of search etc.
    )
    SHOPPER_COHORT = (
        "SHOPPER_COHORT"  # Bid adjustment recommendations for the shopper cohorts (audiences) attached to the campaign.
    )


class AudienceSegment(LenientModel):
    audienceId: str = Field(description="Unique identifier for the audience segment.")
    audienceSegmentType: str = Field(description="Type of audience segment.")


class BiddingStrategyRecommendation(LenientModel):
    """Contains suggested recommendation for the campaign bidding strategy."""

    action: str | None = Field(default=None, description="Type of suggested action.")
    suggestedBiddingStrategy: str | None = Field(
        default=None, description="The suggested bidding strategy value for the campaign."
    )


class BudgetRecommendation(LenientModel):
    """Contains suggested recommendation for the campaign budget."""

    action: str | None = Field(default=None, description="Type of suggested action.")
    suggestedBudget: float | None = Field(default=None, description="The suggested budget value for the campaign.")


class Campaign(StrictModel):
    campaignId: str = Field(description="The identifier of the campaign.")
    recommendationType: Annotated[RecommendationType, lenient_enum(RecommendationType)]


class CampaignRecommendation(LenientModel):
    """This object contains a set of recommendations for a campaign across bid, budget, targeting."""

    biddingStrategyRecommendation: BiddingStrategyRecommendation | None = Field(default=None)
    budgetRecommendation: BudgetRecommendation | None = Field(default=None)
    campaignId: str | None = Field(default=None, description="The identifier of the campaign.")
    keywordTargetingRecommendations: list[KeywordTargetingRecommendation] | None = Field(
        default=None, min_length=0, max_length=50
    )
    placementBiddingRecommendations: list[PlacementBiddingRecommendation] | None = Field(
        default=None, min_length=0, max_length=50
    )
    sevenDaysEstimatedOpportunities: SevenDaysEstimatedOpportunities | None = Field(default=None)
    targetingGroupBidRecommendations: list[TargetingGroupBidRecommendation] | None = Field(
        default=None, min_length=0, max_length=50
    )


class ForecastEstimates(LenientModel):
    endDate: str | None = Field(
        default=None, description="End date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format."
    )
    estimatedAdSpendLower: float | None = Field(default=None, description="Lower estimated ad spend for the campaign.")
    estimatedAdSpendUpper: float | None = Field(default=None, description="Upper estimated ad spend for the campaign.")
    estimatedIncrementalClicksLower: int | None = Field(
        default=None,
        description="Lower bound of the estimated incremental clicks that could be gained if all optimizations are made.",
    )
    estimatedIncrementalClicksUpper: int | None = Field(
        default=None,
        description="Upper bound of the estimated incremental clicks that could be gained if all optimizations are made.",
    )
    estimatedIncrementalConversionsLower: int | None = Field(
        default=None, description="Lower estimated incremental number of conversions for the campaign."
    )
    estimatedIncrementalConversionsUpper: int | None = Field(
        default=None, description="Upper estimated incremental number of conversions for the campaign."
    )
    estimatedIncrementalImpressionsLower: int | None = Field(
        default=None, description="Lower estimated incremental number of impressions for the campaign."
    )
    estimatedIncrementalImpressionsUpper: int | None = Field(
        default=None, description="Upper estimated incremental number of impressions for the campaign."
    )
    estimatedIncrementalSalesLower: float | None = Field(
        default=None, description="Lower estimated incremental sales for the campaign."
    )
    estimatedIncrementalSalesUpper: float | None = Field(
        default=None, description="Upper estimated incremental sales for the campaign."
    )
    startDate: str | None = Field(
        default=None, description="Start date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format."
    )


class GetCampaignRecommendationsRequestV2(StrictModel):
    campaigns: list[Campaign] = Field(
        min_length=1, max_length=10, description="List of campaigns with specific recommendation types requested."
    )
    maxResults: int | None = Field(
        default=1, ge=1, le=5, description="Optional. Limits the number of items to return in the response."
    )
    nextToken: str | None = Field(default=None, description="Optional. Token to retrieve subsequent page of results.")


class GetCampaignRecommendationsResponse(LenientModel):
    nextToken: str | None = Field(
        default=None,
        description="An identifier to fetch next set of campaign recommendations records in the result set if available. This will be null when at the end of result set.",
    )
    recommendations: list[CampaignRecommendation] = Field(
        min_length=0, max_length=50, description="List of campaign recommendations."
    )


class GetCampaignRecommendationsResponseV2(LenientModel):
    nextToken: str | None = Field(
        default=None,
        description="An identifier to fetch next set of recommendations records in the result set if available. This will be null when at the end of result set.",
    )
    recommendations: list[Recommendation] = Field(min_length=0, max_length=50, description="List of recommendations.")


class KeywordTargetingRecommendation(LenientModel):
    """Contains suggested recommendation for the keyword targeting."""

    action: str | None = Field(default=None, description="Type of action for the keyword targeting.")
    adGroupId: str | None = Field(default=None, description="The ad group identifier.")
    keywordId: str | None = Field(default=None, description="The identifier of the keyword targeting.")
    keywordText: str | None = Field(default=None, description="The keyword text.")
    matchType: str | None = Field(
        default=None,
        description="Keyword match type. | Value | Description | | --- | --- | | `BROAD` | Use BROAD to broadly match your keyword targeting ads with search queries.| | `EXACT` | Use EXACT to exactly match your keyword targeting ads with search queries.| | `PHRASE` | Use PHRASE to match your keyword targeting ads with search phrases.| | `GROUP` | Use GROUP to match your keyword targeting ads with keyword group. |",
    )
    suggestedBid: float | None = Field(
        default=None, description="The suggested bid value associated with this keyword targeting clause."
    )


class PlacementBiddingRecommendation(LenientModel):
    """Contains suggested recommendation for a placement bid adjustment."""

    action: str | None = Field(default=None, description="Type of suggested action.")
    incrementalImpressionsLowerPercent: int | None = Field(
        default=None,
        description="Lower bound of the estimated incremental impressions that could be gained if this optimization used",
    )
    incrementalImpressionsUpperPercent: int | None = Field(
        default=None,
        description="Upper bound of the estimated incremental impressions that could be gained if this optimization used",
    )
    placementType: str | None = Field(default=None, description="The placement type.")
    suggestedBidAdjustment: float | None = Field(
        default=None, description="The suggested bid adjustment percent value for this placement type."
    )


class Recommendation(LenientModel):
    campaignId: str = Field(description="The identifier of the campaign.")
    forecastEstimates: ForecastEstimates | None = Field(default=None)
    recommendationDetails: RecommendationDetails
    recommendationType: Annotated[RecommendationType | str, lenient_enum(RecommendationType)]


class RecommendationDetails(LenientModel):
    """Contains one or more recommendation details of different types."""

    biddingStrategyRecommendation: BiddingStrategyRecommendation | None = Field(default=None)
    budgetRecommendation: BudgetRecommendation | None = Field(default=None)
    keywordTargetingRecommendations: list[KeywordTargetingRecommendation] | None = Field(
        default=None, min_length=1, max_length=10, description="List of keyword targeting recommendations."
    )
    placementBiddingRecommendations: list[PlacementBiddingRecommendation] | None = Field(
        default=None, min_length=1, max_length=10, description="List of placement bid recommendations."
    )
    shopperCohortBiddingRecommendation: ShopperCohortBiddingRecommendation | None = Field(default=None)
    targetingGroupBidRecommendations: list[TargetingGroupBidRecommendation] | None = Field(
        default=None, min_length=1, max_length=10, description="List of targeting group bid recommendations."
    )


class SevenDaysEstimatedOpportunities(LenientModel):
    endDate: str | None = Field(
        default=None, description="End date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format."
    )
    estimatedIncrementalClicksLower: int | None = Field(
        default=None,
        description="Lower bound of the estimated incremental clicks that could be gained if all optimizations are made.",
    )
    estimatedIncrementalClicksUpper: int | None = Field(
        default=None,
        description="Upper bound of the estimated incremental clicks that could be gained if all optimizations are made.",
    )
    startDate: str | None = Field(
        default=None, description="Start date of the opportunities date range in YYYY-MM-DDTHH:mm:ssZ format."
    )


class ShopperCohortBiddingRecommendation(LenientModel):
    action: str = Field(description="Recommended action for shopper cohort bidding.")
    audienceSegments: list[AudienceSegment] = Field(
        min_length=1, max_length=10, description="List of audience segments for this recommendation."
    )
    percentage: int = Field(ge=0, le=900, description="Bid adjustment percentage (basis points, e.g., 900 = 9%).")
    shopperCohortType: str = Field(description="Type of shopper cohort.")


class TargetingGroupBidRecommendation(LenientModel):
    """Contains suggested recommendation for the auto targeting group."""

    action: str | None = Field(default=None, description="Type of suggested action.")
    adGroupId: str | None = Field(default=None, description="The ad group identifier.")
    suggestedBid: float | None = Field(
        default=None, description="The suggested bid value associated with this targeting."
    )
    targetId: str | None = Field(default=None, description="The target identifier.")
    targetingGroupExpression: str | None = Field(default=None, description="The type of targeting group expression.")


__all__ = [
    "AudienceSegment",
    "BiddingStrategyRecommendation",
    "BudgetRecommendation",
    "Campaign",
    "CampaignRecommendation",
    "ForecastEstimates",
    "GetCampaignRecommendationsRequestV2",
    "GetCampaignRecommendationsResponse",
    "GetCampaignRecommendationsResponseV2",
    "KeywordTargetingRecommendation",
    "PlacementBiddingRecommendation",
    "Recommendation",
    "RecommendationDetails",
    "RecommendationType",
    "SevenDaysEstimatedOpportunities",
    "ShopperCohortBiddingRecommendation",
    "TargetingGroupBidRecommendation",
]
