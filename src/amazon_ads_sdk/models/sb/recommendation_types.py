"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations


from pydantic import BaseModel, ConfigDict


class SBQueryRecommendationTypeRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = None
    nextToken: str | None = None


class SBRecommendationType(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    recommendationTypeId: str  # The ID of the recommendation type. Format: Either a UUID or a unique descriptive string identifier
    recommendationTypeTitle: str  # Titles or short descriptions of the recommendation


class SBRecommendationTypeSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    recommendationTypes: list[SBRecommendationType] | None = None
