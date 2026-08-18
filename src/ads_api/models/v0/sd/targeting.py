"""Auto-generated models for Targeting from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    BaseTargetingClause,
    CampaignId,
    ContentTargetingPredicate,
    TargetId,
    TargetingPredicate,
    TargetingPredicateBase,
    TargetingPredicateNested,
    TargetResponse,
)


class BaseTargetingClauseOut(LenientModel):
    state: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )


class ContentTargetingPredicateOut(LenientModel):
    """A predicate to match against in the content targeting expression."""

    type: str | None = Field(default=None)
    value: str | None = Field(
        default=None,
        description="""
The value to be targeted.

The following table shows all possible values of the `contentCategorySameAs` predicate.
""",
    )


class CreateTargetingClause(StrictModel):
    state: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    adGroupId: AdGroupId
    expressionType: str = Field(description="Tactic T00020 ad groups only allow manual targeting.")
    expression: CreateTargetingExpression = Field(description="The targeting expression to match against.")


class CreateTargetingExpression(StrictModel):
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


class TargetingClause(LenientModel):
    state: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    expressionType: str | None = Field(
        default=None, description="Tactic T00020 & T00030 ad groups should use 'manual' targeting."
    )
    expression: TargetingExpression | None = Field(
        default=None, description="The targeting expression to match against."
    )
    resolvedExpression: TargetingExpression | None = Field(
        default=None, description="The resolved targeting expression."
    )


class TargetingClauseEx(LenientModel):
    targetId: float | None = Field(default=None)
    adGroupId: float | None = Field(default=None)
    campaignId: float | None = Field(default=None)
    state: str | None = Field(default=None)
    expressionType: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        description="If a value for `bid` is specified, it overrides the current adGroup bid. When using vcpm costType. $1 is the minimum bid for vCPM. Note that this field is ignored for negative targeting clauses.",
    )
    expression: TargetingExpression | None = Field(default=None)
    resolvedExpression: TargetingExpression | None = Field(default=None)
    servingStatus: str | None = Field(default=None, description="The status of the target.")
    creationDate: int | None = Field(default=None, description="Epoch date the target was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch date of the last update to any property associated with the target."
    )


class TargetingExpression(LenientModel):
    """The targeting expression to match against.

    ------- Applicable to contextual or content targeting (T00020) -------
    * A 'TargetingExpression' in a contextual targeting campaign can contain 'TargetingPredicate' or 'ContentTargetingPredicate' components.
    * Contextual expressions must specify either a category predicate or an ASIN predicate, but never both.
    * Only one category may be specified per targeting expression.
    * Only one brand may be specified per targeting expression.
    * Only one asin may be specified per targeting expression.
    * To exclude a brand from a targeting expression you must create a negative targeting expression in the same ad group as the positive targeting expression.

    ------- Applicable to audiences or contextual targeting (T00030) -------
    * A 'TargetingExpression' in a audiences or contextual campaign can contain any target, including 'TargetingPredicate', 'ContentTargetingPredicate', or 'TargetingPredicateNested'.
    """

    pass


class TargetingPredicateBaseOut(LenientModel):
    """A predicate to match against inside the TargetingPredicateNested component (only applicable to audience targeting - T00030).

    * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system.
    * Brand, price, and review predicates are optional and may only be specified if category is also specified.
    * Review predicates accept numbers between 0 and 5 and are inclusive.
    * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    * The 'exactProduct', 'similarProduct', 'relatedProduct', 'negative', and 'audiencesLikelyInterestedInAd' types do not utilize the value field.
    * The only type currently applicable to Amazon Audiences targeting is 'audienceSameAs'.
    * A 'relatedProduct' TargetingPredicateBase will Target an audience that has purchased a related product in the past 7,14,30,60,90,180, or 365 days.
    * The 'audiencesLikelyInterestedInAd' type is only supported when using landingPageType of OFF_AMAZON_LINK."""

    type: str | None = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class TargetingPredicateLegacy(LenientModel):
    type: str | None = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")
    eventType: str | None = Field(
        default=None,
        description="""
The type of event that the value applies to. Only available for similarProduct and exactProduct currently.
* views event type corresponds to a customer who viewed the detail page of the product(s).
""",
    )


class TargetingPredicateNestedOut(LenientModel):
    """A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).

    * For manual ASIN-grain targeting, the value array must contain only, 'exactProduct', 'similarProduct', 'relatedProduct' and 'lookback' TargetingPredicateBase components. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For Amazon Audiences targeting, the TargetingPredicateNested type should be set to 'audience' and the value array should include one TargetingPredicateBase component with type set to 'audienceSameAs'.
    """

    type: str | None = Field(default=None)
    value: list[TargetingPredicateBaseOut] | None = Field(default=None)


class TargetingPredicateOut(LenientModel):
    """A predicate to match against in the targeting expression (only applicable to contextual targeting - T00020).

    * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system.
    * Brand, price, and review predicates are optional and may only be specified if category is also specified.
    * Review predicates accept numbers between 0 and 5 and are inclusive.
    * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    """

    type: str | None = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class UpdateTargetingClause(StrictModel):
    state: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    targetId: TargetId


__all__ = [
    "AdGroupId",
    "BaseTargetingClause",
    "BaseTargetingClauseOut",
    "CampaignId",
    "ContentTargetingPredicate",
    "ContentTargetingPredicateOut",
    "CreateTargetingClause",
    "CreateTargetingExpression",
    "TargetId",
    "TargetResponse",
    "TargetingClause",
    "TargetingClauseEx",
    "TargetingExpression",
    "TargetingPredicate",
    "TargetingPredicateBase",
    "TargetingPredicateBaseOut",
    "TargetingPredicateLegacy",
    "TargetingPredicateNested",
    "TargetingPredicateNestedOut",
    "TargetingPredicateOut",
    "UpdateTargetingClause",
]
