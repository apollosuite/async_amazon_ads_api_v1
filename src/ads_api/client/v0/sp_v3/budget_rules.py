"""BudgetRules resource operations.

Generated from OpenAPI spec (tag: BudgetRules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sp_v3.budget_rules import (
    BulkBudgetRulesAssociationRequest,
    BulkBudgetRulesAssociationResponse,
    BulkBudgetRulesDisAssociationRequest,
    BulkBudgetRulesDisAssociationResponse,
    CreateAssociatedBudgetRulesRequest,
    CreateAssociatedBudgetRulesResponse,
    CreateBudgetRulesResponse,
    CreateSPBudgetRulesRequest,
    DisassociateAssociatedBudgetRuleResponse,
    GetSPBudgetRuleResponse,
    GetSPBudgetRulesForAdvertiserResponse,
    SPGetAssociatedCampaignsResponse,
    SPListAssociatedBudgetRulesResponse,
    UpdateBudgetRulesResponse,
    UpdateSPBudgetRulesRequest,
)


class BudgetRules(BaseResource):

    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: BulkBudgetRulesAssociationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: BulkBudgetRulesAssociationRequest, *, mode: Literal["pydantic"]
    ) -> BulkBudgetRulesAssociationResponse: ...
    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: BulkBudgetRulesAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def bulk_budget_rules_association_for_sp(
        self, body: BulkBudgetRulesAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BulkBudgetRulesAssociationResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique."""

        resp = await self._request("POST", "/sp/budgetRulesAssociation", json=self.dump_json(body))
        return self._response(BulkBudgetRulesAssociationResponse, resp, mode=mode)

    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: BulkBudgetRulesDisAssociationRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: BulkBudgetRulesDisAssociationRequest, *, mode: Literal["pydantic"]
    ) -> BulkBudgetRulesDisAssociationResponse: ...
    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: BulkBudgetRulesDisAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: BulkBudgetRulesDisAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> BulkBudgetRulesDisAssociationResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request("POST", "/sp/budgetRulesAssociation/delete", json=self.dump_json(body))
        return self._response(BulkBudgetRulesDisAssociationResponse, resp, mode=mode)

    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["pydantic"]
    ) -> CreateAssociatedBudgetRulesResponse: ...
    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: CreateAssociatedBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_associated_budget_rules_for_sp_campaigns(
        self,
        campaign_id: int,
        body: CreateAssociatedBudgetRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> CreateAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique."""

        resp = await self._request("POST", f"/sp/campaigns/{campaign_id}/budgetRules", json=self.dump_json(body))
        return self._response(CreateAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: CreateSPBudgetRulesRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: CreateSPBudgetRulesRequest, *, mode: Literal["pydantic"]
    ) -> CreateBudgetRulesResponse: ...
    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: CreateSPBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_budget_rules_for_sp_campaigns(
        self, body: CreateSPBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> CreateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request("POST", "/sp/budgetRules", json=self.dump_json(body))
        return self._response(CreateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic"]
    ) -> DisassociateAssociatedBudgetRuleResponse: ...
    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> DisassociateAssociatedBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request("DELETE", f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(DisassociateAssociatedBudgetRuleResponse, resp, mode=mode)

    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic"]
    ) -> GetSPBudgetRuleResponse: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> GetSPBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}")
        return self._response(GetSPBudgetRuleResponse, resp, mode=mode)

    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: float, *, mode: Literal["dict"] = "dict", next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: float, *, mode: Literal["pydantic"], next_token: str | None = None
    ) -> SPGetAssociatedCampaignsResponse: ...
    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: float, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_campaigns_associated_with_sp_budget_rule(
        self,
        budget_rule_id: str,
        page_size: float,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
        next_token: str | None = None,
    ) -> SPGetAssociatedCampaignsResponse | dict[str, Any] | httpx.Response:
        """"""

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SPGetAssociatedCampaignsResponse, resp, mode=mode)

    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["dict"] = "dict", next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["pydantic"], next_token: str | None = None
    ) -> GetSPBudgetRulesForAdvertiserResponse: ...
    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: float, *, mode: Literal["pydantic", "dict", "raw"] = "dict", next_token: str | None = None
    ) -> GetSPBudgetRulesForAdvertiserResponse | dict[str, Any] | httpx.Response:
        """"""

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sp/budgetRules", params=params)
        return self._response(GetSPBudgetRulesForAdvertiserResponse, resp, mode=mode)

    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic"]
    ) -> SPListAssociatedBudgetRulesResponse: ...
    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> SPListAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """**Authorized resource type**:"""

        resp = await self._request("GET", f"/sp/campaigns/{campaign_id}/budgetRules")
        return self._response(SPListAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: UpdateSPBudgetRulesRequest, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: UpdateSPBudgetRulesRequest, *, mode: Literal["pydantic"]
    ) -> UpdateBudgetRulesResponse: ...
    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: UpdateSPBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_budget_rules_for_sp_campaigns(
        self, body: UpdateSPBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> UpdateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """**Requires one of these permissions**:"""

        resp = await self._request("PUT", "/sp/budgetRules", json=self.dump_json(body))
        return self._response(UpdateBudgetRulesResponse, resp, mode=mode)
