"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex

    from .enums import SBAdvertisingDealPriceType
    from .shared import SBAdvertisingDealPrice
del TYPE_CHECKING


class SBAdvertisingDeal(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str  # A unique identifier for a deal.
    endDateTime: datetime  # The end date time for the deal.
    name: str  # The name of the deal.
    price: SBAdvertisingDealPrice | None = None
    replacingDealId: str | None = (
        None  # The ID of an advertising deal that this deal intends to replace.
    )
    startDateTime: datetime  # The start date time for the deal.
    state: SBAdvertisingDealState | None = None
    status: SBAdvertisingDealStatus


class SBAdvertisingDealAdvertisingDealIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SBAdvertisingDealCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    endDateTime: datetime  # The end date time for the deal.
    name: str  # The name of the deal.
    price: SBCreateAdvertisingDealPrice | None = None
    replacingDealId: str | None = (
        None  # The ID of an advertising deal that this deal intends to replace.
    )
    startDateTime: datetime  # The start date time for the deal.
    state: SBAdvertisingDealState | None = None


class SBAdvertisingDealMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBAdvertisingDealMultiStatusSuccess] | None = None


class SBAdvertisingDealMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDeal: SBAdvertisingDeal
    index: int


class SBAdvertisingDealNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SBAdvertisingDealNameFilterType


class SBAdvertisingDealNameFilterType(StrEnum):
    """| AdvertisingDealNameFilterType | Description |
    |------|------|
    | `BROAD_MATCH` | Filter by broad match. |
    | `EXACT_MATCH` | Filter by exact match. |
    """

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SBAdvertisingDealState(StrEnum):
    """| AdvertisingDealState | Description |
    |------|------|
    | `DRAFT` |  |
    | `PROPOSED` |  |
    """

    DRAFT = "DRAFT"
    PROPOSED = "PROPOSED"


class SBAdvertisingDealStatus(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    status: SBAdvertisingDealStatusEnum


class SBAdvertisingDealStatusEnum(StrEnum):
    """| AdvertisingDealStatusEnum | Description |
    |------|------|
    | `DRAFT` | The deal has not been submitted yet. |
    | `MODERATION_APPROVED` | The deal has passed moderation. |
    | `PROPOSED` | The deal has been submitted for moderation. |
    """

    DRAFT = "DRAFT"
    MODERATION_APPROVED = "MODERATION_APPROVED"
    PROPOSED = "PROPOSED"


class SBAdvertisingDealSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDeals: list[SBAdvertisingDeal] | None = None
    nextToken: str | None = None


class SBAdvertisingDealUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealId: str  # A unique identifier for a deal.
    endDateTime: datetime | None = None  # The end date time for the deal.
    name: str | None = None  # The name of the deal.
    price: SBUpdateAdvertisingDealPrice | None = None
    replacingDealId: str | None = (
        None  # The ID of an advertising deal that this deal intends to replace.
    )
    startDateTime: datetime | None = None  # The start date time for the deal.
    state: SBAdvertisingDealState | None = None


class SBCreateAdvertisingDealPrice(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    priceType: SBAdvertisingDealPriceType
    value: float  # The monetary amount of the price in the given currency.


class SBCreateAdvertisingDealRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDeals: list[SBAdvertisingDealCreate] | None = None


class SBDeleteAdvertisingDealRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealIds: list[str] | None = None


class SBQueryAdvertisingDealRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDealIdFilter: SBAdvertisingDealAdvertisingDealIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SBAdvertisingDealNameFilter | None = None
    nextToken: str | None = None


class SBUpdateAdvertisingDealPrice(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    priceType: SBAdvertisingDealPriceType | None = None
    value: float | None = None  # The monetary amount of the price in the given currency.


class SBUpdateAdvertisingDealRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    advertisingDeals: list[SBAdvertisingDealUpdate] | None = None


__all__ = [
    "SBAdvertisingDeal",
    "SBAdvertisingDealAdvertisingDealIdFilter",
    "SBAdvertisingDealCreate",
    "SBAdvertisingDealMultiStatusResponse",
    "SBAdvertisingDealMultiStatusSuccess",
    "SBAdvertisingDealNameFilter",
    "SBAdvertisingDealNameFilterType",
    "SBAdvertisingDealState",
    "SBAdvertisingDealStatus",
    "SBAdvertisingDealStatusEnum",
    "SBAdvertisingDealSuccessResponse",
    "SBAdvertisingDealUpdate",
    "SBCreateAdvertisingDealPrice",
    "SBCreateAdvertisingDealRequest",
    "SBDeleteAdvertisingDealRequest",
    "SBQueryAdvertisingDealRequest",
    "SBUpdateAdvertisingDealPrice",
    "SBUpdateAdvertisingDealRequest",
]
