"""Auto-generated models for CommitmentSpends from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type DSPCurrencyCode = Literal[
    "AED",  # United Arab Emirates Dirham
    "AUD",  # Australian Dollar
    "BRL",  # Brazilian Real
    "CAD",  # Canadian Dollar
    "DKK",  # Danish Krone
    "EUR",  # Euro
    "GBP",  # British Pound Sterling
    "INR",  # Indian Rupee
    "JPY",  # Japanese Yen
    "MXN",  # Mexican Peso
    "NOK",  # Norwegian Krone
    "NZD",  # New Zealand Dollar
    "SAR",  # Saudi Riyal
    "SEK",  # Swedish Krona
    "SGD",  # Singapore Dollar
    "TRY",  # Turkish Lira
    "USD",  # United States Dollar
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


type DSPErrorCode = Literal[
    "BAD_REQUEST",  # The request is not valid considering the documented schema.
    "CONTENT_TOO_LARGE",  # The request is too large. Consider splitting it into multiple requests.
    "FORBIDDEN",  # The caller is not authorized to make the given request.
    "INTERNAL_ERROR",  # The server encountered an unexpected condition that prevented it from fulfilling the request.
    "NOT_FOUND",  # The requested resource does not exist.
    "TOO_MANY_REQUESTS",  # There have been too many requests, please slow down your call rate.
    "UNAUTHORIZED",  # The request lacks the necessary credentials.
]
"""
Supported values:
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `NOT_FOUND`: The requested resource does not exist.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
"""


type DSPSpendDimensionType = Literal[
    "ADVERTISER",  # Advertiser Level Spend Detail
    "CAMPAIGN",  # Campaign Level Spend Detail
    "COMMITMENT",  # Commitment Level Spend Detail
    "DEAL",  # Deal Level Spend Detail
]
"""
Supported values:
- `COMMITMENT`: Commitment Level Spend Detail
- `ADVERTISER`: Advertiser Level Spend Detail
- `CAMPAIGN`: Campaign Level Spend Detail
- `DEAL`: Deal Level Spend Detail
"""


class DSPCommitmentSpend(LenientModel):
    accruedSpendValue: float | None = Field(
        default=None, description="Actual accrual spend amount in commitment currency."
    )
    accruedToDateTime: datetime = Field(description="Timestamp for accrual spend.")
    commitmentId: DSPCommitmentSpendIdentifierOut
    currencyCode: DSPCurrencyCode | str = Field(description="""
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
""")
    projectedSpendValue: float | None = Field(
        default=None, description="Projected spend amount in commitment currency."
    )
    spendAtRiskValue: float | None = Field(default=None, description="Spend at risk amount in commitment currency.")
    spendDimensionType: DSPSpendDimensionType | str = Field(description="""
Supported values:
- `COMMITMENT`: Commitment Level Spend Detail
- `ADVERTISER`: Advertiser Level Spend Detail
- `CAMPAIGN`: Campaign Level Spend Detail
- `DEAL`: Deal Level Spend Detail
""")


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
    code: DSPErrorCode | str = Field(description="""
Supported values:
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `CONTENT_TOO_LARGE`: The request is too large. Consider splitting it into multiple requests.
- `NOT_FOUND`: The requested resource does not exist.
- `BAD_REQUEST`: The request is not valid considering the documented schema.
""")
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
