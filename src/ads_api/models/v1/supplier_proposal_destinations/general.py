"""Auto-generated models for SupplierProposalDestinations from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    SortDirection,
)

type CountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type SupplierProposalDestinationSortOptionsFields = Literal["supplierProposalDestinationName"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| supplierProposalDestinationName | ASCENDING,DESCENDING |
"""


class QuerySupplierProposalDestinationRequest(StrictModel):
    maxResults: int | None = Field(default=10, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    sort: list[SupplierProposalDestinationSortOption] | None = Field(default=None, min_length=0, max_length=1)
    supplierProposalDestinationIdFilter: SupplierProposalDestinationSupplierProposalDestinationIdFilter | None = Field(
        default=None
    )
    supplierProposalDestinationNameFilter: SupplierProposalDestinationSupplierProposalDestinationNameFilter | None = (
        Field(default=None)
    )


class SupplierProposalDestination(LenientModel):
    countries: list[CountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The list of ISO 3166-1 alpha-2 formatted country codes allowed for the supplier proposal destination.",
    )
    description: str | None = Field(default=None, description="The description of the supplier proposal destination.")
    supplierProposalDestinationId: str = Field(description="The identifier ID for this supplier proposal destination.")
    supplierProposalDestinationName: str = Field(description="The name for the supplier proposal destination.")


class SupplierProposalDestinationSortOption(StrictModel):
    by: SupplierProposalDestinationSortOptionsFields
    direction: SortDirection | None = Field(default=None)


class SupplierProposalDestinationSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposalDestinations: list[SupplierProposalDestination] | None = Field(
        default=None, min_length=0, max_length=100
    )
    totalResults: int | None = Field(default=None)


class SupplierProposalDestinationSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SupplierProposalDestinationSupplierProposalDestinationNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


__all__ = [
    "CountryCode",
    "QuerySupplierProposalDestinationRequest",
    "SortDirection",
    "SupplierProposalDestination",
    "SupplierProposalDestinationSortOption",
    "SupplierProposalDestinationSortOptionsFields",
    "SupplierProposalDestinationSuccessResponse",
    "SupplierProposalDestinationSupplierProposalDestinationIdFilter",
    "SupplierProposalDestinationSupplierProposalDestinationNameFilter",
]
