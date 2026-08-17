"""Auto-generated models for RecommendationTypes from Amazon Ads API v1."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class SBQueryRecommendationTypeRequest(StrictModel):
    maxResults: int | None = Field(default=50, ge=50, le=500)
    nextToken: str | None = Field(default=None)


class SBRecommendationType(LenientModel):
    recommendationTypeId: str = Field(
        description="The ID of the recommendation type. Format: Either a UUID or a unique descriptive string identifier"
    )
    recommendationTypeTitle: str = Field(description="Titles or short descriptions of the recommendation")


class SBRecommendationTypeSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    recommendationTypes: list[SBRecommendationType] | None = Field(default=None, min_length=0, max_length=500)


__all__ = ["SBQueryRecommendationTypeRequest", "SBRecommendationType", "SBRecommendationTypeSuccessResponse"]
