"""Auto-generated models for Product Recommendation Service from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class GetProductRecommendationsRequest(StrictModel):
    """Request structure to get ASIN recommendations for a set of input ASINs."""

    adAsins: list[str] = Field(description="List of input ASINs.")
    count: int | None = Field(
        default=None,
        ge=1,
        description="Count of objects requested in the response. The count will be applied on the objects returned under `recommendations` array in response body.  <ul> <li>Requesting `application/vnd.spproductrecommendationresponse.themes.v3+json` mediatype applies the count on `ThemeRecommendation` objects.If no count value is passed a default of `5` is assumed. The API will return a maximum of `10` themes irrespective of how large the count is set. </li> <li>Requesting `application/vnd.spproductrecommendationresponse.asins.v3+json` mediatype applies count on the `ProductRecommendation` objects in response body.If no count value is passed a default of `100` is assumed. The API will return a maximum of `1000` recommendations irrespective of how large the count is set. </li> </ul> Please refer the response Schemas for more info.",
    )
    cursor: str | None = Field(
        default=None, description="A optional cursor value that can be used to fetch next or previous set of records."
    )
    locale: str | None = Field(
        default=None,
        description="Theme names and descriptions will be provided in the language for your supported locale. Available options are en_US (U.S. English), en_GB (UK English), zh_CN (Chinese), es_ES (Spanish), jp_JP (Japanese), de_DE (German), fr_FR (French), it_IT(Italian). If locale is not provided or unsupported, the theme names and descriptions will be returned in U.S. English (en_US).",
    )


class ProductRecommendation(LenientModel):
    """Recommended asin and related information."""

    recommendedAsin: str | None = Field(default=None, min_length=10, max_length=10, description="Recommended ASIN")
    themes: list[str] | None = Field(default=None, description="List of themes associated with this recommended ASIN.")


class ProductRecommendationsByASIN(LenientModel):
    """Product recommendations supplemented with relevant information."""

    nextCursor: str | None = Field(
        default=None,
        description="An identifier to fetch next set of `ProductRecommendation` records in the result set if available. This will be null when at the end of result set.",
    )
    previousCursor: str | None = Field(
        default=None,
        description="Optional parameter that links to the previous result set served. This parameter will be null on the first request.",
    )
    recommendations: list[ProductRecommendation] | None = Field(
        default=None, description="An array of `ProductRecommendation` objects."
    )


class ProductRecommendationsByTheme(LenientModel):
    """Product recommendations grouped by theme attribute."""

    nextCursor: str | None = Field(
        default=None,
        description="An identifier to fetch next set of `ThemeRecommendation` records in the result set if available. This will be null when at the end of result set.",
    )
    previousCursor: str | None = Field(
        default=None, description="Optional parameter that links to the previous result set served to the requester."
    )
    recommendations: list[ThemeRecommendation] | None = Field(
        default=None, description="An array of `ThemeRecommendation` objects"
    )


class ThemeRecommendation(LenientModel):
    """Recommended asins grouped by theme attribute."""

    description: str | None = Field(
        default=None, description="A theme name representing the context around the recommended list of ASINs."
    )
    recommendedAsins: list[str] | None = Field(
        default=None, description="List of recommended ASINs under current theme."
    )
    theme: str | None = Field(
        default=None, description="A theme name representing the context around the recommended list of ASINs."
    )


__all__ = [
    "GetProductRecommendationsRequest",
    "ProductRecommendation",
    "ProductRecommendationsByASIN",
    "ProductRecommendationsByTheme",
    "ThemeRecommendation",
]
