"""Auto-generated Pydantic models for sd from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, ConfigDict

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum

if TYPE_CHECKING:
    from async_amazon_ads_api_v1.errors import ErrorsIndex

    from .enums import (
        SDAdProduct,
        SDCreateState,
        SDCurrencyCode,
        SDMarketplace,
        SDMarketplaceScope,
        SDState,
        SDUpdateState,
    )
    from .shared import SDStatus
del TYPE_CHECKING


class SDBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetType: Annotated[SDBudgetType | str, lenient_enum(SDBudgetType)]
    budgetValue: SDBudgetValue
    recurrenceTimePeriod: Annotated[SDRecurrence | str, lenient_enum(SDRecurrence)]


class SDBudgetType(StrEnum):
    """| BudgetType | Description |
    |------|------|
    | `MONETARY` |  |
    """

    MONETARY = "MONETARY"


class SDBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SDMonetaryBudgetValue | None = None


class SDCampaign(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    budgets: list[
        SDBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    campaignId: str  # A unique identifier for a campaign.
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode | str, lenient_enum(SDCountryCode)]] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    creationDateTime: datetime  # The date time that the campaign was created.
    endDateTime: datetime | None = None  # The end date time for the campaign.
    lastUpdatedDateTime: datetime  # The date time that the campaign was last updated.
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] | None = (
        None  # This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.
    )
    name: str  # The name of the campaign.
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    startDateTime: datetime  # The start date time for the campaign.
    state: Annotated[SDState | str, lenient_enum(SDState)]
    status: SDStatus | None = None
    tags: list[SDTag] | None = None  # Open ended labels with a key value pair applied to the campaign


class SDCampaignAdProductFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    ]  # AdProduct Description `SPONSORED_DISPLAY` Sponsored Display ad product.


class SDCampaignCampaignIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDCampaignCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProduct: Annotated[SDAdProduct | str, lenient_enum(SDAdProduct)]
    budgets: list[
        SDCreateBudget
    ]  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)]
    countries: list[Annotated[SDCountryCode | str, lenient_enum(SDCountryCode)]] | None = (
        None  # This field is used in Sponsored Ads and ADSP and impacts targeted supply. For Sponsored Ads, the campaign.countries field determines what Amazon retail supply (Amazon.com, Amazon.co.uk, Amazon.mx, etc) the campaign will serve in. Similarly in ADSP, this has an implicit filter on your inventory targets. If you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties. ADSP options include additional countries - for example, choosing Austria means targeting Austria eligible inventory and Amazon retail supply of Amazon.de.
    )
    endDateTime: datetime | None = None  # The end date time for the campaign.
    marketplaceScope: Annotated[SDMarketplaceScope | str, lenient_enum(SDMarketplaceScope)]
    marketplaces: list[Annotated[SDMarketplace | str, lenient_enum(SDMarketplace)]] | None = (
        None  # This represents retail domains such as Amazon.com, Amazon.co.uk, and Amazon.mx, each corresponding to a country where an Amazon customer can shop. ADSP campaigns can be created by specifying either countries or marketplaces, but at least one of these attributes must be provided. In ADSP, this field acts as an implicit filter on your inventory targets. For example, if you choose an inventory target of AMAZON with campaign.countries set to US, this will target the retail supply of Amazon.com and non-retail Amazon properties.
    )
    name: str  # The name of the campaign.
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    startDateTime: datetime  # The start date time for the campaign.
    state: Annotated[SDCreateState | str, lenient_enum(SDCreateState)]
    tags: list[SDCreateTag] | None = None  # Open ended labels with a key value pair applied to the campaign


class SDCampaignMultiStatusResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    error: list[ErrorsIndex] | None = None
    success: list[SDCampaignMultiStatusSuccess] | None = None


class SDCampaignMultiStatusSuccess(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaign: SDCampaign
    index: int


class SDCampaignNameFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]
    queryTermMatchType: Annotated[SDCampaignNameFilterType | str, lenient_enum(SDCampaignNameFilterType)]


class SDCampaignNameFilterType(StrEnum):
    """| CampaignNameFilterType | Description |
    | --- | --- |
    | `EXACT_MATCH` | Filter by exact match. |
    | `BROAD_MATCH` | Filter by broad match. |"""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class SDCampaignPortfolioIdFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[str]


class SDCampaignStateFilter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include: list[
        Annotated[SDState | str, lenient_enum(SDState)]
    ]  # State Description `ENABLED` The object is set active by user and eligible for delivery. `PAUSED` The object is stopped by user and not eligible for delivery. `ARCHIVED` The object is permanently stopped and cannot be reactivated. Terminal end state.


class SDCampaignSuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SDCampaign] | None = None
    nextToken: str | None = None


class SDCampaignUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgets: list[SDCreateBudget] | None = (
        None  # The object containing budget details for the campaign (for campaigns that support multiple budgets).
    )
    campaignId: str  # A unique identifier for a campaign.
    costType: Annotated[SDCostType | str, lenient_enum(SDCostType)] | None = None
    endDateTime: datetime | None = None  # The end date time for the campaign.
    name: str | None = None  # The name of the campaign.
    portfolioId: str | None = None  # The ID of the portfolio associated with the campaign.
    startDateTime: datetime | None = None  # The start date time for the campaign.
    state: Annotated[SDUpdateState | str, lenient_enum(SDUpdateState)] | None = None
    tags: list[SDCreateTag] | None = None  # Open ended labels with a key value pair applied to the campaign


class SDCostType(StrEnum):
    """| CostType | Description |
    |------|------|
    | `CPC` | Cost per click. |
    | `VCPM` | Cost per thousand views. |
    """

    CPC = "CPC"
    VCPM = "VCPM"


class SDCountryCode(StrEnum):
    """| CountryCode | Description |
    |------|------|
    | `AE` |  |
    | `AU` |  |
    | `BE` |  |
    | `BR` |  |
    | `CA` |  |
    | `DE` |  |
    | `EG` |  |
    | `ES` |  |
    | `FR` |  |
    | `GB` |  |
    | `IN` |  |
    | `IT` |  |
    | `JP` |  |
    | `MX` |  |
    | `NL` |  |
    | `PL` |  |
    | `SA` |  |
    | `SE` |  |
    | `SG` |  |
    | `TR` |  |
    | `US` |  |
    """

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


class SDCreateBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetType: Annotated[SDBudgetType | str, lenient_enum(SDBudgetType)]
    budgetValue: SDCreateBudgetValue


class SDCreateBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudgetValue: SDCreateMonetaryBudgetValue | None = None


class SDCreateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SDCampaignCreate] | None = None


class SDCreateMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: float  # The monetary amount of the budget cap in the given currency.


class SDCreateMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SDCreateMonetaryBudget


class SDCreateTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI.
    value: str  # A custom key value pair entered by the advertiser.


class SDDeleteCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaignIds: list[str] | None = None


class SDMonetaryBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    currencyCode: Annotated[SDCurrencyCode | str, lenient_enum(SDCurrencyCode)]
    ruleValue: float | None = None  # The monetary amount of the budget when a budget rule is applied.
    value: float  # The monetary amount of the budget cap in the given currency.


class SDMonetaryBudgetValue(BaseModel):
    model_config = ConfigDict(extra="forbid")

    monetaryBudget: SDMonetaryBudget


class SDQueryCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    adProductFilter: SDCampaignAdProductFilter
    campaignIdFilter: SDCampaignCampaignIdFilter | None = None
    maxResults: int | None = None
    nameFilter: SDCampaignNameFilter | None = None
    nextToken: str | None = None
    portfolioIdFilter: SDCampaignPortfolioIdFilter | None = None
    stateFilter: SDCampaignStateFilter | None = None


class SDRecurrence(StrEnum):
    """| Recurrence | Description |
    |------|------|
    | `DAILY` |  |
    """

    DAILY = "DAILY"


class SDTag(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str  # A custom key value pair entered by the advertiser. For ADSP Campaigns and Ad Groups, Amazon creates a COMMENTS key when the Comments field is populated in UI.
    value: str  # A custom key value pair entered by the advertiser.


class SDUpdateCampaignRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaigns: list[SDCampaignUpdate] | None = None


__all__ = [
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
    "SDCreateTag",
    "SDDeleteCampaignRequest",
    "SDMonetaryBudget",
    "SDMonetaryBudgetValue",
    "SDQueryCampaignRequest",
    "SDRecurrence",
    "SDTag",
    "SDUpdateCampaignRequest",
]
