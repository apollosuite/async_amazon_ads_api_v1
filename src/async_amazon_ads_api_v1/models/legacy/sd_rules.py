"""SD Optimization Rules Pydantic models."""

from __future__ import annotations

import typing

from pydantic import BaseModel, ConfigDict, Field


class SDCreateAssociatedOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRuleIds: list[SDRuleId] | None = Field(
        default=None, min_length=1, max_length=1, description="A list of optimization rule identifiers."
    )


class SDCreateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ruleConditions: list[SDRuleCondition] = Field(
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    state: typing.Literal["enabled", "paused [COMING LATER]"] = Field(description="The state of the optimization rule.")


class SDOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ruleConditions: list[SDRuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: SDRuleId | None = Field(default=None)
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    state: typing.Literal["enabled", "paused [COMING LATER]"] | None = Field(
        default=None, description="The state of the optimization rule."
    )


class SDOptimizationRuleAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    responses: list[SDSingleOptimizationRuleAssociationResponse] | None = Field(
        default=None,
        max_length=1,
        description="An array of response objects. Each response object has code, details and optimizationRuleId.",
    )


class SDOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    description: str | None = Field(default=None, description="A human-readable description of the response.")
    ruleId: SDRuleId | None = Field(default=None)


class SDUpdateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ruleConditions: list[SDRuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleId: SDRuleId
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    state: typing.Literal["enabled", "paused [COMING LATER]"] | None = Field(
        default=None, description="The state of the optimization rule."
    )


class SDBaseOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ruleConditions: list[SDRuleCondition] | None = Field(
        default=None,
        min_length=1,
        max_length=1,
        description="A list of rule conditions that define the advertiser's intent for the outcome of the rule. The rule uses 'AND' logic to combine every condition in this list, and will validate the combination when the rule is created or updated.",
    )
    ruleName: str | None = Field(default=None, description="The name of the optimization rule.")
    state: typing.Literal["enabled", "paused [COMING LATER]"] | None = Field(
        default=None, description="The state of the optimization rule."
    )


class SDRuleCondition(
    BaseModel
):  # A rule condition that defines the advertiser's intent for the outcome of the rule. Certain actions are performed by the product to achieve and maintain the rule condition.
    model_config = ConfigDict(extra="ignore")

    comparisonOperator: typing.Literal["LESS_THAN_OR_EQUAL_TO"] = Field(description="The comparison operator.")
    metricName: typing.Literal["COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS", "COST_PER_CLICK", "COST_PER_ORDER"] = Field(
        description="The name of the metric. Supported rule metrics and corresponding supported comparisonOperators: MetricName ComparisonOperator Description ------------------ -------------------- ------------------- COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS LESS_THAN_OR_EQUAL_TO Maximize viewable impressions while cost per 1000 views less than or equal to `threshold` COST_PER_CLICK LESS_THAN_OR_EQUAL_TO Maximize page visits while cost per click less than or equal to `threshold` COST_PER_ORDER LESS_THAN_OR_EQUAL_TO Maximize viewable impressions/page visits/conversion while cost per order less than or equal to `threshold`"
    )
    threshold: float = Field(
        description="The value of the threshold associated with the metric. The threshold values has defined minimums depending on the metric names in the following table: MetricName Minimum of `threshold` Value ---------------------------------------- ----------------------------------- COST_PER_THOUSAND_VIEWABLE_IMPRESSIONS 1 COST_PER_CLICK 0.5 COST_PER_ORDER 5"
    )


type SDRuleId = str  # The identifier of the optimization rule.


class SDSingleOptimizationRuleAssociationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str | None = Field(default=None, description="The HTTP status code of the response.")
    details: str | None = Field(default=None, description="A human-readable description of the response.")
    optimizationRuleId: SDRuleId | None = Field(default=None)


class SDListOptimizationRulesRequest(BaseModel):  # Request wrapper for GET /sd/optimizationRules.
    model_config = ConfigDict(extra="ignore")

    startIndex: int | None = Field(
        default=None,
        description="Optional. Sets a cursor into the requested set of optimization rules. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.",
    )
    count: int | None = Field(
        default=None,
        description="Optional. Sets the number of OptimizationRule objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten optimization rules set `startIndex=0` and `count=10`. To return the next ten optimization rules, set `startIndex=10` and `count=10`, and so on. Defaults to max page size.",
    )
    stateFilter: str = "enabled"
    name: str | None = Field(
        default=None,
        description="Optional. The returned array includes only optimization rules with the specified name using an exact string match.",
    )
    optimizationRuleIdFilter: str | None = Field(
        default=None,
        description="Optional. The returned array is filtered to include only optimization rules associated with the optimization rule identifiers in the specified comma-delimited list.  Maximum size limit 50.",
    )
    adGroupIdFilter: str | None = Field(
        default=None,
        description="Optional. The returned array is filtered to include only optimization rules associated with the ad group identifiers in the comma-delimited list.  Maximum size limit 50.",
    )


class SDUpdateOptimizationRulesRequest(BaseModel):  # Request wrapper for PUT /sd/optimizationRules.
    model_config = ConfigDict(extra="ignore")

    updateOptimizationRules: list[SDUpdateOptimizationRule] = Field(
        description="Updates one or more optimization rules."
    )


class SDCreateOptimizationRulesRequest(BaseModel):  # Request wrapper for POST /sd/optimizationRules.
    model_config = ConfigDict(extra="ignore")

    createOptimizationRules: list[SDCreateOptimizationRule] = Field(
        description="Creates one or more optimization rules, also known as outcome optimizations."
    )


class SDGetOptimizationRuleRequest(BaseModel):  # Request wrapper for GET /sd/optimizationRules/{optimizationRuleId}.
    model_config = ConfigDict(extra="ignore")

    optimizationRuleId: str = Field(description="The identifier of the requested optimization rule.")


class SDAssociateOptimizationRulesRequest(
    BaseModel
):  # Request wrapper for POST /sd/adGroups/{adGroupId}/optimizationRules.
    model_config = ConfigDict(extra="ignore")

    adGroupId: int = Field(description="The identifier of the ad group.")
    optimizationRuleIds: list[SDRuleId] | None = Field(
        default=None, min_length=1, max_length=1, description="A list of optimization rule identifiers."
    )


class SDListAdGroupsOptimizationRulesRequest(
    BaseModel
):  # Request wrapper for GET /sd/adGroups/{adGroupId}/optimizationRules.
    model_config = ConfigDict(extra="ignore")

    adGroupId: int = Field(description="The identifier of the ad group.")


class SDDisassociateOptimizationRulesRequest(
    BaseModel
):  # Request wrapper for POST /sd/adGroups/{adGroupId}/optimizationRules/disassociate.
    model_config = ConfigDict(extra="ignore")

    adGroupId: int = Field(description="The identifier of the ad group.")
    optimizationRuleIds: list[SDRuleId] | None = Field(
        default=None, min_length=1, max_length=1, description="A list of optimization rule identifiers."
    )


__all__ = [
    "SDBaseOptimizationRule",
    "SDCreateAssociatedOptimizationRulesRequest",
    "SDCreateOptimizationRule",
    "SDOptimizationRule",
    "SDOptimizationRuleAssociationResponse",
    "SDOptimizationRuleResponse",
    "SDRuleCondition",
    "SDRuleId",
    "SDSingleOptimizationRuleAssociationResponse",
    "SDUpdateOptimizationRule",
    "SDAssociateOptimizationRulesRequest",
    "SDCreateOptimizationRulesRequest",
    "SDDisassociateOptimizationRulesRequest",
    "SDGetOptimizationRuleRequest",
    "SDListAdGroupsOptimizationRulesRequest",
    "SDListOptimizationRulesRequest",
    "SDUpdateOptimizationRulesRequest",
]
