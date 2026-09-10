"""Auto-generated models for BrandStoreEditionPublishVersions from Amazon Ads API v1."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v1._shared.general import (
    Error,
    ErrorCode,
    ErrorsIndex,
)

type StorePublishState = Literal["DRAFT", "PUBLISH"]
"""
User State for content

Supported values:
- `DRAFT`: Content is in draft form
- `PUBLISH`: Submit Content to Publish to LIVE / SCHEDULED
"""


type StorePublishStatus = Literal["DRAFT", "REVIEW_IN_PROGRESS"]
"""
Status of content publish

Supported values:
- `DRAFT`: Content is in draft state
- `REVIEW_IN_PROGRESS`: Content is pending publication for review
"""


class BrandStoreEditionPublishVersion(LenientModel):
    editionId: str = Field(description="Reference to the store edition")
    pages: list[StorePageVersion] | None = Field(
        default=None,
        min_length=0,
        max_length=5000,
        description="Collection of page versions included in this publish version",
    )
    publishState: StorePublishState | str
    publishStatus: StorePublishStatus | str
    storeEditionPublishId: str = Field(description="Unique identifier for the publish version")
    storeId: str = Field(description="Identifier of the associated store")


class BrandStoreEditionPublishVersionBrandStoreEditionIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStoreEditionPublishVersionBrandStoreIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1)


class BrandStoreEditionPublishVersionMultiStatusResponse(LenientModel):
    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[BrandStoreEditionPublishVersionMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=1
    )


class BrandStoreEditionPublishVersionMultiStatusSuccess(LenientModel):
    brandStoreEditionPublishVersion: BrandStoreEditionPublishVersion
    index: int = Field(ge=0, le=0)


class BrandStoreEditionPublishVersionStorePublishStatusFilter(StrictModel):
    include: list[StorePublishStatus] = Field(min_length=1, max_length=1)


class BrandStoreEditionPublishVersionSuccessResponse(LenientModel):
    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersion] | None = Field(
        default=None, min_length=0, max_length=50
    )
    nextToken: str | None = Field(default=None)


class BrandStoreEditionPublishVersionUpdate(StrictModel):
    editionId: str | None = Field(default=None, description="Reference to the store edition")
    publishState: StorePublishState | None = Field(default=None)
    storeEditionPublishId: str = Field(description="Unique identifier for the publish version")
    storeId: str | None = Field(default=None, description="Identifier of the associated store")


class QueryBrandStoreEditionPublishVersionRequest(StrictModel):
    editionIdFilter: BrandStoreEditionPublishVersionBrandStoreEditionIdFilter
    maxResults: int | None = Field(default=50, ge=1, le=50)
    nextToken: str | None = Field(default=None)
    publishStatusFilter: BrandStoreEditionPublishVersionStorePublishStatusFilter
    storeIdFilter: BrandStoreEditionPublishVersionBrandStoreIdFilter


class StorePageVersion(LenientModel):
    """Version information for a store page"""

    pageId: str = Field(description="Identifier of the page")
    version: int = Field(description="Version number of the page")


class UpdateBrandStoreEditionPublishVersionRequest(StrictModel):
    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersionUpdate] = Field(min_length=1, max_length=1)


__all__ = [
    "BrandStoreEditionPublishVersion",
    "BrandStoreEditionPublishVersionBrandStoreEditionIdFilter",
    "BrandStoreEditionPublishVersionBrandStoreIdFilter",
    "BrandStoreEditionPublishVersionMultiStatusResponse",
    "BrandStoreEditionPublishVersionMultiStatusSuccess",
    "BrandStoreEditionPublishVersionStorePublishStatusFilter",
    "BrandStoreEditionPublishVersionSuccessResponse",
    "BrandStoreEditionPublishVersionUpdate",
    "Error",
    "ErrorCode",
    "ErrorsIndex",
    "QueryBrandStoreEditionPublishVersionRequest",
    "StorePageVersion",
    "StorePublishState",
    "StorePublishStatus",
    "UpdateBrandStoreEditionPublishVersionRequest",
]
