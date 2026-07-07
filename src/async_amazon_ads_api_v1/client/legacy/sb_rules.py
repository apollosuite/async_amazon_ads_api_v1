"""SB Optimization Rules resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy.sb_rules import (
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


class SBOptimizationRules(_ResourceBase):
    """Sponsored Brands Optimization Rules API (Beta)."""

    async def list_optimization_rules(
        self,
        request: SBListOptimizationRulesRequest,
    ) -> SBListOptimizationRulesResponse:
        """获取优化规则列表。"""
        resp = await self._request(
            "POST",
            "/sb/rules/optimization/list",
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBListOptimizationRulesResponse, resp)

    async def create_optimization_rules(
        self,
        request: SBCreateOptimizationRulesRequest,
    ) -> SBCreateOptimizationRulesResponse:
        """创建优化规则。"""
        resp = await self._request(
            "POST",
            "/sb/rules/optimization",
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBCreateOptimizationRulesResponse, resp)

    async def update_optimization_rules(
        self,
        request: SBUpdateOptimizationRulesRequest,
    ) -> SBUpdateOptimizationRulesResponse:
        """更新优化规则。"""
        resp = await self._request(
            "PUT",
            "/sb/rules/optimization",
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBUpdateOptimizationRulesResponse, resp)

    async def associate_optimization_rules(
        self,
        request: SBAssociateOptimizationRulesRequest,
    ) -> SBAssociateOptimizationRulesResponse:
        """关联一个或多个优化规则。"""
        resp = await self._request(
            "POST",
            "/sb/rules/optimization/associate",
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBAssociateOptimizationRulesResponse, resp)

    async def disassociate_optimization_rules(
        self,
        request: SBDisassociateOptimizationRulesRequest,
    ) -> SBDisassociateOptimizationRulesResponse:
        """解除一个或多个优化规则的关联。"""
        resp = await self._request(
            "POST",
            "/sb/rules/optimization/disassociate",
            headers={
                "Content-Type": "application/vnd.sbruleoptimization.v4+json",
                "Accept": "application/vnd.sbruleoptimization.v4+json",
            },
            json=request.model_dump(exclude_none=True),
        )
        return self._response(SBDisassociateOptimizationRulesResponse, resp)
