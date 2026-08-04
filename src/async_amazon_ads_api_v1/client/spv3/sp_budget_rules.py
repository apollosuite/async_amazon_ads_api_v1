"""SPBudgetRules resource operations.

Generated from OpenAPI spec (tag: BudgetRules).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.spv3.sp_budget_rules import (
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


class SPBudgetRules(BaseResource):

    async def get_sp_budget_rules_for_advertiser(
        self, page_size: int, next_token: str | None = None
    ) -> SPGetBudgetRulesForAdvertiserResponse:
        """

        Parameters
        ----------
        next_token : str
            To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.
        page_size : int
            Sets a limit on the number of results returned. Maximum limit of `pageSize` is 30.
        """

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sp/budgetRules", params=params)
        return self._response(SPGetBudgetRulesForAdvertiserResponse, resp)

    async def create_budget_rules_for_sp_campaigns(
        self, body: SPCreateBudgetRulesRequest
    ) -> SPCreateBudgetRulesResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCreateBudgetRulesResponse, resp)

    async def update_budget_rules_for_sp_campaigns(
        self, body: SPUpdateBudgetRulesRequest
    ) -> SPUpdateBudgetRulesResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sp/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPUpdateBudgetRulesResponse, resp)

    async def get_budget_rule_by_rule_id_for_sp_campaigns(self, budget_rule_id: str) -> SPGetBudgetRuleResponse:
        """Authorized resource type**:

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}")
        return self._response(SPGetBudgetRuleResponse, resp)

    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: int, next_token: str | None = None
    ) -> SPGetAssociatedCampaignsResponse:
        """

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        next_token : str
            To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.
        page_size : int
            Sets a limit on the number of results returned. Maximum limit of `pageSize` is 30.
        """

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SPGetAssociatedCampaignsResponse, resp)

    async def bulk_budget_rules_association_for_sp(
        self, body: SPBulkBudgetRulesAssociationRequest
    ) -> SPBulkBudgetRulesAssociationResponse:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique."""

        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPBulkBudgetRulesAssociationResponse, resp)

    async def bulk_budget_rules_dis_association_for_sp(
        self, body: SPBulkBudgetRulesDisAssociationRequest
    ) -> SPBulkBudgetRulesDisAssociationResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation/delete",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPBulkBudgetRulesDisAssociationResponse, resp)

    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int
    ) -> SPListAssociatedBudgetRulesResponse:
        """Authorized resource type**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        """

        resp = await self._request("GET", f"/sp/campaigns/{campaign_id}/budgetRules")
        return self._response(SPListAssociatedBudgetRulesResponse, resp)

    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: SPCreateAssociatedBudgetRulesRequest
    ) -> SPCreateAssociatedBudgetRulesResponse:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SPCreateAssociatedBudgetRulesRequest
            API request body.
        """

        resp = await self._request(
            "POST",
            f"/sp/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SPCreateAssociatedBudgetRulesResponse, resp)

    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str
    ) -> SPDisassociateAssociatedBudgetRuleResponse:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("DELETE", f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SPDisassociateAssociatedBudgetRuleResponse, resp)
