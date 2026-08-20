"""Auto-generated models for DealPreferences from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type ErrorCode = Literal["BAD_REQUEST", "FORBIDDEN", "INTERNAL_ERROR", "NOT_FOUND", "TOO_MANY_REQUESTS", "UNAUTHORIZED"]
"""
Supported values:
- `BAD_REQUEST`: The request is not valid considering the documented schema.
- `FORBIDDEN`: The caller is not authorized to make the given request.
- `INTERNAL_ERROR`: The server encountered an unexpected condition that prevented it from fulfilling the request.
- `NOT_FOUND`: The requested resource does not exist.
- `TOO_MANY_REQUESTS`: There have been too many requests, please slow down your call rate.
- `UNAUTHORIZED`: The request lacks the necessary credentials.
"""


type SupplierTargetType = Literal["CONTENT_CATEGORY"]


class CreateDealPreferenceRequest(StrictModel):
    dealPreferences: list[DealPreferenceCreate] = Field(min_length=1, max_length=20)


class CreateDealPreferenceTarget(StrictModel):
    """A targeting reference that identifies a specific supplier target item within a destination and publisher."""

    groupId: str = Field(
        description="The string identifying a group of targets. Targets sharing the same groupId are combined with OR logic. Different groupIds are combined with AND logic. If absent, the target is treated as its own implicit group (ANDed with all other groups)."
    )
    negative: bool = Field(
        description="Indicates whether this target is negative (excluded). If not present, defaults to false (inclusive)."
    )
    supplierPublisherId: str | None = Field(default=None, description="The publisher that owns the target item.")
    supplierTargetDestinationId: str = Field(
        description="The supplier destination for this target (e.g., AmazonMedia, AmazonSP, AdX)."
    )
    supplierTargetItemId: str = Field(description="The specific target item to include or exclude.")
    supplierTargetType: SupplierTargetType


class DealPreference(LenientModel):
    advertiserAccountId: str = Field(description="The advertiser account that owns this deal preference.")
    creationDateTime: datetime = Field(description="The date and time the deal preference was created.")
    dealPreferenceId: str = Field(description="Unique identifier for the deal preference.")
    dealPreferenceTargets: list[DealPreferenceTarget] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The targeting settings inherited by deals created under this advertiser account. Targets with the same groupId are combined with OR logic; different groupIds are combined with AND logic. Targets with negative set to true are excluded.",
    )
    lastUpdatedDateTime: datetime = Field(description="The date and time the deal preference was last updated.")


class DealPreferenceCreate(StrictModel):
    dealPreferenceTargets: list[CreateDealPreferenceTarget] | None = Field(
        default=None,
        min_length=0,
        max_length=20,
        description="The targeting settings inherited by deals created under this advertiser account. Targets with the same groupId are combined with OR logic; different groupIds are combined with AND logic. Targets with negative set to true are excluded.",
    )


class DealPreferenceMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=20)
    success: list[DealPreferenceMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=20)


class DealPreferenceMultiStatusSuccess(LenientModel):
    dealPreference: DealPreference
    index: int = Field(ge=0, le=19)


class DealPreferenceSuccessResponse(LenientModel):
    dealPreferences: list[DealPreference] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class DealPreferenceTarget(LenientModel):
    """A targeting reference that identifies a specific supplier target item within a destination and publisher."""

    groupId: str = Field(
        description="The string identifying a group of targets. Targets sharing the same groupId are combined with OR logic. Different groupIds are combined with AND logic. If absent, the target is treated as its own implicit group (ANDed with all other groups)."
    )
    negative: bool = Field(
        description="Indicates whether this target is negative (excluded). If not present, defaults to false (inclusive)."
    )
    supplierPublisherId: str | None = Field(default=None, description="The publisher that owns the target item.")
    supplierTargetDestinationId: str = Field(
        description="The supplier destination for this target (e.g., AmazonMedia, AmazonSP, AdX)."
    )
    supplierTargetItemId: str = Field(description="The specific target item to include or exclude.")
    supplierTargetType: SupplierTargetType | str


class Error(LenientModel):
    code: ErrorCode | str
    fieldLocation: str | None = Field(default=None)
    message: str


class ErrorsIndex(LenientModel):
    errors: list[Error] = Field(min_length=1, max_length=20)
    index: int = Field(ge=0, le=19)


__all__ = [
    "CreateDealPreferenceRequest",
    "CreateDealPreferenceTarget",
    "DealPreference",
    "DealPreferenceCreate",
    "DealPreferenceMultiStatusResponse",
    "DealPreferenceMultiStatusSuccess",
    "DealPreferenceSuccessResponse",
    "DealPreferenceTarget",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "SupplierTargetType",
]
