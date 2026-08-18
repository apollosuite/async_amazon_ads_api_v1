"""Auto-generated models for Ad Groups from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v0._shared import (
    AdGroupId,
    BaseAdGroup,
    CampaignId,
    CreativeTypeInCreativeResponse,
    Tactic,
)


class CreativeType(StrEnum):
    """
    The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. One ad group only supports one type (VIDEO or IMAGE) of creativeType at a time.
    """

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"


class AdGroup(LenientModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: str | None = Field(
        default=None, description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks."
    )
    state: str | None = Field(default=None, description="The state of the ad group.")
    adGroupId: AdGroupId | None = Field(default=None)
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    creativeType: Annotated[CreativeType | str, lenient_enum(CreativeType)] | None = Field(default=None)


class AdGroupResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    adGroupId: AdGroupId | None = Field(default=None)


class AdGroupResponseEx(LenientModel):
    """Object containing an extended set of data fields for an Ad Group."""

    adGroupId: float | None = Field(default=None, description="The identifier of the ad group.")
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: float | None = Field(
        default=None, description="The identifier of the campaign that this ad group is associated with."
    )
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    state: str | None = Field(default=None, description="The delivery state of the ad group.")
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    creativeType: (
        Annotated[CreativeTypeInCreativeResponse | str, lenient_enum(CreativeTypeInCreativeResponse)] | None
    ) = Field(default=None)
    servingStatus: str | None = Field(default=None, description="The status of the ad group.")
    bidOptimization: str | None = Field(
        default=None,
        description="Bid optimization type for the Adgroup. Default behavior is to optimize for clicks. Note, reach, clicks are only accepted with productAds that include landingPageURL OFF_AMAZON_LINK.",
    )
    creationDate: int | None = Field(default=None, description="Epoch time the ad group was created.")
    lastUpdatedDate: int | None = Field(
        default=None, description="Epoch time any property in the ad group was last updated."
    )


class BaseAdGroupOut(LenientModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: str | None = Field(
        default=None, description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks."
    )
    state: str | None = Field(default=None, description="The state of the ad group.")


class CreateAdGroup(StrictModel):
    name: str = Field(description="The name of the ad group.")
    campaignId: CampaignId
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: str | None = Field(
        default=None, description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks."
    )
    state: str = Field(description="The state of the ad group.")
    creativeType: Annotated[CreativeType, lenient_enum(CreativeType)] | None = Field(default=None)


class UpdateAdGroup(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: str | None = Field(
        default=None, description="Bid Optimization for the Adgroup. Default behavior is to optimize for clicks."
    )
    state: str | None = Field(default=None, description="The state of the ad group.")
    adGroupId: AdGroupId


__all__ = [
    "AdGroup",
    "AdGroupId",
    "AdGroupResponse",
    "AdGroupResponseEx",
    "BaseAdGroup",
    "BaseAdGroupOut",
    "CampaignId",
    "CreateAdGroup",
    "CreativeType",
    "CreativeTypeInCreativeResponse",
    "Tactic",
    "UpdateAdGroup",
]
