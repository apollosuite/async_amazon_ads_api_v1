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
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> list[dict[str, Any]]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def associate_optimization_rules_with_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def associate_optimization_rules_with_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """* When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden."""

        resp = await self._request("POST", f"/sd/adGroups/{ad_group_id}/optimizationRules", json=self.dump_json(body))
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)

    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule] | None = None, *, mode: Literal["pydantic"]
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_optimization_rules(
        self, body: list[CreateOptimizationRule] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """* When an optimization rule is associated to an ad group, manual bids for individual targets will be overridden."""

        resp = await self._request("POST", "/sd/optimizationRules", json=self.dump_json(body))
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)

    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["dict"] = "dict",
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic"],
    ) -> OptimizationRuleAssociationResponse: ...
    @overload
    async def disassociate_optimization_rules_from_ad_group(
        self, ad_group_id: int, body: CreateAssociatedOptimizationRulesRequest | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_optimization_rules_from_ad_group(
        self,
        ad_group_id: int,
        body: CreateAssociatedOptimizationRulesRequest | None = None,
        *,
        mode: Literal["pydantic", "dict", "raw"] = "dict",
    ) -> OptimizationRuleAssociationResponse | dict[str, Any] | httpx.Response:
        """* Only one optimization rule can be disassociated per adGroup. This note will be removed when multiple rules are supported per adGroup."""

        resp = await self._request(
            "POST", f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate", json=self.dump_json(body)
        )
        return self._response(OptimizationRuleAssociationResponse, resp, mode=mode)

    @overload
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["pydantic"]
    ) -> list[OptimizationRule]: ...
    @overload
    async def get_ad_groups_optimization_rule(self, ad_group_id: int, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_ad_groups_optimization_rule(
        self, ad_group_id: int, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[OptimizationRule] | list[dict[str, Any]] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule."""

        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return self._response_list(OptimizationRule, resp, mode=mode)

    @overload
    async def get_optimization_rule(
        self, optimization_rule_id: str, *, mode: Literal["dict"] = "dict"
    ) -> dict[str, Any]: ...
    @overload
    async def get_optimization_rule(
        self, optimization_rule_id: str, *, mode: Literal["pydantic"]
    ) -> OptimizationRule: ...
    @overload
    async def get_optimization_rule(self, optimization_rule_id: str, *, mode: Literal["raw"]) -> httpx.Response: ...
    async def get_optimization_rule(
        self, optimization_rule_id: str, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> OptimizationRule | dict[str, Any] | httpx.Response:
        """Gets an OptimizationRule object for a requested Sponsored Display optimization rule."""

        resp = await self._request("GET", f"/sd/optimizationRules/{optimization_rule_id}")
        return self._response(OptimizationRule, resp, mode=mode)

    @overload
    async def list_optimization_rules(
        self,
        *,
        mode: Literal["dict"] = "dict",
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
        mode: Literal["pydantic"],
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
        mode: Literal["pydantic", "dict", "raw"] = "dict",
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
        self, body: list[UpdateOptimizationRule] | None = None, *, mode: Literal["dict"] = "dict"
    ) -> list[dict[str, Any]]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule] | None = None, *, mode: Literal["pydantic"]
    ) -> list[OptimizationRuleResponse]: ...
    @overload
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule] | None = None, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_optimization_rules(
        self, body: list[UpdateOptimizationRule] | None = None, *, mode: Literal["pydantic", "dict", "raw"] = "dict"
    ) -> list[OptimizationRuleResponse] | list[dict[str, Any]] | httpx.Response:
        """"""

        resp = await self._request("PUT", "/sd/optimizationRules", json=self.dump_json(body))
        return self._response_list(OptimizationRuleResponse, resp, mode=mode)
