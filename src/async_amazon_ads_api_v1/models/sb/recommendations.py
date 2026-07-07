"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class SBAlternateBrandIdType(StrEnum):
    """The type of identifier for the alternate brand identifier.

    | AlternateBrandIdType | Description |
    |------|------|
    | `BRAND_REGISTRY` | Previous version of brand identifier retrieved from BrandRegistry. Identifiers of this type are returned by the GET /brands operation. |
    """

    BRAND_REGISTRY = "BRAND_REGISTRY"


class SBBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    model_config = ConfigDict(extra="forbid")

    alternateBrandId: str  # The alternative brand identifier for the brandId.
    alternateBrandIdType: Annotated[SBAlternateBrandIdType | str, lenient_enum(SBAlternateBrandIdType)]


class SBBrandedKeyword(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandAlternateId: SBBrandAlternateId
    keyword: str  # Branded keyword


class SBBrandedKeywordList(BaseModel):
    model_config = ConfigDict(extra="forbid")

    associatedBrandIds: list[str] | None = None  # Brand IDs associated with the branded keyword list
    brandedKeyword: list[SBBrandedKeyword] | None = (
        None  # Branded keywords are specific words or phrases that include a company's brand name or a registered trademark of a brand
    )


class SBBrandedKeywordRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandAlternateId: list[SBBrandAlternateId]
    brandIds: list[str] | None = None  # The brand ID to scope branded keyword recommendations for


class SBCreateBrandAlternateId(BaseModel):
    """Other types of brand identifiers for a brand that are used with other operations."""

    model_config = ConfigDict(extra="forbid")

    alternateBrandId: str  # The alternative brand identifier for the brandId.
    alternateBrandIdType: Annotated[SBAlternateBrandIdType | str, lenient_enum(SBAlternateBrandIdType)]


class SBCreateBrandedKeywordRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandAlternateId: list[SBCreateBrandAlternateId]
    brandIds: list[str] | None = None  # The brand ID to scope branded keyword recommendations for


class SBCreateRecommendationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recommendations: list[SBRecommendationCreate] | None = None


class SBCreateRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedKeywordRecommendationTypeDetails: SBCreateBrandedKeywordRecommendationTypeDetails | None = None


class SBObjectSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedKeywordList: SBBrandedKeywordList | None = None


class SBRecommendation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recommendationId: str  # The identifier of the recommendation
    recommendationType: str  # A unique value to indicate similar recommendations, used for internal purposes only
    recommendationTypeDetails: SBRecommendationTypeDetails | None = None
    recommendedObjects: list[SBRecommendedObject]  # The target objects of the recommendation


class SBRecommendationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recommendationType: str  # A unique value to indicate similar recommendations, used for internal purposes only
    recommendationTypeDetails: SBCreateRecommendationTypeDetails | None = None


class SBRecommendationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBRecommendationMultiStatusSuccess] | None = None


class SBRecommendationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    recommendation: SBRecommendation


class SBRecommendationTypeDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedKeywordRecommendationTypeDetails: SBBrandedKeywordRecommendationTypeDetails | None = None


class SBRecommendedObject(BaseModel):
    """Details of the recommended object"""

    model_config = ConfigDict(extra="forbid")

    recommendedObjectSettings: SBObjectSettings | None = None


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
    "SBObjectSettings",
    "SBRecommendation",
    "SBRecommendationCreate",
    "SBRecommendationMultiStatusResponse",
    "SBRecommendationMultiStatusSuccess",
    "SBRecommendationTypeDetails",
    "SBRecommendedObject",
]
