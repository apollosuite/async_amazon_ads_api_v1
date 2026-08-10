"""SBOptimizationRules resource operations.

Generated from OpenAPI spec (tag: Optimization rules).
"""

from __future__ import annotations

from typing import Any, Literal, overload

import httpx

from async_amazon_ads_api_v1.base import BaseResource
from async_amazon_ads_api_v1.models.sbv4.sb_rules import (
    SBAssociateOptimizationRulesRequest,
    SBAssociateOptimizationRulesResponse,
    SBCreateOptimizationRulesRequest,
    SBCreateOptimizationRulesResponse,
    SBDisassociateOptimizationRulesRequest,
    SBDisassociateOptimizationRulesResponse,
    SBListOptimizationRulesRequest,
    SBListOptimizationRulesResponse,
    SBUpdateOptimizationRulesRequest,
    SBUpdateOptimizationRulesResponse,
)


class SBOptimizationRules(BaseResource):

    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: SBCreateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBCreateOptimizationRulesResponse: ...
    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: SBCreateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def create_sponsored_brands_optimization_rules(
        self, body: SBCreateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def create_sponsored_brands_optimization_rules(
        self, body: SBCreateOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBCreateOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBCreateOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: SBUpdateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBUpdateOptimizationRulesResponse: ...
    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: SBUpdateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def update_sponsored_brands_optimization_rules(
        self, body: SBUpdateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def update_sponsored_brands_optimization_rules(
        self, body: SBUpdateOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBUpdateOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "PUT",
            "/sb/rules/optimization",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBUpdateOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: SBAssociateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBAssociateOptimizationRulesResponse: ...
    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: SBAssociateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def associate_sponsored_brands_optimization_rules(
        self, body: SBAssociateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def associate_sponsored_brands_optimization_rules(
        self, body: SBAssociateOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBAssociateOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """Currently available in beta. Associate one or more optimization rules by providing combinations of entityId-ruleId that require association."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/associate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBAssociateOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: SBListOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBListOptimizationRulesResponse: ...
    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: SBListOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def list_sponsored_brands_optimization_rules(
        self, body: SBListOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def list_sponsored_brands_optimization_rules(
        self, body: SBListOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBListOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/list",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBListOptimizationRulesResponse, resp, mode=mode)

    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: SBDisassociateOptimizationRulesRequest, *, mode: Literal["pydantic"] = "pydantic"
    ) -> SBDisassociateOptimizationRulesResponse: ...
    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: SBDisassociateOptimizationRulesRequest, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: SBDisassociateOptimizationRulesRequest, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    async def disassociate_sponsored_brands_optimization_rules(
        self, body: SBDisassociateOptimizationRulesRequest, *, mode: Literal["pydantic", "dict", "raw"] = "pydantic"
    ) -> SBDisassociateOptimizationRulesResponse | dict[str, Any] | httpx.Response:
        """Currently available in beta. Disassociate one or more optimization rules by providing combinations of entityId-ruleId that require disassociation"""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/disassociate",
            json=self.dump_json(body),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBDisassociateOptimizationRulesResponse, resp, mode=mode)
