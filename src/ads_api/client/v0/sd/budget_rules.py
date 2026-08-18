"""BudgetRules resource operations.

Generated from OpenAPI spec (tag: Budget Rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.budget_rules import (
    CreateAssociatedBudgetRulesRequest,
    CreateAssociatedBudgetRulesResponse,
    CreateBudgetRulesResponse,
    CreateSDBudgetRulesRequest,
    DisassociateAssociatedBudgetRuleResponse,
    GetSDBudgetRuleResponse,
    GetSDBudgetRulesForAdvertiserResponse,
    SDGetAssociatedCampaignsResponse,
    SDListAssociatedBudgetRulesResponse,
    UpdateBudgetRulesResponse,
    UpdateSDBudgetRulesRequest,
)


class BudgetRules(BaseResource):

    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateAssociatedBudgetRulesResponse: ...
    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_associated_budget_rules_for_sd_campaigns(
        self,
        campaign_id: float,
        body: CreateAssociatedBudgetRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> CreateAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique."""

        resp = await self._request("POST", f"/sd/campaigns/{campaign_id}/budgetRules", json=self.dump_json(body))
        return self._response(CreateAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: CreateSDBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> CreateBudgetRulesResponse: ...
    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: CreateSDBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: CreateSDBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_budget_rules_for_sd_campaigns(
        self, body: CreateSDBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> CreateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("POST", "/sd/budgetRules", json=self.dump_json(body))
        return self._response(CreateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: float, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> DisassociateAssociatedBudgetRuleResponse: ...
    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: float, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: float, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: float, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> DisassociateAssociatedBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("DELETE", f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(DisassociateAssociatedBudgetRuleResponse, resp, mode=mode)

    @overload
    async def get_budget_rule_by_rule_id_for_sd_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> GetSDBudgetRuleResponse: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sd_campaigns(
        self, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sd_campaigns(
        self, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_rule_by_rule_id_for_sd_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> GetSDBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}")
        return self._response(GetSDBudgetRuleResponse, resp, mode=mode)

    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self,
        budget_rule_id: str,
        page_size: float,
        *,
        mode: Literal["pydantic"] = "pydantic",
        next_token: str | None = None,
    ) -> SDGetAssociatedCampaignsResponse: ...
    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self, budget_rule_id: str, page_size: float, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self, budget_rule_id: str, page_size: float, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_campaigns_associated_with_sd_budget_rule(
        self,
        budget_rule_id: str,
        page_size: float,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
    ) -> SDGetAssociatedCampaignsResponse | dict[str, Any] | httpx.Response:
        """"""

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SDGetAssociatedCampaignsResponse, resp, mode=mode)

    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None
    ) -> GetSDBudgetRulesForAdvertiserResponse: ...
    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic", next_token: str | None = None
    ) -> GetSDBudgetRulesForAdvertiserResponse | dict[str, Any] | httpx.Response:
        """"""

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/budgetRules", params=params)
        return self._response(GetSDBudgetRulesForAdvertiserResponse, resp, mode=mode)

    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDListAssociatedBudgetRulesResponse: ...
    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: float, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDListAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request("GET", f"/sd/campaigns/{campaign_id}/budgetRules")
        return self._response(SDListAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: UpdateSDBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> UpdateBudgetRulesResponse: ...
    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: UpdateSDBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: UpdateSDBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_budget_rules_for_sd_campaigns(
        self, body: UpdateSDBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> UpdateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/budgetRules", json=self.dump_json(body))
        return self._response(UpdateBudgetRulesResponse, resp, mode=mode)
