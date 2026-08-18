"""Auto-generated models for Snapshots from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class SnapshotRequestStateFilter(StrEnum):
    """
    Optional. Restricts results to entities with state within the specified comma-separated list. Default behavior is to include 'enabled' and 'paused'. You can include 'enabled', 'paused', and 'archived' or any combination.
    """

    enabled = "enabled"
    paused = "paused"
    archived = "archived"


class SnapshotResponseRecordType(StrEnum):
    """
    The record type of the snapshot file.
    """

    campaigns = "campaigns"
    adgroups = "adgroups"
    productAds = "productAds"
    targets = "targets"


class SnapshotResponseStatus(StrEnum):
    """
    The status of the generation of the snapshot.
    """

    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class TacticFilter(StrEnum):
    """
    Optional. Restricts results to entities with the advertising tactic associated with the campaign. Must be one of the following table lists available tactic names:
    |Tactic Name|Type|Description|
    |-----------|-----|-----------|
    |T00020     |Contextual targeting | Choose individual products to show your ads in placements related to those products.<br> Choose individual categories to show your ads in placements related to those categories on and off Amazon.|
    |T00030     |Audiences or Contextual Targeting | Select individual products, categories, refined categories, or audiences to show your ads.|
    """

    T00020 = "T00020"
    T00030 = "T00030"
    T00020_T00030 = "T00020,T00030"


class SnapshotRequest(StrictModel):
    stateFilter: Annotated[SnapshotRequestStateFilter | str, lenient_enum(SnapshotRequestStateFilter)] | None = Field(
        default=None,
        description="Optional. Restricts results to entities with state within the specified comma-separated list. Default behavior is to include 'enabled' and 'paused'. You can include 'enabled', 'paused', and 'archived' or any combination.",
    )
    tacticFilter: Annotated[TacticFilter | str, lenient_enum(TacticFilter)] | None = Field(default=None)


class SnapshotResponse(LenientModel):
    snapshotId: str | None = Field(default=None, description="The identifier of the snapshot that was requested.")
    recordType: Annotated[SnapshotResponseRecordType | str, lenient_enum(SnapshotResponseRecordType)] | None = Field(
        default=None, description="The record type of the snapshot file."
    )
    status: Annotated[SnapshotResponseStatus | str, lenient_enum(SnapshotResponseStatus)] | None = Field(
        default=None, description="The status of the generation of the snapshot."
    )
    statusDetails: str | None = Field(default=None, description="Optional description of the status.")
    location: str | None = Field(
        default=None, description="The URI for the snapshot. It's only available if status is SUCCESS."
    )
    fileSize: float | None = Field(
        default=None, description="The size of the snapshot file in bytes. It's only available if status is SUCCESS."
    )
    expiration: float | None = Field(
        default=None,
        description="The epoch time for expiration of the snapshot file and each snapshot file will be expired in 30 mins after generated. It's only available if status is SUCCESS.",
    )


__all__ = [
    "SnapshotRequest",
    "SnapshotRequestStateFilter",
    "SnapshotResponse",
    "SnapshotResponseRecordType",
    "SnapshotResponseStatus",
    "TacticFilter",
]
