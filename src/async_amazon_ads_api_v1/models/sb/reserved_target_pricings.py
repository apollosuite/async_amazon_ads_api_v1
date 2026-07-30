"""Auto-generated models for ReservedTargetPricings from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .enums import SBErrorCode
from .shared import SBErrorsIndex


class SBCreateReservedTargetPricingRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reservedTargetPricings: list[SBReservedTargetPricingCreate] = Field(min_length=1, max_length=10)


class SBReservedTargetPricing(BaseModel):
    model_config = ConfigDict(extra="allow")

    targetPricingId: str | None = Field(
        default=None, description="A unique identifier for the reserved target pricing."
    )


class SBReservedTargetPricingCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SBReservedTargetPricingMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBReservedTargetPricingMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBReservedTargetPricingMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=9)
    reservedTargetPricing: SBReservedTargetPricing | None = Field(default=None)


__all__ = ["SBCreateReservedTargetPricingRequest", "SBErrorCode", "SBReservedTargetPricingCreate"]
