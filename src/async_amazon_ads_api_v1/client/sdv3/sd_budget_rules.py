"""SDBudgetRules resource operations.

Generated from OpenAPI spec (tag: Budget Rules).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
from async_amazon_ads_api_v1.models.sdv3.sd_budget_rules import (
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


class SDBudgetRules(BaseResource):

    async def get_budget_rule_by_rule_id_for_sd_campaigns(self, budget_rule_id: str) -> SDGetBudgetRuleResponse:
        """

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}")
        return self._response(SDGetBudgetRuleResponse, resp)

    async def create_budget_rules_for_sd_campaigns(
        self, body: SDCreateBudgetRulesRequest
    ) -> SDCreateBudgetRulesResponse:
        """ """

        resp = await self._request(
            "POST",
            "/sd/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDCreateBudgetRulesResponse, resp)

    async def get_sd_budget_rules_for_advertiser(
        self, page_size: int, next_token: str | None = None
    ) -> SDGetBudgetRulesForAdvertiserResponse:
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
        resp = await self._request("GET", "/sd/budgetRules", params=params)
        return self._response(SDGetBudgetRulesForAdvertiserResponse, resp)

    async def update_budget_rules_for_sd_campaigns(
        self, body: SDUpdateBudgetRulesRequest
    ) -> SDUpdateBudgetRulesResponse:
        """ """

        resp = await self._request(
            "PUT",
            "/sd/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDUpdateBudgetRulesResponse, resp)

    async def get_campaigns_associated_with_sd_budget_rule(
        self, budget_rule_id: str, page_size: int, next_token: str | None = None
    ) -> SDGetAssociatedCampaignsResponse:
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
        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SDGetAssociatedCampaignsResponse, resp)

    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: int, budget_rule_id: str
    ) -> SDDisassociateAssociatedBudgetRuleResponse:
        """

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        budget_rule_id : str
            The budget rule identifier.
        """

        resp = await self._request("DELETE", f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SDDisassociateAssociatedBudgetRuleResponse, resp)

    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, body: SDCreateAssociatedBudgetRulesRequest
    ) -> SDCreateAssociatedBudgetRulesResponse:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SDCreateAssociatedBudgetRulesRequest
            API request body.
        """

        resp = await self._request(
            "POST",
            f"/sd/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(exclude_none=True),
        )
        return self._response(SDCreateAssociatedBudgetRulesResponse, resp)

    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int
    ) -> SDListAssociatedBudgetRulesResponse:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        """

        resp = await self._request("GET", f"/sd/campaigns/{campaign_id}/budgetRules")
        return self._response(SDListAssociatedBudgetRulesResponse, resp)
