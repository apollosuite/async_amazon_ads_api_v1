"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from amazon_ads_sdk.errors import ErrorsIndex


class SBCreateKeywordReservationValidationRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    keywordReservationValidations: list[SBKeywordReservationValidationCreate] | None = None


class SBKeywordReservationValidation(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    isReservable: bool  # Whether the keyword can be reserved or not.
    keyword: str  # Keyword to be validated.
    keywordReservationValidationId: str  # The identifier of the KeywordReservationValidation.
    reservationRejectedReason: str | None = (
        None  # Reason why the keyword cannot be reserved. It is present only when isReservable is false.
    )


class SBKeywordReservationValidationCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    keyword: str  # Keyword to be validated.


class SBKeywordReservationValidationMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SBKeywordReservationValidationMultiStatusSuccess] | None = None


class SBKeywordReservationValidationMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    index: int
    keywordReservationValidation: SBKeywordReservationValidation
