"""Auto-generated models for Recommendations from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorCode, ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SBAlternateBrandIdType(StrEnum):
    """
    The type of identifier for the alternate brand identifier.

    | AlternateBrandIdType | Description |
    |------|------|
    | `BRAND_REGISTRY` | Previous version of brand identifier retrieved from BrandRegistry. Identifiers of this type are returned by the GET /brands operation. |
    """

    BRAND_REGISTRY = "BRAND_REGISTRY"


class SBBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    model_config = ConfigDict(extra="allow")

    alternateBrandId: str | None = Field(default=None, description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: Annotated[SBAlternateBrandIdType | str, lenient_enum(SBAlternateBrandIdType)] | None = Field(
        default=None
    )


class SBBrandedKeyword(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandAlternateId: SBBrandAlternateId | None = Field(default=None)
    keyword: str | None = Field(default=None, description="Branded keyword")


class SBBrandedKeywordList(BaseModel):
    model_config = ConfigDict(extra="allow")

    associatedBrandIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Brand IDs associated with the branded keyword list"
    )
    brandedKeyword: list[SBBrandedKeyword] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Branded keywords are specific words or phrases that include a company's brand name or a registered trademark of a brand",
    )


class SBBrandedKeywordRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandAlternateId: list[SBBrandAlternateId] | None = Field(default=None, min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    model_config = ConfigDict(extra="forbid")

    alternateBrandId: str = Field(description="The alternative brand identifier for the brandId.")
    alternateBrandIdType: Annotated[SBAlternateBrandIdType | str, lenient_enum(SBAlternateBrandIdType)]


class SBCreateBrandedKeywordRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandAlternateId: list[SBCreateBrandAlternateId] = Field(min_length=1, max_length=1)
    brandIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="The brand ID to scope branded keyword recommendations for",
    )


class SBCreateRecommendationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recommendations: list[SBRecommendationCreate] | None = Field(default=None, min_length=1, max_length=1)


class SBCreateRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedKeywordRecommendationTypeDetails: SBCreateBrandedKeywordRecommendationTypeDetails | None = None


class SBObjectSettings(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandedKeywordList: SBBrandedKeywordList | None = None


class SBRecommendation(BaseModel):
    model_config = ConfigDict(extra="allow")

    recommendationId: str | None = Field(default=None, description="The identifier of the recommendation")
    recommendationType: str | None = Field(
        default=None, description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBRecommendationTypeDetails | None = Field(default=None)
    recommendedObjects: list[SBRecommendedObject] | None = Field(
        default=None, min_length=1, max_length=10, description="The target objects of the recommendation"
    )


class SBRecommendationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recommendationType: str = Field(
        description="A unique value to indicate similar recommendations, used for internal purposes only"
    )
    recommendationTypeDetails: SBCreateRecommendationTypeDetails | None = Field(default=None)


class SBRecommendationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[SBRecommendationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class SBRecommendationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=0)
    recommendation: SBRecommendation | None = Field(default=None)


class SBRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandedKeywordRecommendationTypeDetails: SBBrandedKeywordRecommendationTypeDetails | None = None


class SBRecommendedObject(BaseModel):
    """Details of the recommended object"""

    model_config = ConfigDict(extra="allow")

    recommendedObjectSettings: SBObjectSettings | None = Field(default=None)


__all__ = [
    "ErrorCode",
    "SBAlternateBrandIdType",
    "SBCreateBrandAlternateId",
    "SBCreateBrandedKeywordRecommendationTypeDetails",
    "SBCreateRecommendationRequest",
    "SBCreateRecommendationTypeDetails",
    "SBRecommendationCreate",
]
