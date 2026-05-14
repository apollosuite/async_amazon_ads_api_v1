"""ad models."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ad_groups import SPAdAdGroupIdFilter
    from ._campaigns import SPAdCampaignIdFilter
    from ._creatives import SPCreateCreative, SPCreative, SPUpdateCreative
    from ._enums import (
        SPAdProduct,
        SPAdType,
        SPCreateState,
        SPMarketplace,
        SPMarketplaceScope,
        SPState,
        SPUpdateState,
    )
    from ._errors import ErrorsIndex
    from ._shared import SPCreateTag, SPStatus, SPTag


class SPAd(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adId: str  # The identifier of the ad.
    adProduct: SPAdProduct
    adType: SPAdType
    campaignId: str  # The campaign associated with the ad. It's a read-only field.
    creationDateTime: datetime  # The date time that the ad was created.
    creative: SPCreative
    globalAdId: str | None = None  # The global ad identifier that manages this marketplace ad.
    lastUpdatedDateTime: datetime  # The date time that the ad was last updated.
    marketplaceScope: SPMarketplaceScope
    marketplaces: list[
        SPMarketplace
    ]  # The list of country codes representing amazon marketplaces in which the global ad is applicable. The marketplaces included should either be same as or subset of parent ad group
    state: SPState
    status: SPStatus | None = None
    tags: list[SPTag] | None = None  # Open ended labels with a key value pair applied to the ad


class SPAdAdIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdCreate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adGroupId: str  # The ad group associated with the ad.
    adProduct: SPAdProduct
    adType: SPAdType
    creative: SPCreateCreative
    state: SPCreateState
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad
    )


class SPAdMultiStatusResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SPAdMultiStatusSuccess] | None = None


class SPAdMultiStatusSuccess(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ad: SPAd
    index: int


class SPAdStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdSuccessResponse(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAd] | None = None
    nextToken: str | None = None


class SPAdUpdate(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adId: str  # The identifier of the ad.
    creative: SPUpdateCreative | None = None
    state: SPUpdateState | None = None
    tags: list[SPCreateTag] | None = (
        None  # Open ended labels with a key value pair applied to the ad
    )


class SPCreateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdCreate] | None = None


class SPDeleteAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    adIds: list[str] | None = None


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


class SPUpdateAdRequest(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    ads: list[SPAdUpdate] | None = None
