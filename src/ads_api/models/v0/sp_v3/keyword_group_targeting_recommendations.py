"""Auto-generated models for Keyword Group Targeting Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class KeywordGroup(LenientModel):
    """Keyword group. Represents a high level keyword targeting intent. e.g. the keyword group "gift" can target relevant search queries containing the word gift"""

    description: str | None = Field(default=None, description="Detailed Keyword group description.")
    id: str = Field(
        description="Unique Identifier for the keyword group. To be passed during targeting clause creation."
    )
    impactSummary: str | None = Field(default=None, description="Summary of impacts.")
    sampleKeywords: list[str] | None = Field(
        default=None, min_length=0, max_length=10, description="Sample keywords that match the group."
    )
    text: str = Field(description="Keyword group text. Can be used for display purposes.")


class KeywordGroupsRecommendationsRequest(StrictModel):
    """Keyword groups request."""

    asins: list[str] = Field(min_length=1, max_length=1000, description="List of ASINs.")
    countryCode: str | None = Field(
        default=None,
        description="The country code representing the origin country of the input ASIN list, it will be used for generating keyword group recommendations.",
    )
    nextToken: str | None = Field(
        default=None, description="If the last response included this field then there are more items to retrieve."
    )


class KeywordGroupsRecommendationsResponse(LenientModel):
    """Keyword group recommendations response."""

    countryCode: str | None = Field(
        default=None,
        description="The country code representing the origin country of the input ASIN list, used for generating keyword group recommendations.",
    )
    keywordGroups: list[KeywordGroup] = Field(
        min_length=0, max_length=50, description="Keyword group recommendations for input list of ASINs."
    )
    nextToken: str | None = Field(
        default=None,
        description="If present then there is more data to retrieve. To retrieve, resend request with token.",
    )


__all__ = ["KeywordGroup", "KeywordGroupsRecommendationsRequest", "KeywordGroupsRecommendationsResponse"]
