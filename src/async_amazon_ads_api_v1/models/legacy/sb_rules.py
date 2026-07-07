"""SB Optimization Rules Pydantic models."""

from __future__ import annotations

import typing

from pydantic import BaseModel, ConfigDict, Field


class SBAssociateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRuleAssociations: list[SBOptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class SBAssociateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRuleAssociations: SBBulkAssociationsOptimizationRuleResponse


class SBCreateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRules: list[SBCreateOptimizationRule] = Field(min_length=1, max_length=10)


class SBCreateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRules: SBBulkCreateOptimizationRuleOperationResponse


class SBDisassociateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRuleDisassociations: list[SBOptimizationRuleToEntityMapping] = Field(min_length=1, max_length=10)


class SBDisassociateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRuleDisassociations: SBBulkDisassociationsOptimizationRuleResponse


class SBListOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    entityFilter: SBEntityFilter | None = Field(default=None)
    maxResults: int | None = Field(
        default=None,
        ge=1,
        le=100,
        description="Number of records to include in the paginated response. Defaults to max page size for given API.",
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    optimizationRuleIdFilter: SBOptimizationRuleIdFilter | None = Field(default=None)


class SBListOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    optimizationRules: list[SBOptimizationRule] = Field(min_length=1, max_length=100)
    totalCount: int | None = Field(default=None, description="The total number of entities.")


class SBUpdateOptimizationRulesRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRules: list[SBUpdateOptimizationRule] = Field(min_length=1, max_length=10)


class SBUpdateOptimizationRulesResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    optimizationRules: SBBulkUpdateOptimizationRuleOperationResponse


class SBBulkAssociationsOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    success: list[SBOptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )


class SBBulkCreateOptimizationRuleOperationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    success: list[SBCreateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBBulkDisassociationsOptimizationRuleResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    success: list[SBOptimizationRuleToEntityMappingSuccessResponseItem] | None = Field(
        default=None, min_length=1, max_length=10
    )


class SBBulkUpdateOptimizationRuleOperationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    error: list[SBOptimizationRuleFailureResponseItem] | None = Field(default=None, min_length=1, max_length=10)
    success: list[SBUpdateOptimizationRuleSuccessResponseItem] | None = Field(default=None, min_length=1, max_length=10)


class SBCreateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    conditions: list[SBRuleCondition] | None = Field(default=None, min_length=1, max_length=1)
    entityId: str | None = Field(default=None, description="Entity object identifier.")
    entityType: typing.Literal["CAMPAIGN"] = "CAMPAIGN"


class SBCreateOptimizationRuleSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    entityId: str = Field(description="Entity object identifier.")
    entityType: str
    index: int = Field(ge=0, le=10, description="The index of the entityId in the array from the request body.")
    optimizationRule: SBOptimizationRule
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class SBEntityFilter(BaseModel):  # Filter optimization rules by entityId and entityType
    model_config = ConfigDict(extra="ignore")

    entityId: str | None = Field(default=None, description="Entity object identifier.")
    entityType: typing.Literal["CAMPAIGN"] = "CAMPAIGN"


class SBOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    conditions: list[SBRuleCondition] | None = Field(default=None, min_length=1, max_length=1)
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")


class SBOptimizationRuleFailureResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    errors: list[SBOptimizationRulesError] | None = Field(
        default=None, min_length=0, max_length=100, description="A list of validation errors"
    )
    index: int = Field(
        ge=0, le=10, description="the index of the optimization rule id/entity Id in the array from the request body."
    )


class SBOptimizationRuleIdFilter(BaseModel):  # Filter optimization rules by the list of optimization rule ids.
    model_config = ConfigDict(extra="ignore")

    include: list[str] | None = Field(default=None, min_length=0, max_length=10)


class SBOptimizationRuleToEntityMapping(BaseModel):
    model_config = ConfigDict(extra="ignore")

    entityId: str = Field(description="Entity object identifier.")
    entityType: typing.Literal["CAMPAIGN"] = Field(description='Enum: "CAMPAIGN"  The type of entity passed.')
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class SBOptimizationRuleToEntityMappingSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    entityId: str = Field(description="Entity object identifier.")
    entityType: str
    index: int = Field(
        ge=0, le=10, description="The index of the entityId/optimizationId in the array from the request body."
    )
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class SBOptimizationRulesError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    code: str = Field(description="The type of the error.")
    message: str = Field(description="Human readable error message.")


class SBRuleCondition(BaseModel):
    model_config = ConfigDict(extra="ignore")

    attributeName: typing.Literal["COST_PER_CLICK"] = Field(
        description='Enum: "COST_PER_CLICK"  The name of the attribute.   Supported rule metrics and corresponding supported comparisonOperators: AttributeName ComparisonOperator Description ------------------------------------ --------------------------- ----------------------------------------------------------------------------------------- COST_PER_CLICK LESS_THAN_OR_EQUAL_TO Maximize page visits while cost per click less than or equal to threshold.'
    )
    criteria: SBValueTypeRuleCriteria


class SBUpdateOptimizationRule(BaseModel):
    model_config = ConfigDict(extra="ignore")

    conditions: list[SBRuleCondition] | None = Field(default=None, min_length=1, max_length=1)
    optimizationRuleId: str | None = Field(default=None, description="The identifier of the optimization rule.")


class SBUpdateOptimizationRuleSuccessResponseItem(BaseModel):
    model_config = ConfigDict(extra="ignore")

    index: int = Field(ge=0, le=10, description="The index of the entityId in the array from the request body.")
    optimizationRule: SBOptimizationRule
    optimizationRuleId: str = Field(description="The identifier of the optimization rule.")


class SBValueTypeRuleCriteria(BaseModel):
    model_config = ConfigDict(extra="ignore")

    comparisonOperator: typing.Literal["LESS_THAN_OR_EQUAL_TO"] = "LESS_THAN_OR_EQUAL_TO"
    value: float | None = Field(default=None, description="The value of the threshold associated with the attribute.")


__all__ = [
    "SBAssociateOptimizationRulesRequest",
    "SBAssociateOptimizationRulesResponse",
    "SBBulkAssociationsOptimizationRuleResponse",
    "SBBulkCreateOptimizationRuleOperationResponse",
    "SBBulkDisassociationsOptimizationRuleResponse",
    "SBBulkUpdateOptimizationRuleOperationResponse",
    "SBCreateOptimizationRule",
    "SBCreateOptimizationRuleSuccessResponseItem",
    "SBCreateOptimizationRulesRequest",
    "SBCreateOptimizationRulesResponse",
    "SBDisassociateOptimizationRulesRequest",
    "SBDisassociateOptimizationRulesResponse",
    "SBEntityFilter",
    "SBListOptimizationRulesRequest",
    "SBListOptimizationRulesResponse",
    "SBOptimizationRule",
    "SBOptimizationRuleFailureResponseItem",
    "SBOptimizationRuleIdFilter",
    "SBOptimizationRuleToEntityMapping",
    "SBOptimizationRuleToEntityMappingSuccessResponseItem",
    "SBOptimizationRulesError",
    "SBRuleCondition",
    "SBUpdateOptimizationRule",
    "SBUpdateOptimizationRuleSuccessResponseItem",
    "SBUpdateOptimizationRulesRequest",
    "SBUpdateOptimizationRulesResponse",
    "SBValueTypeRuleCriteria",
]
