"""Auto-generated models for BrandedKeywordsPricings from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .enums import SBAdvertisingDealPriceType, SBCurrencyCode, SBErrorCode
from .shared import SBAdvertisingDealPrice, SBErrorsIndex


class SBBrandedKeywordsPricing(BaseModel):
    model_config = ConfigDict(extra="allow")

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


class SBBrandedKeywordsPricingCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str | None = Field(
        default=None, description="Identifier of the existing deal to price. Omit when pricing a new deal."
    )
    endDateTime: datetime = Field(description="The end date time for the deal.")
    keywords: list[str] = Field(
        min_length=1, max_length=1000, description="The list of branded keywords advertiser wants to reserve."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")


class SBBrandedKeywordsPricingMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBBrandedKeywordsPricingMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBBrandedKeywordsPricingMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandedKeywordsPricing: SBBrandedKeywordsPricing
    index: int = Field(ge=0, le=9)


class SBCreateBrandedKeywordsPricingRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandedKeywordsPricings: list[SBBrandedKeywordsPricingCreate] | None = Field(
        default=None, min_length=1, max_length=10
    )


class SBKeywordsPricing(BaseModel):
    """The detail of keywords pricing."""

    model_config = ConfigDict(extra="allow")

    price: SBAdvertisingDealPrice
    validKeywords: list[str] = Field(min_length=1, max_length=1000, description="List of valid keywords.")


class SBRejectedKeyword(BaseModel):
    """The detail of a rejected keyword."""

    model_config = ConfigDict(extra="allow")

    keyword: str = Field(description="The keyword that has been rejected.")
    reason: str = Field(description="The reason keyword has been rejected for this advertiser.")


__all__ = [
    "SBAdvertisingDealPriceType",
    "SBBrandedKeywordsPricingCreate",
    "SBCreateBrandedKeywordsPricingRequest",
    "SBCurrencyCode",
    "SBErrorCode",
]
