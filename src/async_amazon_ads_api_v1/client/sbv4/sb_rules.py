"""SBOptimizationRules resource operations.

Generated from OpenAPI spec (tag: Optimization rules).
"""

from __future__ import annotations

from async_amazon_ads_api_v1._base import BaseResource
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

    async def create_sponsored_brands_optimization_rules(
        self, body: SBCreateOptimizationRulesRequest
    ) -> SBCreateOptimizationRulesResponse:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBCreateOptimizationRulesResponse, resp)

    async def update_sponsored_brands_optimization_rules(
        self, body: SBUpdateOptimizationRulesRequest
    ) -> SBUpdateOptimizationRulesResponse:
        """Currently available in beta."""

        resp = await self._request(
            "PUT",
            "/sb/rules/optimization",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBUpdateOptimizationRulesResponse, resp)

    async def associate_sponsored_brands_optimization_rules(
        self, body: SBAssociateOptimizationRulesRequest
    ) -> SBAssociateOptimizationRulesResponse:
        """Currently available in beta. Associate one or more optimization rules by providing combinations of entityId-ruleId that require association."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/associate",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBAssociateOptimizationRulesResponse, resp)

    async def list_sponsored_brands_optimization_rules(
        self, body: SBListOptimizationRulesRequest
    ) -> SBListOptimizationRulesResponse:
        """Currently available in beta."""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/list",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBListOptimizationRulesResponse, resp)

    async def disassociate_sponsored_brands_optimization_rules(
        self, body: SBDisassociateOptimizationRulesRequest
    ) -> SBDisassociateOptimizationRulesResponse:
        """Currently available in beta. Disassociate one or more optimization rules by providing combinations of entityId-ruleId that require disassociation"""

        resp = await self._request(
            "POST",
            "/sb/rules/optimization/disassociate",
            json=body.model_dump(mode="json", exclude_none=True),
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
        )
        return self._response(SBDisassociateOptimizationRulesResponse, resp)
