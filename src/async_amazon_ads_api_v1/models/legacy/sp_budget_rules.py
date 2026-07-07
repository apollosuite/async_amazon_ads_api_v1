"""SP Budget Rules Pydantic models — generated from SponsoredProducts_prod_3p.json."""

from __future__ import annotations

import typing
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class SPBulkBudgetRulesAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesAssociations: list[SPBudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class SPBulkBudgetRulesAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesAssociations: typing.Any | None = Field(default=None)


class SPBulkBudgetRulesDisAssociationRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDisAssociations: list[SPBudgetRulesRelations] | None = Field(
        default=None, max_length=50, description="A list of budget rule campaign details."
    )


class SPBulkBudgetRulesDisAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDisAssociations: typing.Any | None = Field(default=None)


class SPCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SPCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SPAssociatedBudgetRuleResponse] | None = Field(default=None)


class SPCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SPBudgetRuleResponse] | None = Field(default=None)


class SPCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SPBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SPDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    pass


class SPGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRule: SPBudgetRule | None = Field(default=None)


class SPGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesForAdvertiserResponse: list[SPBudgetRule] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SPGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaigns: list[SPAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SPListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedRules: list[SPCampaignBudgetRule] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class SPUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SPBudgetRuleResponse] | None = Field(default=None)


class SPUpdateBudgetRulesRequest(BaseModel):  # Request object for updating budget rule for SP campaign
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SPBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SPAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SPAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="ignore")

    campaignId: str = Field(description="The campaign identifier.")
    campaignName: str = Field(description="The campaign name.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")


class SPBudgetChangeType(StrEnum):  # The value by which to update the budget of the budget rule.
    """The value by which to update the budget of the budget rule."""

    PERCENT = "PERCENT"


class SPBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaignIds: list[str] | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")


class SPBudgetRulesRelations(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRuleId: str = Field(description="The rule identifier.")
    campaignId: str = Field(description="The campaign identifier.")


class SPBulkBudgetRulesRelationsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    campaignId: str | None = Field(default=None, description="The campaign identifier.")
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    index: int | None = Field(default=None, description="The index of the request in the bulk request.")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SPComparisonOperator(StrEnum):  # The comparison operator.
    """The comparison operator."""

    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class SPDateRangeTypeRuleDuration(BaseModel):  # Object representing date range type rule duration.
    model_config = ConfigDict(extra="ignore")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SPDayOfWeek(StrEnum):  # The day of the week.
    """The day of the week."""

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class SPEventTypeRuleDuration(BaseModel):  # Object representing event type rule duration.
    model_config = ConfigDict(extra="ignore")

    endDate: str | None = Field(default=None, description="The event end date in YYYYMMDD format. Read-only.")
    eventId: str = Field(
        description="The event identifier. This value is available from the budget rules recommendation API."
    )
    eventName: str | None = Field(default=None, description="The event name. Read-only.")
    startDate: str | None = Field(
        default=None,
        description="The event start date in YYYYMMDD format. Read-only. Note that this field is present only for announced events.",
    )


class SPPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="ignore")

    comparisonOperator: SPComparisonOperator
    metricName: SPPerformanceMetric
    threshold: float = Field(description="The performance threshold value.")


class SPPerformanceMetric(StrEnum):  # The advertising performance metric.
    """The advertising performance metric."""

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class SPRecurrence(BaseModel):
    model_config = ConfigDict(extra="ignore")

    daysOfWeek: list[SPDayOfWeek] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SPTimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: SPRecurrenceType | None = Field(default=None)


class SPRecurrenceType(StrEnum):  # The frequency of the rule application.
    """The frequency of the rule application."""

    DAILY = "DAILY"


class SPRuleDuration(BaseModel):
    model_config = ConfigDict(extra="ignore")

    dateRangeTypeRuleDuration: SPDateRangeTypeRuleDuration | None = Field(default=None)
    eventTypeRuleDuration: SPEventTypeRuleDuration | None = Field(default=None)


class SPBudgetRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: SPBudgetRuleState | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SPBudgetRuleDetails(BaseModel):  # Object representing details of a budget rule for SP campaign
    model_config = ConfigDict(extra="ignore")

    budgetIncreaseBy: SPBudgetIncreaseBy | None = Field(default=None)
    duration: SPRuleDuration | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SPPerformanceMeasureCondition | None = Field(default=None)
    recurrence: SPRecurrence | None = Field(default=None)
    ruleType: SPRuleType | None = Field(default=None)


class SPCampaignBudgetRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SPBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: SPBudgetRuleState | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SPRuleType(
    StrEnum
):  # The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria."""

    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


class SPBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="ignore")

    type: SPBudgetChangeType
    value: float = Field(description="The budget value.")


class SPBudgetRuleState(StrEnum):  # The budget rule state.
    """The budget rule state."""

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SPTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="ignore")

    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


__all__ = [
    "SPAssociatedBudgetRuleResponse",
    "SPAssociatedCampaign",
    "SPBudgetChangeType",
    "SPBudgetIncreaseBy",
    "SPBudgetRule",
    "SPBudgetRuleDetails",
    "SPBudgetRuleResponse",
    "SPBudgetRuleState",
    "SPBudgetRulesRelations",
    "SPBulkBudgetRulesAssociationRequest",
    "SPBulkBudgetRulesAssociationResponse",
    "SPBulkBudgetRulesDisAssociationRequest",
    "SPBulkBudgetRulesDisAssociationResponse",
    "SPBulkBudgetRulesRelationsResponse",
    "SPCampaignBudgetRule",
    "SPComparisonOperator",
    "SPCreateAssociatedBudgetRulesRequest",
    "SPCreateAssociatedBudgetRulesResponse",
    "SPCreateBudgetRulesRequest",
    "SPCreateBudgetRulesResponse",
    "SPDateRangeTypeRuleDuration",
    "SPDayOfWeek",
    "SPDisassociateAssociatedBudgetRuleResponse",
    "SPEventTypeRuleDuration",
    "SPGetAssociatedCampaignsResponse",
    "SPGetBudgetRuleResponse",
    "SPGetBudgetRulesForAdvertiserResponse",
    "SPListAssociatedBudgetRulesResponse",
    "SPPerformanceMeasureCondition",
    "SPPerformanceMetric",
    "SPRecurrence",
    "SPRecurrenceType",
    "SPRuleDuration",
    "SPRuleType",
    "SPTimeOfDay",
    "SPUpdateBudgetRulesRequest",
    "SPUpdateBudgetRulesResponse",
]
