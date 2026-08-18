"""Auto-generated models for Consolidated Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AudienceSegmentAudienceSegmentType = Literal["BEHAVIOR_DYNAMIC", "SPONSORED_ADS_AMC"]
"""
Type of audience segment.
"""


type BiddingStrategyRecommendationAction = Literal["UPDATE"]
"""
Type of suggested action.
"""


type BiddingStrategyRecommendationSuggestedBiddingStrategy = Literal[
    "AUTO_FOR_SALES",  # Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
    "LEGACY_FOR_SALES",  # Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default.
    "MANUAL",  # Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
]
"""
The suggested bidding strategy value for the campaign.

Supported values:
- `LEGACY_FOR_SALES`: Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default.
- `AUTO_FOR_SALES`: Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
- `MANUAL`: Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
"""


type BudgetRecommendationAction = Literal["DECREASE", "INCREASE"]
"""
Type of suggested action.
"""


type KeywordTargetingRecommendationAction = Literal[
    "ADD",
    "DECREASE",
    "INCREASE",
    "REMOVE",
    "UPDATE",
]
"""
Type of action for the keyword targeting.
"""


type KeywordTargetingRecommendationMatchType = Literal[
    "BROAD",
    "EXACT",
    "GROUP",
    "PHRASE",
]
"""
Keyword match type. | Value | Description | | --- | --- | | `BROAD` | Use BROAD to broadly match your keyword targeting ads with search queries.| | `EXACT` | Use EXACT to exactly match your keyword targeting ads with search queries.| | `PHRASE` | Use PHRASE to match your keyword targeting ads with search phrases.| | `GROUP` | Use GROUP to match your keyword targeting ads with keyword group. |
"""


type PlacementBiddingRecommendationAction = Literal[
    "ADD",
    "DECREASE",
    "INCREASE",
    "REMOVE",
]
"""
Type of suggested action.
"""


type PlacementBiddingRecommendationPlacementType = Literal[
    "PLACEMENT_PRODUCT_PAGE", "PLACEMENT_REST_OF_SEARCH", "PLACEMENT_TOP"
]
"""
The placement type.
"""


type RecommendationType = Literal[
    "BIDDING_STRATEGY",  # Recommendation for the campaign bidding strategy.
    "BUDGET_STRATEGY",  # Recommendation for the campaign budget.
    "KEYWORD",  # Recommendations related to campaign keywords targeting.
    "KEYWORD_GROUP",  # Recommendation related to Keyword groups. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords.
    "PLACEMENT_BIDDING",  # Bid recommendations for campaign placements such as top of search, rest of search etc.
    "SHOPPER_COHORT",  # Bid adjustment recommendations for the shopper cohorts (audiences) attached to the campaign.
]
"""
Type of recommendations requested.

Supported values:
- `BIDDING_STRATEGY`: Recommendation for the campaign bidding strategy.
- `KEYWORD`: Recommendations related to campaign keywords targeting.
- `KEYWORD_GROUP`: Recommendation related to Keyword groups. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords.
- `BUDGET_STRATEGY`: Recommendation for the campaign budget.
- `PLACEMENT_BIDDING`: Bid recommendations for campaign placements such as top of search, rest of search etc.
- `SHOPPER_COHORT`: Bid adjustment recommendations for the shopper cohorts (audiences) attached to the campaign.
"""


type ShopperCohortBiddingRecommendationAction = Literal["ADD", "REMOVE", "UPDATE"]
"""
Recommended action for shopper cohort bidding.
"""


type ShopperCohortBiddingRecommendationShopperCohortType = Literal["AUDIENCE_SEGMENT"]
"""
Type of shopper cohort.
"""


type TargetingGroupBidRecommendationAction = Literal[
    "ADD",
    "DECREASE",
    "INCREASE",
    "REMOVE",
]
"""
Type of suggested action.
"""


type TargetingGroupBidRecommendationTargetingGroupExpression = Literal[
    "CLOSE_MATCH",  # This will show your ad to shoppers who use search terms closely related to your products.
    "COMPLEMENTS",  # This will show your ad to shoppers who view the detail pages of products that complement your product.
    "LOOSE_MATCH",  # This will show your ad to shoppers who use search terms loosely related to your products.
    "SUBSTITUTES",  # This will show your ad to shoppers who use detail pages of products similar to yours.
]
"""
The type of targeting group expression.

Supported values:
- `LOOSE_MATCH`: This will show your ad to shoppers who use search terms loosely related to your products.
- `CLOSE_MATCH`: This will show your ad to shoppers who use search terms closely related to your products.
- `COMPLEMENTS`: This will show your ad to shoppers who view the detail pages of products that complement your product.
- `SUBSTITUTES`: This will show your ad to shoppers who use detail pages of products similar to yours.
"""


class AudienceSegment(LenientModel):
    audienceId: str = Field(description="Unique identifier for the audience segment.")
    audienceSegmentType: AudienceSegmentAudienceSegmentType | str = Field(description="Type of audience segment.")


class BiddingStrategyRecommendation(LenientModel):
    """Contains suggested recommendation for the campaign bidding strategy."""

    action: BiddingStrategyRecommendationAction | str | None = Field(
        default=None, description="Type of suggested action."
    )
    suggestedBiddingStrategy: BiddingStrategyRecommendationSuggestedBiddingStrategy | str | None = Field(
        default=None,
        description="""
The suggested bidding strategy value for the campaign.

Supported values:
- `LEGACY_FOR_SALES`: Dynamic bids - down only | Lowers your bids in real time when your ad may be less likely to convert to a sale. Campaigns created before the release of the bidding controls feature used this setting by default.
- `AUTO_FOR_SALES`: Dynamic bids - up and down | Increases or decreases your bids in real time by a maximum of 100%. With this setting bids increase when your ad is more likely to convert to a sale, and bids decrease when less likely to convert to a sale.
- `MANUAL`: Fixed bid | Uses your exact bid and any placement adjustments you set, and is not subject to dynamic bidding.
""",
    )


class BudgetRecommendation(LenientModel):
    """Contains suggested recommendation for the campaign budget."""

    action: BudgetRecommendationAction | str | None = Field(default=None, description="Type of suggested action.")
    suggestedBudget: float | None = Field(default=None, description="The suggested budget value for the campaign.")


class Campaign(StrictModel):
    campaignId: str = Field(description="The identifier of the campaign.")
    recommendationType: RecommendationType = Field(description="""
Supported values:
- `BIDDING_STRATEGY`: Recommendation for the campaign bidding strategy.
- `KEYWORD`: Recommendations related to campaign keywords targeting.
- `KEYWORD_GROUP`: Recommendation related to Keyword groups. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords.
- `BUDGET_STRATEGY`: Recommendation for the campaign budget.
- `PLACEMENT_BIDDING`: Bid recommendations for campaign placements such as top of search, rest of search etc.
- `SHOPPER_COHORT`: Bid adjustment recommendations for the shopper cohorts (audiences) attached to the campaign.
""")


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

    action: KeywordTargetingRecommendationAction | str | None = Field(
        default=None, description="Type of action for the keyword targeting."
    )
    adGroupId: str | None = Field(default=None, description="The ad group identifier.")
    keywordId: str | None = Field(default=None, description="The identifier of the keyword targeting.")
    keywordText: str | None = Field(default=None, description="The keyword text.")
    matchType: KeywordTargetingRecommendationMatchType | str | None = Field(
        default=None,
        description="Keyword match type. | Value | Description | | --- | --- | | `BROAD` | Use BROAD to broadly match your keyword targeting ads with search queries.| | `EXACT` | Use EXACT to exactly match your keyword targeting ads with search queries.| | `PHRASE` | Use PHRASE to match your keyword targeting ads with search phrases.| | `GROUP` | Use GROUP to match your keyword targeting ads with keyword group. |",
    )
    suggestedBid: float | None = Field(
        default=None, description="The suggested bid value associated with this keyword targeting clause."
    )


class PlacementBiddingRecommendation(LenientModel):
    """Contains suggested recommendation for a placement bid adjustment."""

    action: PlacementBiddingRecommendationAction | str | None = Field(
        default=None, description="Type of suggested action."
    )
    incrementalImpressionsLowerPercent: int | None = Field(
        default=None,
        description="Lower bound of the estimated incremental impressions that could be gained if this optimization used",
    )
    incrementalImpressionsUpperPercent: int | None = Field(
        default=None,
        description="Upper bound of the estimated incremental impressions that could be gained if this optimization used",
    )
    placementType: PlacementBiddingRecommendationPlacementType | str | None = Field(
        default=None, description="The placement type."
    )
    suggestedBidAdjustment: float | None = Field(
        default=None, description="The suggested bid adjustment percent value for this placement type."
    )


class Recommendation(LenientModel):
    campaignId: str = Field(description="The identifier of the campaign.")
    forecastEstimates: ForecastEstimates | None = Field(default=None)
    recommendationDetails: RecommendationDetails
    recommendationType: RecommendationType | str = Field(description="""
Supported values:
- `BIDDING_STRATEGY`: Recommendation for the campaign bidding strategy.
- `KEYWORD`: Recommendations related to campaign keywords targeting.
- `KEYWORD_GROUP`: Recommendation related to Keyword groups. Keyword Groups is a new control for Amazon Ads Sponsored Products keyword-based campaigns that enables advertisers to reach relevant audiences through a collection of keywords.
- `BUDGET_STRATEGY`: Recommendation for the campaign budget.
- `PLACEMENT_BIDDING`: Bid recommendations for campaign placements such as top of search, rest of search etc.
- `SHOPPER_COHORT`: Bid adjustment recommendations for the shopper cohorts (audiences) attached to the campaign.
""")


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
    action: ShopperCohortBiddingRecommendationAction | str = Field(
        description="Recommended action for shopper cohort bidding."
    )
    audienceSegments: list[AudienceSegment] = Field(
        min_length=1, max_length=10, description="List of audience segments for this recommendation."
    )
    percentage: int = Field(ge=0, le=900, description="Bid adjustment percentage (basis points, e.g., 900 = 9%).")
    shopperCohortType: ShopperCohortBiddingRecommendationShopperCohortType | str = Field(
        description="Type of shopper cohort."
    )


class TargetingGroupBidRecommendation(LenientModel):
    """Contains suggested recommendation for the auto targeting group."""

    action: TargetingGroupBidRecommendationAction | str | None = Field(
        default=None, description="Type of suggested action."
    )
    adGroupId: str | None = Field(default=None, description="The ad group identifier.")
    suggestedBid: float | None = Field(
        default=None, description="The suggested bid value associated with this targeting."
    )
    targetId: str | None = Field(default=None, description="The target identifier.")
    targetingGroupExpression: TargetingGroupBidRecommendationTargetingGroupExpression | str | None = Field(
        default=None,
        description="""
The type of targeting group expression.

Supported values:
- `LOOSE_MATCH`: This will show your ad to shoppers who use search terms loosely related to your products.
- `CLOSE_MATCH`: This will show your ad to shoppers who use search terms closely related to your products.
- `COMPLEMENTS`: This will show your ad to shoppers who view the detail pages of products that complement your product.
- `SUBSTITUTES`: This will show your ad to shoppers who use detail pages of products similar to yours.
""",
    )


__all__ = [
    "AudienceSegment",
    "AudienceSegmentAudienceSegmentType",
    "BiddingStrategyRecommendation",
    "BiddingStrategyRecommendationAction",
    "BiddingStrategyRecommendationSuggestedBiddingStrategy",
    "BudgetRecommendation",
    "BudgetRecommendationAction",
    "Campaign",
    "CampaignRecommendation",
    "ForecastEstimates",
    "GetCampaignRecommendationsRequestV2",
    "GetCampaignRecommendationsResponse",
    "GetCampaignRecommendationsResponseV2",
    "KeywordTargetingRecommendation",
    "KeywordTargetingRecommendationAction",
    "KeywordTargetingRecommendationMatchType",
    "PlacementBiddingRecommendation",
    "PlacementBiddingRecommendationAction",
    "PlacementBiddingRecommendationPlacementType",
    "Recommendation",
    "RecommendationDetails",
    "RecommendationType",
    "SevenDaysEstimatedOpportunities",
    "ShopperCohortBiddingRecommendation",
    "ShopperCohortBiddingRecommendationAction",
    "ShopperCohortBiddingRecommendationShopperCohortType",
    "TargetingGroupBidRecommendation",
    "TargetingGroupBidRecommendationAction",
    "TargetingGroupBidRecommendationTargetingGroupExpression",
]
