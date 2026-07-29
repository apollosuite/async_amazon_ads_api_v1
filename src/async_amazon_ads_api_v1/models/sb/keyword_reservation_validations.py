"""Auto-generated models for KeywordReservationValidations from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex


class SBCreateKeywordReservationValidationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordReservationValidations: list[SBKeywordReservationValidationCreate] | None = Field(
        default=None, min_length=1, max_length=1000
    )


class SBKeywordReservationValidation(BaseModel):
    model_config = ConfigDict(extra="allow")

    isReservable: bool = Field(description="Whether the keyword can be reserved or not.")
    keyword: str = Field(description="Keyword to be validated.")
    keywordReservationValidationId: str = Field(description="The identifier of the KeywordReservationValidation.")
    reservationRejectedReason: str | None = Field(
        default=None,
        description="Reason why the keyword cannot be reserved. It is present only when isReservable is false.",
    )


class SBKeywordReservationValidationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keyword: str = Field(description="Keyword to be validated.")


class SBKeywordReservationValidationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBKeywordReservationValidationMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SBKeywordReservationValidationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int = Field(ge=0, le=999)
    keywordReservationValidation: SBKeywordReservationValidation


__all__ = [
    "SBCreateKeywordReservationValidationRequest",
    "SBKeywordReservationValidation",
    "SBKeywordReservationValidationCreate",
    "SBKeywordReservationValidationMultiStatusResponse",
    "SBKeywordReservationValidationMultiStatusSuccess",
]
