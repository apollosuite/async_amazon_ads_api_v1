"""Auto-generated models for Optimization Rules (beta) from Amazon Ads API schema."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SDBaseOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[SDRuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class SDBaseOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[SDRuleConditionResponse] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class SDCreateAssociatedOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    optimizationRuleIds: list[SDRuleId] | None = Field(
        default=None, min_length=1, max_length=1, description="A list of optimization rule identifiers."
    )


class SDCreateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    state: str = Field(description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[SDRuleCondition] = Field(
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )


class SDOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="allow")

    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[SDRuleConditionResponse] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: SDRuleId | None = Field(default=None)


class SDOptimizationRuleAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    responses: list[SDSingleOptimizationRuleAssociationResponse] | None = Field(
        default=None,
        max_length=1,
        description="An array of response objects. Each response object has code, details and optimizationRuleId.",
    )


class SDOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    ruleId: SDRuleId | None = Field(default=None)


class SDRuleCondition(BaseModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    model_config = ConfigDict(extra="forbid")

    metricName: str = Field(description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
|      MetricName      |ComparisonOperator  |Description|
|------------------|--------------------|-------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to `threshold`|
|COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to `threshold`|
|COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`|
""")
    comparisonOperator: str = Field(description="The comparison operator.")
    threshold: float = Field(description="""
The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:
|                  MetricName            | Minimum of `threshold` Value  |
|----------------------------------------|-----------------------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 |
|COST_PER_CLICK                          | 0.5                               |
|COST_PER_ORDER                          | 5                                 |
""")


class SDRuleConditionResponse(BaseModel):
    """A rule condition that defines the advertiser's intent for the outcome of the rule.
    Certain actions are performed by the product to achieve and maintain the rule condition."""

    model_config = ConfigDict(extra="allow")

    metricName: str | None = Field(
        default=None,
        description="""
The name of the metric.
Supported rule metrics and corresponding supported comparisonOperators:
|      MetricName      |ComparisonOperator  |Description|
|------------------|--------------------|-------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS     |              LESS_THAN_OR_EQUAL_TO             |Maximize viewable impressions while cost per 1000 views less than or equal to `threshold`|
|COST_PER_CLICK    |              LESS_THAN_OR_EQUAL_TO            |Maximize page visits while cost per click less than or equal to `threshold`|
|COST_PER_ORDER    |              LESS_THAN_OR_EQUAL_TO            |Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`|
""",
    )
    comparisonOperator: str | None = Field(default=None, description="The comparison operator.")
    threshold: float | None = Field(
        default=None,
        description="""
The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table:
|                  MetricName            | Minimum of `threshold` Value  |
|----------------------------------------|-----------------------------------|
|COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS  | 1                                 |
|COST_PER_CLICK                          | 0.5                               |
|COST_PER_ORDER                          | 5                                 |
""",
    )


type SDRuleId = str  # The identifier of the optimization rule.


class SDSingleOptimizationRuleAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    optimizationRuleId: SDRuleId | None = Field(default=None)


class SDUpdateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    state: str | None = Field(default=None, description="The state of the optimization rule.")
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    ruleConditions: list[SDRuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: SDRuleId


__all__ = [
    "SDBaseOptimizationRule",
    "SDBaseOptimizationRuleResponse",
    "SDCreateAssociatedOptimizationRulesRequest",
    "SDCreateOptimizationRule",
    "SDOptimizationRule",
    "SDOptimizationRuleAssociationResponse",
    "SDOptimizationRuleResponse",
    "SDRuleCondition",
    "SDRuleConditionResponse",
    "SDRuleId",
    "SDSingleOptimizationRuleAssociationResponse",
    "SDUpdateOptimizationRule",
]
