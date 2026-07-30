"""Auto-generated models for KeywordReservationValidations from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from .enums import SBErrorCode
from .shared import SBErrorsIndex


class SBCreateKeywordReservationValidationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keywordReservationValidations: list[SBKeywordReservationValidationCreate] | None = Field(
        default=None, min_length=1, max_length=1000
    )


class SBKeywordReservationValidation(BaseModel):
    model_config = ConfigDict(extra="allow")

    isReservable: bool | None = Field(default=None, description="Whether the keyword can be reserved or not.")
    keyword: str | None = Field(default=None, description="Keyword to be validated.")
    keywordReservationValidationId: str | None = Field(
        default=None, description="The identifier of the KeywordReservationValidation."
    )
    reservationRejectedReason: str | None = Field(
        default=None,
        description="Reason why the keyword cannot be reserved. It is present only when isReservable is false.",
    )


class SBKeywordReservationValidationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    keyword: str = Field(description="Keyword to be validated.")


class SBKeywordReservationValidationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBKeywordReservationValidationMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SBKeywordReservationValidationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int | None = Field(default=None, ge=0, le=999)
    keywordReservationValidation: SBKeywordReservationValidation | None = Field(default=None)


__all__ = ["SBCreateKeywordReservationValidationRequest", "SBErrorCode", "SBKeywordReservationValidationCreate"]
