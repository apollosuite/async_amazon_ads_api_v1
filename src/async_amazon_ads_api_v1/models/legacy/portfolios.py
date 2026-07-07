"""Portfolio Pydantic models — generated from Portfolios_prod_3p.json."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class BudgetUsagePortfolioRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    portfolioIds: list[str] | None = Field(
        default=None, min_length=1, max_length=100, description="A list of portfolio IDs."
    )


class BudgetUsagePortfolioResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[BudgetUsagePortfolioBatchError] | None = Field(
        default=None, description="List of budget usage percentages that failed to pull"
    )
    success: list[BudgetUsagePortfolio] | None = Field(
        default=None, description="List of budget usage percentages that were successfully pulled"
    )


class CreatePortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="ignore")

    portfolios: list[CreatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio to create."
    )


class CreatePortfoliosResponseContent(BaseModel):
    model_config = ConfigDict(extra="ignore")

    portfolios: BulkPortfolioOperationResponse


class ListPortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="ignore")

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
    model_config = ConfigDict(extra="ignore")

    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    portfolios: list[Portfolio] | None = Field(default=None, min_length=0, max_length=1000)
    totalResults: int | None = Field(default=None, description="The total number of entities")


class UpdatePortfoliosRequestContent(BaseModel):
    model_config = ConfigDict(extra="ignore")

    portfolios: list[UpdatePortfolio] = Field(
        min_length=1, max_length=100, description="An array of portfolio with updated values."
    )


class UpdatePortfoliosResponseContent(BaseModel):
    model_config = ConfigDict(extra="ignore")

    portfolios: BulkPortfolioOperationResponse


class BudgetControls(BaseModel):
    model_config = ConfigDict(extra="ignore")

    campaignUnspentBudgetSharing: CampaignUnspentBudgetSharing | None = Field(default=None)


class BudgetUsagePortfolio(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budget: int | None = Field(default=None, description="Budget amount of resource requested")
    budgetUsagePercent: int | None = Field(
        default=None, description="Budget usage percentage (spend / available budget) for the given budget policy."
    )
    index: int | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")
    usageUpdatedTimestamp: str | None = Field(default=None, description="Last evaluation time for budget usage")


class BudgetUsagePortfolioBatchError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="An enumerated error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    index: int | None = Field(default=None, description="An index to maintain order of the portfolioIds")
    portfolioId: str | None = Field(default=None, description="ID of requested resource")


class BulkPortfolioOperationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[PortfolioFailureResponseItem] | None = Field(default=None, min_length=0, max_length=100)
    success: list[PortfolioSuccessResponseItem] | None = Field(default=None, min_length=0, max_length=100)


class CampaignUnspentBudgetSharing(BaseModel):
    model_config = ConfigDict(extra="ignore")

    featureState: FeatureState


class CreatePortfolio(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str = Field(description="The name of the portfolio.")
    state: EntityState


class CurrencyCode(
    StrEnum
):  # The currency used for all monetary values for entities under this profile. Cannot be `null`. Region `countryCode` Country Name `currencyCode` ----- ------ ------ ------ NA US United States USD NA CA Canada CAD NA MX Mexico MXN NA BR Brazil BRL EU UK United Kingdom GBP EU DE Germany EUR EU FR France EUR EU ES Spain EUR EU IT Italy EUR EU NL The Netherlands EUR EU SE Sweden SEK EU PL Poland PLN EU AE United Arab Emirates AED EU TR Turkey TRY FE JP Japan JPY FE AU Australia AUD FE SG Singapore SGD
    """The currency used for all monetary values for entities under this profile. Cannot be `null`. Region `countryCode` Country Name `currencyCode` ----- ------ ------ ------ NA US United States USD NA CA Canada CAD NA MX Mexico MXN NA BR Brazil BRL EU UK United Kingdom GBP EU DE Germany EUR EU FR France EUR EU ES Spain EUR EU IT Italy EUR EU NL The Netherlands EUR EU SE Sweden SEK EU PL Poland PLN EU AE United Arab Emirates AED EU TR Turkey TRY FE JP Japan JPY FE AU Australia AUD FE SG Singapore SGD"""

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


class EntityState(StrEnum):  # The current resource state.
    """The current resource state."""

    ENABLED = "ENABLED"


class EntityStateFilter(BaseModel):  # Filter entities by state
    model_config = ConfigDict(extra="ignore")

    include: list[EntityState] | None = Field(default=None, min_length=1, max_length=1)


class ErrorCause(BaseModel):  # Structure describing error cause - location in the payload and data causing error
    model_config = ConfigDict(extra="ignore")

    location: str = Field(
        description="Error location, JSON Path expression specifying element of API payload causing error"
    )
    trigger: str | None = Field(default=None, description="optional value causing error")


class FeatureState(StrEnum):  # The state for sharing unspent campaign budget.
    """The state for sharing unspent campaign budget."""

    DISABLED = "DISABLED"
    ENABLED = "ENABLED"


class NameFilter(BaseModel):  # Filter entities by name
    model_config = ConfigDict(extra="ignore")

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)
    queryTermMatchType: QueryTermMatchType | None = Field(default=None)


class ObjectIdFilter(BaseModel):  # Filter entities by the list of objectIds
    model_config = ConfigDict(extra="ignore")

    include: list[str] | None = Field(default=None, min_length=1, max_length=1000)


class PolicyType(
    StrEnum
):  # The budget policy. Set to  `DATE_RANGE` to specify a budget for a specific period of time. Set to `MONTHLY_RECURRING` to specify a budget that is automatically renewed at the beginning of each month. To remove budget, set budget `amount`, `startDate`, `endDate` to null and set `policy` to `NO_CAP`.
    """The budget policy. Set to  `DATE_RANGE` to specify a budget for a specific period of time. Set to `MONTHLY_RECURRING` to specify a budget that is automatically renewed at the beginning of each month. To remove budget, set budget `amount`, `startDate`, `endDate` to null and set `policy` to `NO_CAP`."""

    DATE_RANGE = "DATE_RANGE"
    MONTHLY_RECURRING = "MONTHLY_RECURRING"
    NO_CAP = "NO_CAP"
    OTHER = "OTHER"


class Portfolio(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    extendedData: PortfolioExtendedData | None = Field(default=None)
    inBudget: bool | None = Field(default=None, description="States if the portfolio is still within budget.")
    name: str = Field(description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: EntityState


class PortfolioBillingError(BaseModel):  # Errors related to bids
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioBillingErrorReason


class PortfolioBillingErrorReason(StrEnum):
    """PortfolioBillingErrorReason enum."""

    ADVERTISER_SUSPENDED = "ADVERTISER_SUSPENDED"
    BILLING_ACCOUNT_NOT_FOUND = "BILLING_ACCOUNT_NOT_FOUND"
    EXPIRED_PAYMENT_METHOD = "EXPIRED_PAYMENT_METHOD"
    PAYMENT_PROFILE_NOT_FOUND = "PAYMENT_PROFILE_NOT_FOUND"
    VETTING_FAILURE = "VETTING_FAILURE"


class PortfolioBudget(BaseModel):
    model_config = ConfigDict(extra="ignore")

    amount: float | None = Field(default=None, description="The amount of the budget.")
    currencyCode: CurrencyCode | None = Field(default=None)
    endDate: str | None = Field(
        default=None, description="The end date after which the budget is no longer applied in ISO 8601."
    )
    policy: PolicyType | None = Field(default=None)
    startDate: str | None = Field(
        default=None, description="The starting date to which the budget is applied in ISO 8601."
    )


class PortfolioBudgetError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    lowerLimit: str | None = Field(default=None)
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioBudgetErrorReason
    upperLimit: str | None = Field(default=None)


class PortfolioBudgetErrorReason(StrEnum):
    """PortfolioBudgetErrorReason enum."""

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


class PortfolioDateError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioDateErrorReason


class PortfolioDateErrorReason(StrEnum):
    """PortfolioDateErrorReason enum."""

    END_DATE_EARLIER_THAN_TODAY = "END_DATE_EARLIER_THAN_TODAY"
    INVALID_DATE = "INVALID_DATE"
    START_DATE_AFTER_END_DATE = "START_DATE_AFTER_END_DATE"
    START_DATE_EARLIER_THAN_TODAY = "START_DATE_EARLIER_THAN_TODAY"
    START_DATE_EQUAL_END_DATE = "START_DATE_EQUAL_END_DATE"
    START_DATE_NOT_NULL = "START_DATE_NOT_NULL"


class PortfolioDuplicateValueError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioDuplicateValueErrorReason


class PortfolioDuplicateValueErrorReason(StrEnum):
    """PortfolioDuplicateValueErrorReason enum."""

    DUPLICATE_VALUE = "DUPLICATE_VALUE"


class PortfolioEntityNotFoundError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    entityId: str = Field(description="The entity id in the request")
    entityType: PortfolioEntityType
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioEntityNotFoundErrorReason


class PortfolioEntityNotFoundErrorReason(StrEnum):
    """PortfolioEntityNotFoundErrorReason enum."""

    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"


class PortfolioEntityQuotaError(BaseModel):  # Errors related to exceeding quota in portfolios service
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    entityType: PortfolioEntityType
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    quota: str | None = Field(default=None, description="optional current quota")
    quotaScope: PortfolioQuotaScope | None = Field(default=None)
    reason: PortfolioEntityQuotaErrorReason


class PortfolioEntityQuotaErrorReason(StrEnum):
    """PortfolioEntityQuotaErrorReason enum."""

    QUOTA_EXCEEDED = "QUOTA_EXCEEDED"


class PortfolioEntityType(StrEnum):
    """PortfolioEntityType enum."""

    PORTFOLIO = "PORTFOLIO"


class PortfolioExtendedData(BaseModel):
    model_config = ConfigDict(extra="ignore")

    creationDateTime: str | None = Field(default=None, description="Creation date in ISO 8601.")
    lastUpdateDateTime: str | None = Field(default=None, description="Date of last update in ISO 8601.")
    servingStatus: PortfolioServingStatus | None = Field(default=None)
    statusReasons: list[PortfolioServingStatusReason] | None = Field(default=None, min_length=0, max_length=100)


class PortfolioFailureResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    errors: list[PortfolioMutationError] | None = Field(
        default=None, min_length=0, max_length=100, description="a list of validation errors"
    )
    index: int = Field(ge=0, description="the index of the portfolio in the array from the request body")


class PortfolioMalformedValueError(
    BaseModel
):  # Errors being used to represent malformed values e.g. containing not allowed characters, not following patterns etc
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    fragment: str | None = Field(default=None, description="fragment of the value which is wrong")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioMalformedValueErrorReason


class PortfolioMalformedValueErrorReason(StrEnum):
    """PortfolioMalformedValueErrorReason enum."""

    FORBIDDEN_CHARS = "FORBIDDEN_CHARS"
    PATTERN_NOT_MATCHED = "PATTERN_NOT_MATCHED"
    TOO_LONG = "TOO_LONG"
    TOO_SHORT = "TOO_SHORT"


class PortfolioMissingValueError(BaseModel):  # Error describing missing values in API payloads
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioMissingValueErrorReason


class PortfolioMissingValueErrorReason(StrEnum):
    """PortfolioMissingValueErrorReason enum."""

    MISSING_VALUE = "MISSING_VALUE"


class PortfolioMutationError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    errorType: str = Field(description="The type of the error")
    errorValue: PortfolioMutationErrorSelector


class PortfolioMutationErrorSelector(BaseModel):
    model_config = ConfigDict(extra="ignore")

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


class PortfolioOtherError(BaseModel):  # Errors not related to any of the other error types
    model_config = ConfigDict(extra="ignore")

    cause: ErrorCause
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioOtherErrorReason


class PortfolioOtherErrorReason(StrEnum):
    """PortfolioOtherErrorReason enum."""

    OTHER_ERROR = "OTHER_ERROR"


class PortfolioQuotaScope(StrEnum):
    """PortfolioQuotaScope enum."""

    ACCOUNT = "ACCOUNT"


class PortfolioRangeError(BaseModel):  # Errors related to range constraints violations
    model_config = ConfigDict(extra="ignore")

    allowed: list[str] | None = Field(default=None, min_length=1, max_length=100, description="allowed values")
    cause: ErrorCause
    lowerLimit: str | None = Field(default=None, description="optional lower limit")
    marketplace: str | None = Field(default=None)
    message: str = Field(description="Human readable error message")
    reason: PortfolioValueLimitErrorReason
    upperLimit: str | None = Field(default=None, description="optional upper limit")


class PortfolioServingStatus(StrEnum):
    """PortfolioServingStatus enum."""

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
    """PortfolioServingStatusReason enum."""

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


class PortfolioSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    index: int = Field(ge=0, description="the index of the portfolio in the array from the request body")
    portfolio: Portfolio | None = Field(default=None)
    portfolioId: str | None = Field(default=None, description="the Portfolio ID")


class PortfolioValueLimitErrorReason(StrEnum):
    """PortfolioValueLimitErrorReason enum."""

    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    TOO_HIGH = "TOO_HIGH"
    TOO_LOW = "TOO_LOW"


class QueryTermMatchType(StrEnum):
    """QueryTermMatchType enum."""

    BROAD_MATCH = "BROAD_MATCH"
    EXACT_MATCH = "EXACT_MATCH"


class UpdatePortfolio(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budget: PortfolioBudget | None = Field(default=None)
    budgetControls: BudgetControls | None = Field(default=None)
    name: str | None = Field(default=None, description="The name of the portfolio.")
    portfolioId: str = Field(description="The ID of the portfolio.")
    state: EntityState | None = Field(default=None)


__all__ = [
    "BudgetControls",
    "BudgetUsagePortfolio",
    "BudgetUsagePortfolioBatchError",
    "BudgetUsagePortfolioRequest",
    "BudgetUsagePortfolioResponse",
    "BulkPortfolioOperationResponse",
    "CampaignUnspentBudgetSharing",
    "CreatePortfolio",
    "CreatePortfoliosRequestContent",
    "CreatePortfoliosResponseContent",
    "CurrencyCode",
    "EntityState",
    "EntityStateFilter",
    "ErrorCause",
    "FeatureState",
    "ListPortfoliosRequestContent",
    "ListPortfoliosResponseContent",
    "NameFilter",
    "ObjectIdFilter",
    "PolicyType",
    "Portfolio",
    "PortfolioBillingError",
    "PortfolioBillingErrorReason",
    "PortfolioBudget",
    "PortfolioBudgetError",
    "PortfolioBudgetErrorReason",
    "PortfolioDateError",
    "PortfolioDateErrorReason",
    "PortfolioDuplicateValueError",
    "PortfolioDuplicateValueErrorReason",
    "PortfolioEntityNotFoundError",
    "PortfolioEntityNotFoundErrorReason",
    "PortfolioEntityQuotaError",
    "PortfolioEntityQuotaErrorReason",
    "PortfolioEntityType",
    "PortfolioExtendedData",
    "PortfolioFailureResponseItem",
    "PortfolioMalformedValueError",
    "PortfolioMalformedValueErrorReason",
    "PortfolioMissingValueError",
    "PortfolioMissingValueErrorReason",
    "PortfolioMutationError",
    "PortfolioMutationErrorSelector",
    "PortfolioOtherError",
    "PortfolioOtherErrorReason",
    "PortfolioQuotaScope",
    "PortfolioRangeError",
    "PortfolioServingStatus",
    "PortfolioServingStatusReason",
    "PortfolioSuccessResponseItem",
    "PortfolioValueLimitErrorReason",
    "QueryTermMatchType",
    "UpdatePortfolio",
    "UpdatePortfoliosRequestContent",
    "UpdatePortfoliosResponseContent",
]
