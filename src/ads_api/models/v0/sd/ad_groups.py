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
    BaseAdGroupBidOptimization,
    BaseAdGroupState,
    CampaignId,
    CreativeTypeInCreativeResponse,
    Tactic,
)


class AdGroupResponseExBidOptimization(StrEnum):
    """
    Bid optimization type for the Adgroup. Default behavior is to optimize for clicks. Note, reach, clicks are only accepted with productAds that include landingPageURL OFF_AMAZON_LINK.
    |Name|CostType|Description|
    |----|--------|-----------|
    |reach|vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
    |clicks [Default]|cpc|Optimize for page visits.|
    |conversions|cpc|Optimize for conversion.|
    """

    reach = "reach"
    clicks = "clicks"
    conversions = "conversions"


class AdGroupResponseExServingStatus(StrEnum):
    """
    The status of the ad group.
    """

    ADVERTISER_STATUS_ENABLED = "ADVERTISER_STATUS_ENABLED"
    STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ACCOUNT_OUT_OF_BUDGET = "ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    CAMPAIGN_PAUSED = "CAMPAIGN_PAUSED"
    CAMPAIGN_ARCHIVED = "CAMPAIGN_ARCHIVED"
    PENDING_START_DATE = "PENDING_START_DATE"
    ENDED = "ENDED"
    CAMPAIGN_OUT_OF_BUDGET = "CAMPAIGN_OUT_OF_BUDGET"
    AD_GROUP_STATUS_ENABLED = "AD_GROUP_STATUS_ENABLED"
    AD_GROUP_PAUSED = "AD_GROUP_PAUSED"
    AD_GROUP_ARCHIVED = "AD_GROUP_ARCHIVED"
    AD_GROUP_INCOMPLETE = "AD_GROUP_INCOMPLETE"
    AD_GROUP_LOW_BID = "AD_GROUP_LOW_BID"
    ADGROUP_POLICING_PENDING_REVIEW = "ADGROUP_POLICING_PENDING_REVIEW"
    ADGROUP_POLICING_CREATIVE_REJECTED = "ADGROUP_POLICING_CREATIVE_REJECTED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    AD_POLICING_PENDING_REVIEW = "AD_POLICING_PENDING_REVIEW"
    CAMPAIGN_INCOMPLETE = "CAMPAIGN_INCOMPLETE"
    INELIGIBLE = "INELIGIBLE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"


class AdGroupResponseExState(StrEnum):
    """
    The delivery state of the ad group.
    """

    enabled = "enabled"
    paused = "paused"
    archived = "archived"


class CreativeType(StrEnum):
    """
    The type of the associated creative. If the field is empty or null, a default value of IMAGE will be used. One ad group only supports one type (VIDEO or IMAGE) of creativeType at a time.
    |Name|Description|
    |----|-----------|
    |IMAGE |The creative will display static assets (e.g. headline, brandLogo or custom image).|
    |VIDEO |The creative will display video assets. This type of creative must have a video asset provided. Only supported when using productAds with ASIN or SKU.|
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
    bidOptimization: Annotated[BaseAdGroupBidOptimization | str, lenient_enum(BaseAdGroupBidOptimization)] | None = (
        Field(
            default=None,
            description="""
Bid Optimization for the Adgroup. Default behavior is to optimize for clicks.
|Name|CostType|Description|
|----|--------|-----------|
|reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks |cpc|[Default] Optimize for page visits.|
|conversions |cpc|Optimize for conversion.|
""",
        )
    )
    state: Annotated[BaseAdGroupState | str, lenient_enum(BaseAdGroupState)] | None = Field(
        default=None, description="The state of the ad group."
    )
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
    state: Annotated[AdGroupResponseExState | str, lenient_enum(AdGroupResponseExState)] | None = Field(
        default=None, description="The delivery state of the ad group."
    )
    tactic: Annotated[Tactic | str, lenient_enum(Tactic)] | None = Field(default=None)
    creativeType: (
        Annotated[CreativeTypeInCreativeResponse | str, lenient_enum(CreativeTypeInCreativeResponse)] | None
    ) = Field(default=None)
    servingStatus: (
        Annotated[AdGroupResponseExServingStatus | str, lenient_enum(AdGroupResponseExServingStatus)] | None
    ) = Field(default=None, description="The status of the ad group.")
    bidOptimization: (
        Annotated[AdGroupResponseExBidOptimization | str, lenient_enum(AdGroupResponseExBidOptimization)] | None
    ) = Field(
        default=None,
        description="""
Bid optimization type for the Adgroup. Default behavior is to optimize for clicks. Note, reach, clicks are only accepted with productAds that include landingPageURL OFF_AMAZON_LINK.
|Name|CostType|Description|
|----|--------|-----------|
|reach|vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks [Default]|cpc|Optimize for page visits.|
|conversions|cpc|Optimize for conversion.|
""",
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
    bidOptimization: Annotated[BaseAdGroupBidOptimization | str, lenient_enum(BaseAdGroupBidOptimization)] | None = (
        Field(
            default=None,
            description="""
Bid Optimization for the Adgroup. Default behavior is to optimize for clicks.
|Name|CostType|Description|
|----|--------|-----------|
|reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks |cpc|[Default] Optimize for page visits.|
|conversions |cpc|Optimize for conversion.|
""",
        )
    )
    state: Annotated[BaseAdGroupState | str, lenient_enum(BaseAdGroupState)] | None = Field(
        default=None, description="The state of the ad group."
    )


class CreateAdGroup(StrictModel):
    name: str = Field(description="The name of the ad group.")
    campaignId: CampaignId
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: Annotated[BaseAdGroupBidOptimization | str, lenient_enum(BaseAdGroupBidOptimization)] | None = (
        Field(
            default=None,
            description="""
Bid Optimization for the Adgroup. Default behavior is to optimize for clicks.
|Name|CostType|Description|
|----|--------|-----------|
|reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks |cpc|[Default] Optimize for page visits.|
|conversions |cpc|Optimize for conversion.|
""",
        )
    )
    state: Annotated[BaseAdGroupState | str, lenient_enum(BaseAdGroupState)] = Field(
        description="The state of the ad group."
    )
    creativeType: Annotated[CreativeType | str, lenient_enum(CreativeType)] | None = Field(default=None)


class UpdateAdGroup(StrictModel):
    name: str | None = Field(default=None, description="The name of the ad group.")
    campaignId: CampaignId | None = Field(default=None)
    defaultBid: float | None = Field(
        default=None,
        description="The amount of the default bid associated with the ad group. Used if no bid is specified.",
    )
    bidOptimization: Annotated[BaseAdGroupBidOptimization | str, lenient_enum(BaseAdGroupBidOptimization)] | None = (
        Field(
            default=None,
            description="""
Bid Optimization for the Adgroup. Default behavior is to optimize for clicks.
|Name|CostType|Description|
|----|--------|-----------|
|reach |vcpm|Optimize for viewable impressions. $1 is the minimum bid for vCPM.|
|clicks |cpc|[Default] Optimize for page visits.|
|conversions |cpc|Optimize for conversion.|
""",
        )
    )
    state: Annotated[BaseAdGroupState | str, lenient_enum(BaseAdGroupState)] | None = Field(
        default=None, description="The state of the ad group."
    )
    adGroupId: AdGroupId


__all__ = [
    "AdGroup",
    "AdGroupId",
    "AdGroupResponse",
    "AdGroupResponseEx",
    "AdGroupResponseExBidOptimization",
    "AdGroupResponseExServingStatus",
    "AdGroupResponseExState",
    "BaseAdGroup",
    "BaseAdGroupBidOptimization",
    "BaseAdGroupOut",
    "BaseAdGroupState",
    "CampaignId",
    "CreateAdGroup",
    "CreativeType",
    "CreativeTypeInCreativeResponse",
    "Tactic",
    "UpdateAdGroup",
]
