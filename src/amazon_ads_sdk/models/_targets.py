"""target models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ads import SPCreateProductValue, SPProductValue
    from ._enums import (
        SPAdProduct,
        SPCreateState,
        SPCurrencyCode,
        SPKeywordMatchType,
        SPLanguageLocale,
        SPMarketplace,
        SPMarketplaceScope,
        SPProductIdType,
        SPProductMatchType,
        SPState,
        SPTargetLevel,
        SPTargetType,
        SPThemeMatchType,
        SPUpdateState,
    )
    from ._shared import SPCreateTag, SPStatus, SPTag


class SPCreateKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: SPKeywordMatchType
    nativeLanguageKeyword: str | None = (
        None  # The unlocalized keyword text in the preferred locale of the advertiser.
    )
    nativeLanguageLocale: SPLanguageLocale | None = None


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
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the pro
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the produc
    )
    productPrimeShippingEligible: bool | None = (
        None  # Target based on if a product is Prime-shipping eligible.
    )
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the pr
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the produ
    )


class SPCreateProductCategoryRefinementValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPCreateProductCategoryRefinement


class SPCreateProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPCreateProductCategoryRefinementValue


class SPCreateProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: SPProductMatchType
    product: SPCreateProductValue
    productIdType: SPProductIdType


class SPCreateTargetBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.


class SPCreateTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    keywordTarget: SPCreateKeywordTarget | None = None
    productTarget: SPCreateProductTarget | None = None
    productCategoryTarget: SPCreateProductCategoryTarget | None = None
    locationTarget: SPCreateLocationTarget | None = None
    themeTarget: SPCreateThemeTarget | None = None


class SPCreateThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: SPThemeMatchType


class SPKeywordTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The customer search term or text to target
    matchType: SPKeywordMatchType
    nativeLanguageKeyword: str | None = (
        None  # The unlocalized keyword text in the preferred locale of the advertiser.
    )
    nativeLanguageLocale: SPLanguageLocale | None = None


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
    productPriceGreaterThan: float | None = (
        None  # Refinement to target products with a price greater than the value within the pro
    )
    productPriceLessThan: float | None = (
        None  # Refinement to target products with a price less than the value within the produc
    )
    productPrimeShippingEligible: bool | None = (
        None  # Target based on if a product is Prime-shipping eligible.
    )
    productRatingGreaterThan: float | None = (
        None  # Refinement to target products with a rating greater than the value within the pr
    )
    productRatingLessThan: float | None = (
        None  # Refinement to target products with a rating less than the value within the produ
    )


class SPProductCategoryRefinementValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPProductCategoryRefinement


class SPProductCategoryTarget(BaseModel):
    """Targets a specific customer search term."""

    model_config = ConfigDict(extra="forbid")

    productCategoryRefinement: SPProductCategoryRefinementValue


class SPProductTarget(BaseModel):
    """Targets a specific product."""

    model_config = ConfigDict(extra="forbid")

    matchType: SPProductMatchType
    product: SPProductValue
    productIdType: SPProductIdType


class SPTarget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for a
    )
    adProduct: SPAdProduct
    bid: SPTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for c
    )
    creationDateTime: datetime  # The date time the target was created.
    globalTargetId: str | None = (
        None  # The global target identifier that manages this marketplace target.
    )
    lastUpdatedDateTime: datetime  # The date time the target was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of marketplace in which the global target is applicable. The marketplac
    negative: bool  # Indicates whether the target is negative or not.
    state: SPState
    status: SPStatus | None = None
    tags: list[SPTag] | None = None  # Open ended labels with a key value pair applied to the target
    targetDetails: SPTargetDetails
    targetId: str  # A unique identifier for the target.
    targetLevel: SPTargetLevel
    targetType: SPTargetType


class SPTargetBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
    currencyCode: SPCurrencyCode


class SPTargetCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the target. Only used for a
    )
    adProduct: SPAdProduct
    bid: SPCreateTargetBid | None = None
    campaignId: str | None = (
        None  # A unique identifier for the campaign associated with the target. Only used for c
    )
    negative: bool  # Indicates whether the target is negative or not.
    state: SPCreateState
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the target
    )
    targetDetails: SPCreateTargetDetails
    targetType: SPTargetType


class SPTargetDetails(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    keywordTarget: SPKeywordTarget | None = None
    locationTarget: SPLocationTarget | None = None
    productCategoryTarget: SPProductCategoryTarget | None = None
    productTarget: SPProductTarget | None = None
    themeTarget: SPThemeTarget | None = None


class SPTargetMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    index: int
    target: SPTarget


class SPTargetUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bid: SPUpdateTargetBid | None = None
    state: SPUpdateState | None = None
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the target
    )
    targetId: str  # A unique identifier for the target.


class SPThemeTarget(BaseModel):
    """Theme targets let advertisers select high-performing targets based on a common theme."""

    model_config = ConfigDict(extra="forbid")

    matchType: SPThemeMatchType


class SPUpdateTargetBid(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bid: float | None = None  # The maximum bid for a target.
