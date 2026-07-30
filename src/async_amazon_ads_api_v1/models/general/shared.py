"""Auto-generated shared models for cross-tag schemas."""

from __future__ import annotations

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

from .enums import GeneralErrorCode


class GeneralError(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: Annotated[GeneralErrorCode | str, lenient_enum(GeneralErrorCode)] | None = Field(default=None)
    fieldLocation: str | None = Field(default=None)
    message: str | None = Field(default=None)


class GeneralErrorsIndex(BaseModel):
    model_config = ConfigDict(extra="allow")

    errors: list[GeneralError] | None = Field(default=None, min_length=1, max_length=20)
    index: int | None = Field(default=None, ge=0, le=0)
