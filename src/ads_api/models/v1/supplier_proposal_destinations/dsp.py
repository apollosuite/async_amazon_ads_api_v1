"""Auto-generated models for SupplierProposalDestinations from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPSortDirection,
)

type DSPCountryCode = Literal[
    "AD", "AE", "AF", "AG", "AI", "AU", "BR", "CA", "DE", "ES", "FR", "GB", "IT", "JP", "KR", "MX", "US"
]


type DSPSupplierProposalDestinationSortOptionsFields = Literal["supplierProposalDestinationName"]
"""
Specify which field to order by.
| Field Name | Supported Ordering |
| --- | --- |
| supplierProposalDestinationName | ASCENDING,DESCENDING |
"""


class DSPQuerySupplierProposalDestinationRequest(StrictModel):
    maxResults: int | None = Field(default=10, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    sort: list[DSPSupplierProposalDestinationSortOption] | None = Field(default=None, min_length=0, max_length=1)
    supplierProposalDestinationIdFilter: DSPSupplierProposalDestinationSupplierProposalDestinationIdFilter | None = (
        Field(default=None)
    )
    supplierProposalDestinationNameFilter: (
        DSPSupplierProposalDestinationSupplierProposalDestinationNameFilter | None
    ) = Field(default=None)


class DSPSupplierProposalDestination(LenientModel):
    countries: list[DSPCountryCode | str] | None = Field(
        default=None,
        min_length=0,
        max_length=49,
        description="The list of ISO 3166-1 alpha-2 formatted country codes allowed for the supplier proposal destination.",
    )
    description: str | None = Field(default=None, description="The description of the supplier proposal destination.")
    supplierProposalDestinationId: str = Field(description="The identifier ID for this supplier proposal destination.")
    supplierProposalDestinationName: str = Field(description="The name for the supplier proposal destination.")


class DSPSupplierProposalDestinationSortOption(StrictModel):
    by: DSPSupplierProposalDestinationSortOptionsFields
    direction: DSPSortDirection | None = Field(default=None)


class DSPSupplierProposalDestinationSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    supplierProposalDestinations: list[DSPSupplierProposalDestination] | None = Field(
        default=None, min_length=0, max_length=100
    )
    totalResults: int | None = Field(default=None)


class DSPSupplierProposalDestinationSupplierProposalDestinationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class DSPSupplierProposalDestinationSupplierProposalDestinationNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


__all__ = [
    "DSPCountryCode",
    "DSPQuerySupplierProposalDestinationRequest",
    "DSPSortDirection",
    "DSPSupplierProposalDestination",
    "DSPSupplierProposalDestinationSortOption",
    "DSPSupplierProposalDestinationSortOptionsFields",
    "DSPSupplierProposalDestinationSuccessResponse",
    "DSPSupplierProposalDestinationSupplierProposalDestinationIdFilter",
    "DSPSupplierProposalDestinationSupplierProposalDestinationNameFilter",
]
