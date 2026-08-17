"""Auto-generated models for Campaigns from Amazon Ads API v1."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum
from ads_api.models.v1._shared.sd import (
    SDAdProduct,
    SDCreateState,
    SDCurrencyCode,
    SDDeliveryReason,
    SDDeliveryStatus,
    SDError,
    SDErrorCode,
    SDErrorsIndex,
    SDMarketplace,
    SDMarketplaceScope,
    SDState,
    SDStatus,
    SDUpdateState,
)


class SDBudgetType(StrEnum):
    MONETARY = "MONETARY"


class SDCampaignNameFilterType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"  # Filter by broad match.
    EXACT_MATCH = "EXACT_MATCH"  # Filter by exact match.


class SDCostType(StrEnum):
    CPC = "CPC"  # Cost per click.
    VCPM = "VCPM"  # Cost per thousand views.


class SDCountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"


class SDRecurrence(StrEnum):
    DAILY = "DAILY"


class SDBudget(LenientModel):
    budgetType: Annotated[SDBudgetType | str, lenient_enum(SDBudgetType)]
    budgetValue: SDBudgetValue
    recurrenceTimePeriod: Annotated[SDRecurrence | str, lenient_enum(SDRecurrence)]


class SDBudgetValue(LenientModel):
    monetaryBudgetValue: SDMonetaryBudgetValue


class SDCampaign(LenientModel):
    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    budgets: list[SDBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode | str, lenient_enum(SDCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    creationDateTime: datetime = Field(description="The date time that the campaign was created.")
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    lastUpdatedDateTime: datetime = Field(description="The date time that the campaign was last updated.")
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = Field(default=None)
    tags: list[SDTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCampaignAdProductFilter(StrictModel):
    include: list[Annotated[SDAdProduct, lenient_enum(SDAdProduct)]] = Field(min_length=1, max_length=1)


class SDCampaignCampaignIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=1000)


class SDCampaignCreate(StrictModel):
    adProduct: Annotated[SDAdProduct, lenient_enum(SDAdProduct)]
    budgets: list[SDCreateBudget] = Field(
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    costType: Annotated[SDCostType, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode, lenient_enum(SDCountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.",
    )
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    marketplaceScope: Annotated[SDMarketplaceScope, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace, lenient_enum(SDMarketplace)]] | None = Field(
        default=None,
        min_length=0,
        max_length=1,
        description="This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.",
    )
    name: str = Field(description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime = Field(description="The start date time for the campaign.")
    state: Annotated[SDCreateState, lenient_enum(SDCreateState)]
    tags: list[SDCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCampaignMultiStatusResponse(LenientModel):
    error: list[SDErrorsIndex] | None = Field(default=None, min_length=0, max_length=100)
    success: list[SDCampaignMultiStatusSuccess] | None = Field(default=None, min_length=0, max_length=100)


class SDCampaignMultiStatusSuccess(LenientModel):
    campaign: SDCampaign
    index: int = Field(ge=0, le=99)


class SDCampaignNameFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)
    queryTermMatchType: Annotated[SDCampaignNameFilterType, lenient_enum(SDCampaignNameFilterType)]


class SDCampaignPortfolioIdFilter(StrictModel):
    include: list[str] = Field(min_length=1, max_length=100)


class SDCampaignStateFilter(StrictModel):
    include: list[Annotated[SDState, lenient_enum(SDState)]] = Field(min_length=1, max_length=3)


class SDCampaignSuccessResponse(LenientModel):
    campaigns: list[SDCampaign] | None = Field(default=None, min_length=0, max_length=100)
    nextToken: str | None = Field(default=None)


class SDCampaignUpdate(StrictModel):
    budgets: list[SDCreateBudget] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="The object containing budget details for the campaign (for campaigns that support multiple budgets).",
    )
    campaignId: str = Field(description="A unique identifier for a campaign.")
    costType: Annotated[SDCostType, lenient_enum(SDCostType)] | None = Field(default=None)
    endDateTime: datetime | None = Field(default=None, description="The end date time for the campaign.")
    name: str | None = Field(default=None, description="The name of the campaign.")
    portfolioId: str | None = Field(default=None, description="The ID of the portfolio associated with the campaign.")
    startDateTime: datetime | None = Field(default=None, description="The start date time for the campaign.")
    state: Annotated[SDUpdateState, lenient_enum(SDUpdateState)] | None = Field(default=None)
    tags: list[SDCreateTag] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="Open ended labels with a key value pair applied to the campaign",
    )


class SDCreateBudget(StrictModel):
    budgetType: Annotated[SDBudgetType, lenient_enum(SDBudgetType)]
    budgetValue: SDCreateBudgetValue


class SDCreateBudgetValue(StrictModel):
    monetaryBudgetValue: SDCreateMonetaryBudgetValue


class SDCreateCampaignRequest(StrictModel):
    campaigns: list[SDCampaignCreate] = Field(min_length=1, max_length=100)


class SDCreateMonetaryBudget(StrictModel):
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SDCreateMonetaryBudgetValue(StrictModel):
    monetaryBudget: SDCreateMonetaryBudget


class SDCreateTag(StrictModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SDDeleteCampaignRequest(StrictModel):
    campaignIds: list[str] = Field(min_length=1, max_length=100)


class SDMonetaryBudget(LenientModel):
    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    ruleValue: float | None = Field(
        default=None, description="The monetary amount of the budget when a budget rule is applied."
    )
    value: float = Field(description="The monetary amount of the budget cap in the given currency.")


class SDMonetaryBudgetValue(LenientModel):
    monetaryBudget: SDMonetaryBudget


class SDQueryCampaignRequest(StrictModel):
    adProductFilter: SDCampaignAdProductFilter
    campaignIdFilter: SDCampaignCampaignIdFilter | None = Field(default=None)
    maxResults: int | None = Field(default=100, ge=1, le=100)
    nameFilter: SDCampaignNameFilter | None = Field(default=None)
    nextToken: str | None = Field(default=None)
    portfolioIdFilter: SDCampaignPortfolioIdFilter | None = Field(default=None)
    stateFilter: SDCampaignStateFilter | None = Field(default=None)


class SDTag(LenientModel):
    key: str = Field(
        description="A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI."
    )
    value: str = Field(description="A custom key value pair entered by the advertiser.")


class SDUpdateCampaignRequest(StrictModel):
    campaigns: list[SDCampaignUpdate] = Field(min_length=1, max_length=100)


__all__ = [
    "SDAdProduct",
    "SDBudget",
    "SDBudgetType",
    "SDBudgetValue",
    "SDCampaign",
    "SDCampaignAdProductFilter",
    "SDCampaignCampaignIdFilter",
    "SDCampaignCreate",
    "SDCampaignMultiStatusResponse",
    "SDCampaignMultiStatusSuccess",
    "SDCampaignNameFilter",
    "SDCampaignNameFilterType",
    "SDCampaignPortfolioIdFilter",
    "SDCampaignStateFilter",
    "SDCampaignSuccessResponse",
    "SDCampaignUpdate",
    "SDCostType",
    "SDCountryCode",
    "SDCreateBudget",
    "SDCreateBudgetValue",
    "SDCreateCampaignRequest",
    "SDCreateMonetaryBudget",
    "SDCreateMonetaryBudgetValue",
    "SDCreateState",
    "SDCreateTag",
    "SDCurrencyCode",
    "SDDeleteCampaignRequest",
    "SDDeliveryReason",
    "SDDeliveryStatus",
    "SDError",
    "SDErrorCode",
    "SDErrorsIndex",
    "SDMarketplace",
    "SDMarketplaceScope",
    "SDMonetaryBudget",
    "SDMonetaryBudgetValue",
    "SDQueryCampaignRequest",
    "SDRecurrence",
    "SDState",
    "SDStatus",
    "SDTag",
    "SDUpdateCampaignRequest",
    "SDUpdateState",
]
