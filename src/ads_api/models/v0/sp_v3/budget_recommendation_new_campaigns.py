"""Auto-generated models for Budget Recommendation New Campaigns from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class AdGroup(StrictModel):
    adGroupId: str | None = Field(default=None, description="The ad group identifier.")
    asins: list[str] = Field(min_length=1, max_length=50, description="The list of ad ASINs in the ad group.")
    targetingExpressions: list[TargetingExpression] = Field(
        min_length=1, max_length=100, description="The list of targeting expressions. Maximum of 100 per request."
    )


class Adjustment(StrictModel):
    placementAdjustment: PlacementAdjustment | None = Field(default=None)


class Benchmark(LenientModel):
    """Forecasted impact metrics for next 7 days or during special days."""

    benchmarkStatus: str | None = Field(
        default=None,
        description="Specifies the processing status of the benchmark. Success - If all fields in values property (impressions, clicks, conversions) have all non-null values. Failed - If all fields in values property have all null values. Partial - If some of the fields (impressions, clicks, or conversions) in values property have null values.",
    )
    values: Values | None = Field(default=None)


class Bidding(StrictModel):
    """The bidding control configuration for the new campaign."""

    adjustments: list[Adjustment] | None = Field(
        default=None, min_length=0, max_length=2, description="Placement adjustment configuration for the campaign."
    )
    strategy: str = Field(
        description="The bidding strategy selected for the campaign. Use LEGACY_FOR_SALES to lower your bid in real time when your ad may be less likely to convert to a sale. Use AUTO_FOR_SALES to increase your bid in real time when your ad may be more likely to convert to a sale or lower your bid when less likely to convert to a sale. Use MANUAL to use your exact bid along with any manual adjustments."
    )


class Clicks(LenientModel):
    """Clicks benchmark."""

    lower: int | None = Field(default=None, description="lower bound.")
    upper: int | None = Field(default=None, description="upper bound.")


class Conversions(LenientModel):
    """Conversions benchmark."""

    lower: int | None = Field(default=None, description="lower bound.")
    upper: int | None = Field(default=None, description="upper bound.")


class Impressions(LenientModel):
    """Impressions benchmark."""

    lower: int | None = Field(default=None, description="lower bound.")
    upper: int | None = Field(default=None, description="upper bound.")


class InitialBudgetRecommendationRequest(StrictModel):
    adGroups: list[AdGroup] = Field(
        min_length=1, max_length=1, description="The ad group information for this new campaign."
    )
    bidding: Bidding
    endDate: str | None = Field(default=None, description="The end date of the campaign in YYYYMMDD format.")
    startDate: str | None = Field(default=None, description="The start date of the campaign in YYYYMMDD format.")
    targetingType: str = Field(description="Specifies the targeting type.")


class InitialBudgetRecommendationResponse(LenientModel):
    benchmark: Benchmark
    dailyBudget: float = Field(
        description="Recommended daily budget for the new campaign. Note: value -1 means we don’t have enough information to provide a recommendation."
    )
    recommendationId: str | None = Field(default=None, description="Unique identifier for each recommendation.")
    specialEvents: list[SpecialEvent] = Field(
        min_length=0,
        max_length=5,
        description="A list of special events around the start and end date of the campaign.",
    )


class PlacementAdjustment(StrictModel):
    """Specifies bid adjustments based on the placement location. Use `PLACEMENT_TOP` for the top of the search page. Use `PLACEMENT_REST_OF_SEARCH` for the rest of the search page. Use `PLACEMENT_PRODUCT_PAGE` for a product page."""

    percentage: int | None = Field(default=None, ge=0, le=900)
    predicate: str | None = Field(default=None)


class SpecialEvent(LenientModel):
    benchmark: Benchmark | None = Field(default=None)
    budgetModifier: float | None = Field(
        default=None, description="Deprecated. The factor used to boost the recommended budget."
    )
    dailyBudget: float | None = Field(
        default=None, description="Recommended daily budget for the new campaign during the special event period."
    )
    endDate: str | None = Field(default=None, description="The end date of the special event in YYYYMMDD format.")
    eventKey: str | None = Field(default=None, description="The key of the special event.")
    eventName: str | None = Field(default=None, description="The name of the special event.")
    startDate: str | None = Field(default=None, description="The start date of the special event in YYYYMMDD format.")


class TargetingExpression(StrictModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto targeting ads broadly to the specified value. Use `SUBSTITUTES` to display your auto targeting ads along with substitutable products. Use `COMPLEMENTS` to display your auto targeting ads along with affiliated products. Use `KEYWORD_BROAD_MATCH` to broadly match your keyword targeting ads with search queries. Use `KEYWORD_EXACT_MATCH` to exactly match your keyword targeting ads with search queries. Use `KEYWORD_PHRASE_MATCH` to match your keyword targeting ads with search phrases. your keyword targeting ads with search phrases."""

    type: str
    value: str | None = Field(default=None, description="The targeting expression value.")


class Values(LenientModel):
    """Metrics benchmark values."""

    clicks: Clicks | None = Field(default=None)
    conversions: Conversions | None = Field(default=None)
    impressions: Impressions | None = Field(default=None)


__all__ = [
    "AdGroup",
    "Adjustment",
    "Benchmark",
    "Bidding",
    "Clicks",
    "Conversions",
    "Impressions",
    "InitialBudgetRecommendationRequest",
    "InitialBudgetRecommendationResponse",
    "PlacementAdjustment",
    "SpecialEvent",
    "TargetingExpression",
    "Values",
]
