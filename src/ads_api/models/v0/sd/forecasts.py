"""Auto-generated models for Forecasts from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Any

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
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


class CreativeType(StrEnum):
    """
    The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. One ad group only supports one type (VIDEO or IMAGE) of creativeType at a time.
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class ForecastStatus(StrEnum):
    """
    It contains the forecast status. The IMPRESSION_TARGETING_TOO_NARROW field means the targeting  clauses are too narrow, and the IMPRESSION_TARGETING_TOO_BROAD field means the targeting clauses are too broad,  so our inventory impression forecast won't provide any useful information. The COMPLETE field means all the forecasts are complete.
    """

    IMPRESSION_TARGETING_TOO_NARROW = "IMPRESSION_TARGETING_TOO_NARROW"
    IMPRESSION_TARGETING_TOO_BROAD = "IMPRESSION_TARGETING_TOO_BROAD"
    COMPLETE = "COMPLETE"


class LandingPageType(StrEnum):
    """
    The type of the landingPage used. This field is completely optional and will be set in conjunction with the LandingPageURL to indicate the type of landing page that will be set. This field is not supported when using ASIN or SKU fields.
    """

    STORE = "STORE"
    MOMENT = "MOMENT"
    OFF_AMAZON_LINK = "OFF_AMAZON_LINK"


class AdGroup(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: str | None = Field(
        default=None, description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks."
    )
    state: str | None = Field(default=None, description="The state of the ad group.")
    adGroupId: AdGroupId | None = Field(default=None)
    tactic: Annotated[Tactic, lenient_enum(Tactic)] | None = Field(default=None)
    creativeType: Annotated[CreativeType, lenient_enum(CreativeType)] | None = Field(default=None)


class BaseOptimizationRule(StrictModel):
    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class Campaign(StrictModel):
    name: str | None = Field(default=None, description="The name of the campaign.")
    budgetType: str | None = Field(
        default=None,
        description="The time period over which the amount specified in the `budget` property is allocated.",
    )
    budget: float | None = Field(default=None, description="The amount of the budget.")
    startDate: str | None = Field(
        default=None, description="The YYYYMMDD start date of the campaign. The date must be today or in the future."
    )
    endDate: str | None = Field(default=None, description="The YYYYMMDD end date of the campaign.")
    costType: str | None = Field(
        default=None,
        description="""
Determines how the campaign will bid and charge.
To view minimum and maximum bids based on the costType, see [Limits](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace).
""",
    )
    state: str | None = Field(default=None, description="The state of the campaign.")
    portfolioId: int | None = Field(
        default=None,
        description="Identifier of the portfolio that will be associated with the campaign. If null then the campaign will be disassociated from existing portfolio. Campaigns with CPC and vCPM costType are supported.",
    )
    campaignId: CampaignId | None = Field(default=None)
    tactic: Annotated[Tactic, lenient_enum(Tactic)] | None = Field(default=None)
    deliveryProfile: str | None = Field(default=None)
    ruleBasedBudget: RuleBasedBudget | None = Field(default=None)


class Curve(LenientModel):
    """Forecast curve of a certain type. The type could be budget vs forecast outcome."""

    meetThreshold: bool | None = Field(
        default=None, description="True if the budget utilization is good to show the curve."
    )
    graph: str | None = Field(default=None, description="Type of Graph.")
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

    label: str | None = Field(default=None, description="KPI label.")
    value: ForecastRangeDouble | None = Field(default=None)


class Forecast(LenientModel):
    """Forecast impressions, clicks, reach, or conversions."""

    metric: str | None = Field(default=None, description="Describes which metric is forecasted.")
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
    state: str | None = Field(default=None)
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: str | None = Field(default=None)
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
    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: RuleId | None = Field(default=None)


class ProductAd(StrictModel):
    state: str | None = Field(default=None, description="The state of the campaign associated with the product ad.")
    adId: AdId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    campaignId: CampaignId | None = Field(default=None)
    landingPageURL: LandingPageURL | None = Field(default=None)
    landingPageType: Annotated[LandingPageType, lenient_enum(LandingPageType)] | None = Field(default=None)
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

    metricName: str = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
""")
    comparisonOperator: str = Field(description="The comparison operator.")
    threshold: float = Field(
        description="The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:"
    )


class SDForecastRequest(StrictModel):
    """Request payload for SD forecasting. Below are required and optional fields. Fields not listed will not impact forecast results."""

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
    state: str | None = Field(default=None)
    bid: float | None = Field(
        default=None,
        ge=0.02,
        description="The bid will override the adGroup bid if specified. This field is not used for negative targeting clauses. The bid must be less than the maximum allowable bid for the campaign's marketplace; for a list of maximum allowable bids, find the [\"Bid constraints by marketplace\" table in our documentation overview](https://advertising.amazon.com/API/docs/en-us/concepts/limits#bid-constraints-by-marketplace). You cannot manually set a bid when the targeting clause's adGroup has an enabled optimization rule.",
    )
    targetId: TargetId | None = Field(default=None)
    adGroupId: AdGroupId | None = Field(default=None)
    expressionType: str | None = Field(
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
    forecastStatus: Annotated[ForecastStatus | str, lenient_enum(ForecastStatus)] | None = Field(default=None)


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
    type: str | None = Field(default=None)
    value: str | None = Field(default=None, description="The value to be targeted.")
    eventType: str | None = Field(
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
