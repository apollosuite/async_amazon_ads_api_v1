"""Auto-generated models for Commitments from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type DSPCommitmentCommitmentNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `EXACT_MATCH`: Filter by exact match.
- `BROAD_MATCH`: Filter by broad match.
"""


type DSPCurrencyCode = Literal[
    "AED",
    "AUD",
    "BRL",
    "CAD",
    "DKK",
    "EUR",
    "GBP",
    "INR",
    "JPY",
    "MXN",
    "NOK",
    "NZD",
    "SAR",
    "SEK",
    "SGD",
    "TRY",
    "USD",
]
"""
Supported values:
- `AED`: United Arab Emirates Dirham
- `AUD`: Australian Dollar
- `BRL`: Brazilian Real
- `CAD`: Canadian Dollar
- `DKK`: Danish Krone
- `EUR`: Euro
- `GBP`: British Pound Sterling
- `INR`: Indian Rupee
- `JPY`: Japanese Yen
- `MXN`: Mexican Peso
- `NOK`: Norwegian Krone
- `NZD`: New Zealand Dollar
- `SAR`: Saudi Riyal
- `SEK`: Swedish Krona
- `SGD`: Singapore Dollar
- `TRY`: Turkish Lira
- `USD`: United States Dollar
"""


type DSPFulfillmentLevel = Literal["LEVEL_0", "LEVEL_5"]
"""
Supported values:
- `LEVEL_0`: Tracking-only commitments
- `LEVEL_5`: Prioritize commitment over campaign performance
"""


type DSPSpendCalculationMode = Literal["ADVERTISER_ACCOUNT", "CAMPAIGN", "MANAGER_ACCOUNT"]
"""
Supported values:
- `ADVERTISER_ACCOUNT`: Spend is aggregated at the advertiser account level
- `CAMPAIGN`: Spend is aggregated at the campaign level
- `MANAGER_ACCOUNT`: Spend is aggregated at the manager account level
"""


type ErrorCode = Literal[
    "BAD_REQUEST", "CONTENT_TOO_LARGE", "FORBIDDEN", "INTERNAL_ERROR", "NOT_FOUND", "TOO_MANY_REQUESTS", "UNAUTHORIZED"
]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


class DSPCommitment(LenientModel):
    advertiserIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Advertiser IDs associated with the commitment."
    )
    campaignIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Campaign IDs associated with the commitment."
    )
    commitmentId: str = Field(description="A unique identifier for the commitment.")
    commitmentName: str = Field(description="The name of the commitment.")
    committedSpend: float = Field(description="The total committed spend for the commitment.")
    currencyCode: DSPCurrencyCode | str
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime = Field(description="The end date and time of the commitment.")
    fulfillmentLevel: DSPFulfillmentLevel | str
    spendCalculationMode: DSPSpendCalculationMode | str
    startDateTime: datetime = Field(description="The start date and time of the commitment.")


class DSPCommitmentAdvertiserAccountIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class DSPCommitmentAdvertisingDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class DSPCommitmentCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class DSPCommitmentCommitmentIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPCommitmentCommitmentNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)
    queryTermMatchType: DSPCommitmentCommitmentNameFilterType


class DSPCommitmentCreate(StrictModel):
    advertiserIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Advertiser IDs associated with the commitment."
    )
    campaignIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Campaign IDs associated with the commitment."
    )
    commitmentName: str = Field(description="The name of the commitment.")
    committedSpend: float = Field(description="The total committed spend for the commitment.")
    currencyCode: DSPCurrencyCode
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime = Field(description="The end date and time of the commitment.")
    fulfillmentLevel: DSPFulfillmentLevel
    spendCalculationMode: DSPSpendCalculationMode
    startDateTime: datetime = Field(description="The start date and time of the commitment.")


class DSPCommitmentMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[DSPCommitmentMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class DSPCommitmentMultiStatusSuccess(LenientModel):
    commitment: DSPCommitment
    index: int = Field(ge=0, le=999)


class DSPCommitmentSpendCalculationModeFilter(StrictModel):
    include: list[DSPSpendCalculationMode] = Field(min_length=1, max_length=1)


class DSPCommitmentSuccessResponse(LenientModel):
    commitments: list[DSPCommitment] | None = Field(default=None, min_length=0, max_length=1000)
    nextToken: str | None = Field(default=None)


class DSPCommitmentUpdate(StrictModel):
    advertiserIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Advertiser IDs associated with the commitment."
    )
    campaignIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Campaign IDs associated with the commitment."
    )
    commitmentId: str = Field(description="A unique identifier for the commitment.")
    commitmentName: str | None = Field(default=None, description="The name of the commitment.")
    committedSpend: float | None = Field(default=None, description="The total committed spend for the commitment.")
    currencyCode: DSPCurrencyCode | None = Field(default=None)
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime | None = Field(default=None, description="The end date and time of the commitment.")
    fulfillmentLevel: DSPFulfillmentLevel | None = Field(default=None)
    spendCalculationMode: DSPSpendCalculationMode | None = Field(default=None)
    startDateTime: datetime | None = Field(default=None, description="The start date and time of the commitment.")


class DSPCreateCommitmentRequest(StrictModel):
    commitments: list[DSPCommitmentCreate] = Field(min_length=1, max_length=1000)


class DSPQueryCommitmentRequest(StrictModel):
    advertiserIdsFilter: DSPCommitmentAdvertiserAccountIdFilter | None = Field(default=None)
    campaignIdsFilter: DSPCommitmentCampaignIdFilter | None = Field(default=None)
    commitmentIdFilter: DSPCommitmentCommitmentIdFilter | None = Field(default=None)
    commitmentNameFilter: DSPCommitmentCommitmentNameFilter | None = Field(default=None)
    dealIdsFilter: DSPCommitmentAdvertisingDealIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=10, le=1000)
    nextToken: str | None = Field(default=None)
    spendCalculationModeFilter: DSPCommitmentSpendCalculationModeFilter | None = Field(default=None)


class DSPRetrieveCommitmentRequest(StrictModel):
    commitmentIds: list[str] = Field(min_length=1, max_length=1000)


class DSPUpdateCommitmentRequest(StrictModel):
    commitments: list[DSPCommitmentUpdate] = Field(min_length=1, max_length=1000)


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


__all__ = [
    "DSPCommitment",
    "DSPCommitmentAdvertiserAccountIdFilter",
    "DSPCommitmentAdvertisingDealIdFilter",
    "DSPCommitmentCampaignIdFilter",
    "DSPCommitmentCommitmentIdFilter",
    "DSPCommitmentCommitmentNameFilter",
    "DSPCommitmentCommitmentNameFilterType",
    "DSPCommitmentCreate",
    "DSPCommitmentMultiStatusResponse",
    "DSPCommitmentMultiStatusSuccess",
    "DSPCommitmentSpendCalculationModeFilter",
    "DSPCommitmentSuccessResponse",
    "DSPCommitmentUpdate",
    "DSPCreateCommitmentRequest",
    "DSPCurrencyCode",
    "DSPFulfillmentLevel",
    "DSPQueryCommitmentRequest",
    "DSPRetrieveCommitmentRequest",
    "DSPSpendCalculationMode",
    "DSPUpdateCommitmentRequest",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
]
