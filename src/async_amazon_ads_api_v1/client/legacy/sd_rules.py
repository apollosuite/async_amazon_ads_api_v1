"""SD Optimization Rules resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy import (
    SDDisassociateOptimizationRulesRequest,
    SDDisassociateOptimizationRulesResponse,
    SDDisassociationItem,
    SDListOptimizationRulesResponse,
)


class SDOptimizationRules(_ResourceBase):
    """Sponsored Display Optimization Rules API (Beta)."""

    async def list_optimization_rules(self, ad_group_id: str) -> SDListOptimizationRulesResponse:
        """获取广告组关联的优化规则列表。"""
        resp = await self._request("GET", f"/sd/adGroups/{ad_group_id}/optimizationRules")
        return SDListOptimizationRulesResponse.model_validate_json(resp.content)

    async def disassociate_optimization_rules(
        self,
        ad_group_id: str,
        request: SDDisassociateOptimizationRulesRequest,
    ) -> SDDisassociateOptimizationRulesResponse:
        """解除广告组的优化规则关联。"""
        resp = await self._request(
            "POST",
            f"/sd/adGroups/{ad_group_id}/optimizationRules/disassociate",
            json=request.model_dump(exclude_none=True),
        )

        if resp.status_code == 207:
            data = resp.json()
            result = SDDisassociateOptimizationRulesResponse()
            for item in data.get("responses", []):
                di_item = SDDisassociationItem(
                    code=item.get("code"),
                    optimizationRuleId=item.get("optimizationRuleId"),
                    details=item.get("details", "Success"),
                )
                if item.get("code") in ("200", "SUCCESS"):
                    result.success.append(di_item)
                else:
                    result.error.append(di_item)
            return result

        return SDDisassociateOptimizationRulesResponse(
            success=[],
            error=[
                SDDisassociationItem(
                    code=str(resp.status_code),
                    optimizationRuleId=request.optimizationRuleIds[0] if request.optimizationRuleIds else None,
                    description=resp.text,
                )
            ],
        )
