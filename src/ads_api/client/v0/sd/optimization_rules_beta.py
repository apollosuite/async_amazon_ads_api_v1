"""OptimizationRulesBeta resource operations.

Generated from OpenAPI spec (tag: Optimization Rules (beta)).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from ads_api.base import BaseResource
from ads_api.models.v0.sd.optimization_rules_beta import (
    CreateAssociatedOptimizationRulesRequest,
    CreateOptimizationRule,
    OptimizationRule,
    OptimizationRuleAssociationResponse,
    OptimizationRuleResponse,
    UpdateOptimizationRule,
)


class OptimizationRulesBeta(BaseResource):

    @overload
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """* When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden."""

        resp = await self._request("POST", f"/sd/adGroups/{ad_group_id}/optimizationRules", json=self.dump_json(body))
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)

    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """* When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden."""

        resp = await self._request("POST", "/sd/optimizationRules", json=[self.dump_json(x) for x in body])
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)

    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> OptimizationRuleAssociationResponse: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "pydantic",
    ) -> OptimizationRuleAssociationResponse | dict[str, Any] | httpx.Response:
        """* Only one optimization rule can be disassociated per adGroup. This note will be removed when multiple rules are supported per adGroup."""

        resp = await self._request(
            "POST", f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate", json=self.dump_json(body)
        )
        return self._response(OptimizationRuleAssociationResponse, resp, mode=mode)

    @overload
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[OptimizationRule]: ...
    @overload
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def get_ad_groups_optimization_rule(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[OptimizationRule] | list[dict[str, Any]] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule."""

        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return self._response_list(OptimizationRule, resp, mode=mode)

    @overload
    async def get_optimization_rule(
        self, optimization_rule_id: str, *, mode: Literal["pydantic"] = "pydantic"
    ) -> OptimizationRule: ...
    @overload
    async def get_optimization_rule(self, optimization_rule_id: str, *, mode: Literal["dict"]) -> dict[str, Any]: ...
    @overload
    async def get_optimization_rule(self, optimization_rule_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_optimization_rule(
        self, optimization_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> OptimizationRule | dict[str, Any] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule."""

        resp = await self._request("GET", f"/sd/optimizationRules/{optimization_rule_id}")
        return self._response(OptimizationRule, resp, mode=mode)

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
    ) -> list[OptimizationRule]: ...
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
    ) -> list[OptimizationRule] | list[dict[str, Any]] | httpx.Response:
        """Gets an array of OptimizationRule objects for a requested set of Sponsored Display optimization rules."""

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
        return self._response_list(OptimizationRule, resp, mode=mode)

    @overload
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule], *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule], *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule], *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule], *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/optimizationRules", json=[self.dump_json(x) for x in body])
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)
