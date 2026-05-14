"""ad_extension models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ads import SPCreateVideoExtension, SPVideoExtension
    from ._enums import (
        SPAdExtensionStatus,
        SPAdExtensionType,
        SPAdProduct,
        SPCreateState,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from ._shared import SPStatus


class SPAdExtension(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    adExtensionSettings: SPAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | None = None
    adExtensionType: SPAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SPAdProduct
    creationDateTime: datetime  # The date time the ad_extension was created.
    lastUpdatedDateTime: datetime  # The date time the ad_extension was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: SPState
    status: SPStatus | None = None


class SPAdExtensionCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionSettings: SPCreateAdExtensionSettings
    adExtensionStatus: SPAdExtensionStatus | None = None
    adExtensionType: SPAdExtensionType
    adGroupId: str | None = (
        None  # A unique identifier for the ad group associated with the ad_extension.
    )
    adId: str | None = None  # A unique identifier for the ad associated with the ad_extension.
    adProduct: SPAdProduct
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of marketplace in which the global ad_extension is applicable. The mark
    state: SPCreateState


class SPAdExtensionMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtension: SPAdExtension
    index: int


class SPAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    promptExtension: SPPromptExtension | None = None
    videoExtension: SPVideoExtension | None = None


class SPAdExtensionUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adExtensionId: str  # A unique identifier for the ad_extension.
    state: SPUpdateState | None = None


class SPCreateAdExtensionSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    promptExtension: SPCreatePromptExtension | None = None
    videoExtension: SPCreateVideoExtension | None = None


class SPCreatePromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads


class SPPromptExtension(BaseModel):
    """Prompts Ad Extension"""

    model_config = ConfigDict(extra="forbid")

    promptText: str  # The prompt text rendered in the ads
