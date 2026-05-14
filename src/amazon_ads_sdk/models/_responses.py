"""response models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ad_extensions import SPAdExtension, SPAdExtensionMultiStatusSuccess
    from ._ad_groups import SPAdGroup, SPAdGroupMultiStatusSuccess
    from ._ads import SPAd, SPAdMultiStatusSuccess
    from ._campaigns import SPCampaign, SPCampaignMultiStatusSuccess
    from ._enums import ErrorCode
    from ._shared import ErrorsIndex
    from ._targets import SPTarget, SPTargetMultiStatusSuccess


class BadGatewayResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class ContentTooLargeResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


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


class SPAdExtensionMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdExtensionMultiStatusSuccess] | None = None


class SPAdExtensionSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtension] | None = None
    nextToken: str | None = None


class SPAdGroupMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdGroupMultiStatusSuccess] | None = None


class SPAdGroupSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroup] | None = None
    nextToken: str | None = None


class SPAdMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdMultiStatusSuccess] | None = None


class SPAdSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAd] | None = None
    nextToken: str | None = None


class SPCampaignMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPCampaignMultiStatusSuccess] | None = None


class SPCampaignSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaign] | None = None
    nextToken: str | None = None


class SPTargetMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPTargetMultiStatusSuccess] | None = None


class SPTargetSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    nextToken: str | None = None
    targets: list[SPTarget] | None = None


class ServiceUnavailableErrorResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: str
    message: str


class UnauthorizedResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str
