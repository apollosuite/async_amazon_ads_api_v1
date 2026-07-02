"""Budget Rules resource operations — shared across SP / SB / SD."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import ClientContext, _ResourceBase
from async_amazon_ads_api_v1.models.legacy import (
    CreateAssociatedBudgetRulesRequest,
    CreateAssociatedBudgetRulesResponse,
    DisassociateAssociatedBudgetRuleResponse,
    SPListAssociatedBudgetRulesResponse,
)


class BudgetRules(_ResourceBase):
    """Budget Rules API V3 — 预算规则关联操作。

    SP、SB、SD 三套产品共用相同的接口结构，通过 ``product`` 参数切换 API 路径前缀。
    """

    def __init__(self, ctx: ClientContext, product: str = "sp") -> None:
        super().__init__(ctx)
        self._product = product

    async def get_associated_rules(
        self,
        campaign_id: str,
    ) -> SPListAssociatedBudgetRulesResponse:
        resp = await self._request("GET", f"/{self._product}/campaigns/{campaign_id}/budgetRules")
        return SPListAssociatedBudgetRulesResponse.model_construct(**resp.json())

    async def associate_to_campaign(
        self,
        campaign_id: str,
        budget_rule_ids: list[str],
    ) -> CreateAssociatedBudgetRulesResponse:
        body = CreateAssociatedBudgetRulesRequest(budgetRuleIds=budget_rule_ids)
        resp = await self._request(
            "POST",
            f"/{self._product}/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return CreateAssociatedBudgetRulesResponse.model_construct(**resp.json())

    async def disassociate_from_campaign(
        self,
        campaign_id: str,
        budget_rule_id: str,
    ) -> DisassociateAssociatedBudgetRuleResponse:
        resp = await self._request(
            "DELETE",
            f"/{self._product}/campaigns/{campaign_id}/budgetRules/{budget_rule_id}",
        )
        return DisassociateAssociatedBudgetRuleResponse.model_construct(**resp.json())
