"""Auto-generated models for Data rooms from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models._core.lenient_enum import lenient_enum


class AwsRegion(StrEnum):
    """
    Available AWS regions
    """

    eu_west_1 = "eu-west-1"
    us_east_1 = "us-east-1"
    us_west_2 = "us-west-2"


class CreateDataroomResponseContent(LenientModel):
    accountId: str = Field(description="The owner of this Data room")
    assignedToAccountId: str | None = Field(
        default=None, description="The Ads AccountId to which this dataroom is assigned to"
    )
    creationDateTime: datetime = Field(
        description="An ISO UTC Timestamp value representing the time the dataroom was created"
    )
    region: Annotated[AwsRegion | str, lenient_enum(AwsRegion)] | None = Field(default=None)


class GetDataroomMetadataResponseContent(LenientModel):
    activeDestinations: float = Field(description="The number of active destinations for the datasets")
    dataSetsInUse: float = Field(description="The number of datasets currently in use")
    linkedAccounts: float = Field(description="The number of linked accounts associated with the datasets")
    totalDataSets: float = Field(description="The total number of datasets")


class GetDataroomResponseContent(LenientModel):
    accountId: str = Field(description="The owner of this Data room")
    assignedToAccountId: str | None = Field(
        default=None, description="The Ads AccountId to which this dataroom is assigned to"
    )
    creationDateTime: datetime = Field(
        description="An ISO UTC Timestamp value representing the time the dataroom was created"
    )
    region: Annotated[AwsRegion | str, lenient_enum(AwsRegion)] | None = Field(default=None)


__all__ = [
    "AwsRegion",
    "CreateDataroomResponseContent",
    "GetDataroomMetadataResponseContent",
    "GetDataroomResponseContent",
]
