"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex
del TYPE_CHECKING


class SBCreateReservedTargetPricingRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reservedTargetPricings: list[SBReservedTargetPricingCreate] | None = None


class SBReservedTargetPricing(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetPricingId: str  # A unique identifier for the reserved target pricing.


class SBReservedTargetPricingCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    targetPricingId: str  # A unique identifier for the reserved target pricing.


class SBReservedTargetPricingMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBReservedTargetPricingMultiStatusSuccess] | None = None


class SBReservedTargetPricingMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    reservedTargetPricing: SBReservedTargetPricing


__all__ = [
    "SBCreateReservedTargetPricingRequest",
    "SBReservedTargetPricing",
    "SBReservedTargetPricingCreate",
    "SBReservedTargetPricingMultiStatusResponse",
    "SBReservedTargetPricingMultiStatusSuccess",
]
