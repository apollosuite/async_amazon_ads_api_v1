"""target models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SPCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: dict[str, Any]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: dict[str, Any] | None = None
class SPCreateLocationTarget(BaseModel):
    """Target based on geographic location."""
    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.
class SPCreateProductCategoryRefinement(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productBrandId: str | None = None  # The brand ID to target.
    productCategoryId: str | None = None  # The product category ID to target.
    productGenreId: str | None = None  # The product genre ID to target.
    productPriceGreaterThan: float | None = None  # Refinement to target products with a price greater than the value within the pro
    productPriceLessThan: float | None = None  # Refinement to target products with a price less than the value within the produc
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = None  # Refinement to target products with a rating greater than the value within the pr
    productRatingLessThan: float | None = None  # Refinement to target products with a rating less than the value within the produ
class SPCreateProductCategoryRefinementValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]
class SPCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]
class SPCreateProductTarget(BaseModel):
    """Targets a specific product."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
    product: dict[str, Any]
    productIdType: dict[str, Any]
class SPCreateTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
class SPCreateTargetDetails(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
class SPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: dict[str, Any]
    nativeLanguageKeyword: str | None = None  # The unlocalized keyword text in the preferred locale of the advertiser.
    nativeLanguageLocale: dict[str, Any] | None = None
class SPLocationTarget(BaseModel):
    """Target based on geographic location."""
    model_config = ConfigDict(extra="forbid")

    locationId: str  # The ID of the geographic location to target.
class SPProductCategoryRefinement(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productAgeRangeId: str | None = None  # The age range ID to target.
    productAgeRangeIdResolved: str | None = None  # The resolved age range to target.
    productBrandId: str | None = None  # The brand ID to target.
    productBrandIdResolved: str | None = None  # The resolved name of the brand.
    productCategoryId: str | None = None  # The product category ID to target.
    productCategoryIdResolved: str | None = None  # The resolved product category.
    productGenreId: str | None = None  # The product genre ID to target.
    productGenreIdResolved: str | None = None  # The resolved product genre to target.
    productPriceGreaterThan: float | None = None  # Refinement to target products with a price greater than the value within the pro
    productPriceLessThan: float | None = None  # Refinement to target products with a price less than the value within the produc
    productPrimeShippingEligible: bool | None = None  # Target based on if a product is Prime-shipping eligible.
    productRatingGreaterThan: float | None = None  # Refinement to target products with a rating greater than the value within the pr
    productRatingLessThan: float | None = None  # Refinement to target products with a rating less than the value within the produ
class SPProductCategoryRefinementValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]
class SPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""
    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: dict[str, Any]
class SPProductTarget(BaseModel):
    """Targets a specific product."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
    product: dict[str, Any]
    productIdType: dict[str, Any]
class SPTarget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = None  # A unique identifier for the ad group associated with the target. Only used for a
    adProduct: dict[str, Any]
    bid: dict[str, Any] | None = None
    campaignId: str | None = None  # A unique identifier for the campaign associated with the target. Only used for c
    creationDateTime: datetime  # The date time the target was created.
    globalTargetId: str | None = None  # The global target identifier that manages this marketplace target.
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[dict[str, Any]]  # The list of marketplace in which the global target is applicable. The marketplac
    negative: bool  # Indicates whether the target is negative or not.
    state: dict[str, Any]
    status: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: dict[str, Any]
    targetId: str  # A unique identifier for the target.
    targetLevel: dict[str, Any]
    targetType: dict[str, Any]
class SPTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
    currencyCode: dict[str, Any]
class SPTargetCreate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = None  # A unique identifier for the ad group associated with the target. Only used for a
    adProduct: dict[str, Any]
    bid: dict[str, Any] | None = None
    campaignId: str | None = None  # A unique identifier for the campaign associated with the target. Only used for c
    negative: bool  # Indicates whether the target is negative or not.
    state: dict[str, Any]
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: dict[str, Any]
    targetType: dict[str, Any]
class SPTargetDetails(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPTargetMultiStatusSuccess(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    index: int
    target: dict[str, Any]
class SPTargetUpdate(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: dict[str, Any] | None = None
    state: dict[str, Any] | None = None
    tags: list[dict[str, Any]] | None = None  # Open ended labels with a key value pair applied to the target
    targetId: str  # A unique identifier for the target.
class SPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""
    model_config = ConfigDict(extra="forbid")

    matchType: dict[str, Any]
class SPUpdateTargetBid(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.

