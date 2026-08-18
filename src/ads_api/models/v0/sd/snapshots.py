"""Auto-generated models for Snapshots from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type TacticFilter = Literal["T00020", "T00030", "T00020,T00030"]
"""
Optional. Restricts results to entities with the advertising tactic associated with the campaign. Must be one of the following table lists available tactic names:
|Tactic Name|Type|Description|
|-----------|-----|-----------|
|T00020     |Contextual targeting | Choose individual products to show your ads in placements related to those products.<br> Choose individual categories to show your ads in placements related to those categories on and off Amazon.|
|T00030     |Audiences or Contextual Targeting | Select individual products, categories, refined categories, or audiences to show your ads.|
"""


class SnapshotRequest(StrictModel):
    stateFilter: Literal["enabled", "paused", "archived"] | None = Field(
        default=None,
        description="Optional. Restricts results to entities with state within the specified comma-separated list. Default behavior is to include 'enabled' and 'paused'. You can include 'enabled', 'paused', and 'archived' or any combination.",
    )
    tacticFilter: TacticFilter | None = Field(default=None)


class SnapshotResponse(LenientModel):
    snapshotId: str | None = Field(default=None, description="The identifier of the snapshot that was requested.")
    recordType: Literal["campaigns", "adgroups", "productAds", "targets"] | str | None = Field(
        default=None, description="The record type of the snapshot file."
    )
    status: Literal["IN_PROGRESS", "SUCCESS", "FAILURE"] | str | None = Field(
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


__all__ = ["SnapshotRequest", "SnapshotResponse", "TacticFilter"]
