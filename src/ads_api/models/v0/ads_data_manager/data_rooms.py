"""Auto-generated models for Data rooms from Amazon Ads API v0."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel

type AwsRegion = Literal["eu-west-1", "us-east-1", "us-west-2"]
"""
Available AWS regions
"""


class CreateDataroomResponseContent(LenientModel):
    accountId: str = Field(description="The owner of this Data room")
    assignedToAccountId: str | None = Field(
        default=None, description="The Ads AccountId to which this dataroom is assigned to"
    )
    creationDateTime: datetime = Field(
        description="An ISO UTC Timestamp value representing the time the dataroom was created"
    )
    region: AwsRegion | str | None = Field(default=None)


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
    region: AwsRegion | str | None = Field(default=None)


__all__ = [
    "AwsRegion",
    "CreateDataroomResponseContent",
    "GetDataroomMetadataResponseContent",
    "GetDataroomResponseContent",
]
