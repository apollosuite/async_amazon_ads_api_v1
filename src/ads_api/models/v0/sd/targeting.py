"""Auto-generated models for Targeting from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

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
    state: Literal["enabled", "paused", "archived"] | str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )


class ContentTargetingPredicateOut(LenientModel):
    """A predicate to match against in the content targeting expression."""

    type: Literal["contentCategorySameAs"] | str | None = Field(default=None)
    value: str | None = Field(
        default=None,
        description="""
The value to be targeted.

The following table shows all possible values of the `contentCategorySameAs` predicate.
| Category              | Subcategory                             | Value                    |
|-----------------------|-----------------------------------------|--------------------------|
| Movies and Television | All Movies and Television               | amzn1.iab-content.SPSHQ5 |
| Movies and Television | Action or Adventure                     | amzn1.iab-content.325    |
| Movies and Television | Animation or Anime                      | amzn1.iab-content.641    |
| Movies and Television | Biographies                             | amzn1.iab-content.44     |
| Movies and Television | Comedy                                  | amzn1.iab-content.646    |
| Movies and Television | Documentary                             | amzn1.iab-content.332    |
| Movies and Television | Drama                                   | amzn1.iab-content.647    |
| Movies and Television | Factual                                 | amzn1.iab-content.648    |
| Movies and Television | Family                                  | amzn1.iab-content.645    |
| Movies and Television | Fantasy                                 | amzn1.iab-content.335    |
| Movies and Television | History                                 | amzn1.iab-content.EZWB7V |
| Movies and Television | Holiday                                 | amzn1.iab-content.649    |
| Movies and Television | Horror                                  | amzn1.iab-content.336    |
| Movies and Television | Lifestyle                               | amzn1.iab-content.TIFQA5 |
| Movies and Television | Music Video                             | amzn1.iab-content.650    |
| Movies and Television | Musicals                                | amzn1.iab-content.156    |
| Movies and Television | Mystery                                 | amzn1.iab-content.331    |
| Movies and Television | Reality TV                              | amzn1.iab-content.651    |
| Movies and Television | Romance                                 | amzn1.iab-content.326    |
| Movies and Television | Science Fiction                         | amzn1.iab-content.652    |
| Movies and Television | Soap Opera                              | amzn1.iab-content.642    |
| Movies and Television | Special Interest (Indie or Art House)   | amzn1.iab-content.643    |
| Movies and Television | Sports Radio                            | amzn1.iab-content.370    |
| Movies and Television | Talk Show                               | amzn1.iab-content.A0AH3G |
| Movies and Television | True Crime                              | amzn1.iab-content.KHPC5A |
| Movies and Television | Western                                 | amzn1.iab-content.KHPC6A |
| Music and Radio       | All Music and Radio                     | amzn1.iab-content.338    |
| Music and Radio       | Blues                                   | amzn1.iab-content.360    |
| Music and Radio       | Classical Music                         | amzn1.iab-content.346    |
| Music and Radio       | Comedy (Music and Audio)                | amzn1.iab-content.348    |
| Music and Radio       | Pop, Contemporary Hits, or Top 40 Music | amzn1.iab-content.349    |
| Music and Radio       | Country Music                           | amzn1.iab-content.350    |
| Music and Radio       | Dance and Electronic Music              | amzn1.iab-content.351    |
| Music and Radio       | Hip Hop Music                           | amzn1.iab-content.355    |
| Music and Radio       | Inspirational or New Age Music          | amzn1.iab-content.356    |
| Music and Radio       | Jazz                                    | amzn1.iab-content.357    |
| Music and Radio       | Oldies or Adult Standards               | amzn1.iab-content.358    |
| Music and Radio       | R&B, Soul or Funk Music                 | amzn1.iab-content.362    |
| Music and Radio       | Reggae                                  | amzn1.iab-content.359    |
| Music and Radio       | Rock Music                              | amzn1.iab-content.363    |
| Music and Radio       | Songwriters or Folk                     | amzn1.iab-content.353    |
| Music and Radio       | World or International Music            | amzn1.iab-content.352    |
| Video Games           | All Video Games                         | amzn1.iab-content.680    |
| Video Games           | Action-Adventure Games                  | amzn1.iab-content.691    |
| Video Games           | Casual Games                            | amzn1.iab-content.693    |
| Video Games           | Puzzle Video Games                      | amzn1.iab-content.698    |
| Video Games           | Racing Video Games                      | amzn1.iab-content.VK7KD0 |
| Video Games           | Role-Playing Video Games                | amzn1.iab-content.687    |
| Video Games           | Simulation Video Games                  | amzn1.iab-content.688    |
| Video Games           | Sports Video Games                      | amzn1.iab-content.689    |
| Video Games           | Strategy Video Games                    | amzn1.iab-content.690    |
| Video Games           | PC Games                                | amzn1.iab-content.684    |
| Video Games           | Mobile Games                            | amzn1.iab-content.683    |
| Video Games           | Console Games                           | amzn1.iab-content.681    |
| Video Games           | eSports                                 | amzn1.iab-content.682    |
""",
    )


class CreateTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    adGroupId: AdGroupId
    expressionType: Literal["manual", "auto"] = Field(
        description="Tactic T00020 ad groups only allow manual targeting."
    )
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
    state: Literal["enabled", "paused", "archived"] | str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    expressionType: Literal["manual", "auto"] | str | None = Field(
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
    state: Literal["enabled", "paused", "archived"] | str | None = Field(default=None)
    expressionType: Literal["auto", "manual"] | str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        description="If a value for `bid` is specified, it overrides the current adGroup bid. When using vcpm costType. $1 is the minimum bid for vCPM. Note that this field is ignored for negative targeting clauses.",
    )
    expression: TargetingExpression | None = Field(default=None)
    resolvedExpression: TargetingExpression | None = Field(default=None)
    servingStatus: (
        Literal[
            "ADVERTISER_STATUS_ENABLED",
            "STATUS_UNAVAILABLE",
            "ADVERTISER_PAUSED",
            "ACCOUNT_OUT_OF_BUDGET",
            "ADVERTISER_PAYMENT_FAILURE",
            "CAMPAIGN_PAUSED",
            "CAMPAIGN_ARCHIVED",
            "PENDING_START_DATE",
            "ENDED",
            "CAMPAIGN_OUT_OF_BUDGET",
            "AD_GROUP_STATUS_ENABLED",
            "AD_GROUP_PAUSED",
            "AD_GROUP_ARCHIVED",
            "AD_GROUP_INCOMPLETE",
            "AD_GROUP_LOW_BID",
            "TARGET_STATUS_LIVE",
            "TARGET_STATUS_PAUSED",
            "TARGET_STATUS_ARCHIVED",
            "ADVERTISER_EXCEED_SPENDS_LIMIT",
            "AD_POLICING_PENDING_REVIEW",
            "CAMPAIGN_INCOMPLETE",
            "INELIGIBLE",
            "PORTFOLIO_ENDED",
            "PORTFOLIO_OUT_OF_BUDGET",
            "ADVERTISER_ARCHIVED",
            "ADVERTISER_ACCOUNT_OUT_OF_BUDGET",
        ]
        | str
        | None
    ) = Field(default=None, description="The status of the target.")
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

    type: (
        Literal[
            "asinCategorySameAs",
            "asinBrandSameAs",
            "asinPriceBetween",
            "asinPriceGreaterThan",
            "asinPriceLessThan",
            "asinReviewRatingLessThan",
            "asinReviewRatingGreaterThan",
            "asinReviewRatingBetween",
            "similarProduct",
            "exactProduct",
            "asinIsPrimeShippingEligible",
            "asinAgeRangeSameAs",
            "asinGenreSameAs",
            "audienceSameAs",
            "lookback",
            "negative",
            "relatedProduct",
        ]
        | str
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class TargetingPredicateLegacy(LenientModel):
    type: (
        Literal[
            "asinSameAs",
            "asinCategorySameAs",
            "asinBrandSameAs",
            "asinPriceBetween",
            "asinPriceGreaterThan",
            "asinPriceLessThan",
            "asinReviewRatingLessThan",
            "asinReviewRatingGreaterThan",
            "asinReviewRatingBetween",
            "similarProduct",
            "exactProduct",
            "asinIsPrimeShippingEligible",
            "asinAgeRangeSameAs",
            "asinGenreSameAs",
        ]
        | str
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")
    eventType: Literal["views"] | str | None = Field(
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

    type: Literal["views", "audience", "purchases"] | str | None = Field(default=None)
    value: list[TargetingPredicateBaseOut] | None = Field(default=None)


class TargetingPredicateOut(LenientModel):
    """A predicate to match against in the targeting expression (only applicable to contextual targeting - T00020).

    * All IDs passed for category and brand-targeting predicates must be valid IDs in the Amazon Ads browse system.
    * Brand, price, and review predicates are optional and may only be specified if category is also specified.
    * Review predicates accept numbers between 0 and 5 and are inclusive.
    * When using either of the 'between' strings to construct a targeting expression the format of the string is 'double-double' where the first double must be smaller than the second double. Prices are not inclusive.
    """

    type: (
        Literal[
            "asinSameAs",
            "asinCategorySameAs",
            "asinBrandSameAs",
            "asinPriceBetween",
            "asinPriceGreaterThan",
            "asinPriceLessThan",
            "asinReviewRatingLessThan",
            "asinReviewRatingGreaterThan",
            "asinReviewRatingBetween",
            "asinIsPrimeShippingEligible",
            "asinAgeRangeSameAs",
            "asinGenreSameAs",
            "similarProduct",
        ]
        | str
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class UpdateTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)
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
