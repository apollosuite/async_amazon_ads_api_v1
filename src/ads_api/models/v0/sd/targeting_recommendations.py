"""Auto-generated models for Targeting Recommendations from Amazon Ads API v0."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    SDASIN,
    LocationExpression,
    LocationPredicate,
    SDGoalProduct,
)

type SDAudienceCategory = Literal["In-market", "Lifestyle", "Interest", "Life event"]
"""
An audience category determines the goal of the audience such as In-market, Interest, Lifestyle and Life Event
"""


type SDLandingPageType = Literal["OFF_AMAZON_LINK"]
"""
The type of the landingPage used. This field is not supported when using asin field.
"""


type SDRecommendationType = Literal["PRODUCT"]
"""
Signifies a type of recommendation
"""


type SDRecommendationTypeV31 = Literal["PRODUCT", "CATEGORY"]
"""
Signifies a type of recommendation
"""


type SDRecommendationTypeV32 = Literal["PRODUCT", "CATEGORY", "AUDIENCE"]
"""
Signifies a type of recommendation. PRODUCT and CATEGORY are supported by tactic T00020. CATEGORY and AUDIENCE are supported by tactic T00030.
"""


type SDRecommendationTypeV33 = Literal["PRODUCT", "CATEGORY", "AUDIENCE", "CONTENT_CATEGORY"]
"""
Signifies a type of recommendation. PRODUCT, CATEGORY, and CONTENT_CATEGORY are supported by tactic T00020. CATEGORY, AUDIENCE, and CONTENT_CATEGORY are supported by tactic T00030.
"""


type SDTactic = Literal["T00020"]
"""
The advertising tactic associated with the campaign. The following table lists available tactic names:
|Tactic Name|Type|Description|
        |-----------|-----|-----------|
        |T00020 &nbsp;    |Products&nbsp;| Products: Choose individual products to show your ads in placements related to those products.<br>Categories: Choose individual categories to show your ads in placements related to those categories.
"""


type SDTacticV31 = Literal["T00020", "T00030"]
"""
The advertising tactic associated with the campaign. The following table lists available tactic names:
|Tactic Name|Type|Description|
        |-----------|-----|-----------|
        |T00020 &nbsp;    |Products&nbsp;| Products: Choose individual products to show your ads in placements related to those products.<br>Categories: Choose individual categories to show your ads in placements related to those categories.|
        |T00030&nbsp;|Audiences or Contextual Targeting &nbsp;|Select individual products, categories, refined categories, or audiences to show your ads.|
"""


type SDTargetingRecommendationsLocale = Literal[
    "ar_AE",
    "de_DE",
    "en_AE",
    "en_AU",
    "en_CA",
    "en_GB",
    "en_IN",
    "en_SG",
    "en_US",
    "es_ES",
    "es_MX",
    "fr_CA",
    "fr_FR",
    "hi_IN",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "nl_NL",
    "pl_PL",
    "pt_BR",
    "sv_SE",
    "ta_IN",
    "th_TH",
    "tr_TR",
    "vi_VN",
    "zh_CN",
]
"""
List of supported locales.
"""


class SDAdvertisedProduct(StrictModel):
    """Product that advertisers want to advertise. Recommendations will be made for specified products. SDAdvertisedProduct can only contain either asins or landing pages. If landingPageUrl is used, there can only be one item for each request."""

    asin: SDASIN | None = Field(default=None)
    landingPageType: SDLandingPageType | None = Field(default=None)
    landingPageURL: SDLandingPageURL | None = Field(default=None)


type SDAudience = str  # The audience identifier


class SDAudienceCategoryRecommendations(LenientModel):
    """List of recommended standard Amazon audience targets of a specific audience category"""

    category: SDAudienceCategory | str | None = Field(default=None)
    audiences: list[SDAudienceRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended standard Amazon audience targets"
    )


class SDAudienceRecommendation(LenientModel):
    """A recommended standard Amazon audience to target ads on"""

    audience: SDAudience | None = Field(default=None)
    name: str | None = Field(default=None, description="The Amazon audience name")
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation",
    )


class SDAudienceRecommendations(LenientModel):
    audiences: list[SDAudienceCategoryRecommendations] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="List of recommended audience targets, broken down by audience category",
    )


type SDCategory = int  # The category identifier


class SDCategoryRecommendation(LenientModel):
    """A recommended category to target ads on"""

    category: SDCategory | None = Field(default=None)
    name: str | None = Field(default=None, description="The category name")
    path: list[str] | None = Field(
        default=None, min_length=1, description="The path of the category within the category catalogue."
    )
    targetableAsinCountRange: dict[str, Any] | None = Field(
        default=None,
        description="The range of ASINs available within the category catalogue. If no targetable ASIN counts are available then the targetableAsinCountRange value will be null without any properties.",
    )
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation",
    )


class SDCategoryRecommendationV33(LenientModel):
    """A recommended category to target ads on"""

    category: SDCategory | None = Field(default=None)
    name: str | None = Field(default=None, description="The category name")
    translatedName: str | None = Field(
        default=None,
        description="The translated category name by requested locale, field will not be provided if locale is not provided or campaign localization service is down.",
    )
    path: list[str] | None = Field(
        default=None, min_length=1, description="The path of the category within the category catalogue."
    )
    translatedPath: list[str] | None = Field(
        default=None,
        min_length=1,
        description="The translated path of the category within the category catalogue by requested locale, field will not be provided if locale is not provided or campaign localization is down.",
    )
    targetableAsinCountRange: dict[str, Any] | None = Field(
        default=None, description="The range of ASINs available within the category catalogue."
    )
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation.",
    )


class SDCategoryRecommendations(LenientModel):
    categories: list[SDCategoryRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets"
    )


class SDCategoryRecommendationsV33(LenientModel):
    categories: list[SDCategoryRecommendationV33] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets."
    )


type SDContentCategory = str  # The content category value


class SDContentCategoryRecommendations(LenientModel):
    """A recommended content category to target ads on"""

    contentCategory: SDContentCategory | None = Field(default=None)
    name: str | None = Field(default=None, description="The content category name")
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation",
    )


type SDLandingPageURL = str


class SDProductRecommendation(LenientModel):
    """A recommended product to target ads on"""

    asin: SDASIN | None = Field(default=None)
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation",
    )


class SDProductRecommendationV32(LenientModel):
    """A recommended product to target ads on"""

    asin: SDASIN | None = Field(default=None)
    rank: int | None = Field(
        default=None,
        ge=1,
        description="A rank to signify which recommendations are weighed more heavily, with a lower rank signifying a stronger recommendation",
    )
    advertisedAsins: list[SDASIN] | None = Field(
        default=None,
        min_length=1,
        max_length=5,
        description="The top advertised products this recommendation is made for.",
    )


class SDProductRecommendationsV31(LenientModel):
    products: list[SDProductRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )


class SDProductRecommendationsV32(LenientModel):
    products: list[SDProductRecommendationV32] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )


class SDProductTargetingRecommendationsSuccess(LenientModel):
    """Recommendation results for contextual targeting."""

    code: str | None = Field(
        default=None, description="HTTP status code 200 indicating a successful response for product recomendations."
    )
    name: str | None = Field(default=None, description="The theme name specified in the request.")
    recommendations: list[SDProductRecommendationV32] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of recommended products."
    )


class SDProductTargetingRecommendationsSuccessV34(LenientModel):
    """Recommendation results for contextual targeting."""

    code: str | None = Field(
        default=None, description="HTTP status code 200 indicating a successful response for product recommendations."
    )
    name: str | None = Field(default=None, description="The theme name specified in the request.")
    expression: list[SDProductTargetingThemeExpressionOut] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="""
A list of expressions defining the product targeting theme. The list will define an AND operator on different expressions.
For example, asinPriceGreaterThan and asinReviewRatingLessThan can be used to request product recommendations
which are both with greater price and less review rating compared to the goal products.
Note: currently the service only support one item in the array.
""",
    )
    recommendations: list[SDProductRecommendationV32] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of recommended products."
    )


class SDProductTargetingTheme(StrictModel):
    """Contextual targeting theme definitions."""

    name: str = Field(
        min_length=1,
        max_length=100,
        description="""
This is the meaningful theme name which will be used as a unique identifier across various themes in the same request.
This identifier will also be used to map the recommendations back to the theme in the response body.
Note: the value for this field cannot be "default" as that's a reserved keyword in the system.
""",
    )
    expression: list[SDProductTargetingThemeExpression] = Field(
        min_length=1,
        max_length=1,
        description="""
A list of expressions defining the contextual targeting theme. The list will define an AND operator on different expressions.
For example, asinPriceGreaterThan and asinReviewRatingLessThan can be used to request product recommendations
which are both with greater price and less review rating compared to the goal products.
Note: Currently the service only supports one item in the array.
""",
    )


class SDProductTargetingThemeExpression(StrictModel):
    """The expression used to define the contextual targeting theme."""

    type: Literal[
        "asinPriceGreaterThan", "asinBrandSameAs", "asinReviewRatingLessThan", "asinGlanceViewsGreaterThan"
    ] = Field(
        description="The contextual targeting grammar used to define the targeting theme. Note asinAsBestSeller is currently not supported."
    )


class SDProductTargetingThemeExpressionOut(LenientModel):
    """The expression used to define the contextual targeting theme."""

    type: (
        Literal["asinPriceGreaterThan", "asinBrandSameAs", "asinReviewRatingLessThan", "asinGlanceViewsGreaterThan"]
        | str
    ) = Field(
        description="The contextual targeting grammar used to define the targeting theme. Note asinAsBestSeller is currently not supported."
    )


class SDTargetingRecommendations(LenientModel):
    """A collection of targeting recommendations. Results will be sorted with strongest recommendations in the beginning."""

    products: list[SDProductRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )


class SDTargetingRecommendationsProducts(StrictModel):
    """A list of products for which to get targeting recommendations"""

    pass


class SDTargetingRecommendationsProductsV31(StrictModel):
    """A list of products for which to get targeting recommendations. This array can only contain either asins or landing pages. If landingPageUrl is used,
    there can only be one item in the array for each request."""

    pass


class SDTargetingRecommendationsRequest(StrictModel):
    """Request for targeting recommendations"""

    tactic: SDTactic
    products: list[SDGoalProduct] = Field(
        min_length=1, max_length=10000, description="A list of products for which to get targeting recommendations"
    )
    typeFilter: list[SDRecommendationType | str] = Field(
        min_length=1, max_length=1, description="A filter to indicate which types of recommendations to request."
    )


class SDTargetingRecommendationsRequestV31(StrictModel):
    """Request for targeting recommendations"""

    tactic: SDTacticV31
    products: SDTargetingRecommendationsProducts
    typeFilter: SDTargetingRecommendationsTypeFilterV31


class SDTargetingRecommendationsRequestV32(StrictModel):
    """Request for targeting recommendations for API version 3.2."""

    tactic: SDTacticV31
    products: SDTargetingRecommendationsProducts
    typeFilter: SDTargetingRecommendationsTypeFilterV31
    themes: SDTargetingRecommendationsThemes | None = Field(default=None)


class SDTargetingRecommendationsRequestV33(StrictModel):
    """Request for targeting recommendations for API version 3.3."""

    tactic: SDTacticV31
    products: SDTargetingRecommendationsProducts
    typeFilter: SDTargetingRecommendationsTypeFilterV32
    themes: SDTargetingRecommendationsThemes | None = Field(default=None)


class SDTargetingRecommendationsRequestV34(StrictModel):
    """Request for targeting recommendations for API version 3.4."""

    tactic: SDTacticV31
    products: SDTargetingRecommendationsProducts
    typeFilter: SDTargetingRecommendationsTypeFilterV32
    themes: SDTargetingRecommendationsThemes | None = Field(default=None)


class SDTargetingRecommendationsRequestV35(StrictModel):
    """Request for targeting recommendations for API version 3.5."""

    tactic: SDTacticV31
    products: SDTargetingRecommendationsProductsV31
    typeFilter: SDTargetingRecommendationsTypeFilterV33
    themes: SDTargetingRecommendationsThemes | None = Field(default=None)
    categoryType: Literal["views", "purchases"] | None = Field(
        default=None,
        description="""
This field is optional unless the field locationExpression is present in the request. It is used for category audience targeting
to specify if the audience is for views (re-marketing) or purchases (re-purchasing). The specified categories will be returned accordingly.
""",
    )
    locationExpression: list[LocationExpression] | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="""
This optional field is used to specify the locations used in SD location targeting for non-Amazon sellers only at the moment.
Therefore it's only supported if the product is a landing page url.
""",
    )


class SDTargetingRecommendationsResponse(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendations | None = Field(default=None)


class SDTargetingRecommendationsResponseV31(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendationsV31 | None = Field(default=None)


class SDTargetingRecommendationsResponseV32(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendationsV32 | None = Field(default=None)


class SDTargetingRecommendationsResponseV33(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendationsV33 | None = Field(default=None)


class SDTargetingRecommendationsResponseV34(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendationsV34 | None = Field(default=None)


class SDTargetingRecommendationsResponseV35(LenientModel):
    """Response to a request for targeting recommendations."""

    recommendations: SDTargetingRecommendationsV35 | None = Field(default=None)


class SDTargetingRecommendationsThemes(StrictModel):
    """The themes used to refine the recommendations. Currently only contextual targeting themes are supported."""

    product: list[SDProductTargetingTheme] | None = Field(
        default=None,
        min_length=0,
        max_length=5,
        description="A list of themes for product targeting recommendations. If this list is empty, the service will return all the current available theme recommendations. Recommendations will be returned for each theme. If specified, each theme should only include unique expressions.",
    )


class SDTargetingRecommendationsTypeFilterV31(StrictModel):
    """A filter to indicate which types of recommendations to request."""

    pass


class SDTargetingRecommendationsTypeFilterV32(StrictModel):
    """A filter to indicate which types of recommendations to request."""

    pass


class SDTargetingRecommendationsTypeFilterV33(StrictModel):
    """A filter to indicate which types of recommendations to request."""

    pass


class SDTargetingRecommendationsV31(LenientModel):
    products: list[SDProductRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )
    categories: list[SDCategoryRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets"
    )


class SDTargetingRecommendationsV32(LenientModel):
    """For v3.2 the service will continue to return the recommendations returned for v3.1 in products field, and return recommendations for contextual targeting themes in themes field."""

    products: list[SDProductRecommendationV32] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )
    categories: list[SDCategoryRecommendation] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets"
    )
    themes: dict[str, Any] | None = Field(default=None)


class SDTargetingRecommendationsV33(LenientModel):
    """For v3.3 the service will continue to return the recommendations returned for v3.2, and return audience recommendations if requested."""

    products: list[SDProductRecommendationV32] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )
    categories: list[SDCategoryRecommendationV33] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets."
    )
    audiences: list[SDAudienceCategoryRecommendations] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="List of recommended audience targets, broken down by audience category",
    )
    themes: dict[str, Any] | None = Field(default=None)


class SDTargetingRecommendationsV34(LenientModel):
    """For v3.4 the service will continue to return the recommendations returned for v3.2, return audience recommendations if requested, and return the theme expression used in product targeting if requested."""

    products: list[SDProductRecommendationsV32] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )
    categories: list[SDCategoryRecommendationV33] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets"
    )
    audiences: list[SDAudienceCategoryRecommendations] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="List of recommended audience targets, broken down by audience category",
    )
    themes: SDThemeRecommendationsV34 | None = Field(default=None)


class SDTargetingRecommendationsV35(LenientModel):
    """For v3.5 the service will continue to return the recommendations returned for v3.4, return Entertainment targeting recommendations if requested and return asin-less recommendations if a landing page URL was passed in the request"""

    products: list[SDProductRecommendationsV32] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended product targets"
    )
    categories: list[SDCategoryRecommendationV33] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended category targets"
    )
    audiences: list[SDAudienceCategoryRecommendations] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="List of recommended audience targets, broken down by audience category",
    )
    contentCategories: list[SDContentCategoryRecommendations] | None = Field(
        default=None, min_length=0, max_length=1000, description="List of recommended entertainment targets"
    )
    themes: SDThemeRecommendationsV34 | None = Field(default=None)


class SDThemeRecommendations(LenientModel):
    themes: dict[str, Any] | None = Field(default=None)


class SDThemeRecommendationsV34(LenientModel):
    themes: dict[str, Any] | None = Field(default=None)


__all__ = [
    "LocationExpression",
    "LocationPredicate",
    "SDASIN",
    "SDAdvertisedProduct",
    "SDAudience",
    "SDAudienceCategory",
    "SDAudienceCategoryRecommendations",
    "SDAudienceRecommendation",
    "SDAudienceRecommendations",
    "SDCategory",
    "SDCategoryRecommendation",
    "SDCategoryRecommendationV33",
    "SDCategoryRecommendations",
    "SDCategoryRecommendationsV33",
    "SDContentCategory",
    "SDContentCategoryRecommendations",
    "SDGoalProduct",
    "SDLandingPageType",
    "SDLandingPageURL",
    "SDProductRecommendation",
    "SDProductRecommendationV32",
    "SDProductRecommendationsV31",
    "SDProductRecommendationsV32",
    "SDProductTargetingRecommendationsSuccess",
    "SDProductTargetingRecommendationsSuccessV34",
    "SDProductTargetingTheme",
    "SDProductTargetingThemeExpression",
    "SDProductTargetingThemeExpressionOut",
    "SDRecommendationType",
    "SDRecommendationTypeV31",
    "SDRecommendationTypeV32",
    "SDRecommendationTypeV33",
    "SDTactic",
    "SDTacticV31",
    "SDTargetingRecommendations",
    "SDTargetingRecommendationsLocale",
    "SDTargetingRecommendationsProducts",
    "SDTargetingRecommendationsProductsV31",
    "SDTargetingRecommendationsRequest",
    "SDTargetingRecommendationsRequestV31",
    "SDTargetingRecommendationsRequestV32",
    "SDTargetingRecommendationsRequestV33",
    "SDTargetingRecommendationsRequestV34",
    "SDTargetingRecommendationsRequestV35",
    "SDTargetingRecommendationsResponse",
    "SDTargetingRecommendationsResponseV31",
    "SDTargetingRecommendationsResponseV32",
    "SDTargetingRecommendationsResponseV33",
    "SDTargetingRecommendationsResponseV34",
    "SDTargetingRecommendationsResponseV35",
    "SDTargetingRecommendationsThemes",
    "SDTargetingRecommendationsTypeFilterV31",
    "SDTargetingRecommendationsTypeFilterV32",
    "SDTargetingRecommendationsTypeFilterV33",
    "SDTargetingRecommendationsV31",
    "SDTargetingRecommendationsV32",
    "SDTargetingRecommendationsV33",
    "SDTargetingRecommendationsV34",
    "SDTargetingRecommendationsV35",
    "SDThemeRecommendations",
    "SDThemeRecommendationsV34",
]
