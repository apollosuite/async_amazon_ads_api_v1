"""SDBudgetRules resource operations.

Generated from OpenAPI spec (tag: Budget Rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
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

    @overload
    async def get_budget_rule_by_rule_id_for_sd_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDGetBudgetRuleResponse: ...
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
    ) -> SDGetBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}")
        return self._response(SDGetBudgetRuleResponse, resp, mode=mode)

    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: SDCreateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCreateBudgetRulesResponse: ...
    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: SDCreateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_budget_rules_for_sd_campaigns(
        self, body: SDCreateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_budget_rules_for_sd_campaigns(
        self, body: SDCreateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDCreateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """ """

        resp = await self._request(
            "POST",
            "/sd/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDCreateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None
    ) -> SDGetBudgetRulesForAdvertiserResponse: ...
    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_sd_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic", next_token: str | None = None
    ) -> SDGetBudgetRulesForAdvertiserResponse | dict[str, Any] | httpx.Response:
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
        resp = await self._request("GET", "/sd/budgetRules", params=params)
        return self._response(SDGetBudgetRulesForAdvertiserResponse, resp, mode=mode)

    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: SDUpdateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDUpdateBudgetRulesResponse: ...
    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: SDUpdateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_budget_rules_for_sd_campaigns(
        self, body: SDUpdateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_budget_rules_for_sd_campaigns(
        self, body: SDUpdateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDUpdateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """ """

        resp = await self._request(
            "PUT",
            "/sd/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDUpdateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic"] = "pydantic",
        next_token: str | None = None,
    ) -> SDGetAssociatedCampaignsResponse: ...
    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaigns_associated_with_sd_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_campaigns_associated_with_sd_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
    ) -> SDGetAssociatedCampaignsResponse | dict[str, Any] | httpx.Response:
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
        resp = await self._request("GET", f"/sd/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SDGetAssociatedCampaignsResponse, resp, mode=mode)

    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDDisassociateAssociatedBudgetRuleResponse: ...
    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_associated_budget_rule_for_sd_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDDisassociateAssociatedBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        budget_rule_id : str
            The budget rule identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("DELETE", f"/sd/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SDDisassociateAssociatedBudgetRuleResponse, resp, mode=mode)

    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, body: SDCreateAssociatedBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDCreateAssociatedBudgetRulesResponse: ...
    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, body: SDCreateAssociatedBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, body: SDCreateAssociatedBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_associated_budget_rules_for_sd_campaigns(
        self,
        campaign_id: int,
        body: SDCreateAssociatedBudgetRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SDCreateAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SDCreateAssociatedBudgetRulesRequest
            API request body.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "POST",
            f"/sd/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDCreateAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDListAssociatedBudgetRulesResponse: ...
    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_associated_budget_rules_for_sd_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDListAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sd/campaigns/{campaign_id}/budgetRules")
        return self._response(SDListAssociatedBudgetRulesResponse, resp, mode=mode)
