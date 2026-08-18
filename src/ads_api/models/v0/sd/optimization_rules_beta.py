"""Auto-generated models for Optimization Rules (beta) from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    BaseOptimizationRuleState,
    RuleConditionComparisonOperator,
    RuleConditionMetricName,
    RuleId,
)


class BaseOptimizationRule(StrictModel):
    state: BaseOptimizationRuleState | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class BaseOptimizationRuleOut(LenientModel):
    state: BaseOptimizationRuleState | str | None = Field(
        default=None, description="The state of the optimization rule."
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleConditionOut] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class CreateAssociatedOptimizationRulesRequest(StrictModel):
    optimizationRuleIds: list[RuleId] | None = Field(
        default=None, min_length=1, max_length=1, description="A list of optimization rule identifiers."
    )


class CreateOptimizationRule(StrictModel):
    state: BaseOptimizationRuleState = Field(description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] = Field(
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class OptimizationRule(LenientModel):
    state: BaseOptimizationRuleState | str | None = Field(
        default=None, description="The state of the optimization rule."
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleConditionOut] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: RuleId | None = Field(default=None)


class OptimizationRuleAssociationResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    responses: list[SingleOptimizationRuleAssociationResult] | None = Field(
        default=None,
        max_length=1,
        description="An array of response objects. Each response object has code, details and optimizationRuleId.",
    )


class OptimizationRuleResponse(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    ruleId: RuleId | None = Field(default=None)


class RuleCondition(StrictModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    metricName: RuleConditionMetricName = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
|      MetricName      |ComparisonOperator  |Description|
|------------------|--------------------|-------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to `threshold`|
|COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to `threshold`|
|COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`|
""")
    comparisonOperator: RuleConditionComparisonOperator = Field(description="The comparison operator.")
    threshold: float = Field(description="""
The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:
|                  MetricName            | Minimum of `threshold` Value  |
|----------------------------------------|-----------------------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 |
|COST_PER_CLICK                          | 0.5                               |
|COST_PER_ORDER                          | 5                                 |
""")


class RuleConditionOut(LenientModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    metricName: RuleConditionMetricName | str = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
|      MetricName      |ComparisonOperator  |Description|
|------------------|--------------------|-------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to `threshold`|
|COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to `threshold`|
|COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`|
""")
    comparisonOperator: RuleConditionComparisonOperator | str = Field(description="The comparison operator.")
    threshold: float = Field(description="""
The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:
|                  MetricName            | Minimum of `threshold` Value  |
|----------------------------------------|-----------------------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 |
|COST_PER_CLICK                          | 0.5                               |
|COST_PER_ORDER                          | 5                                 |
""")


class SingleOptimizationRuleAssociationResult(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    optimizationRuleId: RuleId | None = Field(default=None)


class UpdateOptimizationRule(StrictModel):
    state: BaseOptimizationRuleState | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: RuleId


__all__ = [
    "BaseOptimizationRule",
    "BaseOptimizationRuleOut",
    "BaseOptimizationRuleState",
    "CreateAssociatedOptimizationRulesRequest",
    "CreateOptimizationRule",
    "OptimizationRule",
    "OptimizationRuleAssociationResponse",
    "OptimizationRuleResponse",
    "RuleCondition",
    "RuleConditionComparisonOperator",
    "RuleConditionMetricName",
    "RuleConditionOut",
    "RuleId",
    "SingleOptimizationRuleAssociationResult",
    "UpdateOptimizationRule",
]
