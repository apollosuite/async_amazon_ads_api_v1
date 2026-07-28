"""Auto-generated models for BrandStoreEditions from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class BrandStoreEdition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str = Field(description="Unique identifier for the edition within the store")
    editionName: str = Field(description="Name of the store edition")
    storeEditionSchedule: StoreEditionSchedule | None = Field(default=None)
    storeId: str = Field(description="Identifier of the associated store")


class BrandStoreEditionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditions: list[BrandStoreEdition] | None = Field(default=None, min_length=0, max_length=50)
    nextToken: str | None = Field(default=None)


class StoreEditionSchedule(BaseModel):
    """Schedule information for store edition."""

    model_config = ConfigDict(extra="forbid")

    endAt: datetime | None = Field(default=None, description="End time for the store edition")
    startAt: datetime | None = Field(default=None, description="Start time for the store edition")


__all__ = ["BrandStoreEdition", "BrandStoreEditionSuccessResponse", "StoreEditionSchedule"]
