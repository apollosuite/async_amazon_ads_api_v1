"""Auto-generated models for SupplierTargetItems from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPSortDirection,
)

type DSPAdProduct = Literal["AMAZON_DSP",]  # Amazon Demand-Side Platform ad product.
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type DSPCountryCode = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AU",
    "BR",
    "CA",
    "DE",
    "ES",
    "FR",
    "GB",
    "IT",
    "JP",
    "KR",
    "MX",
    "US",
]


type DSPSupplierTargetItemNameFilterType = Literal["BROAD_MATCH",]  # Filter by broad match.
"""
Supported values:
- `BROAD_MATCH`: Filter by broad match.
"""


type DSPSupplierTargetItemSortOptionsFields = Literal["name"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| name | ASCENDING,DESCENDING |
"""


type DSPSupplierTargetType = Literal[
    "APP",
    "AUDIENCE",
    "AUDIENCE_AGE",
    "AUDIENCE_EDUCATION",
    "AUDIENCE_GENDER",
    "AUDIENCE_HOMEOWNERSHIP",
    "AUDIENCE_HOUSEHOLD_COMPOSITION",
    "AUDIENCE_HOUSEHOLD_INCOME",
    "AUDIENCE_INTERESTS",
    "AUDIENCE_IN_MARKET",
    "AUDIENCE_MARITAL_STATUS",
    "AUDIENCE_MOOD",
    "AUDIENCE_SOCIOECONOMIC_GROUP",
    "CONTENT_CATEGORY",
    "CONTENT_GENRE",
    "CONTENT_RATING",
    "CONTENT_SENSITIVE_CATEGORY",
    "DAYPART",
    "DAYPART_DAY",
    "DAYPART_TIME",
    "DEVICE_OPERATING_SYSTEM",
    "DEVICE_TYPE",
    "LOCATION_CITY",
    "LOCATION_COUNTRY",
    "LOCATION_DESIGNATED_MARKET_AREA",
    "LOCATION_METRO",
    "LOCATION_POSTAL_CODE",
    "LOCATION_REGION",
    "POSITION_VIDEO",
]


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
    adProduct: DSPAdProduct | str | None = Field(
        default=None,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )
    category: list[str] | None = Field(
        default=None, min_length=0, max_length=49, description="Categories for this targeting item."
    )
    countries: list[DSPCountryCode | str] | None = Field(
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
    supplierTargetType: DSPSupplierTargetType | str


class DSPSupplierTargetItemAdProductFilter(StrictModel):
    include: list[DSPAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
""",
    )


class DSPSupplierTargetItemCategoryFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierTargetItemCountryCodeFilter(StrictModel):
    include: list[DSPCountryCode | str] = Field(min_length=1, max_length=10)


class DSPSupplierTargetItemIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class DSPSupplierTargetItemNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)
    queryTermMatchType: DSPSupplierTargetItemNameFilterType = Field(description="""
Supported values:
- `BROAD_MATCH`: Filter by broad match.
""")


class DSPSupplierTargetItemSortOption(StrictModel):
    by: DSPSupplierTargetItemSortOptionsFields
    direction: DSPSortDirection | None = Field(
        default=None,
        description="""
Supported values:
- `ASCENDING`: Sort in ascending order
- `DESCENDING`: Sort in descending order
""",
    )


class DSPSupplierTargetItemSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierTargetItems: list[DSPSupplierTargetItem] | None = Field(default=None, min_length=0, max_length=500)
    totalResults: int | None = Field(default=None)


class DSPSupplierTargetItemSupplierAdProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierTargetItemSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class DSPSupplierTargetItemSupplierTargetTypeFilter(StrictModel):
    include: list[DSPSupplierTargetType | str] = Field(min_length=1, max_length=12)


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
