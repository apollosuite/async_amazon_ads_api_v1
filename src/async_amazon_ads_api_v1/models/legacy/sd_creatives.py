"""SD Creatives Pydantic models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class SDCreativeItem(BaseModel):
    """A single SD creative within a multi-status response."""

    model_config = ConfigDict(extra="ignore")

    index: int
    code: str | None = None
    details: str | None = None
    description: str | None = None
    creativeId: str | None = None
    creative: Any = None


class SDCreativesResponse(BaseModel):
    """Response for POST /sd/creatives."""

    model_config = ConfigDict(extra="ignore")

    success: list[SDCreativeItem] = []
    error: list[SDCreativeItem] = []


__all__ = [
    "SDCreativeItem",
    "SDCreativesResponse",
]
