"""Auto-generated models for Targets from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.st import (
    STAdProduct,
    STCreateState,
    STDeliveryReason,
    STDeliveryStatus,
    STError,
    STErrorCode,
    STErrorsIndex,
    STState,
    STStatus,
    STUpdateState,
)

type STTargetType = Literal[
    "AUDIENCE",  # Target based on an audience segment.
    "LOCATION",  # Target based on geographic location.
]
"""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `LOCATION`: Target based on geographic location.
"""


class STAudienceTarget(LenientModel):
    """Target based on a specified audience ID."""

    audienceId: STMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )


class STCreateAudienceTarget(StrictModel):
    """Target based on a specified audience ID."""

    audienceId: STCreateMarketplaceStringValue
    groupId: str | None = Field(
        default=None,
        description="The string identifying a group of audiences. Only numbers formatted as strings are accepted (e.g. '1'). To add audiences to a new group, choose any string not currently being used on this ad group. To add audiences to an existing group, use the existing groupId from this ad group. You may specify up to 10 include groups and 1 exclude group.",
    )


class STCreateLocationTarget(StrictModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")


class STCreateMarketplaceStringValue(StrictModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class STCreateTargetDetailsAudienceTarget(StrictModel):
    audienceTarget: STCreateAudienceTarget


class STCreateTargetDetailsLocationTarget(StrictModel):
    locationTarget: STCreateLocationTarget


type STCreateTargetDetails = STCreateTargetDetailsAudienceTarget | STCreateTargetDetailsLocationTarget


class STCreateTargetRequest(StrictModel):
    targets: list[STTargetCreate] = Field(min_length=1, max_length=100)


class STDeleteTargetRequest(StrictModel):
    targetIds: list[str] = Field(min_length=1, max_length=100)


class STLocationTarget(LenientModel):
    """Target based on geographic location."""

    locationId: str = Field(description="The ID of the geographic location to target.")
    locationIdResolved: str | None = Field(
        default=None, description="A human-readable location text. It's a read-only field."
    )


class STMarketplaceStringValue(LenientModel):
    defaultValue: str | None = Field(
        default=None,
        description="The default value. Either the default value or the marketplace settings should always be specified",
    )


class STQueryTargetRequest(StrictModel):
    adGroupIdFilter: STTargetAdGroupIdFilter | None = Field(default=None)
    adProductFilter: STTargetAdProductFilter
    campaignIdFilter: STTargetCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nextToken: str | None = Field(default=None)
    stateFilter: STTargetStateFilter | None = Field(default=None)
    targetIdFilter: STTargetTargetIdFilter | None = Field(default=None)


class STTarget(LenientModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: STAdProduct | str = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    campaignId: str = Field(
        description="A unique identifier for the campaign associated with the target. Only used for campaign-level targets."
    )
    creationDateTime: datetime = Field(description="The date time the target was created.")
    lastUpdatedDateTime: datetime = Field(description="The date time the target was last updated.")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: STState | str = Field(description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    status: STStatus | None = Field(default=None)
    targetDetails: STTargetDetails
    targetId: str = Field(description="A unique identifier for the target.")
    targetType: STTargetType | str = Field(description="""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `LOCATION`: Target based on geographic location.
""")


class STTargetAdGroupIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STTargetAdProductFilter(StrictModel):
    include: list[STAdProduct | str] = Field(
        min_length=1,
        max_length=1,
        description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""",
    )


class STTargetCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STTargetCreate(StrictModel):
    adGroupId: str = Field(
        description="A unique identifier for the ad group associated with the target. Only used for ad-group level targets."
    )
    adProduct: STAdProduct = Field(description="""
Supported values:
- `SPONSORED_TELEVISION`: Sponsored Television ad product.
""")
    negative: bool = Field(description="Indicates whether the target is negative or not.")
    state: STCreateState = Field(description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""")
    targetDetails: STCreateTargetDetails
    targetType: STTargetType = Field(description="""
Supported values:
- `AUDIENCE`: Target based on an audience segment.
- `LOCATION`: Target based on geographic location.
""")


class STTargetDetailsAudienceTarget(LenientModel):
    audienceTarget: STAudienceTarget


class STTargetDetailsLocationTarget(LenientModel):
    locationTarget: STLocationTarget


type STTargetDetails = STTargetDetailsAudienceTarget | STTargetDetailsLocationTarget


class STTargetMultiStatusResponse(LenientModel):
    error: list[STErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[STTargetMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class STTargetMultiStatusSuccess(LenientModel):
    index: int = Field(ge=0, le=99)
    target: STTarget


class STTargetStateFilter(StrictModel):
    include: list[STState | str] = Field(
        min_length=1,
        max_length=3,
        description="""
Supported values:
- `ARCHIVED`: The object is permanently stopped and cannot be reactivated. Terminal end state.
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )


class STTargetSuccessResponse(LenientModel):
    nextToken: str | None = Field(default=None)
    targets: list[STTarget] | None = Field(default=None, min_length=0, max_length=100)
    totalResults: int | None = Field(default=None)


class STTargetTargetIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class STTargetUpdate(StrictModel):
    state: STUpdateState | None = Field(
        default=None,
        description="""
Supported values:
- `ENABLED`: The object is set active by user and eligible for delivery.
- `PAUSED`: The object is stopped by user and not eligible for delivery.
""",
    )
    targetId: str = Field(description="A unique identifier for the target.")


class STUpdateTargetRequest(StrictModel):
    targets: list[STTargetUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "STAdProduct",
    "STAudienceTarget",
    "STCreateAudienceTarget",
    "STCreateLocationTarget",
    "STCreateMarketplaceStringValue",
    "STCreateState",
    "STCreateTargetDetails",
    "STCreateTargetRequest",
    "STDeleteTargetRequest",
    "STDeliveryReason",
    "STDeliveryStatus",
    "STError",
    "STErrorCode",
    "STErrorsIndex",
    "STLocationTarget",
    "STMarketplaceStringValue",
    "STQueryTargetRequest",
    "STState",
    "STStatus",
    "STTarget",
    "STTargetAdGroupIdFilter",
    "STTargetAdProductFilter",
    "STTargetCampaignIdFilter",
    "STTargetCreate",
    "STTargetDetails",
    "STTargetMultiStatusResponse",
    "STTargetMultiStatusSuccess",
    "STTargetStateFilter",
    "STTargetSuccessResponse",
    "STTargetTargetIdFilter",
    "STTargetType",
    "STTargetUpdate",
    "STUpdateState",
    "STUpdateTargetRequest",
]
