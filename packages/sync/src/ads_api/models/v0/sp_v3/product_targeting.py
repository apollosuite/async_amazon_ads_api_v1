"""Auto-generated models for Product Targeting from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class AgeRange(StrictModel):
    id: str | None = Field(
        default=None,
        description="Id of Age Range. This field is REQUIRED if the Age Range object is being used as an input. Use the GetRefinementsForCategory to retrieve Age Range Node IDs.",
    )
    name: str | None = Field(
        default=None,
        description="Name of Age Range. This field is OPTIONAL if the Age Range object is being used as an input.",
    )


class AgeRangeLoP(LenientModel):
    id: str | None = Field(
        default=None,
        description="Id of Age Range. Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Age Range Node IDs.",
    )
    name: str | None = Field(default=None, description="Name of Age Range.")
    translatedName: str | None = Field(
        default=None, description="Translated name of Age Range based off locale sent in request."
    )


class AgeRangeOut(LenientModel):
    id: str | None = Field(
        default=None,
        description="Id of Age Range. This field is REQUIRED if the Age Range object is being used as an input. Use the GetRefinementsForCategory to retrieve Age Range Node IDs.",
    )
    name: str | None = Field(
        default=None,
        description="Name of Age Range. This field is OPTIONAL if the Age Range object is being used as an input.",
    )


class AgeRanges(StrictModel):
    """List of Age Ranges. Use the GetRefinementsForCategory to retrieve Age Ranges. Age Ranges are only available for categories related to children's toys and games."""

    pass


class AgeRangesLoP(LenientModel):
    """List of Age Ranges in a language of preference (LoP). Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Age Ranges. Age Ranges are only available for categories related to children's toys and games."""

    pass


class AgeRangesOut(LenientModel):
    """List of Age Ranges. Use the GetRefinementsForCategory to retrieve Age Ranges. Age Ranges are only available for categories related to children's toys and games."""

    pass


class Brand(StrictModel):
    id: str | None = Field(
        default=None,
        description="Id of brand. This field is REQUIRED if the Brand object is being used as an input. Use the GetRefinementsForCategory to retrieve Brand Node IDs.",
    )
    name: str | None = Field(
        default=None, description="Name of brand. This field is OPTIONAL if the Brand object is being used as an input."
    )


class BrandLoP(LenientModel):
    id: str | None = Field(default=None, description="Id of brand.")
    name: str | None = Field(default=None, description="Name of brand.")


class BrandOut(LenientModel):
    id: str | None = Field(
        default=None,
        description="Id of brand. This field is REQUIRED if the Brand object is being used as an input. Use the GetRefinementsForCategory to retrieve Brand Node IDs.",
    )
    name: str | None = Field(
        default=None, description="Name of brand. This field is OPTIONAL if the Brand object is being used as an input."
    )


class Brands(StrictModel):
    """List of Brands."""

    pass


class BrandsLoP(LenientModel):
    """List of Brands."""

    pass


class BrandsOut(LenientModel):
    """List of Brands."""

    pass


class CategoryItem(LenientModel):
    canBeTargeted: bool | None = Field(
        default=None, description="A flag which indicates if the current node may be targeted"
    )
    id: str | None = Field(default=None, description="The category id of the current node")
    name: str | None = Field(default=None, description="The name of the category")
    parent: str | None = Field(default=None, description="The category id of the parent node")
    path: str | None = Field(
        default=None,
        description="The path of the category, which contains the current category and all parent categories",
    )


class CategoryItemWithAsinCounts(LenientModel):
    asinCounts: IntegerRange | None = Field(default=None, description="An integer range between min and max")
    categoryPath: str | None = Field(
        default=None,
        description="The path of the category, which contains the current category and all parent categories",
    )
    id: str | None = Field(default=None, description="The category id of the current node")
    name: str | None = Field(default=None, description="The name of the category")
    parentCategoryId: str | None = Field(default=None, description="The category id of the parent node")


class CategoryItemWithAsinCountsLoP(LenientModel):
    asinCounts: IntegerRange | None = Field(default=None, description="The number of asins belonging to the category.")
    categoryPath: str | None = Field(
        default=None,
        description="The path of the category, which contains the current category and all parent categories",
    )
    id: str | None = Field(default=None, description="The category id of the current node")
    name: str | None = Field(default=None, description="The name of the category")
    parentCategoryId: str | None = Field(default=None, description="The category id of the parent node")
    translatedCategoryPath: str | None = Field(
        default=None,
        description="The translated path of the category, which contains the current category and all parent categories.",
    )
    translatedName: str | None = Field(default=None, description="The translated name of the category.")


class CategoryRecommendations(LenientModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""

    categories: list[CategoryItem] | None = Field(default=None, description="List of category recommendations")


class CategoryRecommendationsWithAsinCounts(LenientModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""

    categories: list[CategoryItemWithAsinCounts] | None = Field(
        default=None, description="List of category recommendations"
    )


class CategoryRecommendationsWithAsinCountsLoP(LenientModel):
    """Response object for the GetCategoryRecommendationsForAsins API."""

    categories: list[CategoryItemWithAsinCountsLoP] | None = Field(
        default=None, description="List of category recommendations"
    )


class Genre(StrictModel):
    id: str | None = Field(
        default=None,
        description="Id of Genre. This field is REQUIRED if the Genre object is being used as an input. Use the GetRefinementsForCategory to retrieve Genre Node IDs.",
    )
    name: str | None = Field(
        default=None, description="Name of Genre. This field is OPTIONAL if the Genre object is being used as an input."
    )


class GenreLoP(LenientModel):
    id: str | None = Field(
        default=None,
        description="Id of Genre. Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Genre Node IDs.",
    )
    name: str | None = Field(default=None, description="Name of Genre.")
    translatedName: str | None = Field(
        default=None, description="Translated name of the Genre based off locale send in the query parameter."
    )


class GenreOut(LenientModel):
    id: str | None = Field(
        default=None,
        description="Id of Genre. This field is REQUIRED if the Genre object is being used as an input. Use the GetRefinementsForCategory to retrieve Genre Node IDs.",
    )
    name: str | None = Field(
        default=None, description="Name of Genre. This field is OPTIONAL if the Genre object is being used as an input."
    )


class Genres(StrictModel):
    """List of Genres. Use the GetRefinementsForCategory to retrieve Genre Node IDs. Genres are only available for categories related to books."""

    pass


class GenresLoP(LenientModel):
    """List of Genres in a language of preference (LoP). Use the POST /sp/targets/category/{categoryId}/refinements endpoint to retrieve Genre Node IDs. Genres are only available for categories related to books."""

    pass


class GenresOut(LenientModel):
    """List of Genres. Use the GetRefinementsForCategory to retrieve Genre Node IDs. Genres are only available for categories related to books."""

    pass


class GetCategoryRecommendationsForAsinsRequest(StrictModel):
    """Request object to retrieve Category Recommendations based on the input ASINs."""

    asins: list[str] | None = Field(
        default=None,
        max_length=10000,
        description="List of input ASINs. This API does not check if the ASINs are valid ASINs.",
    )
    includeAncestor: bool | None = Field(
        default=None,
        description="Enable this if you would like to retrieve categories which are ancestor nodes of the original recommended categories. This may increase the number of categories returned, but decrease the relevancy of those categories.",
    )


class GetTargetableAsinCountsRequest(StrictModel):
    ageRanges: AgeRanges | None = Field(default=None)
    brands: Brands | None = Field(default=None)
    category: str = Field(
        description="The category node id. Please use the GetTargetableCategories API or GetCategoryRecommendationsForASINs API to retrieve category IDs."
    )
    genres: Genres | None = Field(default=None)
    isPrimeShipping: bool | None = Field(default=None, description="Indicates if products have prime shipping")
    priceRange: PriceRange | None = Field(default=None)
    ratingRange: RatingRange | None = Field(default=None)


class IntegerRange(LenientModel):
    max: int | None = Field(default=None)
    min: int | None = Field(default=None)


class PriceRange(StrictModel):
    """A range of prices. We use this to retrieve the number of targetable ASINs that falls within this price range."""

    max: float | None = Field(default=None)
    min: float | None = Field(default=None)


class RatingRange(StrictModel):
    """Rating range is restricted to integers between 0 and 5, inclusive. Min must be less than or equal to max. We use this to retrieve the number of targetable ASINs that falls within this rating range."""

    max: int | None = Field(default=None)
    min: int | None = Field(default=None)


class Refinements(LenientModel):
    """Response object for the GetRefinementsForCategory API, containing information on Brand Nodes, Age Range Nodes, and Genre Nodes."""

    ageRanges: AgeRangesOut | None = Field(default=None)
    brands: BrandsOut | None = Field(default=None)
    genres: GenresOut | None = Field(default=None)


class RefinementsLoP(LenientModel):
    """Response object for the POST /sp/targets/category/{categoryId}/refinements endpoint, containing information on Brand Nodes, Age Range Nodes, and Genre Nodes."""

    ageRanges: AgeRangesLoP | None = Field(default=None)
    brands: BrandsLoP | None = Field(default=None)
    genres: GenresLoP | None = Field(default=None)


class SearchBrandsRequest(StrictModel):
    """Request object for SearchBrands API."""

    keyword: str


class TargetableAsinCounts(LenientModel):
    """Response object to get number of targetable asins for refinements provided by the user"""

    asinCounts: IntegerRange | None = Field(default=None)


class TargetableCategories(LenientModel):
    """Response object containing all targetable categories for the advertiser's marketplace. ID is the category ID. NA is the name. CH is the list of child categories. TA is if the category is targetable. AsinCountRange is the AsinCounts of the node. Version 4 adds the number of targetable ASINs to each category."""

    categoryTree: str | None = Field(default=None)


class TargetableCategoriesLoP(LenientModel):
    """Response object containing all targetable categories for the advertiser's marketplace in a language of preference (LoP) provide by the locale query parameter. ID is the category ID. NA is the name. TN is the translated name in the language of preference. CH is the list of child categories. TA is if the category is targetable. AsinCountRange is the AsinCounts of the node. Version 4 adds the number of targetable ASINs to each category."""

    categoryTree: str | None = Field(default=None)


__all__ = [
    "AgeRange",
    "AgeRangeLoP",
    "AgeRangeOut",
    "AgeRanges",
    "AgeRangesLoP",
    "AgeRangesOut",
    "Brand",
    "BrandLoP",
    "BrandOut",
    "Brands",
    "BrandsLoP",
    "BrandsOut",
    "CategoryItem",
    "CategoryItemWithAsinCounts",
    "CategoryItemWithAsinCountsLoP",
    "CategoryRecommendations",
    "CategoryRecommendationsWithAsinCounts",
    "CategoryRecommendationsWithAsinCountsLoP",
    "Genre",
    "GenreLoP",
    "GenreOut",
    "Genres",
    "GenresLoP",
    "GenresOut",
    "GetCategoryRecommendationsForAsinsRequest",
    "GetTargetableAsinCountsRequest",
    "IntegerRange",
    "PriceRange",
    "RatingRange",
    "Refinements",
    "RefinementsLoP",
    "SearchBrandsRequest",
    "TargetableAsinCounts",
    "TargetableCategories",
    "TargetableCategoriesLoP",
]
