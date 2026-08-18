"""Auto-generated models for Bid Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    SDASIN,
    SDGoalProduct,
)


class SDBidOptimizationV32(StrEnum):
    """
    Determines what the recommended bids will be optimized for.
    """

    reach = "reach"
    clicks = "clicks"
    conversions = "conversions"


class SDCostTypeV31(StrEnum):
    """
    Determines what performance metric the bid recommendations will be optimized for.
    """

    cpc = "cpc"
    vcpm = "vcpm"


class SDCreativeType(StrEnum):
    """
    The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. Only supports one type (VIDEO or IMAGE) at a time.
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class SDBidRecommendationV31(LenientModel):
    """A recommended bid range to use for a target."""

    rangeLower: float = Field(description="The lowest recommended bid to use to win an ad placement for this target.")
    rangeUpper: float = Field(description="The highest recommended bid to use to win an ad placement for this target.")
    recommended: float = Field(description="The recommended bid to use to win an ad placement for this target.")


class SDContentTargetingPredicateV31(StrictModel):
    """A predicate to match against in the content targeting expression."""

    type: str
    value: str = Field(description="The value to be targeted.")


class SDTargetExpressionV31(StrictModel):
    pass


class SDTargetExpressionV32(StrictModel):
    pass


class SDTargetingBidRecommendationsRequestV31(StrictModel):
    """Request for targeting bid recommendations."""

    products: list[SDGoalProduct] | None = Field(
        default=None,
        min_length=0,
        max_length=10000,
        description="A list of products to tailor bid recommendations for category and audience based targeting clauses.",
    )
    targetingClauses: list[dict[str, Any]] = Field(
        min_length=1, max_length=100, description="A list of targeting clauses to receive bid recommendations for."
    )


class SDTargetingBidRecommendationsRequestV32(StrictModel):
    """Request for targeting bid recommendations."""

    products: list[SDGoalProduct] | None = Field(
        default=None,
        min_length=0,
        max_length=10000,
        description="A list of products to tailor bid recommendations for category and audience based targeting clauses.",
    )
    bidOptimization: Annotated[SDBidOptimizationV32, lenient_enum(SDBidOptimizationV32)]
    costType: Annotated[SDCostTypeV31, lenient_enum(SDCostTypeV31)]
    targetingClauses: list[dict[str, Any]] = Field(
        min_length=1, max_length=100, description="A list of targeting clauses to receive bid recommendations for."
    )


class SDTargetingBidRecommendationsRequestV33(StrictModel):
    """Request for targeting bid recommendations."""

    products: list[SDGoalProduct] | None = Field(
        default=None,
        min_length=0,
        max_length=10000,
        description="A list of products to tailor bid recommendations for category and audience based targeting clauses.",
    )
    bidOptimization: Annotated[SDBidOptimizationV32, lenient_enum(SDBidOptimizationV32)]
    costType: Annotated[SDCostTypeV31, lenient_enum(SDCostTypeV31)]
    creativeType: Annotated[SDCreativeType, lenient_enum(SDCreativeType)] | None = Field(default=None)
    targetingClauses: list[dict[str, Any]] = Field(
        min_length=1, max_length=100, description="A list of targeting clauses to receive bid recommendations for."
    )


class SDTargetingBidRecommendationsRequestV34(StrictModel):
    """Request for targeting bid recommendations."""

    products: list[SDGoalProduct] | None = Field(
        default=None,
        min_length=0,
        max_length=10000,
        description="""
A list of products to tailor bid recommendations for category and audience based targeting clauses.
This array must contain consistent fields of either asins or landing pages (when linking to other pages), these cannot be mixed for any given request.
If landingPageUrl is used, only one item is allowed for the list.
""",
    )
    bidOptimization: Annotated[SDBidOptimizationV32, lenient_enum(SDBidOptimizationV32)]
    costType: Annotated[SDCostTypeV31, lenient_enum(SDCostTypeV31)]
    creativeType: Annotated[SDCreativeType, lenient_enum(SDCreativeType)] | None = Field(default=None)
    targetingClauses: list[dict[str, Any]] = Field(
        min_length=1, max_length=100, description="A list of targeting clauses to receive bid recommendations for."
    )


class SDTargetingBidRecommendationsResponseItemFailureV31Result(LenientModel):
    """Failed bid recommendation response."""

    code: str = Field(description="The HTTP status code of this item.")
    details: str = Field(description="A human-readable description of this item on error.")


class SDTargetingBidRecommendationsResponseItemSuccessV31(LenientModel):
    """A recommended bid range to use for a target."""

    code: str = Field(description="The HTTP status code of this item.")
    rangeLower: float = Field(description="The lowest recommended bid to use to win an ad placement for this target.")
    rangeUpper: float = Field(description="The highest recommended bid to use to win an ad placement for this target.")
    recommended: float = Field(description="The recommended bid to use to win an ad placement for this target.")


class SDTargetingBidRecommendationsResponseV31(LenientModel):
    """Response to a request for targeting bid recommendations."""

    costType: Annotated[SDCostTypeV31 | str, lenient_enum(SDCostTypeV31)]
    bidRecommendations: dict[str, Any] = Field(min_length=1, max_length=100)


class SDTargetingBidRecommendationsResponseV32(LenientModel):
    """Response to a request for targeting bid recommendations."""

    bidOptimization: Annotated[SDBidOptimizationV32 | str, lenient_enum(SDBidOptimizationV32)]
    costType: Annotated[SDCostTypeV31 | str, lenient_enum(SDCostTypeV31)]
    bidRecommendations: dict[str, Any] = Field(min_length=1, max_length=100)


class SDTargetingClauseV31(StrictModel):
    """The targeting clause"""

    expressionType: str = Field(description="Tactic T00020 ad groups only allow manual targeting.")
    expression: SDTargetingExpressionV31


class SDTargetingClauseV32(StrictModel):
    """The targeting clause"""

    expressionType: str = Field(description="Tactic T00020 ad groups only allow manual targeting.")
    expression: SDTargetingExpressionV32


class SDTargetingExpressionV31(StrictModel):
    """The targeting expression to match against.

    ------- Applicable to contextual targeting (T00020) -------
    * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicate' components.
    * Expressions must specify either a category predicate or an ASIN predicate, but never both.
    * Only one category may be specified per targeting expression.
    * Only one brand may be specified per targeting expression.
    * Only one asin may be specified per targeting expression.
    * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.

    ------- Applicable to audiences or contextual targeting (T00030) -------
    * A 'TargetingExpression' in a audiences or contextual campaign can contain any target, including 'TargetingPredicate', 'ContentTargetingPredicate', or 'TargetingPredicateNested'.
    """

    pass


class SDTargetingExpressionV32(StrictModel):
    """The targeting expression to match against.

    ------- Applicable to contextual targeting (T00020) -------
    * A 'TargetingExpression' in a contextual targeting campaign can only contain 'TargetingPredicate' or 'ContentTargetingPredicate' components.
    * Expressions must specify either a category predicate or an ASIN predicate, but never both.
    * Only one category may be specified per targeting expression.
    * Only one brand may be specified per targeting expression.
    * Only one asin may be specified per targeting expression.
    * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.

    ------- Applicable to audiences or contextual targeting (T00030) -------
    * A 'TargetingExpression' in a audiences or contextual campaign can contain any target, including 'TargetingPredicate', 'ContentTargetingPredicate', or 'TargetingPredicateNested'.
    """

    pass


class SDTargetingPredicateBaseV31(StrictModel):
    """A predicate to match against inside the TargetingPredicateNested component (only applicable to audience targeting - T00030).

    * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system.
    * Brand, price, and review predicates are optional and may only be specified if category is also specified.
    * Review predicates accept numbers between 0 and 5 and are inclusive.
    * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    * The exactProduct, similarProduct, relatedProduct, and negative types do not utilize the value field.
    * The only type currently applicable to Amazon Audiences targeting is 'audienceSameAs'."""

    type: str
    value: str | None = Field(default=None, description="The value to be targeted.")


class SDTargetingPredicateNestedV31(StrictModel):
    """A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).

    * For manual ASIN-grain targeting, the value array must contain only, 'exactProduct', 'similarProduct', 'relatedProduct' and 'lookback' TargetingPredicateBase components. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements.
    * For Amazon Audiences targeting, the TargetingPredicateNested type should be set to 'audience' and the value array should include one TargetingPredicateBase component with type set to 'audienceSameAs'.
    """

    type: str
    value: list[SDTargetingPredicateBaseV31]


class SDTargetingPredicateV31(StrictModel):
    """A predicate to match against in the Targeting Expression (only applicable to contextual targeting - T00020).

    * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system.
    * Brand, price, and review predicates are optional and may only be specified if category is also specified.
    * Review predicates accept numbers between 0 and 5 and are inclusive.
    * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    """

    type: str
    value: str | None = Field(default=None, description="The value to be targeted.")


__all__ = [
    "SDASIN",
    "SDBidOptimizationV32",
    "SDBidRecommendationV31",
    "SDContentTargetingPredicateV31",
    "SDCostTypeV31",
    "SDCreativeType",
    "SDGoalProduct",
    "SDTargetExpressionV31",
    "SDTargetExpressionV32",
    "SDTargetingBidRecommendationsRequestV31",
    "SDTargetingBidRecommendationsRequestV32",
    "SDTargetingBidRecommendationsRequestV33",
    "SDTargetingBidRecommendationsRequestV34",
    "SDTargetingBidRecommendationsResponseItemFailureV31Result",
    "SDTargetingBidRecommendationsResponseItemSuccessV31",
    "SDTargetingBidRecommendationsResponseV31",
    "SDTargetingBidRecommendationsResponseV32",
    "SDTargetingClauseV31",
    "SDTargetingClauseV32",
    "SDTargetingExpressionV31",
    "SDTargetingExpressionV32",
    "SDTargetingPredicateBaseV31",
    "SDTargetingPredicateNestedV31",
    "SDTargetingPredicateV31",
]
