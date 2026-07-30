"""Auto-generated shared models for cross-tag schemas."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SDDeliveryReason, SDDeliveryStatus, SDErrorCode


class SDError(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: Annotated[SDErrorCode | str, lenient_enum(SDErrorCode)] | None = Field(default=None)
    fieldLocation: str | None = Field(default=None)
    message: str | None = Field(default=None)


class SDErrorsIndex(BaseModel):
    model_config = ConfigDict(extra="allow")

    errors: list[SDError] | None = Field(default=None, min_length=1, max_length=20)
    index: int | None = Field(default=None, ge=0, le=4999)


class SDStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[Annotated[SDDeliveryReason | str, lenient_enum(SDDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SDDeliveryStatus | str, lenient_enum(SDDeliveryStatus)] | None = Field(default=None)
