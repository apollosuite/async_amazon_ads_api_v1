"""Budget rule enums for old SP API."""

from __future__ import annotations

from enum import StrEnum


class SPRuleType(StrEnum):
    """The type of budget rule.

    SCHEDULE: A budget rule based on a start and end date.
    PERFORMANCE: A budget rule based on advertising performance criteria.
    """

    PERFORMANCE = "PERFORMANCE"
    SCHEDULE = "SCHEDULE"


class BudgetRuleState(StrEnum):
    """The budget rule state."""

    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"


class BudgetChangeType(StrEnum):
    """The value by which to update the budget of the budget rule."""

    PERCENT = "PERCENT"


class RecurrenceType(StrEnum):
    """The frequency of the rule application."""

    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class DayOfWeek(StrEnum):
    """The day of the week."""

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class ComparisonOperator(StrEnum):
    """The comparison operator for performance measure conditions."""

    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"


class PerformanceMetric(StrEnum):
    """The advertising performance metric."""

    ACOS = "ACOS"
    CTR = "CTR"
    CVR = "CVR"
    ROAS = "ROAS"


__all__ = [
    "BudgetChangeType",
    "BudgetRuleState",
    "ComparisonOperator",
    "DayOfWeek",
    "PerformanceMetric",
    "RecurrenceType",
    "SPRuleType",
]
