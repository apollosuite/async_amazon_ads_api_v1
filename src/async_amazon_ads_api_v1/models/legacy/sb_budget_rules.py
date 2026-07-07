"""SB Budget Rules Pydantic models — generated from sponsoredBrands_40_openapi.json."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class SBCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SBCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SBAssociatedBudgetRuleResponse] | None = Field(default=None)


class SBCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SBBudgetRuleResponse] | None = Field(default=None)


class SBCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SBBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SBDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    pass


class SBGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRule: SBBudgetRule | None = Field(default=None)


class SBGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesForAdvertiserResponse: list[SBBudgetRule] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SBGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaigns: list[SBAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SBListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedRules: list[SBCampaignBudgetRule] | None = Field(
        default=None, description="A list of associated budget rules."
    )


class SBUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SBBudgetRuleResponse] | None = Field(default=None)


class SBUpdateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SBBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SBAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SBAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="ignore")

    campaignId: str = Field(description="The campaign identifier.")
    campaignName: str = Field(description="The campaign name.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")


class SBBudgetChangeType(StrEnum):  # The value by which to update the budget of the budget rule.
    """The value by which to update the budget of the budget rule."""

    PERCENT = "PERCENT"


class SBBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaignIds: list[str] | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")


class SBComparisonOperator(StrEnum):  # The comparison operator.
    """The comparison operator."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class SBDateRangeTypeRuleDuration(BaseModel):  # Object representing date range type rule duration.
    model_config = ConfigDict(extra="ignore")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SBDayOfWeek(StrEnum):  # The day of the week.
    """The day of the week."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class SBEventTypeRuleDuration(BaseModel):  # Object representing event type rule duration.
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


class SBPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="ignore")

    comparisonOperator: SBComparisonOperator
    metricName: SBPerformanceMetric
    threshold: float = Field(description="The performance threshold value.")


class SBPerformanceMetric(StrEnum):  # The advertising performance metric.
    """The advertising performance metric."""

    IS = "IS"
    NTB = "NTB"
    ROAS = "ROAS"


class SBRecurrence(BaseModel):
    model_config = ConfigDict(extra="ignore")

    daysOfWeek: list[SBDayOfWeek] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SBTimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: SBRecurrenceType | None = Field(default=None)


class SBRecurrenceType(StrEnum):  # depicts the type of recurrence
    """depicts the type of recurrence"""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class SBRuleDuration(BaseModel):
    model_config = ConfigDict(extra="ignore")

    dateRangeTypeRuleDuration: SBDateRangeTypeRuleDuration | None = Field(default=None)
    eventTypeRuleDuration: SBEventTypeRuleDuration | None = Field(default=None)


class SBBudgetRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SBBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: SBBudgetRuleState | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SBBudgetRuleDetails(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetIncreaseBy: SBBudgetIncreaseBy | None = Field(default=None)
    duration: SBRuleDuration | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SBPerformanceMeasureCondition | None = Field(default=None)
    recurrence: SBRecurrence | None = Field(default=None)
    ruleType: SBRuleType | None = Field(default=None)


class SBCampaignBudgetRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SBBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: SBBudgetRuleState | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule evaluation status. Read-only.")


class SBRuleType(
    StrEnum
):  # The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria."""

    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SBBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="ignore")

    type: SBBudgetChangeType
    value: float = Field(description="The budget value.")


class SBBudgetRuleState(StrEnum):  # The budget rule state.
    """The budget rule state."""

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SBTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="ignore")

    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


__all__ = [
    "SBAssociatedBudgetRuleResponse",
    "SBAssociatedCampaign",
    "SBBudgetChangeType",
    "SBBudgetIncreaseBy",
    "SBBudgetRule",
    "SBBudgetRuleDetails",
    "SBBudgetRuleResponse",
    "SBBudgetRuleState",
    "SBCampaignBudgetRule",
    "SBComparisonOperator",
    "SBCreateAssociatedBudgetRulesRequest",
    "SBCreateAssociatedBudgetRulesResponse",
    "SBCreateBudgetRulesRequest",
    "SBCreateBudgetRulesResponse",
    "SBDateRangeTypeRuleDuration",
    "SBDayOfWeek",
    "SBDisassociateAssociatedBudgetRuleResponse",
    "SBEventTypeRuleDuration",
    "SBGetAssociatedCampaignsResponse",
    "SBGetBudgetRuleResponse",
    "SBGetBudgetRulesForAdvertiserResponse",
    "SBListAssociatedBudgetRulesResponse",
    "SBPerformanceMeasureCondition",
    "SBPerformanceMetric",
    "SBRecurrence",
    "SBRecurrenceType",
    "SBRuleDuration",
    "SBRuleType",
    "SBTimeOfDay",
    "SBUpdateBudgetRulesRequest",
    "SBUpdateBudgetRulesResponse",
]
