"""SP Budget Rules resource operations — from SponsoredProducts_prod_3p.json."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sp_budget_rules import (
    SPBulkBudgetRulesAssociationRequest,
    SPBulkBudgetRulesAssociationResponse,
    SPBulkBudgetRulesDisAssociationRequest,
    SPBulkBudgetRulesDisAssociationResponse,
    SPCreateAssociatedBudgetRulesRequest,
    SPCreateAssociatedBudgetRulesResponse,
    SPCreateBudgetRulesRequest,
    SPCreateBudgetRulesResponse,
    SPDisassociateAssociatedBudgetRuleResponse,
    SPGetAssociatedCampaignsResponse,
    SPGetBudgetRuleResponse,
    SPGetBudgetRulesForAdvertiserResponse,
    SPListAssociatedBudgetRulesResponse,
    SPUpdateBudgetRulesRequest,
    SPUpdateBudgetRulesResponse,
)


class SPBudgetRules(_ResourceBase):
    """Sponsored Products Budget Rules API V4."""

    async def get_budget_rules(
        self,
    ) -> SPGetBudgetRulesForAdvertiserResponse:
        """获取广告主所有预算规则。"""
        resp = await self._request("GET", "/sp/budgetRules")
        return self._response(SPGetBudgetRulesForAdvertiserResponse, resp)

    async def create_budget_rules(
        self,
        request: SPCreateBudgetRulesRequest,
    ) -> SPCreateBudgetRulesResponse:
        """创建预算规则。"""
        resp = await self._request(
            "POST",
            "/sp/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SPCreateBudgetRulesResponse, resp)

    async def update_budget_rules(
        self,
        request: SPUpdateBudgetRulesRequest,
    ) -> SPUpdateBudgetRulesResponse:
        """更新预算规则。"""
        resp = await self._request(
            "PUT",
            "/sp/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SPUpdateBudgetRulesResponse, resp)

    async def get_budget_rule(
        self,
        budget_rule_id: str,
    ) -> SPGetBudgetRuleResponse:
        """按 ID 获取预算规则。"""
        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}")
        return self._response(SPGetBudgetRuleResponse, resp)

    async def get_budget_rule_campaigns(
        self,
        budget_rule_id: str,
    ) -> SPGetAssociatedCampaignsResponse:
        """获取规则关联的广告活动。"""
        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}/campaigns")
        return self._response(SPGetAssociatedCampaignsResponse, resp)

    async def associate_budget_rules(
        self,
        request: SPBulkBudgetRulesAssociationRequest,
    ) -> SPBulkBudgetRulesAssociationResponse:
        """关联预算规则到广告活动。"""
        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SPBulkBudgetRulesAssociationResponse, resp)

    async def disassociate_budget_rules(
        self,
        request: SPBulkBudgetRulesDisAssociationRequest,
    ) -> SPBulkBudgetRulesDisAssociationResponse:
        """解除预算规则关联。"""
        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation/delete",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SPBulkBudgetRulesDisAssociationResponse, resp)

    async def get_campaign_budget_rules(
        self,
        campaign_id: str,
    ) -> SPListAssociatedBudgetRulesResponse:
        """获取广告活动关联的预算规则列表。"""
        resp = await self._request("GET", f"/sp/campaigns/{campaign_id}/budgetRules")
        return self._response(SPListAssociatedBudgetRulesResponse, resp)

    async def associate_to_campaign(
        self,
        campaign_id: str,
        request: SPCreateAssociatedBudgetRulesRequest,
    ) -> SPCreateAssociatedBudgetRulesResponse:
        """关联预算规则到指定广告活动。"""
        resp = await self._request(
            "POST",
            f"/sp/campaigns/{campaign_id}/budgetRules",
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SPCreateAssociatedBudgetRulesResponse, resp)

    async def disassociate_from_campaign(
        self,
        campaign_id: str,
        budget_rule_id: str,
    ) -> SPDisassociateAssociatedBudgetRuleResponse:
        """解除广告活动的指定预算规则。"""
        resp = await self._request(
            "DELETE",
            f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}",
        )
        return self._response(SPDisassociateAssociatedBudgetRuleResponse, resp)
