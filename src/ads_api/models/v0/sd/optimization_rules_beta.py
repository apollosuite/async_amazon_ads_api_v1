"""Auto-generated models for Optimization Rules (beta) from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models.v0._shared import (
    RuleId,
)


class BaseOptimizationRule(StrictModel):
    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class BaseOptimizationRuleOut(LenientModel):
    state: str | None = Field(default=None, description="The state of the optimization rule.")
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
    state: str = Field(description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[RuleCondition] = Field(
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class OptimizationRule(LenientModel):
    state: str | None = Field(default=None, description="The state of the optimization rule.")
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

    metricName: str = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
""")
    comparisonOperator: str = Field(description="The comparison operator.")
    threshold: float = Field(
        description="The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:"
    )


class RuleConditionOut(LenientModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    metricName: str = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
""")
    comparisonOperator: str = Field(description="The comparison operator.")
    threshold: float = Field(
        description="The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:"
    )


class SingleOptimizationRuleAssociationResult(LenientModel):
    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    optimizationRuleId: RuleId | None = Field(default=None)


class UpdateOptimizationRule(StrictModel):
    state: str | None = Field(default=None, description="The state of the optimization rule.")
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
    "CreateAssociatedOptimizationRulesRequest",
    "CreateOptimizationRule",
    "OptimizationRule",
    "OptimizationRuleAssociationResponse",
    "OptimizationRuleResponse",
    "RuleCondition",
    "RuleConditionOut",
    "RuleId",
    "SingleOptimizationRuleAssociationResult",
    "UpdateOptimizationRule",
]
