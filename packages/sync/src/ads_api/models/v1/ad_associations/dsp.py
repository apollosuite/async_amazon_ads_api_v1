"""Auto-generated models for AdAssociations from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.dsp import (
    DSPCreateState,
    DSPError,
    DSPErrorCode,
    DSPErrorsIndex,
    DSPState,
    DSPUpdateState,
)


class DSPAdAssociation(LenientModel):
    adAssociationId: str = Field(description="The unique identifier of the ad association.")
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The ad Id  associated with the ad.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: DSPState | str
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class DSPAdAssociationAdAssociationIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdAssociationAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdAssociationAdIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class DSPAdAssociationCreate(StrictModel):
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The ad Id  associated with the ad.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: DSPCreateState
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class DSPAdAssociationMultiStatusResponse(LenientModel):
    error: list[DSPErrorsIndex] | None = Field(default=None, min_length=0, max_length=20)
    success: list[DSPAdAssociationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=20)


class DSPAdAssociationMultiStatusSuccess(LenientModel):
    adAssociation: DSPAdAssociation
    index: int = Field(ge=0, le=19)


class DSPAdAssociationSuccessResponse(LenientModel):
    adAssociations: list[DSPAdAssociation] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DSPAdAssociationUpdate(StrictModel):
    adAssociationId: str = Field(description="The unique identifier of the ad association.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: DSPUpdateState | None = Field(default=None)
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class DSPCreateAdAssociationRequest(StrictModel):
    adAssociations: list[DSPAdAssociationCreate] = Field(min_length=1, max_length=20)


class DSPDeleteAdAssociationRequest(StrictModel):
    adAssociationIds: list[str] = Field(min_length=1, max_length=20)


class DSPQueryAdAssociationRequest(StrictModel):
    adAssociationIdFilter: DSPAdAssociationAdAssociationIdFilter | None = Field(default=None)
    adGroupIdFilter: DSPAdAssociationAdGroupIdFilter | None = Field(default=None)
    adIdFilter: DSPAdAssociationAdIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)


class DSPUpdateAdAssociationRequest(StrictModel):
    adAssociations: list[DSPAdAssociationUpdate] = Field(min_length=1, max_length=20)


__all__ = [
    "DSPAdAssociation",
    "DSPAdAssociationAdAssociationIdFilter",
    "DSPAdAssociationAdGroupIdFilter",
    "DSPAdAssociationAdIdFilter",
    "DSPAdAssociationCreate",
    "DSPAdAssociationMultiStatusResponse",
    "DSPAdAssociationMultiStatusSuccess",
    "DSPAdAssociationSuccessResponse",
    "DSPAdAssociationUpdate",
    "DSPCreateAdAssociationRequest",
    "DSPCreateState",
    "DSPDeleteAdAssociationRequest",
    "DSPError",
    "DSPErrorCode",
    "DSPErrorsIndex",
    "DSPQueryAdAssociationRequest",
    "DSPState",
    "DSPUpdateAdAssociationRequest",
    "DSPUpdateState",
]
