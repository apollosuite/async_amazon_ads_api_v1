"""Auto-generated models for BrandStores from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class BrandStore(BaseModel):
    model_config = ConfigDict(extra="forbid")

    pageInfos: list[BrandStorePageInfo] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="Collection of BrandStorePageInfo for all pages tied to the brand store",
    )
    storeId: str = Field(description="Unique identifier for the store")
    storeName: str | None = Field(default=None, description="The name of the store")


class BrandStorePageInfo(BaseModel):
    """Structure containing the basic information of a store page"""

    model_config = ConfigDict(extra="forbid")

    tag: str = Field(description="Unique tag for the store page")
    title: str = Field(description="Title of the page")


class BrandStoreStoreNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str] = Field(min_length=1, max_length=1)


class BrandStoreSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStores: list[BrandStore] | None = Field(default=None, min_length=0, max_length=30)
    nextToken: str | None = Field(default=None)


class QueryBrandStoreRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = Field(default=30, ge=1, le=30)
    nextToken: str | None = Field(default=None)
    storeNameFilter: BrandStoreStoreNameFilter


__all__ = [
    "BrandStore",
    "BrandStorePageInfo",
    "BrandStoreStoreNameFilter",
    "BrandStoreSuccessResponse",
    "QueryBrandStoreRequest",
]
