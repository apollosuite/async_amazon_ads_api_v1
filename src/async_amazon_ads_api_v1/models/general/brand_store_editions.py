"""Auto-generated models for BrandStoreEditions from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BrandStoreEdition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    editionId: str  # Unique identifier for the edition within the store
    editionName: str  # Name of the store edition
    storeEditionSchedule: StoreEditionSchedule | None = None
    storeId: str  # Identifier of the associated store


class BrandStoreEditionSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    brandStoreEditions: list[BrandStoreEdition] | None = None
    nextToken: str | None = None


class StoreEditionSchedule(BaseModel):
    """Schedule information for store edition"""

    model_config = ConfigDict(extra="forbid")

    endAt: datetime | None = None  # End time for the store edition
    startAt: datetime | None = None  # Start time for the store edition


__all__ = ["BrandStoreEdition", "BrandStoreEditionSuccessResponse", "StoreEditionSchedule"]
