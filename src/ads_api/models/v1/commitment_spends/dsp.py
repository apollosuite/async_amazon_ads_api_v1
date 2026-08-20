"""Auto-generated models for CommitmentSpends from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPCurrencyCode,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
)

type DSPSpendDimensionType = Literal["ADVERTISER", "CAMPAIGN", "COMMITMENT", "DEAL"]
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
    currencyCode: DSPCurrencyCode | str
    projectedSpendValue: float | None = Field(
        default=None, description="Projected spend amount in commitment currency."
    )
    spendAtRiskValue: float | None = Field(default=None, description="Spend at risk amount in commitment currency.")
    spendDimensionType: DSPSpendDimensionType | str


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
