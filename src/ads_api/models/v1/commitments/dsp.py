"""Auto-generated models for Commitments from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class DSPCommitmentCommitmentNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class DSPCurrencyCode(StrEnum):
    AED = "AED"  # United Arab Emirates Dirham
    AUD = "AUD"  # Australian Dollar
    BRL = "BRL"  # Brazilian Real
    CAD = "CAD"  # Canadian Dollar
    DKK = "DKK"  # Danish Krone
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    INR = "INR"  # Indian Rupee
    JPY = "JPY"  # Japanese Yen
    MXN = "MXN"  # Mexican Peso
    NOK = "NOK"  # Norwegian Krone
    NZD = "NZD"  # New Zealand Dollar
    SAR = "SAR"  # Saudi Riyal
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    TRY = "TRY"  # Turkish Lira
    USD = "USD"  # United States Dollar


class DSPErrorCode(StrEnum):
    BAD_REQUEST = "BAD_REQUEST"  # The request is not valid considering the documented schema.
    CONTENT_TOO_LARGE = "CONTENT_TOO_LARGE"  # The request is too large. Consider splitting it into multiple requests.
    FORBIDDEN = "FORBIDDEN"  # The caller is not authorized to make the given request.
    INTERNAL_ERROR = "INTERNAL_ERROR"  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    NOT_FOUND = "NOT_FOUND"  # The requested resource does not exist.
    TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"  # There have been too many requests, please slow down your call rate.
    UNAUTHORIZED = "UNAUTHORIZED"  # The request lacks the necessary credentials.


class DSPFulfillmentLevel(StrEnum):
    LEVEL_0 = "LEVEL_0"  # Tracking-only commitments
    LEVEL_5 = "LEVEL_5"  # Prioritize commitment over campaign performance


class DSPSpendCalculationMode(StrEnum):
    ADVERTISER_ACCOUNT = "ADVERTISER_ACCOUNT"  # Spend is aggregated at the advertiser account level
    CAMPAIGN = "CAMPAIGN"  # Spend is aggregated at the campaign level
    MANAGER_ACCOUNT = "MANAGER_ACCOUNT"  # Spend is aggregated at the manager account level


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
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime = Field(description="The end date and time of the commitment.")
    fulfillmentLevel: Annotated[DSPFulfillmentLevel | str, lenient_enum(DSPFulfillmentLevel)]
    spendCalculationMode: Annotated[DSPSpendCalculationMode | str, lenient_enum(DSPSpendCalculationMode)]
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
    queryTermMatchType: Annotated[
        DSPCommitmentCommitmentNameFilterType, lenient_enum(DSPCommitmentCommitmentNameFilterType)
    ]


class DSPCommitmentCreate(StrictModel):
    advertiserIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Advertiser IDs associated with the commitment."
    )
    campaignIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Campaign IDs associated with the commitment."
    )
    commitmentName: str = Field(description="The name of the commitment.")
    committedSpend: float = Field(description="The total committed spend for the commitment.")
    currencyCode: Annotated[DSPCurrencyCode, lenient_enum(DSPCurrencyCode)]
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime = Field(description="The end date and time of the commitment.")
    fulfillmentLevel: Annotated[DSPFulfillmentLevel, lenient_enum(DSPFulfillmentLevel)]
    spendCalculationMode: Annotated[DSPSpendCalculationMode, lenient_enum(DSPSpendCalculationMode)]
    startDateTime: datetime = Field(description="The start date and time of the commitment.")


class DSPCommitmentMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[DSPCommitmentMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1000)


class DSPCommitmentMultiStatusSuccess(LenientModel):
    commitment: DSPCommitment
    index: int = Field(ge=0, le=999)


class DSPCommitmentSpendCalculationModeFilter(StrictModel):
    include: list[Annotated[DSPSpendCalculationMode, lenient_enum(DSPSpendCalculationMode)]] = Field(
        min_length=1, max_length=1
    )


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
    currencyCode: Annotated[DSPCurrencyCode, lenient_enum(DSPCurrencyCode)] | None = Field(default=None)
    dealIds: list[str] | None = Field(
        default=None, min_length=0, max_length=1000, description="Deal IDs associated with the commitment."
    )
    endDateTime: datetime | None = Field(default=None, description="The end date and time of the commitment.")
    fulfillmentLevel: Annotated[DSPFulfillmentLevel, lenient_enum(DSPFulfillmentLevel)] | None = Field(default=None)
    spendCalculationMode: Annotated[DSPSpendCalculationMode, lenient_enum(DSPSpendCalculationMode)] | None = Field(
        default=None
    )
    startDateTime: datetime | None = Field(default=None, description="The start date and time of the commitment.")


class DSPCreateCommitmentRequest(StrictModel):
    commitments: list[DSPCommitmentCreate] = Field(min_length=1, max_length=1000)


class DSPError(LenientModel):
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


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
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPFulfillmentLevel",
    "DSPQueryCommitmentRequest",
    "DSPRetrieveCommitmentRequest",
    "DSPSpendCalculationMode",
    "DSPUpdateCommitmentRequest",
]
