"""bid adjustment models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import SPBidStrategy, SPCreativeBidAdjustmentType, SPPlacement


class SPAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


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


class SPCreateAudienceBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    audienceId: str  # The unique identifier of the Audience to apply bid adjustment.
    percentage: int  # The selection of the percentage change associated with a given audience and bid adjustment settings.


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


class SPCreateCreativeBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    creativeType: SPCreativeBidAdjustmentType | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid adjustment settings.


class SPCreatePlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


class SPCreativeBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    creativeType: SPCreativeBidAdjustmentType | None = None
    percentage: int  # The selection of the percentage change associated with the creative type and bid adjustment settings.


class SPPlacementBidAdjustment(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    percentage: int  # The selection of the percentage change associated with a given placement and bid adjustment settings.
    placement: SPPlacement


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
