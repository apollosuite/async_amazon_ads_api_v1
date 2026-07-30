"""Auto-generated models for RecommendationTypes from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SBQueryRecommendationTypeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = Field(default=50, ge=50, le=500)
    nextToken: str | None = Field(default=None)


class SBRecommendationType(BaseModel):
    model_config = ConfigDict(extra="allow")

    recommendationTypeId: str | None = Field(
        default=None,
        description="The ID of the recommendation type. Format: Either a UUID or a unique descriptive string identifier",
    )
    recommendationTypeTitle: str | None = Field(
        default=None, description="Titles or short descriptions of the recommendation"
    )


class SBRecommendationTypeSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(default=None)
    recommendationTypes: list[SBRecommendationType] | None = Field(default=None, min_length=0, max_length=500)


__all__ = ["SBQueryRecommendationTypeRequest", "SBRecommendationType", "SBRecommendationTypeSuccessResponse"]
