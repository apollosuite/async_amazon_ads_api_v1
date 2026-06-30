"""Budget rule Pydantic models for old SP API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

from .enums import (
    BudgetChangeType,
    BudgetRuleState,
    ComparisonOperator,
    DayOfWeek,
    PerformanceMetric,
    RecurrenceType,
    SPRuleType,
)


class BudgetIncreaseBy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: BudgetChangeType
    value: float  # The budget value.


class DateRangeTypeRuleDuration(BaseModel):
    """Object representing date range type rule duration."""

    model_config = ConfigDict(extra="forbid")

    startDate: str  # The start date in YYYYMMDD format.
    endDate: str | None = None  # The end date in YYYYMMDD format.


class EventTypeRuleDuration(BaseModel):
    """Object representing event type rule duration."""

    model_config = ConfigDict(extra="forbid")

    eventId: str  # The event identifier.
    endDate: str | None = None  # The event end date in YYYYMMDD format. Read-only.
    eventName: str | None = None  # The event name. Read-only.
    startDate: str | None = None  # The event start date in YYYYMMDD format. Read-only.


class RuleDuration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dateRangeTypeRuleDuration: DateRangeTypeRuleDuration | None = None
    eventTypeRuleDuration: EventTypeRuleDuration | None = None


class TimeOfDay(BaseModel):
    model_config = ConfigDict(extra="forbid")

    startTime: str | None = None  # Start time in 'hh:mm:ss' format.
    endTime: str | None = None  # End time in 'hh:mm:ss' format.


class PerformanceMeasureCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    comparisonOperator: ComparisonOperator
    metricName: PerformanceMetric
    threshold: float  # The performance threshold value.
    additionalBehavior: Any | None = None


class Recurrence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: RecurrenceType | None = None
    daysOfWeek: list[DayOfWeek] | None = None
    intraDaySchedule: list[TimeOfDay] | None = None


class SPBudgetRuleDetails(BaseModel):
    """Object representing details of a budget rule for SP campaign."""

    model_config = ConfigDict(extra="forbid")

    budgetIncreaseBy: BudgetIncreaseBy | None = None
    duration: RuleDuration | None = None
    name: str | None = None  # The budget rule name. Required to be unique within a campaign.
    performanceMeasureCondition: PerformanceMeasureCondition | None = None
    recurrence: Recurrence | None = None
    ruleType: SPRuleType | None = None


class SPBudgetRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ruleId: str  # The budget rule identifier.
    ruleDetails: SPBudgetRuleDetails | None = None
    ruleState: BudgetRuleState | None = None
    ruleStatus: str | None = None  # The budget rule status. Read-only.
    createdDate: int | None = None  # Epoch time of budget rule creation. Read-only.
    lastUpdatedDate: int | None = None  # Epoch time of budget rule update. Read-only.


class SPCampaignBudgetRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ruleId: str  # The budget rule identifier.
    ruleDetails: SPBudgetRuleDetails | None = None
    ruleState: BudgetRuleState | None = None
    ruleStatus: str | None = None  # The budget rule evaluation status. Read-only.
    createdDate: int | None = None  # Epoch time of budget rule creation. Read-only.
    lastUpdatedDate: int | None = None  # Epoch time of budget rule update. Read-only.


class SPListAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    associatedRules: list[SPCampaignBudgetRule] | None = None  # A list of associated budget rules.


class CreateAssociatedBudgetRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    budgetRuleIds: list[str]  # A list of budget rule identifiers.


class AssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    code: str | None = None  # An enumerated success or error code for machine use.
    details: str | None = None  # A human-readable description of the error, if unsuccessful.
    ruleId: str | None = None  # The budget rule identifier.


class CreateAssociatedBudgetRulesResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    responses: list[AssociatedBudgetRuleResponse] | None = None


class DisassociateAssociatedBudgetRuleResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")


class BudgetRuleError(BaseModel):
    """The Error Response Object."""

    model_config = ConfigDict(extra="forbid")

    code: str | None = None  # An enumerated error code for machine use.
    details: str | None = None  # A human-readable description of the response.


__all__ = [
    "AssociatedBudgetRuleResponse",
    "BudgetIncreaseBy",
    "BudgetRuleError",
    "CreateAssociatedBudgetRulesRequest",
    "CreateAssociatedBudgetRulesResponse",
    "DateRangeTypeRuleDuration",
    "DisassociateAssociatedBudgetRuleResponse",
    "EventTypeRuleDuration",
    "PerformanceMeasureCondition",
    "Recurrence",
    "RuleDuration",
    "SPBudgetRule",
    "SPBudgetRuleDetails",
    "SPCampaignBudgetRule",
    "SPListAssociatedBudgetRulesResponse",
    "TimeOfDay",
]
