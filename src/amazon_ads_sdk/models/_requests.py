"""request models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ad_extensions import SPAdExtensionCreate, SPAdExtensionUpdate
    from ._ad_groups import SPAdGroupCreate, SPAdGroupUpdate
    from ._ads import SPAdCreate, SPAdUpdate
    from ._campaigns import SPCampaignCreate, SPCampaignUpdate
    from ._enums import ErrorCode
    from ._filters import (
        SPAdAdGroupIdFilter,
        SPAdAdIdFilter,
        SPAdAdProductFilter,
        SPAdCampaignIdFilter,
        SPAdExtensionAdExtensionIdFilter,
        SPAdExtensionAdExtensionStatusFilter,
        SPAdExtensionAdExtensionTypeFilter,
        SPAdExtensionAdGroupIdFilter,
        SPAdExtensionAdIdFilter,
        SPAdExtensionAdProductFilter,
        SPAdExtensionStateFilter,
        SPAdGroupAdGroupIdFilter,
        SPAdGroupAdProductFilter,
        SPAdGroupCampaignIdFilter,
        SPAdGroupNameFilter,
        SPAdGroupStateFilter,
        SPAdStateFilter,
        SPCampaignAdProductFilter,
        SPCampaignCampaignIdFilter,
        SPCampaignNameFilter,
        SPCampaignPortfolioIdFilter,
        SPCampaignStateFilter,
        SPTargetAdGroupIdFilter,
        SPTargetAdProductFilter,
        SPTargetCampaignIdFilter,
        SPTargetKeywordFilter,
        SPTargetMatchTypeFilter,
        SPTargetNegativeFilter,
        SPTargetProductIdFilter,
        SPTargetStateFilter,
        SPTargetTargetIdFilter,
        SPTargetTargetTypeFilter,
    )
    from ._targets import SPTargetCreate, SPTargetUpdate


class BadRequestResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str


class SPCreateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionCreate] | None = None


class SPCreateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupCreate] | None = None


class SPCreateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdCreate] | None = None


class SPCreateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignCreate] | None = None


class SPCreateTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetCreate] | None = None


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

    adExtensionIdFilter: SPAdExtensionAdExtensionIdFilter | None = None
    adExtensionStatusFilter: SPAdExtensionAdExtensionStatusFilter | None = None
    adExtensionTypeFilter: SPAdExtensionAdExtensionTypeFilter | None = None
    adGroupIdFilter: SPAdExtensionAdGroupIdFilter | None = None
    adIdFilter: SPAdExtensionAdIdFilter | None = None
    adProductFilter: SPAdExtensionAdProductFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SPAdExtensionStateFilter | None = None


class SPQueryAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdGroupAdGroupIdFilter | None = None
    adProductFilter: SPAdGroupAdProductFilter
    campaignIdFilter: SPAdGroupCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SPAdGroupNameFilter | None = None
    nextToken: str | None = None
    stateFilter: SPAdGroupStateFilter | None = None


class SPQueryAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPAdAdGroupIdFilter | None = None
    adIdFilter: SPAdAdIdFilter | None = None
    adProductFilter: SPAdAdProductFilter
    campaignIdFilter: SPAdCampaignIdFilter | None = None
    maxResults: int | None = None
    nextToken: str | None = None
    stateFilter: SPAdStateFilter | None = None


class SPQueryCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adProductFilter: SPCampaignAdProductFilter
    campaignIdFilter: SPCampaignCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SPCampaignNameFilter | None = None
    nextToken: str | None = None
    portfolioIdFilter: SPCampaignPortfolioIdFilter | None = None
    stateFilter: SPCampaignStateFilter | None = None


class SPQueryTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupIdFilter: SPTargetAdGroupIdFilter | None = None
    adProductFilter: SPTargetAdProductFilter
    campaignIdFilter: SPTargetCampaignIdFilter | None = None
    keywordFilter: SPTargetKeywordFilter | None = None
    matchTypeFilter: SPTargetMatchTypeFilter | None = None
    maxResults: int | None = None
    negativeFilter: SPTargetNegativeFilter | None = None
    nextToken: str | None = None
    productIdFilter: SPTargetProductIdFilter | None = None
    stateFilter: SPTargetStateFilter | None = None
    targetIdFilter: SPTargetTargetIdFilter | None = None
    targetTypeFilter: SPTargetTargetTypeFilter | None = None


class SPUpdateAdExtensionRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensions: list[SPAdExtensionUpdate] | None = None


class SPUpdateAdGroupRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroups: list[SPAdGroupUpdate] | None = None


class SPUpdateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdUpdate] | None = None


class SPUpdateCampaignRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    campaigns: list[SPCampaignUpdate] | None = None


class SPUpdateTargetRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    targets: list[SPTargetUpdate] | None = None


class TooManyRequestsResponseContent(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    code: ErrorCode
    message: str
