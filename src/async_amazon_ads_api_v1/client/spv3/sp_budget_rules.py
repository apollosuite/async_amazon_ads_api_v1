"""SPBudgetRules resource operations.

Generated from OpenAPI spec (tag: BudgetRules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
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

    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic"] = "pydantic", next_token: str | None = None
    ) -> SPGetBudgetRulesForAdvertiserResponse: ...
    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_sp_budget_rules_for_advertiser(
        self, page_size: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic", next_token: str | None = None
    ) -> SPGetBudgetRulesForAdvertiserResponse | dict[str, Any] | httpx.Response:
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
        resp = await self._request("GET", "/sp/budgetRules", params=params)
        return self._response(SPGetBudgetRulesForAdvertiserResponse, resp, mode=mode)

    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: SPCreateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCreateBudgetRulesResponse: ...
    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: SPCreateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_budget_rules_for_sp_campaigns(
        self, body: SPCreateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_budget_rules_for_sp_campaigns(
        self, body: SPCreateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPCreateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SPCreateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: SPUpdateBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPUpdateBudgetRulesResponse: ...
    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: SPUpdateBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_budget_rules_for_sp_campaigns(
        self, body: SPUpdateBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_budget_rules_for_sp_campaigns(
        self, body: SPUpdateBudgetRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPUpdateBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "PUT",
            "/sp/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SPUpdateBudgetRulesResponse, resp, mode=mode)

    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPGetBudgetRuleResponse: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def get_budget_rule_by_rule_id_for_sp_campaigns(
        self, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPGetBudgetRuleResponse | dict[str, Any] | httpx.Response:
        """Authorized resource type**:

        Parameters
        ----------
        budget_rule_id : str
            The budget rule identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}")
        return self._response(SPGetBudgetRuleResponse, resp, mode=mode)

    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic"] = "pydantic",
        next_token: str | None = None,
    ) -> SPGetAssociatedCampaignsResponse: ...
    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["dict"], next_token: str | None = None
    ) -> dict[str, Any]: ...
    @overload
    async def get_campaigns_associated_with_sp_budget_rule(
        self, budget_rule_id: str, page_size: int, *, mode: Literal["raw"], next_token: str | None = None
    ) -> httpx.Response: ...
    async def get_campaigns_associated_with_sp_budget_rule(
        self,
        budget_rule_id: str,
        page_size: int,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        next_token: str | None = None,
    ) -> SPGetAssociatedCampaignsResponse | dict[str, Any] | httpx.Response:
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
        resp = await self._request("GET", f"/sp/budgetRules/{budget_rule_id}/campaigns", params=params)
        return self._response(SPGetAssociatedCampaignsResponse, resp, mode=mode)

    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: SPBulkBudgetRulesAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPBulkBudgetRulesAssociationResponse: ...
    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: SPBulkBudgetRulesAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def bulk_budget_rules_association_for_sp(
        self, body: SPBulkBudgetRulesAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def bulk_budget_rules_association_for_sp(
        self, body: SPBulkBudgetRulesAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPBulkBudgetRulesAssociationResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique."""

        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SPBulkBudgetRulesAssociationResponse, resp, mode=mode)

    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: SPBulkBudgetRulesDisAssociationRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPBulkBudgetRulesDisAssociationResponse: ...
    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: SPBulkBudgetRulesDisAssociationRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: SPBulkBudgetRulesDisAssociationRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def bulk_budget_rules_dis_association_for_sp(
        self, body: SPBulkBudgetRulesDisAssociationRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPBulkBudgetRulesDisAssociationResponse | dict[str, Any] | httpx.Response:
        """Requires one of these permissions**:"""

        resp = await self._request(
            "POST",
            "/sp/budgetRulesAssociation/delete",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SPBulkBudgetRulesDisAssociationResponse, resp, mode=mode)

    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPListAssociatedBudgetRulesResponse: ...
    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPListAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """Authorized resource type**:

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sp/campaigns/{campaign_id}/budgetRules")
        return self._response(SPListAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: SPCreateAssociatedBudgetRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPCreateAssociatedBudgetRulesResponse: ...
    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: SPCreateAssociatedBudgetRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_associated_budget_rules_for_sp_campaigns(
        self, campaign_id: int, body: SPCreateAssociatedBudgetRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_associated_budget_rules_for_sp_campaigns(
        self,
        campaign_id: int,
        body: SPCreateAssociatedBudgetRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SPCreateAssociatedBudgetRulesResponse | dict[str, Any] | httpx.Response:
        """A maximum of 250 rules can be associated to a campaign. Note that the name of each rule associated to a campaign is required to be unique.

        Parameters
        ----------
        campaign_id : int
            The campaign identifier.
        body : SPCreateAssociatedBudgetRulesRequest
            API request body.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "POST",
            f"/sp/campaigns/{campaign_id}/budgetRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SPCreateAssociatedBudgetRulesResponse, resp, mode=mode)

    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SPDisassociateAssociatedBudgetRuleResponse: ...
    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_associated_budget_rule_for_sp_campaigns(
        self, campaign_id: int, budget_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SPDisassociateAssociatedBudgetRuleResponse | dict[str, Any] | httpx.Response:
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

        resp = await self._request("DELETE", f"/sp/campaigns/{campaign_id}/budgetRules/{budget_rule_id}")
        return self._response(SPDisassociateAssociatedBudgetRuleResponse, resp, mode=mode)
