"""SBBudgetRules resource operations.

Generated from OpenAPI spec (tag: Budget rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

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

    @overload
    async def create_budget_rules_for_sb_campaigns(
        self, body: SBCreateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCreateBudgetRulesResponse: ...
    @overload
    async def create_budget_rules_for_sb_campaigns(
        self, body: SBCreateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_budget_rules_for_sb_campaigns(
        self, body: SBCreateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_budget_rules_for_sb_campaigns(
        self, body: SBCreateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCreateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sb/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCreateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def update_budget_rules_for_sb_campaigns(
        self, body: SBUpdateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBUpdateBudgetRulesResponse: ...
    @overload
    async def update_budget_rules_for_sb_campaigns(
        self, body: SBUpdateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_budget_rules_for_sb_campaigns(
        self, body: SBUpdateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_budget_rules_for_sb_campaigns(
        self, body: SBUpdateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBUpdateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sb/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBUpdateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def get_sb_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None
    ) -> SBGetBudgetRulesForAdvertiserResponse: ...
    @overload
    async def get_sb_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_sb_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_sb_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic", next_token: str | None = None
    ) -> SBGetBudgetRulesForAdvertiserResponse | dict[str, Any] | httpx.Response:
        """

        Parameters
        ----------
        next_token : str
            To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.
        page_size : int
            Sets a limit on the number of results returned. Maximum limit of `pageSize` is 30.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sb/budgetRules", params=params)
        return self._response(SBGetBudgetRulesForAdvertiserResponse, resp, mode=mode)

    @overload
    async def get_budget_rule_by_rule_id_for_sb_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBGetBudgetRuleResponse: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sb_campaigns(
        self, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sb_campaigns(
        self, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_rule_by_rule_id_for_sb_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBGetBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}")
        return self._response(SBGetBudgetRuleResponse, resp, mode=mode)

    @overload
    async def create_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, body: SBCreateAssociatedBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCreateAssociatedBudgetRulesResponse: ...
    @overload
    async def create_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, body: SBCreateAssociatedBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, body: SBCreateAssociatedBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_associated_budget_rules_for_sb_campaigns(
        self,
        campaign_id: int,
        body: SBCreateAssociatedBudgetRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SBCreateAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SBCreateAssociatedBudgetRulesRequest
            API request body.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "POST",
            f"/sb/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(mode="json", exclude_none=True),
        )
        return self._response(SBCreateAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def list_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBListAssociatedBudgetRulesResponse: ...
    @overload
    async def list_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_associated_budget_rules_for_sb_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBListAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sb/campaigns/{campaign_id}/budgetRules")
        return self._response(SBListAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def get_campaigns_associated_with_sb_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic"] = "pydantic",
        next_token: str | None = None,
    ) -> SBGetAssociatedCampaignsResponse: ...
    @overload
    async def get_campaigns_associated_with_sb_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaigns_associated_with_sb_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_campaigns_associated_with_sb_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
    ) -> SBGetAssociatedCampaignsResponse | dict[str, Any] | httpx.Response:
        """

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        next_token : str
            To retrieve the next page of results, call the same operation and specify this token in the request. If the `nextToken` field is empty, there are no further results.
        page_size : int
            Sets a limit on the number of results returned. Maximum limit of `pageSize` is 30.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        params = {
            "nextToken": next_token,
            "pageSize": page_size,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", f"/sb/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SBGetAssociatedCampaignsResponse, resp, mode=mode)

    @overload
    async def disassociate_associated_budget_rule_for_sb_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBDisassociateAssociatedBudgetRuleResponse: ...
    @overload
    async def disassociate_associated_budget_rule_for_sb_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_associated_budget_rule_for_sb_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_associated_budget_rule_for_sb_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBDisassociateAssociatedBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        budget_rule_id : str
            The budget rule identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("DELETE", f"/sb/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SBDisassociateAssociatedBudgetRuleResponse, resp, mode=mode)
