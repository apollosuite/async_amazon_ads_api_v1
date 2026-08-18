"""Auto-generated models for Multi Country Theme-based bid recommendations from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    BidAnalyses,
    BidAnalysesPerPlacement,
    BidAnalysis,
    BidAnalysisImpactMetrics,
    BidAnalysisType,
    Theme,
)


class MultiCountryTargetingExpressionType(StrEnum):
    CLOSE_MATCH = "CLOSE_MATCH"
    COMPLEMENTS = "COMPLEMENTS"
    KEYWORD_BROAD_MATCH = "KEYWORD_BROAD_MATCH"
    KEYWORD_EXACT_MATCH = "KEYWORD_EXACT_MATCH"
    KEYWORD_GROUP = "KEYWORD_GROUP"
    KEYWORD_PHRASE_MATCH = "KEYWORD_PHRASE_MATCH"
    LOOSE_MATCH = "LOOSE_MATCH"
    PAT_ASIN = "PAT_ASIN"
    PAT_CATEGORY = "PAT_CATEGORY"
    PAT_CATEGORY_REFINEMENT = "PAT_CATEGORY_REFINEMENT"
    SUBSTITUTES = "SUBSTITUTES"


class MultiCountryBidAnalysesPerTargetingExpression(LenientModel):
    countryBidAnalyses: dict[str, BidAnalysesPerPlacement] | None = Field(default=None)
    expression: MultiCountryTargetingExpression


class MultiCountryBidRecommendationError(LenientModel):
    code: str | None = Field(default=None, description="Machine readable error code.")
    countryCodes: list[str] | None = Field(default=None, description="Countries where error have occurred")
    message: str | None = Field(default=None, description="Human readable 1 liner error message")


class MultiCountryBidRecommendationPerTargetingExpression(LenientModel):
    countrySuggestedBids: dict[str, SuggestedBidValues]
    expression: MultiCountryTargetingExpression


class MultiCountryTargetingExpression(LenientModel):
    """The targeting expression. The `type` property specifies the targeting option. Use `CLOSE_MATCH` to match your auto targeting ads closely to the specified value. Use `LOOSE_MATCH` to match your auto targeting ads broadly to the specified value. Use `SUBSTITUTES` to display your auto targeting ads along with substitutable products. Use `COMPLEMENTS` to display your auto targeting ads along with affiliated products. Use `KEYWORD_BROAD_MATCH` to broadly match your keyword targeting ads with search queries. Use `KEYWORD_EXACT_MATCH` to exactly match your keyword targeting ads with search queries. Use `KEYWORD_PHRASE_MATCH` to match your keyword targeting ads with search phrases. your keyword targeting ads with search phrases. Use `PAT_ASIN` to match your product attribute targeting ads with product ASIN. Use `PAT_CATEGORY` to match your product attribute targeting ads with product category. Use `PAT_CATEGORY_REFINEMENT` to match your product attribute targeting ads with product attribute, including brand, price, rating, prime shipping eligible, age range and genre. Use `KEYWORD_GROUP` to match your keyword targeting ads with keyword group."""

    countryValues: dict[str, str] | None = Field(default=None)
    type: Annotated[MultiCountryTargetingExpressionType | str, lenient_enum(MultiCountryTargetingExpressionType)]


class MultiCountryThemeBasedBidRecommendation(LenientModel):
    bidAnalysesForTargetingExpressions: list[MultiCountryBidAnalysesPerTargetingExpression] | None = Field(
        default=None, description="The bid analyses for targeting expressions listed in the request."
    )
    bidRecommendationsForTargetingExpressions: list[MultiCountryBidRecommendationPerTargetingExpression] = Field(
        description="The bid recommendations for targeting expressions listed in the request."
    )
    theme: Annotated[Theme | str, lenient_enum(Theme)]


class MultiCountryThemeBasedBidRecommendationResponse(LenientModel):
    """A list of multi country bid recommendation themes and associated bid recommendations."""

    bidRecommendations: list[MultiCountryThemeBasedBidRecommendation] = Field(min_length=0, max_length=2)
    errors: list[MultiCountryBidRecommendationError] | None = Field(
        default=None, description="List of errors occurred while processing multi country request."
    )


class SuggestedBidValues(LenientModel):
    pass


__all__ = [
    "BidAnalyses",
    "BidAnalysesPerPlacement",
    "BidAnalysis",
    "BidAnalysisImpactMetrics",
    "BidAnalysisType",
    "MultiCountryBidAnalysesPerTargetingExpression",
    "MultiCountryBidRecommendationError",
    "MultiCountryBidRecommendationPerTargetingExpression",
    "MultiCountryTargetingExpression",
    "MultiCountryTargetingExpressionType",
    "MultiCountryThemeBasedBidRecommendation",
    "MultiCountryThemeBasedBidRecommendationResponse",
    "SuggestedBidValues",
    "Theme",
]
