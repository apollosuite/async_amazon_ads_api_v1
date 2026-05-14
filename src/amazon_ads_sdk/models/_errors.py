"""error and HTTP response models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import ErrorCode


class BadGatewayResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class BadRequestResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class ContentTooLargeResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class Error(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    fieldLocation: str | None = None
    message: str


class ErrorsIndex(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    errors: list[Error]
    index: int


class ForbiddenResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class GatewayTimeoutResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class InternalServerErrorResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class NotFoundResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class ServiceUnavailableErrorResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class TooManyRequestsResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class UnauthorizedResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str
