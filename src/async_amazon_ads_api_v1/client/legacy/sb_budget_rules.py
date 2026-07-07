"""SB Budget Rules resource operations — from sponsoredBrands_40_openapi.json."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sb_budget_rules import (
    SBCreateAssociatedBudgetRulesRequest,
    SBCreateAssociatedBudgetRulesResponse,
    SBCreateBudgetRulesRequest,
    SBCreateBudgetRulesResponse,
    SBDisassociateAssociatedBudgetRuleResponse,
    SBGetAssociatedCampaignsResponse,
    SBGetBudgetRuleResponse,
    SBGetBudgetRulesForAdvertiserResponse,
    SBListAssociatedBudgetRulesResponse,
    SBUpdateBudgetRulesRequest,
    SBUpdateBudgetRulesResponse,
)


class SBBudgetRules(_ResourceBase):
    """Sponsored Brands Budget Rules API."""

    async def get_budget_rules(
        self,
    ) -> SBGetBudgetRulesForAdvertiserResponse:
        """获取广告主所有预算规则。"""
        resp = await self._request("GET", "/sb/budgetRules")
        return self._response(SBGetBudgetRulesForAdvertiserResponse, resp)

    async def create_budget_rules(
        self,
        request: SBCreateBudgetRulesRequest,
    ) -> SBCreateBudgetRulesResponse:
        """创建预算规则。"""
        resp = await self._request(
            "POST",
            "/sb/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBCreateBudgetRulesResponse, resp)

    async def update_budget_rules(
        self,
        request: SBUpdateBudgetRulesRequest,
    ) -> SBUpdateBudgetRulesResponse:
        """更新预算规则。"""
        resp = await self._request(
            "PUT",
            "/sb/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBUpdateBudgetRulesResponse, resp)

    async def get_budget_rule(
        self,
        budget_rule_id: str,
    ) -> SBGetBudgetRuleResponse:
        """按 ID 获取预算规则。"""
        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}")
        return self._response(SBGetBudgetRuleResponse, resp)

    async def get_budget_rule_campaigns(
        self,
        budget_rule_id: str,
    ) -> SBGetAssociatedCampaignsResponse:
        """获取规则关联的广告活动。"""
        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}/campaigns")
        return self._response(SBGetAssociatedCampaignsResponse, resp)

    async def get_campaign_budget_rules(
        self,
        campaign_id: str,
    ) -> SBListAssociatedBudgetRulesResponse:
        """获取广告活动关联的预算规则列表。"""
        resp = await self._request("GET", f"/sb/campaigns/{campaign_id}/budgetRules")
        return self._response(SBListAssociatedBudgetRulesResponse, resp)

    async def associate_to_campaign(
        self,
        campaign_id: str,
        request: SBCreateAssociatedBudgetRulesRequest,
    ) -> SBCreateAssociatedBudgetRulesResponse:
        """关联预算规则到指定广告活动。"""
        resp = await self._request(
            "POST",
            f"/sb/campaigns/{campaign_id}/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBCreateAssociatedBudgetRulesResponse, resp)

    async def disassociate_from_campaign(
        self,
        campaign_id: str,
        budget_rule_id: str,
    ) -> SBDisassociateAssociatedBudgetRuleResponse:
        """解除广告活动的指定预算规则。"""
        resp = await self._request(
            "DELETE",
            f"/sb/campaigns/{campaign_id}/budgetRules/{budget_rule_id}",
        )
        return self._response(SBDisassociateAssociatedBudgetRuleResponse, resp)
