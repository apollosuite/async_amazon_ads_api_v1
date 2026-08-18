"""Auto-generated models for Theme-based bid recommendations from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models.v0._shared import (
    BidAnalyses,
    BidAnalysesPerPlacement,
    BidAnalysis,
    BidAnalysisImpactMetrics,
    ImpactMetric,
    ImpactMetrics,
    RangeMetricValue,
    Theme,
)


class BidAnalysesPerTargetingExpression(LenientModel):
    bidAnalyses: BidAnalysesPerPlacement
    targetingExpression: TargetingExpressionV4


class BidRecommendationPerTargetingExpression(LenientModel):
    bidValues: list[BidValue] = Field(max_length=3)
    targetingExpression: TargetingExpression


class BidRecommendationPerTargetingExpressionV4(LenientModel):
    bidValues: list[BidValue] = Field(max_length=3)
    targetingExpression: TargetingExpressionV4


class BidRecommendationPerTargetingExpressionV5(LenientModel):
    bidValues: list[BidValue] = Field(max_length=3)
    suggestedBidImpactMetrics: dict[str, Any] | None = Field(default=None)
    targetingExpression: TargetingExpressionV4


class BidValue(LenientModel):
    """Bid value of the bid recommendations."""

    suggestedBid: float = Field(ge=0, description="The suggested bid.")


class TargetingExpression(LenientModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto targeting ads broadly to the specified value. Use `SUBSTITUTES` to display your auto targeting ads along with substitutable products. Use `COMPLEMENTS` to display your auto targeting ads along with affiliated products. Use `KEYWORD_BROAD_MATCH` to broadly match your keyword targeting ads with search queries. Use `KEYWORD_EXACT_MATCH` to exactly match your keyword targeting ads with search queries. Use `KEYWORD_PHRASE_MATCH` to match your keyword targeting ads with search phrases. your keyword targeting ads with search phrases."""

    type: (
        Literal[
            "CLOSE_MATCH",
            "COMPLEMENTS",
            "KEYWORD_BROAD_MATCH",
            "KEYWORD_EXACT_MATCH",
            "KEYWORD_PHRASE_MATCH",
            "LOOSE_MATCH",
            "SUBSTITUTES",
        ]
        | str
    )
    value: str | None = Field(default=None, description="The targeting expression value.")


class TargetingExpressionV4(LenientModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto targeting ads broadly to the specified value. Use `SUBSTITUTES` to display your auto targeting ads along with substitutable products. Use `COMPLEMENTS` to display your auto targeting ads along with affiliated products. Use `KEYWORD_BROAD_MATCH` to broadly match your keyword targeting ads with search queries. Use `KEYWORD_EXACT_MATCH` to exactly match your keyword targeting ads with search queries. Use `KEYWORD_PHRASE_MATCH` to match your keyword targeting ads with search phrases. your keyword targeting ads with search phrases. Use `PAT_ASIN` to match your product attribute targeting ads with product ASIN. Use `PAT_CATEGORY` to match your product attribute targeting ads with product category. Use `PAT_CATEGORY_REFINEMENT` to match your product attribute targeting ads with product attribute, including brand, price, rating, prime shipping eligible, age range and genre. Use `KEYWORD_GROUP` to match your keyword targeting ads with keyword group."""

    type: (
        Literal[
            "CLOSE_MATCH",
            "COMPLEMENTS",
            "KEYWORD_BROAD_MATCH",
            "KEYWORD_EXACT_MATCH",
            "KEYWORD_GROUP",
            "KEYWORD_PHRASE_MATCH",
            "LOOSE_MATCH",
            "PAT_ASIN",
            "PAT_CATEGORY",
            "PAT_CATEGORY_REFINEMENT",
            "SUBSTITUTES",
        ]
        | str
    )
    value: str | None = Field(default=None, description="The targeting expression value.")


class ThemeBasedBidRecommendation(LenientModel):
    bidRecommendationsForTargetingExpressions: list[BidRecommendationPerTargetingExpression] = Field(
        description="The bid recommendations for targeting expressions listed in the request."
    )
    impactMetrics: ImpactMetrics | None = Field(default=None)
    theme: Theme | str


class ThemeBasedBidRecommendationResponse(LenientModel):
    """A list of bid recommendation themes and associated bid recommendations."""

    bidRecommendations: list[ThemeBasedBidRecommendation] = Field(max_length=2)


class ThemeBasedBidRecommendationResponseV4(LenientModel):
    """A list of bid recommendation themes and associated bid recommendations."""

    bidRecommendations: list[ThemeBasedBidRecommendationV4] = Field(max_length=2)


class ThemeBasedBidRecommendationResponseV5(LenientModel):
    """A list of bid recommendation themes and associated bid recommendations."""

    bidRecommendations: list[ThemeBasedBidRecommendationV5] = Field(max_length=2)


class ThemeBasedBidRecommendationV4(LenientModel):
    bidRecommendationsForTargetingExpressions: list[BidRecommendationPerTargetingExpressionV4] = Field(
        description="The bid recommendations for targeting expressions listed in the request."
    )
    theme: Theme | str


class ThemeBasedBidRecommendationV5(LenientModel):
    bidAnalysesForTargetingExpressions: list[BidAnalysesPerTargetingExpression] | None = Field(
        default=None, description="The bid analyses for targeting expressions listed in the request."
    )
    bidRecommendationsForTargetingExpressions: list[BidRecommendationPerTargetingExpressionV5] = Field(
        description="The bid recommendations for targeting expressions listed in the request."
    )
    theme: Theme | str


__all__ = [
    "BidAnalyses",
    "BidAnalysesPerPlacement",
    "BidAnalysesPerTargetingExpression",
    "BidAnalysis",
    "BidAnalysisImpactMetrics",
    "BidRecommendationPerTargetingExpression",
    "BidRecommendationPerTargetingExpressionV4",
    "BidRecommendationPerTargetingExpressionV5",
    "BidValue",
    "ImpactMetric",
    "ImpactMetrics",
    "RangeMetricValue",
    "TargetingExpression",
    "TargetingExpressionV4",
    "Theme",
    "ThemeBasedBidRecommendation",
    "ThemeBasedBidRecommendationResponse",
    "ThemeBasedBidRecommendationResponseV4",
    "ThemeBasedBidRecommendationResponseV5",
    "ThemeBasedBidRecommendationV4",
    "ThemeBasedBidRecommendationV5",
]
