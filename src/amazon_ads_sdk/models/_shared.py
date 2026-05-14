"""shared models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import SPDeliveryReason, SPDeliveryStatus


class SPAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPCreateAutoCreationSettings(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    autoCreateTargets: bool  # Gives Amazon permission to automatically create targets associated with the campaign based on the products being advertised.
    autoManageCampaign: bool | None = (
        None  # Flag that allows Amazon to manage the lifecycle of your Campaign.
    )


class SPCreateTag(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser.
    value: str  # A custom key value pair entered by the advertiser.


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
