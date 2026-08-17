"""Auto-generated models for Forecasts from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class SBCampaignPerformanceForecastsRequestContent(StrictModel):
    campaigns: list[SBForecastingRequestCampaignObject] = Field(min_length=1, max_length=1)


class SBCampaignPerformanceForecastsResponseContent(LenientModel):
    """Response object for /sb/forecasts containing a list of performance forecast for the campaign."""

    campaigns: SBForecastingResponseCampaignObject | None = Field(default=None)


class SBForecastingAdGroup(StrictModel):
    """The ad group settings."""

    targets: list[SBForecastingProductTarget] | None = Field(default=None, min_length=0, max_length=100)
    negativeTargets: list[SBForecastingNegativeProductTarget] | None = Field(default=None, min_length=0, max_length=100)
    landingPages: list[SBForecastingLandingPageObject] | None = Field(default=None, min_length=0, max_length=100)
    themes: list[SBForecastingTheme] | None = Field(default=None, min_length=0, max_length=100)
    keywords: list[SBForecastingKeyword] | None = Field(default=None, min_length=0, max_length=100)
    negativeKeywords: list[SBForecastingNegativeKeyword] | None = Field(default=None, min_length=0, max_length=100)
    creativeAsins: list[str] | None = Field(default=None)


class SBForecastingErrorObject(LenientModel):
    index: int | None = Field(
        default=None,
        description="Correlates the campaign to the campaign list index specified in the request. Zero-based.",
    )
    code: str | None = Field(default=None, description="The forecast error code.")
    description: str | None = Field(default=None, description="The forecast error description.")


class SBForecastingKeyword(StrictModel):
    """Keyword associated with the campaign."""

    keywordText: str | None = Field(default=None, description="The keyword text. Maximum of 10 words.")
    matchType: str | None = Field(
        default=None,
        description="The match type. Valid value: EXACT, PHRASE, BROAD. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Advertising support center.",
    )
    bid: float | None = Field(
        default=None,
        description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.",
    )


class SBForecastingLandingPageObject(StrictModel):
    landingPageUrl: str | None = Field(default=None, description="Landing page information.")


class SBForecastingMetric(LenientModel):
    """The forecast metric."""

    metric: str | None = Field(
        default=None, description="The forecast metric name. Currently supported metrics are IMPRESSION and CLICK."
    )
    value: SBForecastingMetricValue | None = Field(default=None)


class SBForecastingMetricValue(LenientModel):
    """The forecast min and max value."""

    min: float | None = Field(default=None, ge=0.0, le=10000.0, description="The forecast min value.")
    max: float | None = Field(default=None, ge=0.0, le=10000.0, description="The forecast max value.")


class SBForecastingNegativeKeyword(StrictModel):
    """Negative keyword associated with the campaign."""

    keywordText: str | None = Field(default=None, description="The keyword text. Maximum of 10 words.")
    matchType: str | None = Field(
        default=None,
        description="The negative match type. Valid value: NEGATIVE_EXACT, NEGATIVE_PHRASE. For more information, see [negative keyword match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Advertising support center.",
    )


class SBForecastingNegativeProductExpression(StrictModel):
    """Negative expression settings for the target."""

    type: str | None = Field(
        default=None,
        description="The negative expression type associated with the target. Valid value: ASIN_BRAND_SAME_AS, ASIN_SAME_AS.",
    )
    value: str | None = Field(default=None, description="The expression value associated with targets.")


class SBForecastingNegativeProductTarget(StrictModel):
    """The negative target associated with the ad group."""

    expressions: list[SBForecastingNegativeProductExpression] | None = Field(default=None, min_length=0, max_length=100)


class SBForecastingProductExpression(StrictModel):
    """Expression settings for the target."""

    type: str | None = Field(
        default=None,
        description="The expression type associated with the target. Valid value: ASIN_CATEGORY_SAME_AS, ASIN_BRAND_SAME_AS, ASIN_PRICE_LESS_THAN, ASIN_PRICE_BETWEEN, ASIN_PRICE_GREATER_THAN, ASIN_REVIEW_RATING_LESS_THAN, ASIN_REVIEW_RATING_BETWEEN, ASIN_REVIEW_RATING_GREATER_THAN, ASIN_SAME_AS.",
    )
    value: str | None = Field(default=None, description="The expression value associated with targets.")


class SBForecastingProductTarget(StrictModel):
    """The target associated with the ad group."""

    expressions: list[SBForecastingProductExpression] | None = Field(default=None, min_length=0, max_length=100)
    bid: float | None = Field(
        default=None,
        description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.",
    )


class SBForecastingRequestCampaignObject(StrictModel):
    """The campaign settings."""

    budget: float = Field(description="The amount of the budget.")
    budgetType: str = Field(description="Budget can be set to DAILY or LIFETIME.")
    forecastType: str = Field(description="""
The forecast type. can be set to WEEKLY or MONTHLY.

**If have not set the forecastType during campaign creation then use WEEKLY as goal value.**
""")
    startDate: datetime | None = Field(
        default=None,
        description="The YYYY-MM-DD start date for the campaign. If this field is not set to a value, the current date is used.",
    )
    endDate: datetime | None = Field(
        default=None,
        description="The YYYY-MM-DD end date for the campaign. Must be greater than the value for `startDate`. If not specified, the campaign has no end date and runs continuously.",
    )
    goal: str | None = Field(
        default=None,
        description="""
Goal will allow you to set goal type to help drive your campaign performance.

**If have not set the goal during campaign creation then use PAGE_VISIT as goal type.**

The goal type of the campaign. Initial launch only supports PAGE_VISIT.

BRAND_IMPRESSION_SHARE - This goal is a PREVIEW ONLY and cannot be set currently. It will allow you grown your brand impression share on top of search placement.

PAGE_VISIT - This goal drives traffic to your landing and detail pages through all placements.

ACQUIRE_NEW_CUSTOMERS - This property is a PREVIEW ONLY and cannot be used as part of a request or response. This goal drives new customer acquisition for your brands.

AD_VIEWS - This property is a PREVIEW ONLY and cannot be used as part of a request or response. This goal maximizes view for your ads.
""",
    )
    adGroups: list[SBForecastingAdGroup] = Field(min_length=1, max_length=1)


class SBForecastingResponseCampaignObject(LenientModel):
    successes: list[SBForecastingSuccessObject] | None = Field(default=None, min_length=0, max_length=1)
    errors: list[SBForecastingErrorObject] | None = Field(default=None, min_length=0, max_length=1)


class SBForecastingSuccessCampaign(LenientModel):
    forecasts: list[SBForecastingMetric] | None = Field(default=None, min_length=1, max_length=2)
    forecastTimestamp: str | None = Field(default=None, description="The forecast timestamp.")


class SBForecastingSuccessObject(LenientModel):
    index: int | None = Field(
        default=None,
        description="Correlates the campaign to the campaign list index specified in the request. Zero-based.",
    )
    campaign: SBForecastingSuccessCampaign | None = Field(default=None)


class SBForecastingTheme(StrictModel):
    """The theme."""

    themeType: str | None = Field(
        default=None,
        description="""
The theme target type. Valid value: KEYWORDS_RELATED_TO_YOUR_BRAND, KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES.

KEYWORDS_RELATED_TO_YOUR_BRAND - keywords related to brands.

KEYWORDS_RELATED_TO_YOUR_LANDING_PAGES - keywords related to your landing pages.
""",
    )
    bid: float | None = Field(
        default=None,
        description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account.",
    )


__all__ = [
    "SBCampaignPerformanceForecastsRequestContent",
    "SBCampaignPerformanceForecastsResponseContent",
    "SBForecastingAdGroup",
    "SBForecastingErrorObject",
    "SBForecastingKeyword",
    "SBForecastingLandingPageObject",
    "SBForecastingMetric",
    "SBForecastingMetricValue",
    "SBForecastingNegativeKeyword",
    "SBForecastingNegativeProductExpression",
    "SBForecastingNegativeProductTarget",
    "SBForecastingProductExpression",
    "SBForecastingProductTarget",
    "SBForecastingRequestCampaignObject",
    "SBForecastingResponseCampaignObject",
    "SBForecastingSuccessCampaign",
    "SBForecastingSuccessObject",
    "SBForecastingTheme",
]
