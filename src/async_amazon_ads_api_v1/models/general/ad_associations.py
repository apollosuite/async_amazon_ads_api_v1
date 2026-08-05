"""Auto-generated models for AdAssociations from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import GeneralErrorCode
from .shared import GeneralErrorsIndex


class AdState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **State Enum:**

    | State | Description |
    |------|------|
    | `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
    | `DRAFT` | The resource is in draft status and has not yet been proposed or enabled. |
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    | `PROPOSED` | Indicates an entity staged for review and adoption by advertisers. |
    """

    ARCHIVED = "ARCHIVED"
    DRAFT = "DRAFT"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    PROPOSED = "PROPOSED"


class CreateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **CreateState Enum:**

    | CreateState | Description |
    |------|------|
    | `DRAFT` | The resource is in draft status and has not yet been proposed or enabled. |
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    | `PROPOSED` | Indicates an entity staged for review and adoption by advertisers. |
    """

    DRAFT = "DRAFT"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    PROPOSED = "PROPOSED"


class UpdateState(StrEnum):
    """
    The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery
    **UpdateState Enum:**

    | UpdateState | Description |
    |------|------|
    | `DRAFT` | The resource is in draft status and has not yet been proposed or enabled. |
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    | `PROPOSED` | Indicates an entity staged for review and adoption by advertisers. |
    """

    DRAFT = "DRAFT"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    PROPOSED = "PROPOSED"


class AdAssociation(BaseModel):
    model_config = ConfigDict(extra="allow")

    adAssociationId: str = Field(description="The unique identifier of the ad association.")
    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The ad Id  associated with the ad.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: Annotated[AdState | str, lenient_enum(AdState)]
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class AdAssociationAdAssociationIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class AdAssociationAdGroupIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class AdAssociationAdIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=100)


class AdAssociationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adGroupId: str = Field(description="The ad group associated with the ad.")
    adId: str = Field(description="The ad Id  associated with the ad.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: Annotated[CreateState | str, lenient_enum(CreateState)]
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class AdAssociationMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[GeneralErrorsIndex] | None = Field(default=None, min_length=0, max_length=20)
    success: list[AdAssociationMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=20)


class AdAssociationMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="allow")

    adAssociation: AdAssociation
    index: int = Field(ge=0, le=19)


class AdAssociationSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    adAssociations: list[AdAssociation] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class AdAssociationUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationId: str = Field(description="The unique identifier of the ad association.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the ad association.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the ad association.")
    state: Annotated[UpdateState | str, lenient_enum(UpdateState)] | None = Field(default=None)
    weight: int | None = Field(
        default=None,
        description="The relative percentage of traffic which would be directed to the associated Ad Creative in the Ad Group.",
    )


class CreateAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociations: list[AdAssociationCreate] = Field(min_length=1, max_length=20)


class DeleteAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationIds: list[str] = Field(min_length=1, max_length=20)


class QueryAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociationIdFilter: AdAssociationAdAssociationIdFilter | None = Field(default=None)
    adGroupIdFilter: AdAssociationAdGroupIdFilter | None = Field(default=None)
    adIdFilter: AdAssociationAdIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)


class UpdateAdAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adAssociations: list[AdAssociationUpdate] = Field(min_length=1, max_length=20)


__all__ = [
    "AdAssociationAdAssociationIdFilter",
    "AdAssociationAdGroupIdFilter",
    "AdAssociationAdIdFilter",
    "AdAssociationCreate",
    "AdAssociationUpdate",
    "AdState",
    "CreateAdAssociationRequest",
    "CreateState",
    "DeleteAdAssociationRequest",
    "GeneralErrorCode",
    "QueryAdAssociationRequest",
    "UpdateAdAssociationRequest",
    "UpdateState",
]
