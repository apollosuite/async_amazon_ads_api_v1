"""Auto-generated shared models for cross-tag schemas."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SBAdvertisingDealPriceType, SBCurrencyCode, SBDeliveryReason, SBDeliveryStatus, SBErrorCode


class SBAdvertisingDealPrice(BaseModel):
    model_config = ConfigDict(extra="allow")

    currencyCode: Annotated[SBCurrencyCode | str, lenient_enum(SBCurrencyCode)] | None = Field(default=None)
    priceType: Annotated[SBAdvertisingDealPriceType | str, lenient_enum(SBAdvertisingDealPriceType)] | None = Field(
        default=None
    )
    value: float | None = Field(default=None, description="The monetary amount of the price in the given currency.")


class SBCreateTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SBError(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: Annotated[SBErrorCode | str, lenient_enum(SBErrorCode)] | None = Field(default=None)
    fieldLocation: str | None = Field(default=None)
    message: str | None = Field(default=None)


class SBErrorsIndex(BaseModel):
    model_config = ConfigDict(extra="allow")

    errors: list[SBError] | None = Field(default=None, min_length=1, max_length=20)
    index: int | None = Field(default=None, ge=0, le=4999)


class SBStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[Annotated[SBDeliveryReason | str, lenient_enum(SBDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SBDeliveryStatus | str, lenient_enum(SBDeliveryStatus)] | None = Field(default=None)


class SBTag(BaseModel):
    model_config = ConfigDict(extra="allow")

    key: str | None = Field(
        default=None,
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI.",
    )
    value: str | None = Field(default=None, description="A custom key value pair entered by the advertiser.")


__all__ = ["SBCreateTag"]
