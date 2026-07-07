"""SD Optimization Rules resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sd_rules import (
    SDAssociateOptimizationRulesRequest,
    SDCreateOptimizationRulesRequest,
    SDDisassociateOptimizationRulesRequest,
    SDGetOptimizationRuleRequest,
    SDListAdGroupsOptimizationRulesRequest,
    SDListOptimizationRulesRequest,
    SDOptimizationRule,
    SDOptimizationRuleAssociationResponse,
    SDOptimizationRuleResponse,
    SDUpdateOptimizationRulesRequest,
)


class SDOptimizationRules(_ResourceBase):
    """Sponsored Display Optimization Rules API (Beta)."""

    async def list_optimization_rules(
        self,
        request: SDListOptimizationRulesRequest,
    ) -> list[SDOptimizationRule]:
        """获取优化规则列表。"""
        resp = await self._request(
            "GET",
            "/sd/optimizationRules",
            params=request.model_dump(exclude_none=True),
        )
        return [SDOptimizationRule.model_construct(**item) for item in resp.json()]

    async def list_ad_group_optimization_rules(
        self,
        request: SDListAdGroupsOptimizationRulesRequest,
    ) -> list[SDOptimizationRule]:
        """获取广告组关联的优化规则列表。"""
        resp = await self._request(
            "GET",
            f"/sd/adGroups/{request.adGroupId}/optimizationRules",
        )
        return [SDOptimizationRule.model_construct(**item) for item in resp.json()]

    async def create_optimization_rules(
        self,
        request: SDCreateOptimizationRulesRequest,
    ) -> list[SDOptimizationRuleResponse]:
        """创建优化规则。"""
        resp = await self._request(
            "POST",
            "/sd/optimizationRules",
            json=[i.model_dump() for i in request.createOptimizationRules],
        )
        return [SDOptimizationRuleResponse.model_construct(**item) for item in resp.json()]

    async def update_optimization_rules(
        self,
        request: SDUpdateOptimizationRulesRequest,
    ) -> list[SDOptimizationRuleResponse]:
        """更新优化规则。"""
        resp = await self._request(
            "PUT",
            "/sd/optimizationRules",
            json=request.updateOptimizationRules,
        )
        return [SDOptimizationRuleResponse.model_construct(**item) for item in resp.json()]

    async def get_optimization_rule(
        self,
        request: SDGetOptimizationRuleRequest,
    ) -> SDOptimizationRule:
        """获取单个优化规则。"""
        resp = await self._request(
            "GET",
            f"/sd/optimizationRules/{request.optimizationRuleId}",
        )
        return self._response(SDOptimizationRule, resp)

    async def associate_optimization_rules(
        self,
        request: SDAssociateOptimizationRulesRequest,
    ) -> list[SDOptimizationRuleResponse]:
        """关联优化规则到广告组。"""
        resp = await self._request(
            "POST",
            f"/sd/adGroups/{request.adGroupId}/optimizationRules",
            json=request.model_dump(exclude_none=True, exclude={"adGroupId"}),
        )
        return [SDOptimizationRuleResponse.model_construct(**item) for item in resp.json()]

    async def disassociate_optimization_rules(
        self,
        request: SDDisassociateOptimizationRulesRequest,
    ) -> SDOptimizationRuleAssociationResponse:
        """解除广告组的优化规则关联。"""
        resp = await self._request(
            "POST",
            f"/sd/adGroups/{request.adGroupId}/optimizationRules/disassociate",
            json=request.model_dump(exclude_none=True, exclude={"adGroupId"}),
        )
        return self._response(SDOptimizationRuleAssociationResponse, resp)
