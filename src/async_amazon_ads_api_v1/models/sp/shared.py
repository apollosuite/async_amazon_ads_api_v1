"""Auto-generated shared models for cross-tag schemas."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import SPDeliveryReason, SPDeliveryStatus, SPErrorCode


class SPCreateTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SPError(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: Annotated[SPErrorCode | str, lenient_enum(SPErrorCode)]
    fieldLocation: str | None = Field(default=None)
    message: str


class SPErrorsIndex(BaseModel):
    model_config = ConfigDict(extra="allow")

    errors: list[SPError] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=999)


class SPStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    deliveryReasons: list[Annotated[SPDeliveryReason | str, lenient_enum(SPDeliveryReason)]] | None = Field(
        default=None, min_length=0, max_length=50, description="This is the list of reasons behind the delivery status."
    )
    deliveryStatus: Annotated[SPDeliveryStatus | str, lenient_enum(SPDeliveryStatus)]


class SPTag(BaseModel):
    model_config = ConfigDict(extra="allow")

    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


__all__ = ["SPCreateTag"]
