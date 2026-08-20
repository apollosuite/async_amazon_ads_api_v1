"""Auto-generated models for Recommendations from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBError,
    SBErrorCode,
    SBErrorsIndex,
)

type SBAlternateBrandIdType = Literal["BRAND_REGISTRY"]
"""
The type of identifier for the alternate brand identifier.

Supported values:
- `BRAND_REGISTRY`: Previous version of brand identifier retrieved from BrandRegistry. Identifiers of this type are returned by the GET /brands operation.
"""


class SBBrandAlternateId(LenientModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    alternateBrandId: str = Field(description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: SBAlternateBrandIdType | str


class SBBrandedKeyword(LenientModel):
    brandAlternateId: SBBrandAlternateId
    keyword: str = Field(description="Branded keyword")


class SBBrandedKeywordList(LenientModel):
    associatedBrandIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Brand IDs associated with the branded keyword list"
    )
    brandedKeyword: list[SBBrandedKeyword] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Branded keywords are specific words or phrases that include a company's brand name or a registered trademark of a brand",
    )


class SBBrandedKeywordRecommendationTypeDetails(LenientModel):
    brandAlternateId: list[SBBrandAlternateId] = Field(min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateBrandAlternateId(StrictModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    alternateBrandId: str = Field(description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: SBAlternateBrandIdType


class SBCreateBrandedKeywordRecommendationTypeDetails(StrictModel):
    brandAlternateId: list[SBCreateBrandAlternateId] = Field(min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateRecommendationRequest(StrictModel):
    recommendations: list[SBRecommendationCreate] | None = Field(default=None, min_length=1, max_length=1)


class SBCreateRecommendationTypeDetails(StrictModel):
    brandedKeywordRecommendationTypeDetails: SBCreateBrandedKeywordRecommendationTypeDetails


class SBObjectSettings(LenientModel):
    brandedKeywordList: SBBrandedKeywordList


class SBRecommendation(LenientModel):
    recommendationId: str = Field(description="The identifier of the recommendation")
    recommendationType: str = Field(
        description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBRecommendationTypeDetails | None = Field(default=None)
    recommendedObjects: list[SBRecommendedObject] = Field(
        min_length=1, max_length=10, description="The target objects of the recommendation"
    )


class SBRecommendationCreate(StrictModel):
    recommendationType: str = Field(
        description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBCreateRecommendationTypeDetails | None = Field(default=None)


class SBRecommendationMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[SBRecommendationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class SBRecommendationMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=0)
    recommendation: SBRecommendation


class SBRecommendationTypeDetails(LenientModel):
    brandedKeywordRecommendationTypeDetails: SBBrandedKeywordRecommendationTypeDetails


class SBRecommendedObject(LenientModel):
    """Details of the recommended object"""

    recommendedObjectSettings: SBObjectSettings | None = Field(default=None)


__all__ = [
    "SBAlternateBrandIdType",
    "SBBrandAlternateId",
    "SBBrandedKeyword",
    "SBBrandedKeywordList",
    "SBBrandedKeywordRecommendationTypeDetails",
    "SBCreateBrandAlternateId",
    "SBCreateBrandedKeywordRecommendationTypeDetails",
    "SBCreateRecommendationRequest",
    "SBCreateRecommendationTypeDetails",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBObjectSettings",
    "SBRecommendation",
    "SBRecommendationCreate",
    "SBRecommendationMultiStatusResponse",
    "SBRecommendationMultiStatusSuccess",
    "SBRecommendationTypeDetails",
    "SBRecommendedObject",
]
