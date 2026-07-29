"""SD Optimization Rules resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.legacy.sd_rules import (
    SDCreateAssociatedOptimizationRulesRequest,
    SDCreateOptimizationRule,
    SDOptimizationRule,
    SDOptimizationRuleAssociationResponse,
    SDOptimizationRuleResponse,
    SDUpdateOptimizationRule,
)


class SDOptimizationRules(BaseResource):
    """Sponsored Display Optimization Rules API (Beta)."""

    async def list_optimization_rules(
        self,
        *,
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str = "enabled",
        name: str | None = None,
        optimization_rule_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
    ) -> list[SDOptimizationRule]:
        """获取优化规则列表。"""
        params: dict[str, Any] = {
            k: v
            for k, v in {
                "stateFilter": state_filter,
                "startIndex": start_index,
                "count": count,
                "name": name,
                "optimizationRuleIdFilter": optimization_rule_id_filter,
                "adGroupIdFilter": ad_group_id_filter,
            }.items()
            if v is not None
        }
        resp = await self._request("GET", "/sd/optimizationRules", params=params)
        return self._response_list(SDOptimizationRule, resp)

    async def list_ad_group_optimization_rules(self, ad_group_id: int) -> list[SDOptimizationRule]:
        """获取广告组关联的优化规则列表。"""
        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return self._response_list(SDOptimizationRule, resp)

    async def create_optimization_rules(
        self,
        rules: list[SDCreateOptimizationRule],
    ) -> list[SDOptimizationRuleResponse]:
        """创建优化规则。"""
        resp = await self._request("POST", "/sd/optimizationRules", json=self._dump(rules))
        return self._response_list(SDOptimizationRuleResponse, resp)

    async def update_optimization_rules(
        self,
        rules: list[SDUpdateOptimizationRule],
    ) -> list[SDOptimizationRuleResponse]:
        """更新优化规则。"""
        resp = await self._request("PUT", "/sd/optimizationRules", json=self._dump(rules))
        return self._response_list(SDOptimizationRuleResponse, resp)

    async def get_optimization_rule(self, optimization_rule_id: str) -> SDOptimizationRule:
        """获取单个优化规则。"""
        resp = await self._request("GET", f"/sd/optimizationRules/{optimization_rule_id}")
        return self._response(SDOptimizationRule, resp)

    async def associate_optimization_rules(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
    ) -> list[SDOptimizationRuleResponse]:
        """关联优化规则到广告组。"""
        resp = await self._request(
            "POST",
            f"/sd/adGroups/{ad_group_id}/optimizationRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response_list(SDOptimizationRuleResponse, resp)

    async def disassociate_optimization_rules(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
    ) -> SDOptimizationRuleAssociationResponse:
        """解除广告组的优化规则关联。"""
        resp = await self._request(
            "POST",
            f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SDOptimizationRuleAssociationResponse, resp)
