"""Auto-generated models for BrandHomeAPIService from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class BrandHomeState(StrEnum):
    """
    Status of a resource
    """

    APPROVED = "APPROVED"
    CANCELED = "CANCELED"
    DRAFT = "DRAFT"
    LIVE = "LIVE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    SCHEDULED = "SCHEDULED"


class IdentifierType(StrEnum):
    """
    Identifier type for requested entity/resource
    """

    ASIN = "ASIN"
    BRAND_AID_ID = "BRAND_AID_ID"
    ENTITY_ID = "ENTITY_ID"
    GCOR = "GCOR"
    NODE = "NODE"
    STORE = "STORE"


class ListPagesRequest(BaseModel):
    """Request Object for ListPages API"""

    model_config = ConfigDict(extra="forbid")

    identifier: str = Field(
        description="Identifier for requested store. Currently supported: store's brand-/sub-entityId and storeId."
    )
    identifierType: Annotated[IdentifierType | str, lenient_enum(IdentifierType)]
    maxResults: int | None = Field(
        default=None,
        ge=1,
        le=30,
        description="Optional: Max number of entries returned in a call. Supported values are 1-30 inclusive. Defaults to 30.",
    )
    nextToken: str | None = Field(
        default=None,
        description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.",
    )


class ListPagesResponse(BaseModel):
    """Response Object for ListPages API"""

    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(
        default=None,
        description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.",
    )
    storePages: list[StorePageInfo] | None = Field(
        default=None, description="Paginated list of `StorePageInfos`'s. Result list size <= maxResults."
    )


class ListStoresRequest(BaseModel):
    """Request Object for ListStores API"""

    model_config = ConfigDict(extra="forbid")

    identifier: str | None = Field(
        default=None, description="Optional: Identifier for requested entity. Currently supported: Advertiser entityId."
    )
    identifierType: Annotated[IdentifierType | str, lenient_enum(IdentifierType)] | None = Field(default=None)
    maxResults: int | None = Field(
        default=None,
        ge=1,
        le=30,
        description="Optional: Max number of entries returned in a call. Supported values are 1-30 inclusive. Defaults to 30.",
    )
    nextToken: str | None = Field(
        default=None,
        description="Optional: Pagination input token. If provided, returns the next paginated result of size <= `maxResults`.",
    )


class ListStoresResponse(BaseModel):
    """Response Object for ListStores API"""

    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(
        default=None, description="Nullable. The next token to be used for paginated querying."
    )
    stores: list[StoreInfo] = Field(
        description="Paginated list of `StoreInfo`'s. Result list size <= maxResults. If advertiser has no stores, returns empty list."
    )


type StoreId = str  # The Store Identifier.


class StoreInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    brandEntityId: str | None = Field(default=None, description="The ID of the Brand Entity associated with the store")
    storeId: StoreId | None = Field(default=None)
    storeName: str | None = Field(default=None, description="The name of the store")
    storeStatus: Annotated[BrandHomeState | str, lenient_enum(BrandHomeState)] | None = Field(default=None)


class StorePageInfo(BaseModel):
    model_config = ConfigDict(extra="allow")

    storePageId: str | None = Field(default=None, description="The ID of the store page")
    storePageName: str | None = Field(default=None, description="The name of the store page")
    storePageStatus: Annotated[BrandHomeState | str, lenient_enum(BrandHomeState)] | None = Field(default=None)
    storePageUrl: str | None = Field(default=None, description="The URL of the store page")


__all__ = ["BrandHomeState", "IdentifierType", "ListPagesRequest", "ListStoresRequest", "StoreId"]
