"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex
    from .shared import SBAdvertisingDealPrice


class SBBrandedKeywordsPricing(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str | None = (
        None  # Identifier of the existing deal to price. Omit when pricing a new deal.
    )
    brandedKeywordsPricingId: str  # A unique identifier for the branded keywords pricing.
    endDateTime: datetime  # The end date time for the deal.
    keywords: list[str]  # The list of branded keywords advertiser wants to reserve.
    keywordsPricing: SBKeywordsPricing | None = None
    rejectedKeywords: list[SBRejectedKeyword] | None = (
        None  # The list of branded keywords rejected for reservation by this advertiser.
    )
    startDateTime: datetime  # The start date time for the deal.


class SBBrandedKeywordsPricingCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str | None = (
        None  # Identifier of the existing deal to price. Omit when pricing a new deal.
    )
    endDateTime: datetime  # The end date time for the deal.
    keywords: list[str]  # The list of branded keywords advertiser wants to reserve.
    startDateTime: datetime  # The start date time for the deal.


class SBBrandedKeywordsPricingMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBBrandedKeywordsPricingMultiStatusSuccess] | None = None


class SBBrandedKeywordsPricingMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    brandedKeywordsPricing: SBBrandedKeywordsPricing
    index: int


class SBCreateBrandedKeywordsPricingRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    brandedKeywordsPricings: list[SBBrandedKeywordsPricingCreate] | None = None


class SBKeywordsPricing(BaseModel):
    """The detail of keywords pricing."""

    model_config = ConfigDict(extra="forbid")

    price: SBAdvertisingDealPrice
    validKeywords: list[str]  # List of valid keywords.


class SBRejectedKeyword(BaseModel):
    """The detail of a rejected keyword."""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # The keyword that has been rejected.
    reason: str  # The reason keyword has been rejected for this advertiser.
