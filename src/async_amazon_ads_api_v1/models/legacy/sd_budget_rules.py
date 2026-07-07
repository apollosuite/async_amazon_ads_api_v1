"""SD Budget Rules Pydantic models — generated from sponsoredDisplay_30_openapi.yaml."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class SDCreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRuleIds: list[str] | None = Field(
        default=None, max_length=25, description="A list of budget rule identifiers."
    )


class SDCreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SDAssociatedBudgetRuleResponse] | None = Field(default=None)


class SDCreateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SDBudgetRuleResponse] | None = Field(default=None)


class SDCreateBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SDBudgetRuleDetails] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SDDisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    pass


class SDGetBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRule: SDBudgetRule | None = Field(default=None)


class SDGetBudgetRulesForAdvertiserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    budgetRulesForAdvertiserResponse: list[SDBudgetRule] | None = Field(
        default=None, min_length=0, max_length=30, description="A list of rules created by the advertiser."
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SDGetAssociatedCampaignsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaigns: list[SDAssociatedCampaign] | None = Field(
        default=None,
        min_length=0,
        max_length=30,
        description="A list of campaigns that are associated to this budget rule.",
    )
    nextToken: str | None = Field(
        default=None,
        description="To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.",
    )


class SDListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedRules: list[SDBudgetRule] | None = Field(default=None, description="A list of associated budget rules.")


class SDUpdateBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    responses: list[SDBudgetRuleResponse] | None = Field(default=None)


class SDUpdateBudgetRulesRequest(BaseModel):  # Request object for updating budget rule for SD campaign
    model_config = ConfigDict(extra="ignore")

    budgetRulesDetails: list[SDBudgetRule] | None = Field(
        default=None, max_length=25, description="A list of budget rule details."
    )


class SDAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The budget rule identifier.")


class SDAssociatedCampaign(BaseModel):
    model_config = ConfigDict(extra="ignore")

    campaignId: str = Field(description="The campaign identifier.")
    campaignName: str = Field(description="The campaign name.")
    ruleStatus: str = Field(description="The budget rule evaluation status for this campaign. Read-only.")


class SDBudgetChangeType(StrEnum):  # The value by which to update the budget of the budget rule.
    """The value by which to update the budget of the budget rule."""

    PERCENT = "PERCENT"


class SDBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    associatedCampaignIds: list[str] | None = Field(default=None)
    code: str | None = Field(default=None, description="An enumerated success or error code for machine use.")
    details: str | None = Field(default=None, description="A human-readable description of the error, if unsuccessful")
    ruleId: str | None = Field(default=None, description="The rule identifier.")


class SDComparisonOperator(StrEnum):  # The comparison operator.
    """The comparison operator."""

    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"


class SDDateRangeTypeRuleDuration(BaseModel):  # Object representing date range type rule duration.
    model_config = ConfigDict(extra="ignore")

    endDate: str | None = Field(
        default=None,
        description="The end date of the budget rule in YYYYMMDD format. The end date is inclusive. Required to be equal or greater than `startDate`.",
    )
    startDate: str = Field(
        description="The start date of the budget rule in YYYYMMDD format. The start date is inclusive. Required to be greater than or equal to current date."
    )


class SDDayOfWeek(StrEnum):  # The day of the week.
    """The day of the week."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class SDEventTypeRuleDuration(BaseModel):  # Object representing event type rule duration.
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


class SDPerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="ignore")

    comparisonOperator: SDComparisonOperator
    metricName: SDPerformanceMetric
    threshold: float = Field(description="The performance threshold value.")


class SDPerformanceMetric(StrEnum):  # The advertising performance metric.
    """The advertising performance metric."""

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


class SDRecurrence(BaseModel):
    model_config = ConfigDict(extra="ignore")

    daysOfWeek: list[SDDayOfWeek] | None = Field(
        default=None,
        description="Object representing days of the week for weekly type rule. It is not required for daily recurrence type",
    )
    intraDaySchedule: list[SDTimeOfDay] | None = Field(
        default=None,
        max_length=1,
        description="List of objects representing start and end time of desired intra-day budget rule window",
    )
    type: SDRecurrenceType | None = Field(default=None)


class SDRecurrenceType(StrEnum):  # depicts the type of recurrence
    """depicts the type of recurrence"""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class SDRuleDuration(BaseModel):
    model_config = ConfigDict(extra="ignore")

    dateRangeTypeRuleDuration: SDDateRangeTypeRuleDuration | None = Field(default=None)
    eventTypeRuleDuration: SDEventTypeRuleDuration | None = Field(default=None)


class SDBudgetRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    createdDate: int | None = Field(default=None, description="Epoch time of budget rule creation. Read-only.")
    lastUpdatedDate: int | None = Field(default=None, description="Epoch time of budget rule update. Read-only.")
    ruleDetails: SDBudgetRuleDetails | None = Field(default=None)
    ruleId: str = Field(description="The budget rule identifier.")
    ruleState: SDBudgetRuleState | None = Field(default=None)
    ruleStatus: str | None = Field(default=None, description="The budget rule status. Read-only.")


class SDBudgetRuleDetails(BaseModel):  # Object representing details of a budget rule for SD campaign
    model_config = ConfigDict(extra="ignore")

    budgetIncreaseBy: SDBudgetIncreaseBy | None = Field(default=None)
    duration: SDRuleDuration | None = Field(default=None)
    name: str | None = Field(
        default=None, max_length=355, description="The budget rule name. Required to be unique within a campaign."
    )
    performanceMeasureCondition: SDPerformanceMeasureCondition | None = Field(default=None)
    recurrence: SDRecurrence | None = Field(default=None)
    ruleType: SDRuleType | None = Field(default=None)


class SDRuleType(
    StrEnum
):  # The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria.
    """The type of budget rule. SCHEDULE: A budget rule based on a start and end date. PERFORMANCE: A budget rule based on advertising performance criteria."""

    SCHEDULE = "SCHEDULE"
    PERFORMANCE = "PERFORMANCE"


class SDBudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="ignore")

    type: SDBudgetChangeType
    value: float = Field(description="The budget value.")


class SDBudgetRuleState(StrEnum):  # The budget rule state.
    """The budget rule state."""

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class SDTimeOfDay(BaseModel):
    model_config = ConfigDict(extra="ignore")

    endTime: str | None = Field(
        default=None,
        description="The end time of intra-day budget rule window in the format 'hh:mm:ss'. Required to be greater than start-time.",
    )
    startTime: str | None = Field(
        default=None, description="The start time of intra-day budget rule window in the format 'hh:mm:ss'"
    )


__all__ = [
    "SDAssociatedBudgetRuleResponse",
    "SDAssociatedCampaign",
    "SDBudgetChangeType",
    "SDBudgetIncreaseBy",
    "SDBudgetRule",
    "SDBudgetRuleDetails",
    "SDBudgetRuleResponse",
    "SDBudgetRuleState",
    "SDComparisonOperator",
    "SDCreateAssociatedBudgetRulesRequest",
    "SDCreateAssociatedBudgetRulesResponse",
    "SDCreateBudgetRulesRequest",
    "SDCreateBudgetRulesResponse",
    "SDDateRangeTypeRuleDuration",
    "SDDayOfWeek",
    "SDDisassociateAssociatedBudgetRuleResponse",
    "SDEventTypeRuleDuration",
    "SDGetAssociatedCampaignsResponse",
    "SDGetBudgetRuleResponse",
    "SDGetBudgetRulesForAdvertiserResponse",
    "SDListAssociatedBudgetRulesResponse",
    "SDPerformanceMeasureCondition",
    "SDPerformanceMetric",
    "SDRecurrence",
    "SDRecurrenceType",
    "SDRuleDuration",
    "SDRuleType",
    "SDTimeOfDay",
    "SDUpdateBudgetRulesRequest",
    "SDUpdateBudgetRulesResponse",
]
