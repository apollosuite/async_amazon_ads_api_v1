"""Auto-generated models for Product targeting categories from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    SBTargetingBrand,
)


class SBTargetingLocale(StrEnum):
    """
    The locale to which the caller wishes to translate the targetable categories or refinements to. For example, if the caller wishes to receive the targetable categories in Simplified Chinese, the locale parameter should be set to zh_CN. If no locale is provided, the returned tagetable categories will be in the default language of the marketplace.
    """

    ar_AE = "ar_AE"
    de_DE = "de_DE"
    en_AE = "en_AE"
    en_AU = "en_AU"
    en_CA = "en_CA"
    en_GB = "en_GB"
    en_IN = "en_IN"
    en_SG = "en_SG"
    en_US = "en_US"
    es_ES = "es_ES"
    es_MX = "es_MX"
    fr_CA = "fr_CA"
    fr_FR = "fr_FR"
    hi_IN = "hi_IN"
    it_IT = "it_IT"
    ja_JP = "ja_JP"
    ko_KR = "ko_KR"
    nl_NL = "nl_NL"
    pl_PL = "pl_PL"
    pt_BR = "pt_BR"
    sv_SE = "sv_SE"
    ta_IN = "ta_IN"
    th_TH = "th_TH"
    tr_TR = "tr_TR"
    vi_VN = "vi_VN"
    zh_CN = "zh_CN"


class SBTargetingSupplySource(StrEnum):
    """
    [UPDATE: As of 05/28/2024, `STREAMING_VIDEO` is deprecated].
     The supply source where the target will be used. Use `AMAZON` for placements on Amazon website. Use `STREAMING_VIDEO` for off-site video placements such as IMDb TV.
    """

    AMAZON = "AMAZON"
    STREAMING_VIDEO = "STREAMING_VIDEO"


class SBTargetingAgeRange(LenientModel):
    ageRangeRefinementId: str = Field(
        description="Id of Age Range. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Age Range Refinement IDs."
    )
    name: str | None = Field(default=None, description="Name of Age Range.")
    translatedName: str | None = Field(
        default=None, description="Translated name of Age Range based off locale sent in request."
    )


class SBTargetingCategory(LenientModel):
    """Category details."""

    asinCountRange: SBTargetingIntegerRange | None = Field(default=None)
    isTargetable: bool | None = Field(default=None, description="If the category is targetable or not.")
    parentCategoryRefinementId: str | None = Field(
        default=None,
        description="The category refinement id of the parent category. Missing parentCategoryRefinementId signifies this is a root category.",
    )
    estimatedReach: SBTargetingEstimatedReachRange | None = Field(default=None)
    name: str | None = Field(default=None, description="Name of category.")
    translatedName: str | None = Field(default=None, description="Translated name of the category.")
    categoryRefinementId: str | None = Field(
        default=None,
        description="The category refinement id. Please use /sb/targets/categories or /sb/recommendations/targets/category to retrieve category IDs.",
    )


class SBTargetingEstimatedReachRange(LenientModel):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class SBTargetingGenre(LenientModel):
    genreRefinementId: str = Field(
        description="Id of Genre. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Genre Refinement IDs."
    )
    name: str | None = Field(default=None, description="Name of Genre.")
    translatedName: str | None = Field(
        default=None, description="Translated name of Genre based off locale sent in request."
    )


class SBTargetingGetRefinementsForCategoryResponseContent(LenientModel):
    """Response object for /sb/targets/categories/{categoryRefinementId}/refinements containing information on Brand Nodes, Age Range Nodes, and Genre Nodes.
    Response is paginated with pagination occurring for all three arrays at once.
    Example: If there are 800 brands, 5 age ranges, and 600 genres, the first response will return 500 brands, 5 age ranges, and 500 genres. The next paginated response will return 300 brands, 0 age ranges, and 100 genres.
    """

    ageRanges: list[SBTargetingAgeRange] | None = Field(
        default=None,
        max_length=500,
        description="List of Age Ranges. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Age Ranges. Age Ranges are only available for categories related to children's toys and games.",
    )
    brands: list[SBTargetingBrand] | None = Field(default=None, max_length=500, description="List of Brands.")
    genres: list[SBTargetingGenre] | None = Field(
        default=None,
        max_length=500,
        description="List of Genres. Use /sb/targets/categories/{categoryRefinementId}/refinements to retrieve Genre Node IDs. Genres are only available for categories related to books.",
    )
    nextToken: str | None = Field(
        default=None,
        description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results, call the same operation and specify this token in the request. If the `NextToken` field is empty, there are no further results.",
    )


class SBTargetingGetTargetableASINCountsRequestContent(StrictModel):
    ageRanges: list[str] | None = Field(default=None, max_length=100, description="List of Age Range Refinement Ids.")
    brands: list[str] | None = Field(default=None, max_length=100, description="List of Brand Refinement Ids.")
    genres: list[str] | None = Field(default=None, max_length=100, description="List of Genre Refinement Ids.")
    isPrimeShipping: bool | None = Field(
        default=None,
        description="Indicates if products have prime shipping. Leave empty to include both prime shipping and non-prime shipping products.",
    )
    ratingRange: SBTargetingRatingRange | None = Field(default=None)
    category: str = Field(
        description="The category refinement id. Please use /sb/targets/categories or /sb/recommendations/targets/category to retrieve category IDs."
    )
    priceRange: SBTargetingPriceRange | None = Field(default=None)


class SBTargetingGetTargetableASINCountsResponseContent(LenientModel):
    """Response object for /sb/targets/products/count to get number of targetable asins for refinements provided by the user"""

    asinCounts: SBTargetingIntegerRange | None = Field(default=None)


class SBTargetingGetTargetableCategoriesResponseContent(LenientModel):
    """Response object for /sb/targets/categories containing all targetable categories for the advertiser's marketplace."""

    nextToken: str | None = Field(
        default=None,
        description="Operations that return paginated results include a pagination token in this field. To retrieve the next page of results, call the same operation and specify this token in the request. If the `NextToken` field is empty, there are no further results.",
    )
    categoryTree: list[SBTargetingCategory] | None = Field(
        default=None, max_length=5000, description="List of categories."
    )


class SBTargetingIntegerRange(LenientModel):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class SBTargetingPriceRange(StrictModel):
    """A range of prices. We use this to retrieve the number of targetable ASINs that falls within this price range."""

    min: float | None = Field(default=None)
    max: float | None = Field(default=None)


class SBTargetingRatingRange(StrictModel):
    """Rating range is restricted to integers between 0 and 5, inclusive. Min must be less than or equal to max. We use this to retrieve the number of targetable ASINs that falls within this rating range."""

    min: int | None = Field(default=None, ge=0, le=5)
    max: int | None = Field(default=None, ge=0, le=5)


__all__ = [
    "SBTargetingAgeRange",
    "SBTargetingBrand",
    "SBTargetingCategory",
    "SBTargetingEstimatedReachRange",
    "SBTargetingGenre",
    "SBTargetingGetRefinementsForCategoryResponseContent",
    "SBTargetingGetTargetableASINCountsRequestContent",
    "SBTargetingGetTargetableASINCountsResponseContent",
    "SBTargetingGetTargetableCategoriesResponseContent",
    "SBTargetingIntegerRange",
    "SBTargetingLocale",
    "SBTargetingPriceRange",
    "SBTargetingRatingRange",
    "SBTargetingSupplySource",
]
