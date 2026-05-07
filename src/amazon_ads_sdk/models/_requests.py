"""request models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class BadRequestResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str


class SPCreateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None


class SPCreateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None


class SPCreateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None


class SPCreateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None


class SPCreateTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    targets: list[dict[str, Any]] | None = None


class SPDeleteAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIds: list[str] | None = None


class SPDeleteAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adIds: list[str] | None = None


class SPDeleteCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] | None = None


class SPDeleteTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    targetIds: list[str] | None = None


class SPQueryAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionIdFilter: dict[str, Any] | None = None
    adExtensionStatusFilter: dict[str, Any] | None = None
    adExtensionTypeFilter: dict[str, Any] | None = None
    adGroupIdFilter: dict[str, Any] | None = None
    adIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None


class SPQueryAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nameFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None


class SPQueryAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: dict[str, Any] | None = None


class SPQueryCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    nameFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    portfolioIdFilter: dict[str, Any] | None = None
    stateFilter: dict[str, Any] | None = None


class SPQueryTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: dict[str, Any] | None = None
    adProductFilter: dict[str, Any]
    campaignIdFilter: dict[str, Any] | None = None
    keywordFilter: dict[str, Any] | None = None
    matchTypeFilter: dict[str, Any] | None = None
    maxResults: int | None = None
    negativeFilter: dict[str, Any] | None = None
    nextToken: str | None = None
    productIdFilter: dict[str, Any] | None = None
    stateFilter: dict[str, Any] | None = None
    targetIdFilter: dict[str, Any] | None = None
    targetTypeFilter: dict[str, Any] | None = None


class SPUpdateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[dict[str, Any]] | None = None


class SPUpdateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[dict[str, Any]] | None = None


class SPUpdateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[dict[str, Any]] | None = None


class SPUpdateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[dict[str, Any]] | None = None


class SPUpdateTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    targets: list[dict[str, Any]] | None = None


class TooManyRequestsResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    message: str
