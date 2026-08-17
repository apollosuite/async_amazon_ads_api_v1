"""Auto-generated models for CommitmentSpends from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


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


class DSPSpendDimensionType(StrEnum):
    ADVERTISER = "ADVERTISER"  # Advertiser Level Spend Detail
    CAMPAIGN = "CAMPAIGN"  # Campaign Level Spend Detail
    COMMITMENT = "COMMITMENT"  # Commitment Level Spend Detail
    DEAL = "DEAL"  # Deal Level Spend Detail


class DSPCommitmentSpend(LenientModel):
    accruedSpendValue: float | None = Field(
        default=None, description="Actual accrual spend amount in commitment currency."
    )
    accruedToDateTime: datetime = Field(description="Timestamp for accrual spend.")
    commitmentId: DSPCommitmentSpendIdentifierOut
    currencyCode: Annotated[DSPCurrencyCode | str, lenient_enum(DSPCurrencyCode)]
    projectedSpendValue: float | None = Field(
        default=None, description="Projected spend amount in commitment currency."
    )
    spendAtRiskValue: float | None = Field(default=None, description="Spend at risk amount in commitment currency.")
    spendDimensionType: Annotated[DSPSpendDimensionType | str, lenient_enum(DSPSpendDimensionType)]


class DSPCommitmentSpendIdentifier(StrictModel):
    commitmentId: str = Field(description="Commitment ID associated with the commitment.")
    spendDimension: DSPSpendDimension | None = Field(default=None)


class DSPCommitmentSpendIdentifierOut(LenientModel):
    commitmentId: str = Field(description="Commitment ID associated with the commitment.")
    spendDimension: DSPSpendDimensionOut | None = Field(default=None)


class DSPCommitmentSpendMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[DSPCommitmentSpendMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=1)


class DSPCommitmentSpendMultiStatusSuccess(LenientModel):
    commitmentSpend: DSPCommitmentSpend
    index: int = Field(ge=0, le=0)


class DSPError(LenientModel):
    code: Annotated[DSPErrorCode | str, lenient_enum(DSPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class DSPErrorsIndex(LenientModel):
    errors: list[DSPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class DSPRetrieveCommitmentSpendRequest(StrictModel):
    commitmentIds: list[DSPCommitmentSpendIdentifier] = Field(min_length=1, max_length=1)


class DSPSpendDimensionAdvertiserAccountId(StrictModel):
    advertiserAccountId: str


class DSPSpendDimensionCampaignId(StrictModel):
    campaignId: str


class DSPSpendDimensionDealId(StrictModel):
    dealId: str


type DSPSpendDimension = DSPSpendDimensionAdvertiserAccountId | DSPSpendDimensionCampaignId | DSPSpendDimensionDealId


class DSPSpendDimensionOutAdvertiserAccountId(LenientModel):
    advertiserAccountId: str


class DSPSpendDimensionOutCampaignId(LenientModel):
    campaignId: str


class DSPSpendDimensionOutDealId(LenientModel):
    dealId: str


type DSPSpendDimensionOut = DSPSpendDimensionOutAdvertiserAccountId | DSPSpendDimensionOutCampaignId | DSPSpendDimensionOutDealId

__all__ = [
    "DSPCommitmentSpend",
    "DSPCommitmentSpendIdentifier",
    "DSPCommitmentSpendIdentifierOut",
    "DSPCommitmentSpendMultiStatusResponse",
    "DSPCommitmentSpendMultiStatusSuccess",
    "DSPCurrencyCode",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPRetrieveCommitmentSpendRequest",
    "DSPSpendDimension",
    "DSPSpendDimensionOut",
    "DSPSpendDimensionType",
]
