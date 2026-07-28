"""Auto-generated models for BrandStoreEditionPublishVersions from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.errors import ErrorsIndex
from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class StorePublishState(StrEnum):
    """User State for content  StorePublishState Description ------ ------ `DRAFT` Content is in draft form `PUBLISH`
    Submit Content to Publish to LIVE / SCHEDULED."""

    DRAFT = "DRAFT"
    PUBLISH = "PUBLISH"


class StorePublishStatus(StrEnum):
    """Status of content publish  StorePublishStatus Description ------ ------ `DRAFT` Content is in draft state
    `REVIEW_IN_PROGRESS` Content is pending publication for review."""

    DRAFT = "DRAFT"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"


class BrandStoreEditionPublishVersion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str = Field(description="Reference to the store edition")
    pages: list[StorePageVersion] | None = Field(
        default=None,
        min_length=0,
        max_length=5000,
        description="Collection of page versions included in this publish version",
    )
    publishState: Annotated[StorePublishState | str, lenient_enum(StorePublishState)]
    publishStatus: Annotated[StorePublishStatus | str, lenient_enum(StorePublishStatus)]
    storeEditionPublishId: str = Field(description="Unique identifier for the publish version")
    storeId: str = Field(description="Identifier of the associated store")


class BrandStoreEditionPublishVersionBrandStoreEditionIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1)


class BrandStoreEditionPublishVersionBrandStoreIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1)


class BrandStoreEditionPublishVersionMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = Field(default=None, min_length=0, max_length=1)
    success: list[BrandStoreEditionPublishVersionMultiStatusSuccess] | None = Field(
        default=None, min_length=0, max_length=1
    )


class BrandStoreEditionPublishVersionMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersion: BrandStoreEditionPublishVersion
    index: int = Field(ge=0, le=0)


class BrandStoreEditionPublishVersionStorePublishStatusFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[StorePublishStatus | str, lenient_enum(StorePublishStatus)]] = Field(
        min_length=1,
        max_length=1,
        description="PublishStatus Description `DRAFT` Content is in draft state `REVIEW_IN_PROGRESS` Content is pending publication for review",
    )


class BrandStoreEditionPublishVersionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersion] | None = Field(
        default=None, min_length=0, max_length=50
    )
    nextToken: str | None = Field(default=None)


class BrandStoreEditionPublishVersionUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str | None = Field(default=None, description="Reference to the store edition")
    publishState: Annotated[StorePublishState | str, lenient_enum(StorePublishState)] | None = Field(default=None)
    storeEditionPublishId: str = Field(description="Unique identifier for the publish version")
    storeId: str | None = Field(default=None, description="Identifier of the associated store")


class QueryBrandStoreEditionPublishVersionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionIdFilter: BrandStoreEditionPublishVersionBrandStoreEditionIdFilter
    maxResults: int | None = Field(default=50, ge=1, le=50)
    nextToken: str | None = Field(default=None)
    publishStatusFilter: BrandStoreEditionPublishVersionStorePublishStatusFilter
    storeIdFilter: BrandStoreEditionPublishVersionBrandStoreIdFilter


class StorePageVersion(BaseModel):
    """Version information for a store page."""

    model_config = ConfigDict(extra="forbid")

    pageId: str = Field(description="Identifier of the page")
    version: int = Field(description="Version number of the page")


class UpdateBrandStoreEditionPublishVersionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditionPublishVersions: list[BrandStoreEditionPublishVersionUpdate] | None = Field(
        default=None, min_length=1, max_length=1
    )


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
