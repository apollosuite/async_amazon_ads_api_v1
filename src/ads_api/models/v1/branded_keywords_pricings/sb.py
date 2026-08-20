"""Auto-generated models for BrandedKeywordsPricings from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBAdvertisingDealPrice,
    SBAdvertisingDealPriceType,
    SBCurrencyCode,
    SBError,
    SBErrorCode,
    SBErrorsIndex,
)


class SBBrandedKeywordsPricing(LenientModel):
    advertisingDealId: str | None = Field(
        default=None, description="Identifier of the existing deal to price. Omit when pricing a new deal."
    )
    brandedKeywordsPricingId: str = Field(description="A unique identifier for the branded keywords pricing.")
    endDateTime: datetime = Field(description="The end date time for the deal.")
    keywords: list[str] = Field(
        min_length=1, max_length=1000, description="The list of branded keywords advertiser wants to reserve."
    )
    keywordsPricing: SBKeywordsPricing | None = Field(default=None)
    rejectedKeywords: list[SBRejectedKeyword] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="The list of branded keywords rejected for reservation by this advertiser.",
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")


class SBBrandedKeywordsPricingCreate(StrictModel):
    advertisingDealId: str | None = Field(
        default=None, description="Identifier of the existing deal to price. Omit when pricing a new deal."
    )
    endDateTime: datetime = Field(description="The end date time for the deal.")
    keywords: list[str] = Field(
        min_length=1, max_length=1000, description="The list of branded keywords advertiser wants to reserve."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")


class SBBrandedKeywordsPricingMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBBrandedKeywordsPricingMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBBrandedKeywordsPricingMultiStatusSuccess(LenientModel):
    brandedKeywordsPricing: SBBrandedKeywordsPricing
    index: int = Field(ge=0, le=9)


class SBCreateBrandedKeywordsPricingRequest(StrictModel):
    brandedKeywordsPricings: list[SBBrandedKeywordsPricingCreate] | None = Field(
        default=None, min_length=1, max_length=10
    )


class SBKeywordsPricing(LenientModel):
    """The detail of keywords pricing."""

    price: SBAdvertisingDealPrice
    validKeywords: list[str] = Field(min_length=1, max_length=1000, description="List of valid keywords.")


class SBRejectedKeyword(LenientModel):
    """The detail of a rejected keyword."""

    keyword: str = Field(description="The keyword that has been rejected.")
    reason: str = Field(description="The reason keyword has been rejected for this advertiser.")


__all__ = [
    "SBAdvertisingDealPrice",
    "SBAdvertisingDealPriceType",
    "SBBrandedKeywordsPricing",
    "SBBrandedKeywordsPricingCreate",
    "SBBrandedKeywordsPricingMultiStatusResponse",
    "SBBrandedKeywordsPricingMultiStatusSuccess",
    "SBCreateBrandedKeywordsPricingRequest",
    "SBCurrencyCode",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBKeywordsPricing",
    "SBRejectedKeyword",
]
