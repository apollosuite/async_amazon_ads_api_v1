"""shared models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class Error(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    code: dict[str, Any]
    fieldLocation: str | None = None
    message: str
class ErrorsIndex(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    errors: list[dict[str, Any]]
    index: int
class SPAutoCreationSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the camp
    autoManageCampaign: bool | None = None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
class SPBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.
class SPBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None
class SPBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    budgetType: dict[str, Any]
    budgetValue: dict[str, Any]
    recurrenceTimePeriod: dict[str, Any]
class SPBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    marketplaceBudgetAllocation: dict[str, Any] | None = None
    offAmazonBudgetControlStrategy: dict[str, Any] | None = None
class SPBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPCreateAutoCreationSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the camp
    autoManageCampaign: bool | None = None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
class SPCreateBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.
class SPCreateBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None
class SPCreateBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    budgetType: dict[str, Any]
    budgetValue: dict[str, Any]
    recurrenceTimePeriod: dict[str, Any]
class SPCreateBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: dict[str, Any] | None = None
class SPCreateBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPCreateCampaignOptimizations(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None
class SPCreateGlobalStoreSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: dict[str, Any] | None = None
class SPCreateMonetaryBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.
class SPCreateMonetaryBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: dict[str, Any]
class SPCreatePlacementBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid
    placement: dict[str, Any]
class SPCreateTag(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.
class SPCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPGlobalStoreSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    catalogSourceMarketplace: dict[str, Any] | None = None
class SPMonetaryBudget(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    currencyCode: dict[str, Any]
    ruleValue: float | None = None  # The monetary amount of the budget when a budget rule is applied.
    value: float  # The monetary amount of the budget cap in the given currency.
class SPMonetaryBudgetValue(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: dict[str, Any]
class SPPlacementBidAdjustment(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid
    placement: dict[str, Any]
class SPStatus(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    deliveryReasons: list[dict[str, Any]] | None = None  # This is the list of reasons behind the delivery status.
    deliveryStatus: dict[str, Any]
class SPTag(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.
class SPUpdateBidAdjustments(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    audienceBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on the audiences
    creativeBidAdjustments: list[dict[str, Any]] | None = None  # Bid Adjustments based on ads being shown as a creative. Range of bid adjustment
    placementBidAdjustments: list[dict[str, Any]] | None = None  # Bid adjustments based on ad placements.
class SPUpdateBidSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidAdjustments: dict[str, Any] | None = None
    bidStrategy: dict[str, Any] | None = None
class SPUpdateBudgetSettings(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    offAmazonBudgetControlStrategy: dict[str, Any] | None = None
class SPUpdateCampaignOptimizations(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    bidSettings: dict[str, Any] | None = None
    budgetSettings: dict[str, Any] | None = None
class SPUpdateCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")
class SPUpdateProductCreative(BaseModel):
    """"""
    model_config = ConfigDict(extra="forbid")

    productCreativeSettings: dict[str, Any] | None = None
class SPUpdateProductCreativeSettings(BaseModel):
    """An ad with a creative built based on the product being advertised."""
    model_config = ConfigDict(extra="forbid")

    spotlightVideos: dict[str, Any] | None = None
class SPUpdateSpotlightVideoSettings(BaseModel):
    """An ad with a creative built with spotlight videos."""
    model_config = ConfigDict(extra="forbid")

    optimizeText: bool | None = None  # If the advertiser wants text they provided to be optimized by Amazon or not.
    videos: list[dict[str, Any]] | None = None  # The video asset(s) to use for the Sponsored Product experience.

