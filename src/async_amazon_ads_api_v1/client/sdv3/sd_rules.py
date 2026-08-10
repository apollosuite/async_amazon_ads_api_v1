"""SDOptimizationRules resource operations.

Generated from OpenAPI spec (tag: Optimization Rules (beta)).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sdv3.sd_rules import (
    SDCreateAssociatedOptimizationRulesRequest,
    SDCreateOptimizationRule,
    SDOptimizationRule,
    SDOptimizationRuleAssociationResponse,
    SDOptimizationRuleResponse,
    SDUpdateOptimizationRule,
)


class SDOptimizationRules(BaseResource):

    @overload
    async def list_optimization_rules(
        self,
        *,
        mode: Literal["pydantic"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        name: str | None = None,
        optimization_rule_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
    ) -> list[SDOptimizationRule]: ...
    @overload
    async def list_optimization_rules(
        self,
        *,
        mode: Literal["dict"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        name: str | None = None,
        optimization_rule_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
    ) -> list[dict[str, Any]]: ...
    @overload
    async def list_optimization_rules(
        self,
        *,
        mode: Literal["raw"],
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        name: str | None = None,
        optimization_rule_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
    ) -> httpx.Response: ...
    async def list_optimization_rules(
        self,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
        start_index: int | None = None,
        count: int | None = None,
        state_filter: str | None = None,
        name: str | None = None,
        optimization_rule_id_filter: str | None = None,
        ad_group_id_filter: str | None = None,
    ) -> list[SDOptimizationRule] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of OptimizationRule objects for a requested set of Sponsored Display optimization rules.

                Parameters
                ----------
                start_index : int
                    Optional. Sets a cursor into the requested set of optimization rules. Use in conjunction with the `count` parameter to control pagination of the returned array. 0-indexed record offset for the result set, defaults to 0.
                count : int
                    Optional. Sets the number of OptimizationRule objects in the returned array. Use in conjunction with the `startIndex` parameter to control pagination. For example, to return the first ten optimization rules set `startIndex=0` and `count=10`. To return the next ten optimization rules, set `startIndex=10` and `count=10`, and so on. Defaults to max page size.
                state_filter : str
                    Optional. The returned array is filtered to include only optimization rules with state set to one of the values in the specified comma-delimited list.
        Available values:
          - enabled
          - paused [COMING LATER]
          - enabled, paused [COMING LATER]
                name : str
                    Optional. The returned array includes only optimization rules with the specified name using an exact string match.
                optimization_rule_id_filter : str
                    Optional. The returned array is filtered to include only optimization rules associated with the optimization rule identifiers in the specified comma-delimited list.

        Maximum size limit 50.
                ad_group_id_filter : str
                    Optional. The returned array is filtered to include only optimization rules associated with the ad group identifiers in the comma-delimited list.

        Maximum size limit 50.
                mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
                    Response parsing mode.
        """

        params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "optimizationRuleIdFilter": optimization_rule_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
        }
        params = {k: v for k, v in params.items() if v is not None}
        resp = await self._request("GET", "/sd/optimizationRules", params=params)
        return self._response_list(SDOptimizationRule, resp, mode=mode)

    @overload
    async def update_optimization_rules(
        self, body: list[SDUpdateOptimizationRule], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[SDOptimizationRuleResponse]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[SDUpdateOptimizationRule], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[SDUpdateOptimizationRule], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rules(
        self, body: list[SDUpdateOptimizationRule], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[SDOptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """ """

        resp = await self._request(
            "PUT",
            "/sd/optimizationRules",
            json=[x.model_dump(mode="json", exclude_unset=True) for x in body],
        )
        return self._response_list(SDOptimizationRuleResponse, resp, mode=mode)

    @overload
    async def create_optimization_rules(
        self, body: list[SDCreateOptimizationRule], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[SDOptimizationRuleResponse]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[SDCreateOptimizationRule], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[SDCreateOptimizationRule], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rules(
        self, body: list[SDCreateOptimizationRule], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[SDOptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden."""

        resp = await self._request(
            "POST",
            "/sd/optimizationRules",
            json=[x.model_dump(mode="json", exclude_unset=True) for x in body],
        )
        return self._response_list(SDOptimizationRuleResponse, resp, mode=mode)

    @overload
    async def endpoint_3(
        self, optimization_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SDOptimizationRule: ...
    @overload
    async def endpoint_3(self, optimization_rule_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def endpoint_3(self, optimization_rule_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def endpoint_3(
        self, optimization_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SDOptimizationRule | dict[str, Any] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule.

        Parameters
        ----------
        optimization_rule_id : str
            The identifier of the requested optimization rule.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sd/optimizationRules/{optimization_rule_id}")
        return self._response(SDOptimizationRule, resp, mode=mode)

    @overload
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> list[SDOptimizationRuleResponse]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self, ad_group_id: int, body: SDCreateAssociatedOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self, ad_group_id: int, body: SDCreateAssociatedOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> list[SDOptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden.

        Parameters
        ----------
        ad_group_id : int
            The identifier of the ad group.
        body : SDCreateAssociatedOptimizationRulesRequest
            API request body.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "POST",
            f"/sd/adGroups/{ad_group_id}/optimizationRules",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response_list(SDOptimizationRuleResponse, resp, mode=mode)

    @overload
    async def endpoint_5(
        self, ad_group_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[SDOptimizationRule]: ...
    @overload
    async def endpoint_5(self, ad_group_id: int, *, mode: Literal["dict"]) -> list[dict[str, Any]]: ...
    @overload
    async def endpoint_5(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def endpoint_5(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[SDOptimizationRule] | list[dict[str, Any]] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule.

        Parameters
        ----------
        ad_group_id : int
            The identifier of the ad group.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return self._response_list(SDOptimizationRule, resp, mode=mode)

    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> SDOptimizationRuleAssociationResponse: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self, ad_group_id: int, body: SDCreateAssociatedOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self, ad_group_id: int, body: SDCreateAssociatedOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: SDCreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> SDOptimizationRuleAssociationResponse | dict[str, Any] | httpx.Response:
        """Only one optimization rule can be disassociated per adGroup. This note will be removed when multiple rules are supported per adGroup.

        Parameters
        ----------
        ad_group_id : int
            The identifier of the ad group.
        body : SDCreateAssociatedOptimizationRulesRequest
            API request body.
        mode : {'pydantic', 'dict', 'raw'}, default 'pydantic'
            Response parsing mode.
        """

        resp = await self._request(
            "POST",
            f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate",
            json=body.model_dump(mode="json", exclude_unset=True),
        )
        return self._response(SDOptimizationRuleAssociationResponse, resp, mode=mode)
