"""request models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import ErrorCode


class BadRequestResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class TooManyRequestsResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str
