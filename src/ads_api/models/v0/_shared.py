"""Shared models reused across Amazon Ads API v0 entities."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type CreateOrUpdateEntityState = Literal["ENABLED", "PAUSED"]
"""
Entity state for create or update operation.
"""


type CreativePropertyToOptimize = Literal["HEADLINE"]
"""
| CreativePropertyToOptimize                            |  Description                                                                            |
|------------------------------------|-----------------------------------------------------------------------------------------|
| HEADLINE                            | Optimizes headlines by leveraging provided versions and customizing them based on factors such as audience, placement, and featured products.                                                                            |
"""


type CreativeStatus = Literal[
    "SUBMITTED_FOR_MODERATION",
    "PENDING_TRANSLATION",
    "PENDING_MODERATION_REVIEW",
    "APPROVED_BY_MODERATION",
    "REJECTED_BY_MODERATION",
    "PUBLISHED",
]
"""
The lifecycle status of a creative
"""


type CreativeTypeInCreativeResponse = Literal["IMAGE", "VIDEO"]
"""
The type of the creative.
|Name|Description|
|----|-----------|
|IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
|VIDEO |The creative will display video assets. This type of creative must have video assets provided.|
"""


type EntityState = Literal["ENABLED", "PAUSED", "ARCHIVED"]
"""
The current resource state.
"""


type LocationPredicate = Literal["location"]
"""
The location category.
"""


type MmpName = Literal["ADJUST", "AIRBRIDGE", "APPSFLYER", "BRANCH", "KOCHAVA", "SINGULAR", "TENJIN"]
"""
Supported Mobile Measurement Partner names
"""


type MmpPlatform = Literal["ANDROID", "FIRE_TABLET", "FIRE_TV", "IOS"]
"""
Supported mobile platforms for MMP tracking
"""


type QueryTermMatchType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Defines how would the string resource field (e.g. campaign name, ad group name) be matched with the query term in filter.
"""


type SponsoredProductsBiddingErrorReason = Literal[
    "BID_AUDIENCES_MORE_THAN_ALLOWED",
    "BID_GT_BUDGET",
    "BID_INVALID_AUDIENCE_ID",
    "BID_INVALID_AUDIENCE_SEGMENT_TYPE",
    "BID_INVALID_PLACEMENT",
    "BID_INVALID_SHOPPER_COHORT_TYPE",
    "BID_MISSING_AUDIENCES",
    "BID_OUT_OF_MARKET_PLACE_RANGE",
    "BID_SHOPPER_COHORTS_MORE_THAN_ALLOWED",
]


type SponsoredProductsBillingErrorReason = Literal[
    "ADVERTISER_BILLING_SETUP_INCOMPLETE",
    "ADVERTISER_SUSPENDED",
    "BILLING_ACCOUNT_NOT_FOUND",
    "EXPIRED_PAYMENT_METHOD",
    "PAYMENT_PROFILE_NOT_FOUND",
    "VETTING_FAILURE",
]


type SponsoredProductsCreateOrUpdateEntityState = Literal["ENABLED", "PAUSED", "PROPOSED"]
"""
Entity state for create or update operation
"""


type SponsoredProductsCreateOrUpdateNegativeMatchType = Literal["NEGATIVE_BROAD", "NEGATIVE_EXACT", "NEGATIVE_PHRASE"]


type SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType = Literal[
    "ASIN_BRAND_SAME_AS", "ASIN_SAME_AS"
]
"""
The type of nagative targeting expression. You can only specify values for the following predicates:

Supported values:
- `ASIN_BRAND_SAME_AS`: Target the brand that is the same as the brand expressed.
- `ASIN_SAME_AS`: Target an ASIN that is the same as the ASIN expressed.
"""


type SponsoredProductsDuplicateValueErrorReason = Literal[
    "DUPLICATE_VALUE", "MARKETPLACE_ATTRIBUTES_REPEATED", "NAME_NOT_UNIQUE"
]


type SponsoredProductsEntityNotFoundErrorReason = Literal["ENTITY_NOT_FOUND"]


type SponsoredProductsEntityState = Literal[
    "ARCHIVED", "ENABLED", "ENABLING", "OTHER", "PAUSED", "PROPOSED", "USER_DELETED"
]
"""
The current resource state.

Supported values:
- `ENABLED`: Enabled State
- `PAUSED`: Paused State
- `PROPOSED`: Proposed State (Upcoming Feature)
- `ARCHIVED`: ARCHIVED State
- `ENABLING`: State for Draft Entity Only
- `USER_DELETED`: State for Draft Entity Only
- `OTHER`: Read Only
"""


type SponsoredProductsEntityStateErrorReason = Literal[
    "ARCHIVED_ENTITY_CANNOT_BE_MODIFIED",
    "AUTO_TARGETING_CLAUSE_CANNOT_BE_ARCHIVED_MANUALLY",
    "INVALID_STATE_TRANSITION",
    "INVALID_TARGET_STATE",
    "MARKETPLACE_STATE_CANNOT_BE_ARCHIVED",
    "PARENT_ARCHIVED_FORBIDS_UPDATES",
    "PARENT_ENTITY_FORBIDS_CREATION",
    "PARENT_STATUS_FORBIDS_UPDATES_AND_CREATES",
]


type SponsoredProductsEntityType = Literal[
    "AD_GROUP",
    "CAMPAIGN",
    "CAMPAIGN_NEGATIVE_KEYWORD",
    "CAMPAIGN_NEGATIVE_TARGETING_CLAUSE",
    "KEYWORD",
    "NEGATIVE_KEYWORD",
    "NEGATIVE_TARGETING_CLAUSE",
    "PRODUCT_AD",
    "TARGETING_CLAUSE",
]


type SponsoredProductsExpressionTypeErrorReason = Literal["UNSUPPORTED_EXPRESSION_TYPE"]


type SponsoredProductsInternalServerErrorReason = Literal["INTERNAL_ERROR"]


type SponsoredProductsKeywordServingStatus = Literal[
    "ACCOUNT_OUT_OF_BUDGET",
    "ADVERTISER_ARCHIVED",
    "ADVERTISER_EXCEED_SPENDS_LIMIT",
    "ADVERTISER_OUT_OF_BUDGET",
    "ADVERTISER_PAUSED",
    "ADVERTISER_PAYMENT_FAILURE",
    "ADVERTISER_POLICING_PENDING_REVIEW",
    "ADVERTISER_POLICING_SUSPENDED",
    "AD_GROUP_ARCHIVED",
    "AD_GROUP_INCOMPLETE",
    "AD_GROUP_LOW_BID",
    "AD_GROUP_PAUSED",
    "AD_GROUP_POLICING_CREATIVE_REJECTED",
    "AD_GROUP_POLICING_PENDING_REVIEW",
    "AD_GROUP_STATUS_ENABLED",
    "CAMPAIGN_ARCHIVED",
    "CAMPAIGN_INCOMPLETE",
    "CAMPAIGN_OUT_OF_BUDGET",
    "CAMPAIGN_PAUSED",
    "CAMPAIGN_STATUS_ENABLED",
    "ENDED",
    "OTHER",
    "PENDING_REVIEW",
    "PENDING_START_DATE",
    "PORTFOLIO_ARCHIVED",
    "PORTFOLIO_ENDED",
    "PORTFOLIO_OUT_OF_BUDGET",
    "PORTFOLIO_PAUSED",
    "PORTFOLIO_PENDING_START_DATE",
    "PORTFOLIO_STATUS_ENABLED",
    "REJECTED",
    "TARGETING_CLAUSE_ARCHIVED",
    "TARGETING_CLAUSE_BLOCKED",
    "TARGETING_CLAUSE_PAUSED",
    "TARGETING_CLAUSE_POLICING_SUSPENDED",
    "TARGETING_CLAUSE_STATUS_LIVE",
]


type SponsoredProductsKeywordServingStatusReason = Literal[
    "ACCOUNT_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_ARCHIVED_DETAIL",
    "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL",
    "ADVERTISER_OUT_OF_BUDGET_DETAIL",
    "ADVERTISER_PAUSED_DETAIL",
    "ADVERTISER_PAYMENT_FAILURE_DETAIL",
    "ADVERTISER_POLICING_PENDING_REVIEW_DETAIL",
    "ADVERTISER_POLICING_SUSPENDED_DETAIL",
    "AD_GROUP_ARCHIVED_DETAIL",
    "AD_GROUP_INCOMPLETE_DETAIL",
    "AD_GROUP_LOW_BID_DETAIL",
    "AD_GROUP_PAUSED_DETAIL",
    "AD_GROUP_POLICING_CREATIVE_REJECTED_DETAIL",
    "AD_GROUP_POLICING_PENDING_REVIEW_DETAIL",
    "AD_GROUP_STATUS_ENABLED_DETAIL",
    "CAMPAIGN_ARCHIVED_DETAIL",
    "CAMPAIGN_INCOMPLETE_DETAIL",
    "CAMPAIGN_OUT_OF_BUDGET_DETAIL",
    "CAMPAIGN_PAUSED_DETAIL",
    "CAMPAIGN_STATUS_ENABLED_DETAIL",
    "ENDED_DETAIL",
    "OTHER",
    "PENDING_REVIEW_DETAIL",
    "PENDING_START_DATE_DETAIL",
    "PORTFOLIO_ARCHIVED_DETAIL",
    "PORTFOLIO_ENDED_DETAIL",
    "PORTFOLIO_OUT_OF_BUDGET_DETAIL",
    "PORTFOLIO_PAUSED_DETAIL",
    "PORTFOLIO_PENDING_START_DATE_DETAIL",
    "PORTFOLIO_STATUS_ENABLED_DETAIL",
    "REJECTED_DETAIL",
    "TARGETING_CLAUSE_ARCHIVED_DETAIL",
    "TARGETING_CLAUSE_BLOCKED_DETAIL",
    "TARGETING_CLAUSE_PAUSED_DETAIL",
    "TARGETING_CLAUSE_POLICING_SUSPENDED_DETAIL",
    "TARGETING_CLAUSE_STATUS_LIVE_DETAIL",
]


type SponsoredProductsLocaleErrorReason = Literal["INVALID_LOCALE"]


type SponsoredProductsMalformedValueErrorReason = Literal[
    "BLANK", "FORBIDDEN_CHARS", "LEADING_OR_TRAILING_WHITESPACE", "PATTERN_NOT_MATCHED", "TOO_LONG", "TOO_SHORT"
]


type SponsoredProductsMarketplace = Literal[
    "AE",
    "AU",
    "BR",
    "CA",
    "DE",
    "EG",
    "ES",
    "FR",
    "IN",
    "IT",
    "JP",
    "MX",
    "NL",
    "PL",
    "SA",
    "SE",
    "SG",
    "TR",
    "UK",
    "US",
]


type SponsoredProductsMissingValueErrorReason = Literal["MISSING_VALUE"]


type SponsoredProductsNegativeMatchType = Literal["NEGATIVE_BROAD", "NEGATIVE_EXACT", "NEGATIVE_PHRASE", "OTHER"]


type SponsoredProductsNegativeTargetingExpressionPredicateType = Literal["ASIN_BRAND_SAME_AS", "ASIN_SAME_AS", "OTHER"]
"""
The type of nagative targeting expression. You can only specify values for the following predicates:

Supported values:
- `ASIN_BRAND_SAME_AS`: Target the brand that is the same as the brand expressed.
- `ASIN_SAME_AS`: Target an ASIN that is the same as the ASIN expressed.
- `OTHER`: Other Type.
"""


type SponsoredProductsOtherErrorReason = Literal["OTHER_ERROR"]


type SponsoredProductsParentEntityErrorReason = Literal[
    "PARENT_ENTITY_ARCHIVED", "PARENT_ENTITY_DOES_NOT_TARGET_THESE_MARKETPLACES", "PARENT_ENTITY_NOT_FOUND"
]


type SponsoredProductsQueryTermMatchType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Match type for query filters.

Supported values:
- `BROAD_MATCH`: Match if the queried value contains the filter value (substring matching). Note: If queryTermMatchType is set to BROAD_MATCH, only matches for the first query included will be returned.
- `EXACT_MATCH`: Match if the queried value is exactly equivalent to the filter value.
"""


type SponsoredProductsQuotaErrorReason = Literal["NON_ARCHIVED_QUOTA_EXCEEDED", "QUOTA_EXCEEDED"]


type SponsoredProductsQuotaScope = Literal["ACCOUNT", "PARENT_ENTITY"]


type SponsoredProductsTargetingClauseSetupErrorReason = Literal[
    "AUTO_TARGETING_CLAUSE_CANNOT_BE_CREATED_MANUALLY",
    "TARGETING_EXPRESSION_INVALID_VALUE",
    "TARGETING_TYPE_NOT_ALLOWED_FOR_AUTO_TARGETING_CAMPAIGN",
    "TYPE_CONFLICT_IN_AD_GROUP",
]


type SponsoredProductsTargetingType = Literal["AUTO", "MANUAL"]


type SponsoredProductsThrottledErrorReason = Literal["THROTTLED"]


type SponsoredProductsValueLimitErrorReason = Literal["INVALID_ENUM_VALUE", "NOT_IN_LIST", "TOO_HIGH", "TOO_LOW"]


type Tactic = Literal["T00020", "T00030"]
"""
The advertising tactic associated with the campaign. The following table lists available tactic names:
|Tactic Name|Type|Description|
|-----------|-----|-----------|
|T00020     |Contextual targeting | Choose individual products to show your ads in placements related to those products.<br> Choose individual categories to show your ads in placements related to those categories on and off Amazon.|
|T00030     |Audiences or Contextual Targeting | Select individual products, categories, refined categories, or audiences to show your ads.|
"""


type Theme = Literal["BFCM_HOLIDAY", "CONVERSION_OPPORTUNITIES", "FALL_PRIME_DEAL_EVENT", "PRIME_DAY"]
"""
The bid recommendation theme. This API currently supports `CONVERSION_OPPORTUNITIES`, `PRIME_DAY`, `FALL_PRIME_DEAL_EVENT`, and `BFCM_HOLIDAY` themes.
"""


type AdGroupId = int  # The identifier of the ad group.

type AdId = int  # The identifier of the product ad.

type AdName = str  # The name of the ad. Note that this field is not supported when using ASIN or SKU fields.


class BaseAdGroup(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: Literal["reach", "clicks", "conversions"] | None = Field(
        default=None,
        description="""
Bid Optimization for the Adgroup. Default behavior is to optimize for clicks.
|Name|CostType|Description|
|----|--------|-----------|
|reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks |cpc|[Default] Optimize for page visits.|
|conversions |cpc|Optimize for conversion.|
""",
    )
    state: Literal["enabled", "paused", "archived"] | None = Field(
        default=None, description="The state of the ad group."
    )


class BaseCampaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: Literal["daily"] | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: Literal["cpc", "vcpm"] | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
|Name|Description|
|----|----------|
|cpc |[Default] The performance of this campaign is measured by the clicks triggered by the ad.|
|vcpm |The performance of this campaign is measured by the viewed impressions triggered by the ad. |

To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: Literal["enabled", "paused", "archived"] | None = Field(
        default=None, description="The state of the campaign."
    )
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )


class BaseNegativeTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)


class BaseProductAd(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(
        default=None, description="The state of the campaign associated with the product ad."
    )


class BaseTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )


class BidAnalyses(LenientModel):
    pass


class BidAnalysesPerPlacement(LenientModel):
    ALL: BidAnalyses
    PLACEMENT_PRODUCT_PAGE: BidAnalyses
    PLACEMENT_REST_OF_SEARCH: BidAnalyses
    PLACEMENT_TOP: BidAnalyses


class BidAnalysis(LenientModel):
    bid: float = Field(ge=0)
    impactMetrics: BidAnalysisImpactMetrics
    type: Literal["ALTERNATIVE", "SUGGESTED", "SUGGESTED_LOWER", "SUGGESTED_UPPER"] | str = Field(
        description="The type of bids in bid analyses. <br>`SUGGESTED_UPPER` - The upper bound for the suggested bid. <br>`SUGGESTED_LOWER` - The lower bound for the suggested bid. <br>`SUGGESTED` - The suggested bid value. <br>'ALTERNATIVE' - The alternative bids that is included in the bid analyses."
    )


class BidAnalysisImpactMetrics(LenientModel):
    estimatedImpressionAvg: int = Field(description="Number indicating the average of the estimated impressions")
    estimatedImpressionLower: int = Field(description="Number indicating a lower bound of the estimated impressions")
    estimatedImpressionUpper: int = Field(description="Number indicating an upper bound of the estimated impressions")


class BiddingError(LenientModel):
    """Errors related to bids."""

    reason: str = Field(description="Exact error reason.")
    cause: ErrorCause
    upperLimit: str | None = Field(default=None)
    lowerLimit: str | None = Field(default=None)
    message: str = Field(description="Human readable error message.")


type CampaignId = int  # The identifier of the campaign.


class ContentTargetingPredicate(StrictModel):
    """A predicate to match against in the content targeting expression."""

    type: Literal["contentCategorySameAs"] | None = Field(default=None)
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


class CustomImage(StrictModel):
    assetId: str | None = Field(default=None)
    crop: CustomImageCrop | None = Field(default=None)
    url: str | None = Field(default=None)


class CustomImageCrop(StrictModel):
    """The crop to apply to the selected Custom image. A Custom image must have a 1200x628 aspect ratio, with a .01 delta for floating point precision. If a customImageAssetId is supplied but a crop is not, the crop will be defaulted to the whole image."""

    top: float | None = Field(default=None)
    left: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)


class CustomImageCropOut(LenientModel):
    """The crop to apply to the selected Custom image. A Custom image must have a 1200x628 aspect ratio, with a .01 delta for floating point precision. If a customImageAssetId is supplied but a crop is not, the crop will be defaulted to the whole image."""

    top: float | None = Field(default=None)
    left: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)


class CustomImageOut(LenientModel):
    assetId: str | None = Field(default=None)
    crop: CustomImageCropOut | None = Field(default=None)
    url: str | None = Field(default=None)


class DateError(LenientModel):
    """Errors related to dates."""

    reason: str = Field(description="Exact error reason..")
    cause: ErrorCause
    message: str = Field(description="Human readable error message.")


class DisassociateAssociatedBudgetRuleResponse(LenientModel):
    pass


class EntityStateFilter(StrictModel):
    """Filter entities by state."""

    include: list[EntityState] | None = Field(default=None, min_length=0, max_length=10)


class ErrorCause(LenientModel):
    """Structure describing error cause - location in the payload and data causing error."""

    location: str = Field(
        description="Error location, JSON Path expression specifying element of API payload causing error."
    )
    trigger: str | None = Field(default=None, description="Optional value causing error.")


class ExternalIdentity(StrictModel):
    """Support for externalIdentity is planned for the future."""

    experianId: str | None = Field(default=None, description="User identifier provided by Experian")
    kantarId: str | None = Field(default=None, description="User identifier provided by Kantar")
    liveRampId: str | None = Field(default=None, description="User identifier provided by LiveRamp")
    maId: str | None = Field(
        default=None, description="Mobile advertising identifier (IDFA for iOS or GAID for Android)"
    )
    merkleId: str | None = Field(default=None, description="User identifier provided by Merkle")
    merkuryId: str | None = Field(default=None, description="User identifier provided by Merkle Merkury")
    neustarId: str | None = Field(default=None, description="User identifier provided by Neustar")
    realId: str | None = Field(default=None, description="User identifier provided by RealId")
    sambaTvId: str | None = Field(default=None, description="User identifier provided by Samba TV")
    transunionId: str | None = Field(default=None, description="User identifier provided by TransUnion")


class HashedPii(StrictModel):
    """Structure representing hashed personally identifiable information (PII)."""

    ad: str | None = Field(default=None, description="Normalized and SHA-256 hashed street address")
    cty: str | None = Field(default=None, description="Normalized and SHA-256 hashed city name")
    em: str | None = Field(default=None, description="Normalized and SHA-256 hashed email address")
    fn: str | None = Field(default=None, description="Normalized and SHA-256 hashed first name")
    ln: str | None = Field(default=None, description="Normalized and SHA-256 hashed last name")
    ph: str | None = Field(default=None, description="Normalized and SHA-256 hashed phone number")
    st: str | None = Field(default=None, description="Normalized and SHA-256 hashed state or region code")
    zip: str | None = Field(default=None, description="Normalized and SHA-256 hashed postal or zip code")


class Identity(StrictModel):
    """Either one hashedPII object or external identity object is required"""

    externalIdentities: list[ExternalIdentity] | None = Field(default=None, min_length=0, max_length=10)
    hashedPiis: list[HashedPii] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="List of hashed personally-identifiable information records to be matched with Amazon identities for future use. All inputs must be properly normalized and SHA-256 hashed.",
    )


class ImpactMetric(LenientModel):
    """The impact metrics are given in the same order of suggested bids. <br> Note: This object is nullable"""

    values: list[RangeMetricValue] | None = Field(default=None)


class ImpactMetrics(LenientModel):
    """For the CONVERSION_OPPORTUNITIES theme, the impact metrics are weekly clicks and orders received for similar products. For other event-based themes, the impact metrics are clicks and orders received for similar products during the event days. <br> Note: This object is nullable"""

    clicks: ImpactMetric | None = Field(default=None)
    orders: ImpactMetric | None = Field(default=None)


type LandingPageURL = str


class LocationExpression(StrictModel):
    type: LocationPredicate | None = Field(default=None)
    value: str | None = Field(
        default=None,
        description="The location identifier. Currently, this can correspond to either a 'city', 'state', 'dma', 'postal code', or 'country'. Its value is discoverable using the GET /locations API.",
    )


class Metadata(LenientModel):
    """Container for dataset metadata"""

    mmpMetadata: MmpMetadata | None = Field(default=None)


class MmpMetadata(LenientModel):
    """MMP (Mobile Measurement Partner) metadata for dataset tracking"""

    appName: str = Field(max_length=100, description="User-defined application name for MMP Registration")
    bundleId: str = Field(max_length=255, description="Bundle ID parsed from app store URL")
    isExistingApp: bool | None = Field(
        default=None, description="Whether the app was already registered prior to migration"
    )
    mmpAppId: str | None = Field(default=None, description="Unique app registration ID generated by Amazon")
    mmpName: MmpName | str
    platform: MmpPlatform | str
    skAdNetworkReference: bool | None = Field(default=None, description="SKAdNetwork enablement reference")
    sourceAdvertiserAccountId: str | None = Field(
        default=None, description="Advertiser account ID of the source system prior to migration"
    )


class NameFilter(StrictModel):
    """Filter entities by name."""

    queryTermMatchType: QueryTermMatchType | None = Field(default=None)
    include: list[str] | None = Field(default=None, min_length=0, max_length=100)


class NegativeTargetingExpression(StrictModel):
    type: Literal["asinSameAs", "asinBrandSameAs"] | None = Field(
        default=None,
        description="The intent type. See the [targeting topic](https://advertising.amazon.com/help#GQCBASRVERXSARL3) in the Amazon Ads support center for more information.",
    )
    value: str | None = Field(
        default=None, description="The value to be negatively targeted. Used only in manual expressions."
    )


class ObjectIdFilter(StrictModel):
    """Filter entities by the list of objectIds."""

    include: list[str] | None = Field(default=None, min_length=0, max_length=10)


class OtherError(LenientModel):
    """Errors not related to any of the other error types."""

    reason: str
    cause: ErrorCause
    message: str = Field(description="Human readable error message.")


class RangeError(LenientModel):
    """Errors related to range constraints violations."""

    reason: str
    allowed: list[str] | None = Field(default=None, min_length=0, max_length=100, description="Allowed values.")
    cause: ErrorCause
    upperLimit: str | None = Field(default=None, description="Optional upper limit.")
    lowerLimit: str | None = Field(default=None, description="Optional lower limit.")
    message: str = Field(description="Human readable error message.")


class RangeMetricValue(LenientModel):
    """Describes lower and upper bounds of the range. <br> Note: This object is nullable"""

    lower: int | None = Field(default=None)
    upper: int | None = Field(default=None)


type RuleId = str  # The identifier of the optimization rule.


class SBTargetingBrand(LenientModel):
    brandRefinementId: str = Field(
        description="Id of brand. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Brand Refinement IDs."
    )
    name: str | None = Field(default=None, description="Name of brand.")


type SDASIN = str  # Amazon Standard Identification Number


class SDGoalProduct(StrictModel):
    """A product an advertisers wants to advertise. Recommendations will be made for specified goal products."""

    asin: SDASIN


class SponsoredProductsAsinFilter(StrictModel):
    include: list[str] | None = Field(default=None, max_length=100)
    queryTermMatchType: SponsoredProductsQueryTermMatchType | None = Field(default=None)


class SponsoredProductsBiddingError(LenientModel):
    """Errors related to bids"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    lowerLimit: str | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsBiddingErrorReason | str
    upperLimit: str | None = Field(default=None)


class SponsoredProductsBillingError(LenientModel):
    """Errors related to bids"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsBillingErrorReason | str


class SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate(StrictModel):
    type: SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType
    value: str | None = Field(default=None, description="The expression value")


class SponsoredProductsDuplicateValueError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsDuplicateValueErrorReason | str


class SponsoredProductsEntityNotFoundError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    entityId: str = Field(description="The entity id in the request")
    entityType: SponsoredProductsEntityType | str
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsEntityNotFoundErrorReason | str


class SponsoredProductsEntityQuotaError(LenientModel):
    """Errors related to exceeding quota in campaign management service"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    entityType: SponsoredProductsEntityType | str
    message: str = Field(description="Human readable error message")
    quota: str | None = Field(default=None, description="optional current quota")
    quotaScope: SponsoredProductsQuotaScope | str | None = Field(default=None)
    reason: SponsoredProductsQuotaErrorReason | str


class SponsoredProductsEntityStateError(LenientModel):
    """entity state update errors"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    entityType: SponsoredProductsEntityType | str
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsEntityStateErrorReason | str


class SponsoredProductsEntityStateFilter(StrictModel):
    """Filter entities by state. To filter live entities, only 'ENABLED', 'PAUSED' and 'ARCHIVED' can be used"""

    include: list[SponsoredProductsEntityState] = Field(min_length=0, max_length=10)


class SponsoredProductsErrorCause(LenientModel):
    """Structure describing error cause - location in the payload and data causing error"""

    location: str = Field(
        description="Error location, JSON Path expression specifying element of API payload causing error"
    )
    trigger: str | None = Field(default=None, description="optional value causing error")


class SponsoredProductsExpressionTypeError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsExpressionTypeErrorReason | str


class SponsoredProductsInternalServerError(LenientModel):
    """Error that represents non-retryable API service error. Sending the same request will result in another error."""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsInternalServerErrorReason | str


class SponsoredProductsKeywordServingStatusDetail(LenientModel):
    helpUrl: str | None = Field(
        default=None, description="A URL with additional information about the status identifier."
    )
    message: str | None = Field(
        default=None, description="A human-readable description of the status identifier specified in the name field."
    )
    name: SponsoredProductsKeywordServingStatusReason | str | None = Field(default=None)


class SponsoredProductsKeywordTextFilter(StrictModel):
    """Filter by keywordText"""

    include: list[str] | None = Field(default=None, min_length=0, max_length=100)
    queryTermMatchType: SponsoredProductsQueryTermMatchType


class SponsoredProductsLocaleError(LenientModel):
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsLocaleErrorReason | str


class SponsoredProductsMalformedValueError(LenientModel):
    """Errors being used to represent malformed values
    e.g. containing not allowed characters, not following patters etc"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    fragment: str | None = Field(default=None, description="fragment of the value which is wrong")
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsMalformedValueErrorReason | str


class SponsoredProductsMissingValueError(LenientModel):
    """Error describing missing values in API payloads"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsMissingValueErrorReason | str


class SponsoredProductsNameFilter(StrictModel):
    """Filter entities by name"""

    include: list[str] | None = Field(default=None, min_length=0, max_length=100)
    queryTermMatchType: SponsoredProductsQueryTermMatchType | None = Field(default=None)


class SponsoredProductsNegativeTargetingExpressionPredicate(LenientModel):
    type: SponsoredProductsNegativeTargetingExpressionPredicateType | str | None = Field(default=None)
    value: str | None = Field(default=None, description="The expression value")


class SponsoredProductsObjectIdFilter(StrictModel):
    """Filter entities by the list of objectIds"""

    include: list[str] = Field(min_length=0, max_length=1000)


class SponsoredProductsOtherError(LenientModel):
    """Errors not related to any of the other error types"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsOtherErrorReason | str


class SponsoredProductsParentEntityError(LenientModel):
    """Errors related to parent entity"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsParentEntityErrorReason | str


class SponsoredProductsRangeError(LenientModel):
    """Errors related to range constraints violations"""

    allowed: list[str] | None = Field(default=None, description="allowed values")
    cause: SponsoredProductsErrorCause | None = Field(default=None)
    lowerLimit: str | None = Field(default=None, description="optional lower limit")
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsValueLimitErrorReason | str
    upperLimit: str | None = Field(default=None, description="optional upper limit")


class SponsoredProductsReducedObjectIdFilter(StrictModel):
    """Filter entities by the list of objectIds"""

    include: list[str] = Field(min_length=0, max_length=100)


class SponsoredProductsTags(StrictModel):
    """A list of advertiser-specified custom identifiers for the campaign. Each customer identifier is a key-value pair. You can specify a maximum of 50 identifiers."""

    pass


class SponsoredProductsTargetingClauseSetupError(LenientModel):
    """Errors related to targeting clause setup"""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    marketplace: SponsoredProductsMarketplace | str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsTargetingClauseSetupErrorReason | str


class SponsoredProductsThrottledError(LenientModel):
    """Error that represents failure due to API caller exceeding allowed service limits."""

    cause: SponsoredProductsErrorCause | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: SponsoredProductsThrottledErrorReason | str


class Subpage(StrictModel):
    pageTitle: str | None = Field(default=None)
    asin: str | None = Field(default=None)
    url: str | None = Field(default=None)


class SubpageOut(LenientModel):
    pageTitle: str | None = Field(default=None)
    asin: str | None = Field(default=None)
    url: str | None = Field(default=None)


type TargetId = int


class TargetResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    targetId: TargetId | None = Field(default=None)


class TargetingPredicate(StrictModel):
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
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class TargetingPredicateBase(StrictModel):
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
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")


class TargetingPredicateNested(StrictModel):
    """A behavioral event and list of targeting predicates that represents an audience to target (only applicable to audience targeting - T00030).

    * For manual ASIN-grain targeting, the value array must contain only, 'exactProduct', 'similarProduct', 'relatedProduct' and 'lookback' TargetingPredicateBase components. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For manual Category-grain targeting, the value array must contain a 'lookback' and 'asinCategorySameAs' TargetingPredicateBase component, which can be further refined with optional brand, price, star-rating and shipping eligibility refinements. The 'lookback' is mandatory and the value should be set to '7', '14', '30', '60', '90', '180' or '365'.
    * For Amazon Audiences targeting, the TargetingPredicateNested type should be set to 'audience' and the value array should include one TargetingPredicateBase component with type set to 'audienceSameAs'.
    """

    type: Literal["views", "audience", "purchases"] | None = Field(default=None)
    value: list[TargetingPredicateBase] | None = Field(default=None)


__all__ = [
    "AdGroupId",
    "AdId",
    "AdName",
    "BaseAdGroup",
    "BaseCampaign",
    "BaseNegativeTargetingClause",
    "BaseProductAd",
    "BaseTargetingClause",
    "BidAnalyses",
    "BidAnalysesPerPlacement",
    "BidAnalysis",
    "BidAnalysisImpactMetrics",
    "BiddingError",
    "CampaignId",
    "ContentTargetingPredicate",
    "CreateOrUpdateEntityState",
    "CreativePropertyToOptimize",
    "CreativeStatus",
    "CreativeTypeInCreativeResponse",
    "CustomImage",
    "CustomImageCrop",
    "CustomImageCropOut",
    "CustomImageOut",
    "DateError",
    "DisassociateAssociatedBudgetRuleResponse",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "ExternalIdentity",
    "HashedPii",
    "Identity",
    "ImpactMetric",
    "ImpactMetrics",
    "LandingPageURL",
    "LocationExpression",
    "LocationPredicate",
    "Metadata",
    "MmpMetadata",
    "MmpName",
    "MmpPlatform",
    "NameFilter",
    "NegativeTargetingExpression",
    "ObjectIdFilter",
    "OtherError",
    "QueryTermMatchType",
    "RangeError",
    "RangeMetricValue",
    "RuleId",
    "SBTargetingBrand",
    "SDASIN",
    "SDGoalProduct",
    "SponsoredProductsAsinFilter",
    "SponsoredProductsBiddingError",
    "SponsoredProductsBiddingErrorReason",
    "SponsoredProductsBillingError",
    "SponsoredProductsBillingErrorReason",
    "SponsoredProductsCreateOrUpdateEntityState",
    "SponsoredProductsCreateOrUpdateNegativeMatchType",
    "SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicate",
    "SponsoredProductsCreateOrUpdateNegativeTargetingExpressionPredicateType",
    "SponsoredProductsDuplicateValueError",
    "SponsoredProductsDuplicateValueErrorReason",
    "SponsoredProductsEntityNotFoundError",
    "SponsoredProductsEntityNotFoundErrorReason",
    "SponsoredProductsEntityQuotaError",
    "SponsoredProductsEntityState",
    "SponsoredProductsEntityStateError",
    "SponsoredProductsEntityStateErrorReason",
    "SponsoredProductsEntityStateFilter",
    "SponsoredProductsEntityType",
    "SponsoredProductsErrorCause",
    "SponsoredProductsExpressionTypeError",
    "SponsoredProductsExpressionTypeErrorReason",
    "SponsoredProductsInternalServerError",
    "SponsoredProductsInternalServerErrorReason",
    "SponsoredProductsKeywordServingStatus",
    "SponsoredProductsKeywordServingStatusDetail",
    "SponsoredProductsKeywordServingStatusReason",
    "SponsoredProductsKeywordTextFilter",
    "SponsoredProductsLocaleError",
    "SponsoredProductsLocaleErrorReason",
    "SponsoredProductsMalformedValueError",
    "SponsoredProductsMalformedValueErrorReason",
    "SponsoredProductsMarketplace",
    "SponsoredProductsMissingValueError",
    "SponsoredProductsMissingValueErrorReason",
    "SponsoredProductsNameFilter",
    "SponsoredProductsNegativeMatchType",
    "SponsoredProductsNegativeTargetingExpressionPredicate",
    "SponsoredProductsNegativeTargetingExpressionPredicateType",
    "SponsoredProductsObjectIdFilter",
    "SponsoredProductsOtherError",
    "SponsoredProductsOtherErrorReason",
    "SponsoredProductsParentEntityError",
    "SponsoredProductsParentEntityErrorReason",
    "SponsoredProductsQueryTermMatchType",
    "SponsoredProductsQuotaErrorReason",
    "SponsoredProductsQuotaScope",
    "SponsoredProductsRangeError",
    "SponsoredProductsReducedObjectIdFilter",
    "SponsoredProductsTags",
    "SponsoredProductsTargetingClauseSetupError",
    "SponsoredProductsTargetingClauseSetupErrorReason",
    "SponsoredProductsTargetingType",
    "SponsoredProductsThrottledError",
    "SponsoredProductsThrottledErrorReason",
    "SponsoredProductsValueLimitErrorReason",
    "Subpage",
    "SubpageOut",
    "Tactic",
    "TargetId",
    "TargetResponse",
    "TargetingPredicate",
    "TargetingPredicateBase",
    "TargetingPredicateNested",
    "Theme",
]
