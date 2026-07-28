"""Auto-generated models for BrandStoreEditionPublishVersions from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class StorePublishState(StrEnum):
    """User State for content  StorePublishState Description ------ ------ `DRAFT` Content is in draft form `PUBLISH` Submit Content to Publish to LIVE / SCHEDULED"""

    DRAFT = "DRAFT"
    PUBLISH = "PUBLISH"


class StorePublishStatus(StrEnum):
    """Status of content publish  StorePublishStatus Description ------ ------ `DRAFT` Content is in draft state `REVIEW_IN_PROGRESS` Content is pending publication for review"""

    DRAFT = "DRAFT"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"


class BrandStoreEditionPublishVersion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str  # Reference to the store edition
    pages: list[StorePageVersion] | None = None  # Collection of page versions included in this publish version
    publishState: Annotated[StorePublishState | str, lenient_enum(StorePublishState)]
    publishStatus: Annotated[StorePublishStatus | str, lenient_enum(StorePublishStatus)]
    storeEditionPublishId: str  # Unique identifier for the publish version
    storeId: str  # Identifier of the associated store


class BrandStoreEditionPublishVersionBrandStoreEditionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStoreEditionPublishVersionBrandStoreIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStoreEditionPublishVersionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[BrandStoreEditionPublishVersionMultiStatusSuccess] | None = None


class BrandStoreEditionPublishVersionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersion: BrandStoreEditionPublishVersion
    index: int


class BrandStoreEditionPublishVersionStorePublishStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[StorePublishStatus | str, lenient_enum(StorePublishStatus)]
    ]  # PublishStatus Description `DRAFT` Content is in draft state `REVIEW_IN_PROGRESS` Content is pending publication for review


class BrandStoreEditionPublishVersionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersion] | None = None
    nextToken: str | None = None


class BrandStoreEditionPublishVersionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str | None = None  # Reference to the store edition
    publishState: Annotated[StorePublishState | str, lenient_enum(StorePublishState)] | None = None
    storeEditionPublishId: str  # Unique identifier for the publish version
    storeId: str | None = None  # Identifier of the associated store


class QueryBrandStoreEditionPublishVersionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionIdFilter: BrandStoreEditionPublishVersionBrandStoreEditionIdFilter
    maxResults: int | None = None
    nextToken: str | None = None
    publishStatusFilter: BrandStoreEditionPublishVersionStorePublishStatusFilter
    storeIdFilter: BrandStoreEditionPublishVersionBrandStoreIdFilter


class StorePageVersion(BaseModel):
    """Version information for a store page"""

    model_config = ConfigDict(extra="forbid")

    pageId: str  # Identifier of the page
    version: int  # Version number of the page


class UpdateBrandStoreEditionPublishVersionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersionUpdate] | None = None


__all__ = [
    "StorePublishState",
    "StorePublishStatus",
    "BrandStoreEditionPublishVersion",
    "BrandStoreEditionPublishVersionBrandStoreEditionIdFilter",
    "BrandStoreEditionPublishVersionBrandStoreIdFilter",
    "BrandStoreEditionPublishVersionMultiStatusResponse",
    "BrandStoreEditionPublishVersionMultiStatusSuccess",
    "BrandStoreEditionPublishVersionStorePublishStatusFilter",
    "BrandStoreEditionPublishVersionSuccessResponse",
    "BrandStoreEditionPublishVersionUpdate",
    "QueryBrandStoreEditionPublishVersionRequest",
    "StorePageVersion",
    "UpdateBrandStoreEditionPublishVersionRequest",
]
