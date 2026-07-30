"""Auto-generated models for Portfolios from Amazon Ads API schema."""

from __future__ import annotations

from datetime import date, datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum


class EntityState(StrEnum):
    """
    The current resource state.
    """

    ENABLED = "ENABLED"


class FeatureState(StrEnum):
    """
    The state for sharing unspent campaign budget.
    """

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class PolicyType(StrEnum):
    """
    The budget policy. Set to  `DATE_RANGE` to specify a budget for a specific period of time. Set to `MONTHLY_RECURRING` to specify a budget that is automatically renewed at the beginning of each month. To remove budget, set budget `amount`, `startDate`, `endDate` to null and set `policy` to `NO_CAP`.
    """

    DATE_RANGE = "DATE_RANGE"
    MONTHLY_RECURRING = "MONTHLY_RECURRING"
    NO_CAP = "NO_CAP"
    OTHER = "OTHER"


class PortfolioBillingErrorReason(StrEnum):
    ADVERTISER_SUSPENDED = "ADVERTISER_SUSPENDED"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    VETTING_FAILURE = "VETTING_FAILURE"


class PortfolioBudgetErrorReason(StrEnum):
    BUDGETING_POLICY_INVALID = "BUDGETING_POLICY_INVALID"
    BUDGET_AMOUNT_INVALID = "BUDGET_AMOUNT_INVALID"
    BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS = "BUDGET_CURRENCY_DOES_NOT_MATCH_MARKETPLACE_SETTINGS"
    BUDGET_LT_DEFAULT_BIDS = "BUDGET_LT_DEFAULT_BIDS"
    BUDGET_LT_KEYWORD_BIDS = "BUDGET_LT_KEYWORD_BIDS"
    BUDGET_LT_PREDEFINED_TARGET_BIDS = "BUDGET_LT_PREDEFINED_TARGET_BIDS"
    BUDGET_OUT_OF_MARKET_PLACE_RANGE = "BUDGET_OUT_OF_MARKET_PLACE_RANGE"
    BUDGET_TOO_HIGH = "BUDGET_TOO_HIGH"
    BUDGET_TOO_LOW = "BUDGET_TOO_LOW"
    MISSING_BUDGETING_POLICY = "MISSING_BUDGETING_POLICY"
    MISSING_IN_BUDGET_FLAG = "MISSING_IN_BUDGET_FLAG"


class PortfolioCurrencyCode(StrEnum):
    """
    The currency used for all monetary values for entities under this profile. Cannot be `null`.
    |Region|`countryCode`|Country Name|`currencyCode`|
    |-----|------|------|------|
    |NA|US|United States|USD|
    |NA|CA|Canada|CAD|
    |NA|MX|Mexico|MXN|
    |NA|BR|Brazil|BRL|
    |EU|UK|United Kingdom|GBP|
    |EU|DE|Germany|EUR|
    |EU|FR|France|EUR|
    |EU|ES|Spain|EUR|
    |EU|IT|Italy|EUR|
    |EU|NL|The Netherlands|EUR|
    |EU|SE|Sweden|SEK|
    |EU|PL|Poland|PLN|
    |EU|AE|United Arab Emirates|AED|
    |EU|TR|Turkey|TRY|
    |FE|JP|Japan|JPY|
    |FE|AU|Australia|AUD|
    |FE|SG|Singapore|SGD|
    """

    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    NGN = "NGN"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"


class PortfolioDateErrorReason(StrEnum):
    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_EQUAL_END_DATE = "START_DATE_EQUAL_END_DATE"
    START_DATE_NOT_NULL = "START_DATE_NOT_NULL"


class PortfolioDuplicateValueErrorReason(StrEnum):
    DUPLICATE_VALUE = "DUPLICATE_VALUE"


class PortfolioEntityNotFoundErrorReason(StrEnum):
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"


class PortfolioEntityQuotaErrorReason(StrEnum):
    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"


class PortfolioEntityType(StrEnum):
    PORTFOLIO = "PORTFOLIO"


class PortfolioMalformedValueErrorReason(StrEnum):
    FORBIDDEN_CHARS = "FORBIDDEN_CHARS"
    PATTERN_NOT_MATCHED = "PATTERN_NOT_MATCHED"
    TOO_LONG = "TOO_LONG"
    TOO_SHORT = "TOO_SHORT"


class PortfolioMissingValueErrorReason(StrEnum):
    MISSING_VALUE = "MISSING_VALUE"


class PortfolioOtherErrorReason(StrEnum):
    OTHER_ERROR = "OTHER_ERROR"


class PortfolioQuotaScope(StrEnum):
    ACCOUNT = "ACCOUNT"


class PortfolioServingStatus(StrEnum):
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET"
    ADVERTISER_ARCHIVED = "ADVERTISER_ARCHIVED"
    ADVERTISER_EXCEED_SPENDS_LIMIT = "ADVERTISER_EXCEED_SPENDS_LIMIT"
    ADVERTISER_OUT_OF_BUDGET = "ADVERTISER_OUT_OF_BUDGET"
    ADVERTISER_OUT_OF_PREPAY_BALANCE = "ADVERTISER_OUT_OF_PREPAY_BALANCE"
    ADVERTISER_PAUSED = "ADVERTISER_PAUSED"
    ADVERTISER_PAYMENT_FAILURE = "ADVERTISER_PAYMENT_FAILURE"
    PORTFOLIO_ENDED = "PORTFOLIO_ENDED"
    PORTFOLIO_OUT_OF_BUDGET = "PORTFOLIO_OUT_OF_BUDGET"
    PORTFOLIO_PENDING_START_DATE = "PORTFOLIO_PENDING_START_DATE"
    PORTFOLIO_STATUS_ENABLED = "PORTFOLIO_STATUS_ENABLED"


class PortfolioServingStatusReason(StrEnum):
    ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL = "ADVERTISER_ACCOUNT_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_ARCHIVED_DETAIL = "ADVERTISER_ARCHIVED_DETAIL"
    ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL = "ADVERTISER_EXCEED_SPENDS_LIMIT_DETAIL"
    ADVERTISER_OUT_OF_BUDGET_DETAIL = "ADVERTISER_OUT_OF_BUDGET_DETAIL"
    ADVERTISER_OUT_OF_PREPAY_BALANCE_DETAIL = "ADVERTISER_OUT_OF_PREPAY_BALANCE_DETAIL"
    ADVERTISER_PAUSED_DETAIL = "ADVERTISER_PAUSED_DETAIL"
    ADVERTISER_PAYMENT_FAILURE_DETAIL = "ADVERTISER_PAYMENT_FAILURE_DETAIL"
    PORTFOLIO_ENDED_DETAIL = "PORTFOLIO_ENDED_DETAIL"
    PORTFOLIO_OUT_OF_BUDGET_DETAIL = "PORTFOLIO_OUT_OF_BUDGET_DETAIL"
    PORTFOLIO_PENDING_START_DATE_DETAIL = "PORTFOLIO_PENDING_START_DATE_DETAIL"
    PORTFOLIO_STATUS_ENABLED_DETAIL = "PORTFOLIO_STATUS_ENABLED_DETAIL"


class PortfolioValueLimitErrorReason(StrEnum):
    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class QueryTermMatchType(StrEnum):
    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class BudgetControls(BaseModel):
    model_config = ConfigDict(extra="forbid")

    campaignUnspentBudgetSharing: CampaignUnspentBudgetSharing | None = Field(default=None)


class BudgetControlsOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    campaignUnspentBudgetSharing: CampaignUnspentBudgetSharingOut | None = Field(default=None)


class BulkPortfolioOperationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    error: list[PortfolioFailureResponseItem] | None = Field(default=None, min_length=0, max_length=100)
    success: list[PortfolioSuccessResponseItem] | None = Field(default=None, min_length=0, max_length=100)


class CampaignUnspentBudgetSharing(BaseModel):
    model_config = ConfigDict(extra="forbid")

    featureState: Annotated[FeatureState | str, lenient_enum(FeatureState)]


class CampaignUnspentBudgetSharingOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    featureState: Annotated[FeatureState | str, lenient_enum(FeatureState)]


class CreatePortfolio(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str = Field(description="The name of the portfolio.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)]


class CreatePortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    portfolios: list[CreatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio to create."
    )


class CreatePortfoliosResponseContent(BaseModel):
    model_config = ConfigDict(extra="allow")

    portfolios: BulkPortfolioOperationResponse


class EntityStateFilter(BaseModel):
    """Filter entities by state"""

    model_config = ConfigDict(extra="forbid")

    include: list[Annotated[EntityState | str, lenient_enum(EntityState)]] | None = Field(
        default=None, min_length=1, max_length=1
    )


class ErrorCause(BaseModel):
    """Structure describing error cause - location in the payload and data causing error"""

    model_config = ConfigDict(extra="allow")

    location: str = Field(
        description="Error location, JSON Path expression specifying element of API payload causing error"
    )
    trigger: str | None = Field(default=None, description="optional value causing error")


class ListPortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    includeExtendedDataFields: bool | None = Field(
        default=None,
        description="whether to get a list of targetingClauses with extended data fields (creationDate, lastUpdateDate, servingStatus).",
    )
    nameFilter: NameFilter | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolioIdFilter: ObjectIdFilter | None = Field(default=None)
    stateFilter: EntityStateFilter | None = Field(default=None)


class ListPortfoliosResponseContent(BaseModel):
    model_config = ConfigDict(extra="allow")

    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolios: list[Portfolio] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None, description="The total number of entities")


class NameFilter(BaseModel):
    """Filter entities by name"""

    model_config = ConfigDict(extra="forbid")

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)
    queryTermMatchType: Annotated[QueryTermMatchType | str, lenient_enum(QueryTermMatchType)] | None = Field(
        default=None
    )


class ObjectIdFilter(BaseModel):
    """Filter entities by the list of objectIds"""

    model_config = ConfigDict(extra="forbid")

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)


class Portfolio(BaseModel):
    model_config = ConfigDict(extra="allow")

    budget: PortfolioBudgetOut | None = Field(default=None)
    budgetControls: BudgetControlsOut | None = Field(default=None)
    extendedData: PortfolioExtendedData | None = Field(default=None)
    inBudget: bool | None = Field(default=None, description="States if the portfolio is still within budget.")
    name: str = Field(description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)]


class PortfolioBillingError(BaseModel):
    """Errors related to bids"""

    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioBillingErrorReason | str, lenient_enum(PortfolioBillingErrorReason)]


class PortfolioBudget(BaseModel):
    model_config = ConfigDict(extra="forbid")

    amount: float | None = Field(default=None, description="The amount of the budget.")
    currencyCode: Annotated[PortfolioCurrencyCode | str, lenient_enum(PortfolioCurrencyCode)] | None = Field(
        default=None
    )
    endDate: date | None = Field(
        default=None, description="The end date after which the budget is no longer applied in ISO 8601."
    )
    policy: Annotated[PolicyType | str, lenient_enum(PolicyType)] | None = Field(default=None)
    startDate: date | None = Field(
        default=None, description="The starting date to which the budget is applied in ISO 8601."
    )


class PortfolioBudgetError(BaseModel):
    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    lowerLimit: str | None = Field(default=None)
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioBudgetErrorReason | str, lenient_enum(PortfolioBudgetErrorReason)]
    upperLimit: str | None = Field(default=None)


class PortfolioBudgetOut(BaseModel):
    model_config = ConfigDict(extra="allow")

    amount: float | None = Field(default=None, description="The amount of the budget.")
    currencyCode: Annotated[PortfolioCurrencyCode | str, lenient_enum(PortfolioCurrencyCode)] | None = Field(
        default=None
    )
    endDate: date | None = Field(
        default=None, description="The end date after which the budget is no longer applied in ISO 8601."
    )
    policy: Annotated[PolicyType | str, lenient_enum(PolicyType)] | None = Field(default=None)
    startDate: date | None = Field(
        default=None, description="The starting date to which the budget is applied in ISO 8601."
    )


class PortfolioDateError(BaseModel):
    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioDateErrorReason | str, lenient_enum(PortfolioDateErrorReason)]


class PortfolioDuplicateValueError(BaseModel):
    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioDuplicateValueErrorReason | str, lenient_enum(PortfolioDuplicateValueErrorReason)]


class PortfolioEntityNotFoundError(BaseModel):
    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    entityId: str = Field(description="The entity id in the request")
    entityType: Annotated[PortfolioEntityType | str, lenient_enum(PortfolioEntityType)]
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioEntityNotFoundErrorReason | str, lenient_enum(PortfolioEntityNotFoundErrorReason)]


class PortfolioEntityQuotaError(BaseModel):
    """Errors related to exceeding quota in portfolios service"""

    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    entityType: Annotated[PortfolioEntityType | str, lenient_enum(PortfolioEntityType)]
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    quota: str | None = Field(default=None, description="optional current quota")
    quotaScope: Annotated[PortfolioQuotaScope | str, lenient_enum(PortfolioQuotaScope)] | None = Field(default=None)
    reason: Annotated[PortfolioEntityQuotaErrorReason | str, lenient_enum(PortfolioEntityQuotaErrorReason)]


class PortfolioExtendedData(BaseModel):
    model_config = ConfigDict(extra="allow")

    creationDateTime: datetime | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: datetime | None = Field(default=None, description="Date of last update in ISO 8601.")
    servingStatus: Annotated[PortfolioServingStatus | str, lenient_enum(PortfolioServingStatus)] | None = Field(
        default=None
    )
    statusReasons: (
        list[Annotated[PortfolioServingStatusReason | str, lenient_enum(PortfolioServingStatusReason)]] | None
    ) = Field(default=None, min_length=0, max_length=100)


class PortfolioFailureResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    errors: list[PortfolioMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="a list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the portfolio in the array from the request body")


class PortfolioMalformedValueError(BaseModel):
    """Errors being used to represent malformed values
    e.g. containing not allowed characters, not following patterns etc"""

    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    fragment: str | None = Field(default=None, description="fragment of the value which is wrong")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioMalformedValueErrorReason | str, lenient_enum(PortfolioMalformedValueErrorReason)]


class PortfolioMissingValueError(BaseModel):
    """Error describing missing values in API payloads"""

    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioMissingValueErrorReason | str, lenient_enum(PortfolioMissingValueErrorReason)]


class PortfolioMutationError(BaseModel):
    model_config = ConfigDict(extra="allow")

    errorType: str = Field(description="The type of the error")
    errorValue: PortfolioMutationErrorSelector


class PortfolioMutationErrorSelector(BaseModel):
    model_config = ConfigDict(extra="allow")

    billingError: PortfolioBillingError | None = Field(default=None)
    budgetError: PortfolioBudgetError | None = Field(default=None)
    dateError: PortfolioDateError | None = Field(default=None)
    duplicateValueError: PortfolioDuplicateValueError | None = Field(default=None)
    entityNotFoundError: PortfolioEntityNotFoundError | None = Field(default=None)
    entityQuotaError: PortfolioEntityQuotaError | None = Field(default=None)
    malformedValueError: PortfolioMalformedValueError | None = Field(default=None)
    missingValueError: PortfolioMissingValueError | None = Field(default=None)
    otherError: PortfolioOtherError | None = Field(default=None)
    rangeError: PortfolioRangeError | None = Field(default=None)


class PortfolioOtherError(BaseModel):
    """Errors not related to any of the other error types"""

    model_config = ConfigDict(extra="allow")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioOtherErrorReason | str, lenient_enum(PortfolioOtherErrorReason)]


class PortfolioRangeError(BaseModel):
    """Errors related to range constraints violations"""

    model_config = ConfigDict(extra="allow")

    allowed: list[str] | None = Field(default=None, min_length=1, max_length=100, description="allowed values")
    cause: ErrorCause
    lowerLimit: str | None = Field(default=None, description="optional lower limit")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: Annotated[PortfolioValueLimitErrorReason | str, lenient_enum(PortfolioValueLimitErrorReason)]
    upperLimit: str | None = Field(default=None, description="optional upper limit")


class PortfolioSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    index: int = Field(ge=0, description="the index of the portfolio in the array from the request body")
    portfolio: Portfolio | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="the Portfolio ID")


class UpdatePortfolio(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: Annotated[EntityState | str, lenient_enum(EntityState)] | None = Field(default=None)


class UpdatePortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    portfolios: list[UpdatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio with updated values."
    )


class UpdatePortfoliosResponseContent(BaseModel):
    model_config = ConfigDict(extra="allow")

    portfolios: BulkPortfolioOperationResponse


__all__ = [
    "BudgetControls",
    "CampaignUnspentBudgetSharing",
    "CreatePortfolio",
    "CreatePortfoliosRequestContent",
    "EntityState",
    "EntityStateFilter",
    "FeatureState",
    "ListPortfoliosRequestContent",
    "NameFilter",
    "ObjectIdFilter",
    "PolicyType",
    "PortfolioBillingErrorReason",
    "PortfolioBudget",
    "PortfolioBudgetErrorReason",
    "PortfolioCurrencyCode",
    "PortfolioDateErrorReason",
    "PortfolioDuplicateValueErrorReason",
    "PortfolioEntityNotFoundErrorReason",
    "PortfolioEntityQuotaErrorReason",
    "PortfolioEntityType",
    "PortfolioMalformedValueErrorReason",
    "PortfolioMissingValueErrorReason",
    "PortfolioOtherErrorReason",
    "PortfolioQuotaScope",
    "PortfolioServingStatus",
    "PortfolioServingStatusReason",
    "PortfolioValueLimitErrorReason",
    "QueryTermMatchType",
    "UpdatePortfolio",
    "UpdatePortfoliosRequestContent",
]
