"""SD Optimization Rules Pydantic models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, RootModel


class SDOptimizationRule(BaseModel):
    """Individual SD optimization rule."""

    model_config = ConfigDict(extra="ignore")

    optimizationRuleId: str | None = None
    adGroupId: str | None = None
    ruleName: str | None = None
    ruleDescription: str | None = None
    ruleCondition: str | None = None
    ruleValue: float | None = None
    state: str | None = None
    creationDate: int | None = None
    lastUpdatedDate: int | None = None


SDListOptimizationRulesResponse = RootModel[list[SDOptimizationRule]]


class SDDisassociateOptimizationRulesRequest(BaseModel):
    """Request body for POST /sd/adGroups/{adGroupId}/optimizationRules/disassociate."""

    model_config = ConfigDict(extra="ignore")

    optimizationRuleIds: list[str]


class SDDisassociationItem(BaseModel):
    """Single item within the disassociation multi-status response."""

    model_config = ConfigDict(extra="ignore")

    code: str | None = None
    optimizationRuleId: str | None = None
    details: str | None = None


class SDDisassociateOptimizationRulesResponse(BaseModel):
    """Response for POST /sd/adGroups/{adGroupId}/optimizationRules/disassociate."""

    model_config = ConfigDict(extra="ignore")

    success: list[SDDisassociationItem] = []
    error: list[SDDisassociationItem] = []


__all__ = [
    "SDOptimizationRule",
    "SDListOptimizationRulesResponse",
    "SDDisassociateOptimizationRulesRequest",
    "SDDisassociationItem",
    "SDDisassociateOptimizationRulesResponse",
]
