"""Auto-generated models for ReservedTargetPricings from Amazon Ads API v1."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBError,
    SBErrorCode,
    SBErrorsIndex,
)


class SBCreateReservedTargetPricingRequest(StrictModel):
    reservedTargetPricings: list[SBReservedTargetPricingCreate] = Field(min_length=1, max_length=10)


class SBReservedTargetPricing(LenientModel):
    targetPricingId: str = Field(description="A unique identifier for the reserved target pricing.")


class SBReservedTargetPricingCreate(StrictModel):
    pass


class SBReservedTargetPricingMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBReservedTargetPricingMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBReservedTargetPricingMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=9)
    reservedTargetPricing: SBReservedTargetPricing


__all__ = [
    "SBCreateReservedTargetPricingRequest",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBReservedTargetPricing",
    "SBReservedTargetPricingCreate",
    "SBReservedTargetPricingMultiStatusResponse",
    "SBReservedTargetPricingMultiStatusSuccess",
]
