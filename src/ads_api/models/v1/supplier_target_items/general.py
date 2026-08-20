"""Auto-generated models for SupplierTargetItems from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    SortDirection,
)

type AdProduct = Literal["AMAZON_DSP"]
"""
Supported values:
- `AMAZON_DSP`: Amazon Demand-Side Platform ad product.
"""


type CountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type SupplierTargetItemNameFilterType = Literal["BROAD_MATCH"]
"""
Supported values:
- `BROAD_MATCH`: Filter by broad match.
"""


type SupplierTargetItemSortOptionsFields = Literal["name"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| name | ASCENDING,DESCENDING |
"""


type SupplierTargetType = Literal[
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


class QuerySupplierTargetItemRequest(StrictModel):
    adProductFilter: SupplierTargetItemAdProductFilter
    categoryFilter: SupplierTargetItemCategoryFilter | None = Field(default=None)
    countriesFilter: SupplierTargetItemCountryCodeFilter | None = Field(default=None)
    idFilter: SupplierTargetItemIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=20, ge=1, le=500)
    nameFilter: SupplierTargetItemNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    sort: list[SupplierTargetItemSortOption] | None = Field(default=None, min_length=0, max_length=1)
    supplierAdProductIdFilter: SupplierTargetItemSupplierAdProductIdFilter
    supplierProposalDestinationIdFilter: SupplierTargetItemSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierTargetTypeFilter: SupplierTargetItemSupplierTargetTypeFilter


class SupplierTargetItem(LenientModel):
    adProduct: AdProduct | str | None = Field(default=None)
    category: list[str] | None = Field(
        default=None, min_length=0, max_length=49, description="Categories for this targeting item."
    )
    countries: list[CountryCode | str] | None = Field(
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
    supplierTargetType: SupplierTargetType | str


class SupplierTargetItemAdProductFilter(StrictModel):
    include: list[AdProduct] = Field(min_length=1, max_length=1)


class SupplierTargetItemCategoryFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SupplierTargetItemCountryCodeFilter(StrictModel):
    include: list[CountryCode] = Field(min_length=1, max_length=10)


class SupplierTargetItemIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=50)


class SupplierTargetItemNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)
    queryTermMatchType: SupplierTargetItemNameFilterType


class SupplierTargetItemSortOption(StrictModel):
    by: SupplierTargetItemSortOptionsFields
    direction: SortDirection | None = Field(default=None)


class SupplierTargetItemSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierTargetItems: list[SupplierTargetItem] | None = Field(default=None, min_length=0, max_length=500)
    totalResults: int | None = Field(default=None)


class SupplierTargetItemSupplierAdProductIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SupplierTargetItemSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class SupplierTargetItemSupplierTargetTypeFilter(StrictModel):
    include: list[SupplierTargetType] = Field(min_length=1, max_length=12)


__all__ = [
    "AdProduct",
    "CountryCode",
    "QuerySupplierTargetItemRequest",
    "SortDirection",
    "SupplierTargetItem",
    "SupplierTargetItemAdProductFilter",
    "SupplierTargetItemCategoryFilter",
    "SupplierTargetItemCountryCodeFilter",
    "SupplierTargetItemIdFilter",
    "SupplierTargetItemNameFilter",
    "SupplierTargetItemNameFilterType",
    "SupplierTargetItemSortOption",
    "SupplierTargetItemSortOptionsFields",
    "SupplierTargetItemSuccessResponse",
    "SupplierTargetItemSupplierAdProductIdFilter",
    "SupplierTargetItemSupplierProposalDestinationIdFilter",
    "SupplierTargetItemSupplierTargetTypeFilter",
    "SupplierTargetType",
]
