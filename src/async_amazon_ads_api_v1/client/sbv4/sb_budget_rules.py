"""SBBudgetRules resource operations.

Generated from OpenAPI spec (tag: Budget rules).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sbv4.sb_budget_rules import (
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


class SBBudgetRules(BaseResource):

    async def create_budget_rules_for_sb_campaigns(
        self, body: SBCreateBudgetRulesRequest
    ) -> SBCreateBudgetRulesResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sb/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBCreateBudgetRulesResponse, resp)

    async def update_budget_rules_for_sb_campaigns(
        self, body: SBUpdateBudgetRulesRequest
    ) -> SBUpdateBudgetRulesResponse:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sb/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBUpdateBudgetRulesResponse, resp)

    async def get_sb_budget_rules_for_advertiser(
        self, page_size: int, next_token: str | None = None
    ) -> SBGetBudgetRulesForAdvertiserResponse:
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
        resp = await self._request("GET", "/sb/budgetRules", params=params)
        return self._response(SBGetBudgetRulesForAdvertiserResponse, resp)

    async def get_budget_rule_by_rule_id_for_sb_campaigns(self, budget_rule_id: str) -> SBGetBudgetRuleResponse:
        """Requires one of these permissions**:

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}")
        return self._response(SBGetBudgetRuleResponse, resp)

    async def create_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, body: SBCreateAssociatedBudgetRulesRequest
    ) -> SBCreateAssociatedBudgetRulesResponse:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SBCreateAssociatedBudgetRulesRequest
            API request body.
        """

        resp = await self._request(
            "POST",
            f"/sb/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SBCreateAssociatedBudgetRulesResponse, resp)

    async def list_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int
    ) -> SBListAssociatedBudgetRulesResponse:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        """

        resp = await self._request("GET", f"/sb/campaigns/{campaign_id}/budgetRules")
        return self._response(SBListAssociatedBudgetRulesResponse, resp)

    async def get_campaigns_associated_with_sb_budget_rule(
        self, budget_rule_id: str, page_size: int, next_token: str | None = None
    ) -> SBGetAssociatedCampaignsResponse:
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
        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SBGetAssociatedCampaignsResponse, resp)

    async def disassociate_associated_budget_rule_for_sb_campaigns(
        self, campaign_id: int, budget_rule_id: str
    ) -> SBDisassociateAssociatedBudgetRuleResponse:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("DELETE", f"/sb/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SBDisassociateAssociatedBudgetRuleResponse, resp)
