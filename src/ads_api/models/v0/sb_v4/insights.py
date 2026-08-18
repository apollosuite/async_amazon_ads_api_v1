"""Auto-generated models for Insights from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class SBInsightsAdFormat(StrEnum):
    """
    Type of Ad format.
    """

    PRODUCT_COLLECTION = "PRODUCT_COLLECTION"
    STORE_SPOTLIGHT = "STORE_SPOTLIGHT"
    VIDEO = "VIDEO"
    BRAND_VIDEO = "BRAND_VIDEO"


class SBInsightsKeywordAlertType(StrEnum):
    """
    Keyword alert insights associated with the selected keyword targets and bids.
    LOW_KEYWORD_TRAFFIC is provided if the keyword has very low traffic and is available in all marketplaces.
    LOW_BID is provided if the selected bid is low compared to the historical bids for this keyword
    and is only available in the following marketplaces: US, CA, MX, BR, UK, DE, FR, ES, IT, IN, AE, NL, SE, JP, AU, SG.
    """

    LOW_KEYWORD_TRAFFIC = "LOW_KEYWORD_TRAFFIC"
    LOW_BID = "LOW_BID"


class SBInsightsMatchType(StrEnum):
    """
    The match type. For more information, see [match types](https://advertising.amazon.com/help#GHTRFDZRJPW6764R) in the Amazon Advertising support center.
    """

    EXACT = "EXACT"
    PHRASE = "PHRASE"
    BROAD = "BROAD"


class SBInsightsAdGroup(StrictModel):
    """The ad group settings."""

    keywords: list[SBInsightsKeyword] | None = Field(default=None, min_length=0, max_length=800)
    adFormat: Annotated[SBInsightsAdFormat | str, lenient_enum(SBInsightsAdFormat)]


class SBInsightsCampaignInsightsRequestContent(StrictModel):
    adGroups: list[SBInsightsAdGroup] = Field(min_length=0, max_length=100)


class SBInsightsCampaignInsightsResponseContent(LenientModel):
    """Response object for /sb/campaigns/insights containing a list of insights for the campaign."""

    insights: list[SBInsightsObject] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(
        default=None,
        description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results, call the same operation and specify this token in the request. If the `NextToken` field is empty, there are no further results.",
    )


class SBInsightsKeyword(StrictModel):
    """Keyword associated with the campaign."""

    matchType: Annotated[SBInsightsMatchType | str, lenient_enum(SBInsightsMatchType)]
    bid: float = Field(
        description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account. For more information, see [supported features](https://advertising.amazon.com/API/docs/v2/guides/supported_features)."
    )
    keywordText: str = Field(description="The keyword text. Maximum of 10 words.")


class SBInsightsKeywordInsight(LenientModel):
    """Insights for keywords selected for targeting."""

    alerts: list[Annotated[SBInsightsKeywordAlertType | str, lenient_enum(SBInsightsKeywordAlertType)]] | None = Field(
        default=None, min_length=0, max_length=10
    )
    searchTermImpressionShare: float | None = Field(
        default=None,
        ge=0,
        le=100,
        description="""
The account-level ad-attributed impression share for the search-term / keyword.
Provides percentage share of all ad impressions the advertiser has for the keyword in the last 7 days.
This metric helps advertisers identify potential opportunities based on their share of relevant keywords.
This information is only available for keywords the advertiser targeted with ad impressions.
Only available in the following marketplaces: US, CA, MX, UK, DE, FR, ES, IT, IN, JP.
""",
    )
    matchType: Annotated[SBInsightsMatchType | str, lenient_enum(SBInsightsMatchType)] | None = Field(default=None)
    adGroupIndex: int | None = Field(
        default=None,
        description="Correlates the ad group to the ad group array index specified in the request. Zero-based.",
    )
    searchTermImpressionRank: int | None = Field(
        default=None,
        description="""
The account-level ad-attributed impression rank for the search-term / keyword.
Provides the [1:N] place the advertiser ranks among all advertisers for the keyword by ad impressions in a marketplace in the last 7 days.
It tells an advertiser how many advertisers had higher share of ad impressions.
This information is only available for keywords the advertiser targeted with ad impressions.
Only available in the following marketplaces: US, CA, MX, UK, DE, FR, ES, IT, IN, JP.
""",
    )
    bid: float | None = Field(
        default=None,
        description="The associated bid. Note that this value must be less than the budget associated with the Advertiser account. For more information, see [supported features](https://advertising.amazon.com/API/docs/v2/guides/supported_features).",
    )
    keywordIndex: int | None = Field(
        default=None,
        description="Correlates the keyword to the keyword array index specified in the request. Zero-based.",
    )
    keywordText: str | None = Field(default=None, description="The keyword text. Maximum of 10 words.")


class SBInsightsObject(LenientModel):
    keywordInsight: SBInsightsKeywordInsight


__all__ = [
    "SBInsightsAdFormat",
    "SBInsightsAdGroup",
    "SBInsightsCampaignInsightsRequestContent",
    "SBInsightsCampaignInsightsResponseContent",
    "SBInsightsKeyword",
    "SBInsightsKeywordAlertType",
    "SBInsightsKeywordInsight",
    "SBInsightsMatchType",
    "SBInsightsObject",
]
