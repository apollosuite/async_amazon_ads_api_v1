"""SD Budget Rules resource operations — from sponsoredDisplay_30_openapi.yaml."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sd_budget_rules import (
    SDCreateAssociatedBudgetRulesRequest,
    SDCreateAssociatedBudgetRulesResponse,
    SDCreateBudgetRulesRequest,
    SDCreateBudgetRulesResponse,
    SDDisassociateAssociatedBudgetRuleResponse,
    SDGetAssociatedCampaignsResponse,
    SDGetBudgetRuleResponse,
    SDGetBudgetRulesForAdvertiserResponse,
    SDListAssociatedBudgetRulesResponse,
    SDUpdateBudgetRulesRequest,
    SDUpdateBudgetRulesResponse,
)


class SDBudgetRules(_ResourceBase):
    """Sponsored Display Budget Rules API."""

    async def get_budget_rules(
        self,
    ) -> SDGetBudgetRulesForAdvertiserResponse:
        """获取广告主所有预算规则。"""
        resp = await self._request("GET", "/sd/budgetRules")
        return self._response(SDGetBudgetRulesForAdvertiserResponse, resp)

    async def create_budget_rules(
        self,
        request: SDCreateBudgetRulesRequest,
    ) -> SDCreateBudgetRulesResponse:
        """创建预算规则。"""
        resp = await self._request(
            "POST",
            "/sd/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SDCreateBudgetRulesResponse, resp)

    async def update_budget_rules(
        self,
        request: SDUpdateBudgetRulesRequest,
    ) -> SDUpdateBudgetRulesResponse:
        """更新预算规则。"""
        resp = await self._request(
            "PUT",
            "/sd/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SDUpdateBudgetRulesResponse, resp)

    async def get_budget_rule(
        self,
        budget_rule_id: str,
    ) -> SDGetBudgetRuleResponse:
        """按 ID 获取预算规则。"""
        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}")
        return self._response(SDGetBudgetRuleResponse, resp)

    async def get_budget_rule_campaigns(
        self,
        budget_rule_id: str,
    ) -> SDGetAssociatedCampaignsResponse:
        """获取规则关联的广告活动。"""
        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}/campaigns")
        return self._response(SDGetAssociatedCampaignsResponse, resp)

    async def get_campaign_budget_rules(
        self,
        campaign_id: str,
    ) -> SDListAssociatedBudgetRulesResponse:
        """获取广告活动关联的预算规则列表。"""
        resp = await self._request("GET", f"/sd/campaigns/{campaign_id}/budgetRules")
        return self._response(SDListAssociatedBudgetRulesResponse, resp)

    async def associate_to_campaign(
        self,
        campaign_id: str,
        request: SDCreateAssociatedBudgetRulesRequest,
    ) -> SDCreateAssociatedBudgetRulesResponse:
        """关联预算规则到指定广告活动。"""
        resp = await self._request(
            "POST",
            f"/sd/campaigns/{campaign_id}/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SDCreateAssociatedBudgetRulesResponse, resp)

    async def disassociate_from_campaign(
        self,
        campaign_id: str,
        budget_rule_id: str,
    ) -> SDDisassociateAssociatedBudgetRuleResponse:
        """解除广告活动的指定预算规则。"""
        resp = await self._request(
            "DELETE",
            f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}",
        )
        return self._response(SDDisassociateAssociatedBudgetRuleResponse, resp)
