"""Auto-generated models for SupplierTargetItems from Amazon Ads API v1."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.dsp import (
    DSPSortDirection,
)


class DSPAdProduct(StrEnum):
    AMAZON_DSP = "AMAZON_DSP"  # Amazon Demand-Side Platform ad product.


class DSPCountryCode(StrEnum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AU = "AU"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IT = "IT"
    JP = "JP"
    KR = "KR"
    MX = "MX"
    US = "US"


class DSPSupplierTargetItemNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.


class DSPSupplierTargetItemSortOptionsFields(StrEnum):
    """
    Specify which field to order by.
    """

    name = "name"


class DSPSupplierTargetType(StrEnum):
    APP = "APP"
    AUDIENCE = "AUDIENCE"
    AUDIENCE_AGE = "AUDIENCE_AGE"
    AUDIENCE_EDUCATION = "AUDIENCE_EDUCATION"
    AUDIENCE_GENDER = "AUDIENCE_GENDER"
    AUDIENCE_HOMEOWNERSHIP = "AUDIENCE_HOMEOWNERSHIP"
    AUDIENCE_HOUSEHOLD_COMPOSITION = "AUDIENCE_HOUSEHOLD_COMPOSITION"
    AUDIENCE_HOUSEHOLD_INCOME = "AUDIENCE_HOUSEHOLD_INCOME"
    AUDIENCE_INTERESTS = "AUDIENCE_INTERESTS"
    AUDIENCE_IN_MARKET = "AUDIENCE_IN_MARKET"
    AUDIENCE_MARITAL_STATUS = "AUDIENCE_MARITAL_STATUS"
    AUDIENCE_MOOD = "AUDIENCE_MOOD"
    AUDIENCE_SOCIOECONOMIC_GROUP = "AUDIENCE_SOCIOECONOMIC_GROUP"
    CONTENT_CATEGORY = "CONTENT_CATEGORY"
    CONTENT_GENRE = "CONTENT_GENRE"
    CONTENT_RATING = "CONTENT_RATING"
    CONTENT_SENSITIVE_CATEGORY = "CONTENT_SENSITIVE_CATEGORY"
    DAYPART = "DAYPART"
    DAYPART_DAY = "DAYPART_DAY"
    DAYPART_TIME = "DAYPART_TIME"
    DEVICE_OPERATING_SYSTEM = "DEVICE_OPERATING_SYSTEM"
    DEVICE_TYPE = "DEVICE_TYPE"
    LOCATION_CITY = "LOCATION_CITY"
    LOCATION_COUNTRY = "LOCATION_COUNTRY"
    LOCATION_DESIGNATED_MARKET_AREA = "LOCATION_DESIGNATED_MARKET_AREA"
    LOCATION_METRO = "LOCATION_METRO"
    LOCATION_POSTAL_CODE = "LOCATION_POSTAL_CODE"
    LOCATION_REGION = "LOCATION_REGION"
    POSITION_VIDEO = "POSITION_VIDEO"


class DSPQuerySupplierTargetItemRequest(StrictModel):
    adProductFilter: DSPSupplierTargetItemAdProductFilter
    categoryFilter: DSPSupplierTargetItemCategoryFilter | None = Field(default=None)
    countriesFilter: DSPSupplierTargetItemCountryCodeFilter | None = Field(default=None)
    idFilter: DSPSupplierTargetItemIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=20, ge=1, le=500)
    nameFilter: DSPSupplierTargetItemNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    sort: list[DSPSupplierTargetItemSortOption] | None = Field(default=None, min_length=0, max_length=1)
    supplierAdProductIdFilter: DSPSupplierTargetItemSupplierAdProductIdFilter
    supplierProposalDestinationIdFilter: DSPSupplierTargetItemSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierTargetTypeFilter: DSPSupplierTargetItemSupplierTargetTypeFilter


class DSPSupplierTargetItem(LenientModel):
    adProduct: Annotated[DSPAdProduct | str, lenient_enum(DSPAdProduct)] | None = Field(default=None)
    category: list[str] | None = Field(
        default=None, min_length=0, max_length=49, description="Categories for this targeting item."
    )
    countries: list[Annotated[DSPCountryCode | str, lenient_enum(DSPCountryCode)]] | None = Field(
        default=None, min_length=0, max_length=49, description="Countries where this targeting item is available."
    )
    description: str | None = Field(default=None, description="Description of the targeting item.")
    id: str = Field(description="Unique identifier for the targeting item.")
    name: str = Field(description="Name of the targeting item.")
    supplierAdProductId: str | None = Field(
        default=None, description="The supplier ad product associated with this targeting item."
    )
    supplierProposalDestinationId: str | None = Field(
        default=None, description="Supplier proposal destination identifier."
    )
    supplierTargetType: Annotated[DSPSupplierTargetType | str, lenient_enum(DSPSupplierTargetType)]


class DSPSupplierTargetItemAdProductFilter(StrictModel):
    include: list[Annotated[DSPAdProduct, lenient_enum(DSPAdProduct)]] = Field(min_length=1, max_length=1)


class DSPSupplierTargetItemCategoryFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierTargetItemCountryCodeFilter(StrictModel):
    include: list[Annotated[DSPCountryCode, lenient_enum(DSPCountryCode)]] = Field(min_length=1, max_length=10)


class DSPSupplierTargetItemIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierTargetItemNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)
    queryTermMatchType: Annotated[
        DSPSupplierTargetItemNameFilterType, lenient_enum(DSPSupplierTargetItemNameFilterType)
    ]


class DSPSupplierTargetItemSortOption(StrictModel):
    by: Annotated[DSPSupplierTargetItemSortOptionsFields, lenient_enum(DSPSupplierTargetItemSortOptionsFields)]
    direction: Annotated[DSPSortDirection, lenient_enum(DSPSortDirection)] | None = Field(default=None)


class DSPSupplierTargetItemSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierTargetItems: list[DSPSupplierTargetItem] | None = Field(default=None, min_length=0, max_length=500)
    totalResults: int | None = Field(default=None)


class DSPSupplierTargetItemSupplierAdProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierTargetItemSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierTargetItemSupplierTargetTypeFilter(StrictModel):
    include: list[Annotated[DSPSupplierTargetType, lenient_enum(DSPSupplierTargetType)]] = Field(
        min_length=1, max_length=12
    )


__all__ = [
    "DSPAdProduct",
    "DSPCountryCode",
    "DSPQuerySupplierTargetItemRequest",
    "DSPSortDirection",
    "DSPSupplierTargetItem",
    "DSPSupplierTargetItemAdProductFilter",
    "DSPSupplierTargetItemCategoryFilter",
    "DSPSupplierTargetItemCountryCodeFilter",
    "DSPSupplierTargetItemIdFilter",
    "DSPSupplierTargetItemNameFilter",
    "DSPSupplierTargetItemNameFilterType",
    "DSPSupplierTargetItemSortOption",
    "DSPSupplierTargetItemSortOptionsFields",
    "DSPSupplierTargetItemSuccessResponse",
    "DSPSupplierTargetItemSupplierAdProductIdFilter",
    "DSPSupplierTargetItemSupplierProposalDestinationIdFilter",
    "DSPSupplierTargetItemSupplierTargetTypeFilter",
    "DSPSupplierTargetType",
]
