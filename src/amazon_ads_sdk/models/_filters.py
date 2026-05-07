"""filter models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class SPAdAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdExtensionIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdExtensionStatusFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of thi


class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension. `VIDEO`


class SPAdExtensionAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdExtensionAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdExtensionStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # State Description `ENABLED` The object is set active by user and eligible for de


class SPAdGroupAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdGroupCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]


class SPAdGroupStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # State Description `ENABLED` The object is set active by user and eligible for de


class SPAdStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # State Description `ENABLED` The object is set active by user and eligible for de


class SPCampaignAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPCampaignCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]


class SPCampaignPortfolioIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # State Description `ENABLED` The object is set active by user and eligible for de


class SPTargetAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPTargetCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetKeywordFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]


class SPTargetMatchTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # MatchType Description `KEYWORDS_RELATED_TO_GIFTS` Search terms related to gifts.


class SPTargetNegativeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[bool]


class SPTargetProductIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: dict[str, Any]


class SPTargetStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # State Description `ENABLED` The object is set active by user and eligible for de


class SPTargetTargetIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetTargetTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        dict[str, Any]
    ]  # TargetType Description `KEYWORD` Target based on customer search terms. `PRODUCT
