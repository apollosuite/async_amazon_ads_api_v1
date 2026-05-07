"""ad_extension models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SPAdExtension(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: dict[str, Any]
    adExtensionStatus: dict[str, Any] | None = None
    adExtensionType: dict[str, Any]
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: dict[str, Any]
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: dict[str, Any]
    marketplaces: list[
        dict[str, Any]
    ]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: dict[str, Any]
    status: dict[str, Any] | None = None


class SPAdExtensionCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: dict[str, Any]
    adExtensionStatus: dict[str, Any] | None = None
    adExtensionType: dict[str, Any]
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: dict[str, Any]
    marketplaceScope: dict[str, Any]
    marketplaces: list[
        dict[str, Any]
    ]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: dict[str, Any]


class SPAdExtensionMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtension: dict[str, Any]
    index: int


class SPAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")


class SPAdExtensionUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: dict[str, Any] | None = None


class SPCreateAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")


class SPCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SPPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads
