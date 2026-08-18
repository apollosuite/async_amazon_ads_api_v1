"""Auto-generated models for Forecasts from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    AdGroupId,
    AdId,
    AdName,
    BaseAdGroup,
    BaseCampaign,
    BaseNegativeTargetingClause,
    BaseProductAd,
    BaseTargetingClause,
    CampaignId,
    ContentTargetingPredicate,
    LandingPageURL,
    LocationExpression,
    LocationPredicate,
    NegativeTargetingExpression,
    RuleId,
    Tactic,
    TargetId,
    TargetingPredicate,
    TargetingPredicateBase,
    TargetingPredicateNested,
)

type CreativeType = Literal["IMAGE", "VIDEO"]
"""
The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. One ad group only supports one type (VIDEO or IMAGE) of creativeType at a time.
|Name|Description|
|----|-----------|
|IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
|VIDEO |The creative will display video assets. This type of creative must have a video asset provided. Only supported when using productAds with ASIN or SKU.|
"""


type ForecastStatus = Literal["IMPRESSION_TARGETING_TOO_NARROW", "IMPRESSION_TARGETING_TOO_BROAD", "COMPLETE"]
"""
It contains the forecast status. The IMPRESSION_TARGETING_TOO_NARROW field means the targeting  clauses are too narrow, and the IMPRESSION_TARGETING_TOO_BROAD field means the targeting clauses are too broad,  so our inventory impression forecast won't provide any useful information. The COMPLETE field means all the forecasts are complete.
"""


type LandingPageType = Literal["STORE", "MOMENT", "OFF_AMAZON_LINK"]
"""
The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
"""


class AdGroup(StrictModel):
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
    adGroupId: AdGroupId | None = Field(default=None)
    tactic: Tactic | None = Field(default=None)
    creativeType: CreativeType | None = Field(default=None)


class BaseOptimizationRule(StrictModel):
    state: Literal["enabled", "paused [COMING LATER]"] | None = Field(
        default=None, description="The state of the optimization rule."
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class Campaign(StrictModel):
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
    campaignId: CampaignId | None = Field(default=None)
    tactic: Tactic | None = Field(default=None)
    deliveryProfile: Literal["as_soon_as_possible"] | None = Field(default=None)
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class Curve(LenientModel):
    """Forecast curve of a certain type. The type could be budget vs forecast outcome."""

    meetThreshold: bool | None = Field(
        default=None, description="True if the budget utilization is good to show the curve."
    )
    graph: Literal["BUDGET"] | str | None = Field(default=None, description="Type of Graph.")
    points: list[CurvePoint] | None = Field(default=None, min_length=50, max_length=100)


class CurvePoint(LenientModel):
    """A single point on a curve."""

    isFocus: bool | None = Field(default=None, description="If this point is the point with the focus circle.")
    x: dict[str, Any] | None = Field(default=None, description="x-axis value.")
    y: list[CurvePointRangedValue] | None = Field(
        default=None, min_length=0, max_length=2, description="y-axis value of multiple KPI types."
    )


class CurvePointFixedValue(LenientModel):
    value: float | None = Field(default=None)


class CurvePointRangedValue(LenientModel):
    """A ranged value."""

    label: Literal["CLICKS", "REACH"] | str | None = Field(default=None, description="KPI label.")
    value: ForecastRangeDouble | None = Field(default=None)


class Forecast(LenientModel):
    """Forecast impressions, clicks, reach, or conversions."""

    metric: Literal["IMPRESSIONS", "REACH", "CLICKS", "CONVERSIONS"] | str | None = Field(
        default=None,
        description="""
Describes which metric is forecasted.
|Name|Description|
|-----------|------------------------|
|IMPRESSIONS| Available impressions|
|REACH      | Delivered viewable impressions|
|CLICKS     | Delivered page visits|
|CONVERSIONS| [Preview only] Delivered conversions|
""",
    )
    value: ForecastRange | None = Field(default=None)


class ForecastRange(LenientModel):
    """Forecast range values."""

    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ForecastRangeDouble(LenientModel):
    """A range of value."""

    min: float | None = Field(default=None, description="Lower bound.")
    mean: float | None = Field(default=None, description="Geometric mean of the upper and lower bounds.")
    max: float | None = Field(default=None, description="Upper bound.")


class NegativeTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: Literal["manual", "auto"] | None = Field(default=None)
    expression: list[NegativeTargetingExpression] | None = Field(
        default=None,
        description="""
The expression to negatively match against.
* Only one brand may be specified per targeting expression.
* Only one asin may be specified per targeting expression.
* To exclude a brand from a targeting expression, you must create a negative targeting expression in the same ad group as the positive targeting expression.
""",
    )
    resolvedExpression: list[NegativeTargetingExpression] | None = Field(
        default=None, description="The resolved negative targeting expression."
    )


class OptimizationRule(StrictModel):
    state: Literal["enabled", "paused [COMING LATER]"] | None = Field(
        default=None, description="The state of the optimization rule."
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: RuleId | None = Field(default=None)


class ProductAd(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(
        default=None, description="The state of the campaign associated with the product ad."
    )
    adId: AdId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: LandingPageType | None = Field(default=None)
    adName: AdName | None = Field(default=None)
    asin: str | None = Field(
        default=None,
        description="The Amazon ASIN of the product advertised by the product ad. This parameter is included in the response for sellers and vendors.",
    )
    sku: str | None = Field(
        default=None,
        description="The Amazon SKU of the product advertised by the product ad. This parameter is included in the response for sellers.",
    )


class RuleBasedBudget(StrictModel):
    isProcessing: bool | None = Field(default=None)
    applicableRuleName: str | None = Field(default=None)
    value: float | None = Field(default=None)
    applicableRuleId: str | None = Field(default=None)


class RuleCondition(StrictModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    metricName: Literal["COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS", "COST_PER_CLICK", "COST_PER_ORDER"] = Field(
        description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
|      MetricName      |ComparisonOperator  |Description|
|------------------|--------------------|-------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to `threshold`|
|COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to `threshold`|
|COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`|
"""
    )
    comparisonOperator: Literal["LESS_THAN_OR_EQUAL_TO"] = Field(description="The comparison operator.")
    threshold: float = Field(description="""
The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:
|                  MetricName            | Minimum of `threshold` Value  |
|----------------------------------------|-----------------------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 |
|COST_PER_CLICK                          | 0.5                               |
|COST_PER_ORDER                          | 5                                 |
""")


class SDForecastRequest(StrictModel):
    """Request payload for SD forecasting. Below are required and optional fields. Fields not listed will not impact forecast results.
    |Field              |Object            |Required|
    |-------------------|------------------|--------|
    |startDate          |Campaign          |required|
    |endDate            |Campaign          |optional|
    |costType           |Campaign          |optional|
    |bidOptimization    |AdGroup           |required|
    |creativeType       |AdGroup           |optional|
    |defaultBid         |AdGroup           |optional|
    |asin               |ProductAds        |required for vendors|
    |sku                |ProductAds        |required for sellers|
    |bid                |TargetingClauses  |required when defaultBid is not set|
    |expression         |TargetingClauses  |required|
    |ruleConditions     |OptimizationRules |optional|"""

    campaign: Campaign
    adGroup: AdGroup
    optimizationRules: list[OptimizationRule] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="A list of SD optimization rules. Forecast will be affected by the optimization strategy rules.  Currently, supported rule metrics by forecast are `COST_PER_CLICK`, `COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS` and `COST_PER_ORDER`.",
    )
    productAds: list[ProductAd] = Field(min_length=1, max_length=100)
    targetingClauses: list[SDForecastRequestTargetingClause] = Field(
        min_length=1, max_length=100, description="A list of SD targeting clauses."
    )
    negativeTargetingClauses: list[NegativeTargetingClause] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of SD negative targeting clauses."
    )
    locationExpressions: list[LocationExpression] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="A list of location expressions. Only applicable for advertisers using landingPageType of OFF_AMAZON_LINK.",
    )


class SDForecastRequestTargetingClause(StrictModel):
    state: Literal["enabled", "paused", "archived"] | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: Literal["manual", "auto"] | None = Field(
        default=None, description="Tactic T00020 & T00030 ad groups should use 'manual' targeting."
    )
    expression: TargetingExpression | None = Field(
        default=None, description="The targeting expression to match against."
    )
    resolvedExpression: TargetingExpression | None = Field(
        default=None, description="The resolved targeting expression."
    )


class SDForecastResponse(LenientModel):
    """Response to a request for SD forecasting."""

    bidOptimization: str | None = Field(default=None)
    lifetimeForecasts: list[Forecast] | None = Field(
        default=None,
        min_length=1,
        max_length=4,
        description="Forecasts for campaign start date and end date. Default end date is start date plus 7 days.",
    )
    weeklyForecasts: list[Forecast] | None = Field(
        default=None, min_length=1, max_length=4, description="Weekly average forecasts."
    )
    dailyForecasts: list[Forecast] | None = Field(
        default=None, min_length=1, max_length=4, description="Daily average forecasts."
    )
    curves: list[Curve] | None = Field(default=None, min_length=0, max_length=10, description="Forecasting curves.")
    forecastStatus: ForecastStatus | str | None = Field(default=None)


class TargetingExpression(StrictModel):
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


class TargetingPredicateLegacy(StrictModel):
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
        | None
    ) = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")
    eventType: Literal["views"] | None = Field(
        default=None,
        description="""
The type of event that the value applies to. Only available for similarProduct and exactProduct currently.
* views event type corresponds to a customer who viewed the detail page of the product(s).
""",
    )


__all__ = [
    "AdGroup",
    "AdGroupId",
    "AdId",
    "AdName",
    "BaseAdGroup",
    "BaseCampaign",
    "BaseNegativeTargetingClause",
    "BaseOptimizationRule",
    "BaseProductAd",
    "BaseTargetingClause",
    "Campaign",
    "CampaignId",
    "ContentTargetingPredicate",
    "CreativeType",
    "Curve",
    "CurvePoint",
    "CurvePointFixedValue",
    "CurvePointRangedValue",
    "Forecast",
    "ForecastRange",
    "ForecastRangeDouble",
    "ForecastStatus",
    "LandingPageType",
    "LandingPageURL",
    "LocationExpression",
    "LocationPredicate",
    "NegativeTargetingClause",
    "NegativeTargetingExpression",
    "OptimizationRule",
    "ProductAd",
    "RuleBasedBudget",
    "RuleCondition",
    "RuleId",
    "SDForecastRequest",
    "SDForecastRequestTargetingClause",
    "SDForecastResponse",
    "Tactic",
    "TargetId",
    "TargetingExpression",
    "TargetingPredicate",
    "TargetingPredicateBase",
    "TargetingPredicateLegacy",
    "TargetingPredicateNested",
]
