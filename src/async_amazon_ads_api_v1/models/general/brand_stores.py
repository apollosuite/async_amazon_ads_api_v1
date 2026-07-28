"""Auto-generated models for BrandStores from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BrandStore(BaseModel):
    model_config = ConfigDict(extra="forbid")

    pageInfos: list[BrandStorePageInfo] | None = (
        None  # Collection of BrandStorePageInfo for all pages tied to the brand store
    )
    storeId: str  # Unique identifier for the store
    storeName: str | None = None  # The name of the store


class BrandStorePageInfo(BaseModel):
    """Structure containing the basic information of a store page"""

    model_config = ConfigDict(extra="forbid")

    tag: str  # Unique tag for the store page
    title: str  # Title of the page


class BrandStoreStoreNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class BrandStoreSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStores: list[BrandStore] | None = None
    nextToken: str | None = None


class QueryBrandStoreRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    maxResults: int | None = None
    nextToken: str | None = None
    storeNameFilter: BrandStoreStoreNameFilter


__all__ = [
    "BrandStore",
    "BrandStorePageInfo",
    "BrandStoreStoreNameFilter",
    "BrandStoreSuccessResponse",
    "QueryBrandStoreRequest",
]
