"""Auto-generated models for AdAssociations from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class CreateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery **CreateState Enum:**  CreateState Description ------ ------ `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery."""

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class State(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery **State Enum:**  State Description ------ ------ `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state. `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery."""

    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class UpdateState(StrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery **UpdateState Enum:**  UpdateState Description ------ ------ `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery."""

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class AdAssociation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationId: str  # The unique identifier of the ad association.
    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The ad Id  associated with the ad.
    endDateTime: datetime | None = None  # The end date time for the ad association.
    startDateTime: datetime | None = None  # The start date time for the ad association.
    state: Annotated[State | str, lenient_enum(State)]
    weight: int | None = (
        None  # The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.
    )


class AdAssociationAdAssociationIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class AdAssociationAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class AdAssociationAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class AdAssociationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The ad Id  associated with the ad.
    endDateTime: datetime | None = None  # The end date time for the ad association.
    startDateTime: datetime | None = None  # The start date time for the ad association.
    state: Annotated[CreateState | str, lenient_enum(CreateState)]
    weight: int | None = (
        None  # The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.
    )


class AdAssociationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[AdAssociationMultiStatusSuccess] | None = None


class AdAssociationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociation: AdAssociation
    index: int


class AdAssociationSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociations: list[AdAssociation] | None = None
    nextToken: str | None = None


class AdAssociationUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationId: str  # The unique identifier of the ad association.
    endDateTime: datetime | None = None  # The end date time for the ad association.
    startDateTime: datetime | None = None  # The start date time for the ad association.
    state: Annotated[UpdateState | str, lenient_enum(UpdateState)] | None = None
    weight: int | None = (
        None  # The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.
    )


class CreateAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociations: list[AdAssociationCreate]


class DeleteAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationIds: list[str]


class QueryAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationIdFilter: AdAssociationAdAssociationIdFilter | None = None
    adGroupIdFilter: AdAssociationAdGroupIdFilter | None = None
    adIdFilter: AdAssociationAdIdFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None


class UpdateAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociations: list[AdAssociationUpdate]


__all__ = [
    "CreateState",
    "State",
    "UpdateState",
    "AdAssociation",
    "AdAssociationAdAssociationIdFilter",
    "AdAssociationAdGroupIdFilter",
    "AdAssociationAdIdFilter",
    "AdAssociationCreate",
    "AdAssociationMultiStatusResponse",
    "AdAssociationMultiStatusSuccess",
    "AdAssociationSuccessResponse",
    "AdAssociationUpdate",
    "CreateAdAssociationRequest",
    "DeleteAdAssociationRequest",
    "QueryAdAssociationRequest",
    "UpdateAdAssociationRequest",
]
