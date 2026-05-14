"""shared models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._ads import (
        SPAudienceBidAdjustment,
        SPCreateAudienceBidAdjustment,
        SPCreateCreativeBidAdjustment,
        SPCreateVideo,
        SPCreativeBidAdjustment,
        SPProductCreative,
    )
    from ._enums import (
        ErrorCode,
        SPBidStrategy,
        SPBudgetType,
        SPCurrencyCode,
        SPDeliveryReason,
        SPDeliveryStatus,
        SPMarketplace,
        SPMarketplaceBudgetAllocation,
        SPOffAmazonBudgetControlStrategy,
        SPPlacement,
        SPRecurrence,
    )


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


class SPAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPPlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    marketplaceBudgetAllocation: SPMarketplaceBudgetAllocation | None = None
    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPMonetaryBudgetValue | None = None


class SPCreateAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPCreateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPCreateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPCreateBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPCreateBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    budgetType: SPBudgetType
    budgetValue: SPCreateBudgetValue
    recurrenceTimePeriod: SPRecurrence


class SPCreateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPCreateBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SPCreateMonetaryBudgetValue | None = None


class SPCreateGlobalStoreSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: SPMarketplace | None = None


class SPCreateMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.


class SPCreateMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPCreateMonetaryBudget


class SPCreatePlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


class SPCreateTag(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.


class SPCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreative: SPProductCreative | None = None


class SPGlobalStoreSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: SPMarketplace | None = None


class SPMonetaryBudget(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    currencyCode: SPCurrencyCode
    ruleValue: float | None = (
        None  # The monetary amount of the budget when a budget rule is applied.
    )
    value: float  # The monetary amount of the budget cap in the given currency.


class SPMonetaryBudgetValue(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SPMonetaryBudget


class SPPlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


class SPStatus(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    deliveryReasons: list[SPDeliveryReason] | None = (
        None  # This is the list of reasons behind the delivery status.
    )
    deliveryStatus: SPDeliveryStatus


class SPTag(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.


class SPUpdateBidAdjustments(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[SPCreateAudienceBidAdjustment] | None = (
        None  # Bid Adjustments based on the audiences
    )
    creativeBidAdjustments: list[SPCreateCreativeBidAdjustment] | None = (
        None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment value would be 0:900
    )
    placementBidAdjustments: list[SPCreatePlacementBidAdjustment] | None = (
        None  # Bid adjustments based on ad placements.
    )


class SPUpdateBidSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    bidAdjustments: SPUpdateBidAdjustments | None = None
    bidStrategy: SPBidStrategy | None = None


class SPUpdateBudgetSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: SPOffAmazonBudgetControlStrategy | None = None


class SPUpdateCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreative: SPUpdateProductCreative | None = None


class SPUpdateProductCreative(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: SPUpdateProductCreativeSettings | None = None


class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""

    model_config = ConfigDict(extra="forbid")

    spotlightVideos: SPUpdateSpotlightVideoSettings | None = None


class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""

    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = (
        None  # If the advertiser wants text they provided to be optimized by Amazon or not.
    )
    videos: list[SPCreateVideo] | None = (
        None  # The video asset(s) to use for the Sponsored Product experience.
    )
