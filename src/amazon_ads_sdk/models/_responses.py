"""response models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class BadGatewayResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class ContentTooLargeResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str


class ForbiddenResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
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

    code: dict[str, Any]
    message: str


class SPAdExtensionMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None


class SPAdExtensionSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None
    nextToken: str | None = None


class SPAdGroupMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None


class SPAdGroupSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None
    nextToken: str | None = None


class SPAdMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None


class SPAdSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None
    nextToken: str | None = None


class SPCampaignMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None


class SPCampaignSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None
    nextToken: str | None = None


class SPTargetMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[dict[str, Any]] | None = None
    success: list[dict[str, Any]] | None = None


class SPTargetSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[dict[str, Any]] | None = None


class ServiceUnavailableErrorResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class UnauthorizedResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str
