"""Auto-generated models for KeywordReservationValidations from Amazon Ads API v1."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.sb import (
    SBError,
    SBErrorCode,
    SBErrorsIndex,
)


class SBCreateKeywordReservationValidationRequest(StrictModel):
    keywordReservationValidations: list[SBKeywordReservationValidationCreate] | None = Field(
        default=None, min_length=1, max_length=1000
    )


class SBKeywordReservationValidation(LenientModel):
    isReservable: bool = Field(description="Whether the keyword can be reserved or not.")
    keyword: str = Field(description="Keyword to be validated.")
    keywordReservationValidationId: str = Field(description="The identifier of the KeywordReservationValidation.")
    reservationRejectedReason: str | None = Field(
        default=None,
        description="Reason why the keyword cannot be reserved. It is present only when isReservable is false.",
    )


class SBKeywordReservationValidationCreate(StrictModel):
    keyword: str = Field(description="Keyword to be validated.")


class SBKeywordReservationValidationMultiStatusResponse(LenientModel):
    error: list[SBErrorsIndex] | None = Field(default=None, min_length=0, max_length=1000)
    success: list[SBKeywordReservationValidationMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=1000
    )


class SBKeywordReservationValidationMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=999)
    keywordReservationValidation: SBKeywordReservationValidation


__all__ = [
    "SBCreateKeywordReservationValidationRequest",
    "SBError",
    "SBErrorCode",
    "SBErrorsIndex",
    "SBKeywordReservationValidation",
    "SBKeywordReservationValidationCreate",
    "SBKeywordReservationValidationMultiStatusResponse",
    "SBKeywordReservationValidationMultiStatusSuccess",
]
