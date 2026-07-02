"""SB Optimization Rules resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy import (
    SBDisassociateOptimizationRulesRequest,
    SBDisassociateOptimizationRulesResponse,
    SBDisassociationResult,
    SBListOptimizationRulesResponse,
)


class SBOptimizationRules(_ResourceBase):
    """Sponsored Brands Optimization Rules API (Beta)."""

    async def list_optimization_rules(
        self,
        campaign_id: str | None = None,
        max_results: int | None = None,
        next_token: str | None = None,
    ) -> SBListOptimizationRulesResponse:
        """获取优化规则列表。"""
        payload: dict[str, str | int] = {}
        if campaign_id:
            payload["entityFilter"] = {
                "entityType": "CAMPAIGN",
                "entityId": campaign_id,
            }
        if max_results:
            payload["maxResults"] = max_results
        if next_token:
            payload["nextToken"] = next_token

        resp = await self._request("POST", "/sb/rules/optimization/list", json=payload)
        return SBListOptimizationRulesResponse.model_construct(**resp.json())

    async def disassociate_optimization_rules(
        self,
        request: SBDisassociateOptimizationRulesRequest,
    ) -> SBDisassociateOptimizationRulesResponse:
        """解除一个或多个优化规则的关联。"""
        resp = await self._request(
            "POST",
            "/sb/rules/optimization/disassociate",
            json=request.model_dump(exclude_none=True),
        )

        if resp.status_code == 207:
            data = resp.json()
            if "optimizationRuleDisassociations" in data:
                dis_data = data["optimizationRuleDisassociations"]
                return SBDisassociateOptimizationRulesResponse(
                    success=[
                        SBDisassociationResult(**item) if isinstance(item, dict) else item
                        for item in dis_data.get("success", [])
                    ],
                    error=[
                        SBDisassociationResult(**item) if isinstance(item, dict) else item
                        for item in dis_data.get("error", [])
                    ],
                )

        return SBDisassociateOptimizationRulesResponse(
            success=[],
            error=[
                SBDisassociationResult(
                    code=str(resp.status_code),
                    description=resp.text,
                )
            ],
        )
