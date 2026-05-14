"""filter models."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from ._enums import (
        SPAdExtensionStatus,
        SPAdExtensionType,
        SPAdGroupNameFilterType,
        SPAdProduct,
        SPCampaignNameFilterType,
        SPMatchType,
        SPState,
        SPTargetKeywordFilterType,
        SPTargetProductIdFilterType,
        SPTargetType,
    )


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
        SPAdProduct
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
        SPAdExtensionStatus
    ]  # AdExtensionStatus Description `OPTED_OUT` If the advertiser has opted out of this Ad Extension.


class SPAdExtensionAdExtensionTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdExtensionType
    ]  # AdExtensionType Description `PROMPTS` Enables Prompt based Ad Extension. `VIDEO` Enables Video based Ad Extension.


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
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdExtensionStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdGroupAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPAdGroupCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPAdGroupNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPAdGroupNameFilterType


class SPAdGroupStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPAdStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPCampaignAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPCampaignCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignNameFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPCampaignNameFilterType


class SPCampaignPortfolioIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPCampaignStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPTargetAdGroupIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetAdProductFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPAdProduct
    ]  # AdProduct Description `SPONSORED_PRODUCTS` Sponsored Products ad product.


class SPTargetCampaignIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetKeywordFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPTargetKeywordFilterType


class SPTargetMatchTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPMatchType
    ]  # MatchType Description `KEYWORDS_RELATED_TO_GIFTS` Search terms related to gifts. `KEYWORDS_RELATED_TO_PEER_BRANDS_PRODUCT_CATEGORY` Search terms that shoppers often use when searching for and interacting with products from other brands in the category of your advertised products. The peer brands are selected automatically. `PRODUCT_SIMILAR` Products similar to the specified product. `BROAD` Broad match search terms. This expands matching on user intent beyond PHRASE. `EXACT` Exact match search terms. `KEYWORDS_RELATED_TO_YOUR_PRODUCT_CATEGORY` Search terms shoppers often use to search for products in the same category as the products you're advertising. `KEYWORDS_RELATED_TO_YOUR_BRAND` Search terms related to your brand. `PRODUCT_SUBSTITUTES` Products that can be substituted for advertised product. `KEYWORDS_LOOSE_MATCH` Search terms loosely matching advertised product. `PHRASE` Phrase match search terms. This expands matching on user intent beyond EXACT. `KEYWORDS_CLOSE_MATCH` Search terms closely matching advertised product. `PRODUCT_COMPLEMENTS` Products that complement advertised product. `PRODUCT_EXACT` Products exactly matching the specified product. `KEYWORDS_RELATED_TO_PRIME_DAY` Search terms that shoppers are likely to use during Prime Day. These keywords can include terms related to the event, like "prime day", combined with product-specific terms. These keywords can help you expand reach to shoppers during the sales event. These keywords will only match queries through the end of Prime Day.


class SPTargetNegativeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[bool]


class SPTargetProductIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: SPTargetProductIdFilterType


class SPTargetStateFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPState
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SPTargetTargetIdFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SPTargetTargetTypeFilter(BaseModel):
    """"""

    model_config = ConfigDict(extra="forbid")

    include: list[
        SPTargetType
    ]  # TargetType Description `KEYWORD` Target based on customer search terms. `PRODUCT` Target based on a specific product. `PRODUCT_CATEGORY` Target based on a product category. `LOCATION` Target based on geographic location. `THEME` Target based on a keyword theme. These were formerly known as Auto Targets for Sponsored Products.
