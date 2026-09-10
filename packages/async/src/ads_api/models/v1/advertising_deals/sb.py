"""Auto-generated models for AdvertisingDeals from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

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

type SBAdvertisingDealNameFilterType = Literal["BROAD_MATCH", "EXACT_MATCH"]
"""
Supported values:
- `BROAD_MATCH`: Filter by broad match.
- `EXACT_MATCH`: Filter by exact match.
"""


type SBAdvertisingDealState = Literal["DRAFT", "PROPOSED"]


type SBAdvertisingDealStatusEnum = Literal["DRAFT", "MODERATION_APPROVED", "PROPOSED"]
"""
Supported values:
- `DRAFT`: The deal has not been submitted yet.
- `MODERATION_APPROVED`: The deal has passed moderation.
- `PROPOSED`: The deal has been submitted for moderation.
"""


class SBAdvertisingDeal(LenientModel):
    advertisingDealId: str = Field(description="A unique identifier for a deal.")
    endDateTime: datetime = Field(description="The end date time for the deal.")
    name: str = Field(description="The name of the deal.")
    price: SBAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")
    state: SBAdvertisingDealState | str | None = Field(default=None)
    status: SBAdvertisingDealStatus


class SBAdvertisingDealAdvertisingDealIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)


class SBAdvertisingDealCreate(StrictModel):
    endDateTime: datetime = Field(description="The end date time for the deal.")
    name: str = Field(description="The name of the deal.")
    price: SBCreateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")
    state: SBAdvertisingDealState | None = Field(default=None)


class SBAdvertisingDealMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdvertisingDealMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdvertisingDealMultiStatusSuccess(LenientModel):
    advertisingDeal: SBAdvertisingDeal
    index: int = Field(ge=0, le=9)


class SBAdvertisingDealNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=10)
    queryTermMatchType: SBAdvertisingDealNameFilterType


class SBAdvertisingDealStatus(LenientModel):
    status: SBAdvertisingDealStatusEnum | str


class SBAdvertisingDealSuccessResponse(LenientModel):
    advertisingDeals: list[SBAdvertisingDeal] | None = Field(default=None, min_length=0, max_length=50)
    nextToken: str | None = Field(default=None)


class SBAdvertisingDealUpdate(StrictModel):
    advertisingDealId: str = Field(description="A unique identifier for a deal.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the deal.")
    name: str | None = Field(default=None, description="The name of the deal.")
    price: SBUpdateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the deal.")
    state: SBAdvertisingDealState | None = Field(default=None)


class SBCreateAdvertisingDealPrice(StrictModel):
    priceType: SBAdvertisingDealPriceType
    value: float = Field(description="The monetary amount of the price in the given currency.")


class SBCreateAdvertisingDealRequest(StrictModel):
    advertisingDeals: list[SBAdvertisingDealCreate] | None = Field(default=None, min_length=1, max_length=10)


class SBDeleteAdvertisingDealRequest(StrictModel):
    advertisingDealIds: list[str] | None = Field(default=None, min_length=1, max_length=10)


class SBQueryAdvertisingDealRequest(StrictModel):
    advertisingDealIdFilter: SBAdvertisingDealAdvertisingDealIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=50)
    nameFilter: SBAdvertisingDealNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)


class SBUpdateAdvertisingDealPrice(StrictModel):
    priceType: SBAdvertisingDealPriceType | None = Field(default=None)
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class SBUpdateAdvertisingDealRequest(StrictModel):
    advertisingDeals: list[SBAdvertisingDealUpdate] | None = Field(default=None, min_length=1, max_length=10)


__all__ = [
    "SBAdvertisingDeal",
    "SBAdvertisingDealAdvertisingDealIdFilter",
    "SBAdvertisingDealCreate",
    "SBAdvertisingDealMultiStatusResponse",
    "SBAdvertisingDealMultiStatusSuccess",
    "SBAdvertisingDealNameFilter",
    "SBAdvertisingDealNameFilterType",
    "SBAdvertisingDealPrice",
    "SBAdvertisingDealPriceType",
    "SBAdvertisingDealState",
    "SBAdvertisingDealStatus",
    "SBAdvertisingDealStatusEnum",
    "SBAdvertisingDealSuccessResponse",
    "SBAdvertisingDealUpdate",
    "SBCreateAdvertisingDealPrice",
    "SBCreateAdvertisingDealRequest",
    "SBCurrencyCode",
    "SBDeleteAdvertisingDealRequest",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBQueryAdvertisingDealRequest",
    "SBUpdateAdvertisingDealPrice",
    "SBUpdateAdvertisingDealRequest",
]
