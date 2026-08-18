"""Auto-generated models for Keyword Targets from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models.v0._shared import (
    ImpactMetric,
    ImpactMetrics,
    RangeMetricValue,
)

type KeywordBidInfoMatchType = Literal["BROAD", "EXACT", "PHRASE"]
"""
Keyword match type. The default value will be BROAD.
"""


type KeywordTargetMatchType = Literal["BROAD", "EXACT", "PHRASE"]
"""
Keyword match type. The default value will be BROAD.
"""


type ThemedBidMatchType = Literal["BROAD", "EXACT", "PHRASE"]
"""
Keyword match type. The default value will be BROAD.
"""


class BidSuggestion(LenientModel):
    """Suggested bid range in major and minor currency units (example: dollars and cents)."""

    bidRecId: str | None = Field(default=None, description="The bid recommendation id")
    rangeEnd: float | None = Field(default=None, description="The bid range end")
    rangeStart: float | None = Field(default=None, description="The bid range start")
    suggested: float | None = Field(default=None, description="The suggested bid")


class BidValues(LenientModel):
    """Suggested bid range"""

    rangeEnd: float | None = Field(default=None, description="The bid range end")
    rangeStart: float | None = Field(default=None, description="The bid range start")
    suggested: float | None = Field(default=None, description="The suggested bid")


class GlobalRankedTargetWithThemedBidsResponse(LenientModel):
    countryCodes: dict[str, RankedTargetWithThemedBidsResponse] | None = Field(default=None)


class KeywordBidInfo(LenientModel):
    bid: float | None = Field(
        default=None,
        description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.",
    )
    matchType: KeywordBidInfoMatchType | str | None = Field(
        default=None, description="Keyword match type. The default value will be BROAD."
    )
    rank: float | None = Field(default=None, description="The keyword target rank")
    suggestedBid: BidSuggestion | None = Field(default=None)


class KeywordTarget(LenientModel):
    bid: float | None = Field(
        default=None,
        description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.",
    )
    keyword: str | None = Field(default=None, description="The keyword value")
    matchType: KeywordTargetMatchType | str | None = Field(
        default=None, description="Keyword match type. The default value will be BROAD."
    )
    userSelectedKeyword: bool | None = Field(
        default=None, description="Flag that tells if keyword was selected by the user or was recommended by KRS"
    )


class KeywordTargetResponse(LenientModel):
    bid: float | None = Field(
        default=None,
        description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.",
    )
    keyword: str | None = Field(default=None, description="The keyword value")
    matchType: KeywordTargetMatchType | str | None = Field(
        default=None, description="Keyword match type. The default value will be BROAD."
    )
    userSelectedKeyword: bool | None = Field(
        default=None, description="Flag that tells if keyword was selected by the user or was recommended by KRS"
    )


class RankedTargetResponse(LenientModel):
    keywordTargetList: list[dict[str, Any]] | None = Field(
        default=None, min_length=0, max_length=200, description="A list of ranked keyword targets"
    )


class RankedTargetWithThemedBids(LenientModel):
    bidInfo: list[dict[str, Any]] | None = Field(
        default=None, min_length=0, max_length=15, description="A list of keyword bid info"
    )
    keyword: str | None = Field(default=None, description="The keyword value")
    recId: str | None = Field(default=None, description="The recommended keyword target id")
    searchTermImpressionRank: float | None = Field(
        default=None,
        description="The account-level ad-attributed impression rank for the search-term/keyword. Provides [1:N] place the advertiser ranks among all advertisers for the keyword by ad impressions in a marketplace in the last 30 days. It tells an advertiser how many advertisers had higher share of ad impressions. This information is only available for keywords the advertiser targeted with ad impressions.",
    )
    searchTermImpressionShare: float | None = Field(
        default=None,
        description="The account-level ad-attributed impression share for the search-term/keyword. Provides percentage share of all ad impressions the advertiser has for the keyword in the last 30 days. This metric helps advertisers identify potential opportunities based on their share on relevant keywords. This information is only available for keywords the advertiser targeted with ad impressions.",
    )
    translation: str | None = Field(default=None, description="The translation of keyword if a locale is passed in")
    userSelectedKeyword: bool | None = Field(
        default=None, description="Flag that tells if keyword was selected by the user or was recommended by KRS"
    )


class RankedTargetWithThemedBidsList(LenientModel):
    pass


class RankedTargetWithThemedBidsResponse(LenientModel):
    impactMetrics: list[ImpactMetrics] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="A list of impact metrics which anticipates the number of clicks and orders you will receive if you target all targeting expressions using the low, medium, and high suggested bid.",
    )
    keywordTargetList: RankedTargetWithThemedBidsList | None = Field(default=None)


class RecKeywordTarget(LenientModel):
    bidInfo: list[dict[str, Any]] | None = Field(
        default=None, min_length=0, max_length=3, description="A list of keyword bid info"
    )
    keyword: str | None = Field(default=None, description="The keyword value")
    recId: str | None = Field(default=None, description="The recommended keyword target id")
    searchTermImpressionRank: float | None = Field(
        default=None,
        description="The account-level ad-attributed impression rank for the search-term/keyword. Provides [1:N] place the advertiser ranks among all advertisers for the keyword by ad impressions in a marketplace in the last 30 days. It tells an advertiser how many advertisers had higher share of ad impressions. This information is only available for keywords the advertiser targeted with ad impressions.",
    )
    searchTermImpressionShare: float | None = Field(
        default=None,
        description="The account-level ad-attributed impression share for the search-term/keyword. Provides percentage share of all ad impressions the advertiser has for the keyword in the last 30 days. This metric helps advertisers identify potential opportunities based on their share on relevant keywords. This information is only available for keywords the advertiser targeted with ad impressions.",
    )
    translation: str | None = Field(default=None, description="The translation of keyword if a locale is passed in")
    userSelectedKeyword: bool | None = Field(
        default=None, description="Flag that tells if keyword was selected by the user or was recommended by KRS"
    )


class ThemedBid(LenientModel):
    bid: float | None = Field(
        default=None,
        description="The bid value for the keyword, in minor currency units (example: cents). The default value will be the suggested bid.",
    )
    matchType: ThemedBidMatchType | str | None = Field(
        default=None, description="Keyword match type. The default value will be BROAD."
    )
    rank: float | None = Field(default=None, description="The keyword target rank.")
    suggestedBid: BidValues | None = Field(default=None)
    theme: str | None = Field(
        default=None, description="The theme of the bid recommendation. The default theme is CONVERSION_OPPORTUNITIES."
    )


__all__ = [
    "BidSuggestion",
    "BidValues",
    "GlobalRankedTargetWithThemedBidsResponse",
    "ImpactMetric",
    "ImpactMetrics",
    "KeywordBidInfo",
    "KeywordBidInfoMatchType",
    "KeywordTarget",
    "KeywordTargetMatchType",
    "KeywordTargetResponse",
    "RangeMetricValue",
    "RankedTargetResponse",
    "RankedTargetWithThemedBids",
    "RankedTargetWithThemedBidsList",
    "RankedTargetWithThemedBidsResponse",
    "RecKeywordTarget",
    "ThemedBid",
    "ThemedBidMatchType",
]
