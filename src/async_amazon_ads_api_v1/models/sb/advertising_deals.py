"""Auto-generated models for AdvertisingDeals from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorCode, ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .campaigns import SBCurrencyCode


class SBAdvertisingDealNameFilterType(StrEnum):
    """
    | AdvertisingDealNameFilterType | Description |
    |------|------|
    | `BROAD_MATCH` | Filter by broad match. |
    | `EXACT_MATCH` | Filter by exact match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdvertisingDealPriceType(StrEnum):
    """
    | AdvertisingDealPriceType | Description |
    |------|------|
    | `FIXED_PRICE` | Sale price for a specific ad placement regardless of auction performance. |
    """

    FIXED_PRICE = "FIXED_PRICE"


class SBAdvertisingDealState(StrEnum):
    """
    | AdvertisingDealState | Description |
    |------|------|
    | `DRAFT` |  |
    | `PROPOSED` |  |
    """

    DRAFT = "DRAFT"
    PROPOSED = "PROPOSED"


class SBAdvertisingDealStatusEnum(StrEnum):
    """
    | AdvertisingDealStatusEnum | Description |
    |------|------|
    | `DRAFT` | The deal has not been submitted yet. |
    | `MODERATION_APPROVED` | The deal has passed moderation. |
    | `PROPOSED` | The deal has been submitted for moderation. |
    """

    DRAFT = "DRAFT"
    MODERATION_APPROVED = "MODERATION_APPROVED"
    PROPOSED = "PROPOSED"


class SBAdvertisingDeal(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDealId: str | None = Field(default=None, description="A unique identifier for a deal.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the deal.")
    name: str | None = Field(default=None, description="The name of the deal.")
    price: SBAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the deal.")
    state: Annotated[SBAdvertisingDealState | str, lenient_enum(SBAdvertisingDealState)] | None = Field(default=None)
    status: SBAdvertisingDealStatus | None = Field(default=None)


class SBAdvertisingDealAdvertisingDealIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)


class SBAdvertisingDealCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    endDateTime: datetime = Field(description="The end date time for the deal.")
    name: str = Field(description="The name of the deal.")
    price: SBCreateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime = Field(description="The start date time for the deal.")
    state: Annotated[SBAdvertisingDealState | str, lenient_enum(SBAdvertisingDealState)] | None = Field(default=None)


class SBAdvertisingDealMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=10)
    success: list[SBAdvertisingDealMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=10)


class SBAdvertisingDealMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDeal: SBAdvertisingDeal | None = Field(default=None)
    index: int | None = Field(default=None, ge=0, le=9)


class SBAdvertisingDealNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=10)
    queryTermMatchType: Annotated[SBAdvertisingDealNameFilterType | str, lenient_enum(SBAdvertisingDealNameFilterType)]


class SBAdvertisingDealPrice(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)] | None = Field(default=None)
    priceType: Annotated[SBAdvertisingDealPriceType | str, lenient_enum(SBAdvertisingDealPriceType)] | None = Field(
        default=None
    )
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class SBAdvertisingDealStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    status: Annotated[SBAdvertisingDealStatusEnum | str, lenient_enum(SBAdvertisingDealStatusEnum)] | None = Field(
        default=None
    )


class SBAdvertisingDealSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    advertisingDeals: list[SBAdvertisingDeal] | None = Field(default=None, min_length=0, max_length=50)
    nextToken: str | None = Field(default=None)


class SBAdvertisingDealUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str = Field(description="A unique identifier for a deal.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the deal.")
    name: str | None = Field(default=None, description="The name of the deal.")
    price: SBUpdateAdvertisingDealPrice | None = Field(default=None)
    replacingDealId: str | None = Field(
        default=None, description="The ID of an advertising deal that this deal intends to replace."
    )
    startDateTime: datetime | None = Field(default=None, description="The start date time for the deal.")
    state: Annotated[SBAdvertisingDealState | str, lenient_enum(SBAdvertisingDealState)] | None = Field(default=None)


class SBCreateAdvertisingDealPrice(BaseModel):
    model_config = ConfigDict(extra="forbid")

    priceType: Annotated[SBAdvertisingDealPriceType | str, lenient_enum(SBAdvertisingDealPriceType)]
    value: float = Field(description="The monetary amount of the price in the given currency.")


class SBCreateAdvertisingDealRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDeals: list[SBAdvertisingDealCreate] | None = Field(default=None, min_length=1, max_length=10)


class SBDeleteAdvertisingDealRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealIds: list[str] | None = Field(default=None, min_length=1, max_length=10)


class SBQueryAdvertisingDealRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDealIdFilter: SBAdvertisingDealAdvertisingDealIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=10, ge=1, le=50)
    nameFilter: SBAdvertisingDealNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)


class SBUpdateAdvertisingDealPrice(BaseModel):
    model_config = ConfigDict(extra="forbid")

    priceType: Annotated[SBAdvertisingDealPriceType | str, lenient_enum(SBAdvertisingDealPriceType)] | None = Field(
        default=None
    )
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class SBUpdateAdvertisingDealRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    advertisingDeals: list[SBAdvertisingDealUpdate] | None = Field(default=None, min_length=1, max_length=10)


__all__ = [
    "ErrorCode",
    "SBAdvertisingDealAdvertisingDealIdFilter",
    "SBAdvertisingDealCreate",
    "SBAdvertisingDealNameFilter",
    "SBAdvertisingDealNameFilterType",
    "SBAdvertisingDealPriceType",
    "SBAdvertisingDealState",
    "SBAdvertisingDealStatusEnum",
    "SBAdvertisingDealUpdate",
    "SBCreateAdvertisingDealPrice",
    "SBCreateAdvertisingDealRequest",
    "SBCurrencyCode",
    "SBDeleteAdvertisingDealRequest",
    "SBQueryAdvertisingDealRequest",
    "SBUpdateAdvertisingDealPrice",
    "SBUpdateAdvertisingDealRequest",
]
