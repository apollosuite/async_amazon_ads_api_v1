"""Portfolios resource operations."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import ClientContext, _ResourceBase
from async_amazon_ads_api_v1.models.legacy import (
    Portfolio,
    PortfolioListRequest,
    PortfolioListResponse,
    PortfolioUpdateItem,
    PortfolioUpdateResponse,
)


class Portfolios(_ResourceBase):
    """Portfolio Management API V3 — 投资组合管理。

    支持传入 ``ClientContext``（无需 profile_id）或完整的 ``ctx``。
    """

    def __init__(self, ctx: ClientContext) -> None:
        super().__init__(ctx)

    async def list(
        self,
        request: PortfolioListRequest | None = None,
    ) -> PortfolioListResponse:
        """获取投资组合列表。"""
        body = request.model_dump(exclude_none=True) if request else {}
        resp = await self._request("POST", "/portfolios/list", json=body)
        return PortfolioListResponse.model_construct(**resp.json())

    async def update(self, portfolios: list[Portfolio]) -> PortfolioUpdateResponse:
        """批量更新投资组合。"""
        payload = [p.model_dump(exclude_none=True) for p in portfolios]
        resp = await self._request("PUT", "/portfolios", json={"portfolios": payload})

        if resp.status_code == 207:
            data = resp.json()
            pf_data = data.get("portfolios", {})
            success = pf_data.get("success", [])
            errors = [PortfolioUpdateItem(**e) if isinstance(e, dict) else e for e in pf_data.get("error", [])]
            return PortfolioUpdateResponse(success=success, error=errors)

        return PortfolioUpdateResponse(
            success=[],
            error=[
                PortfolioUpdateItem(
                    index=i,
                    errors=[
                        {
                            "errorType": "API_ERROR",
                            "errorValue": {
                                "otherError": {
                                    "message": f"{resp.status_code}:{resp.text}",
                                    "reason": "OTHER_ERROR",
                                    "cause": {"location": "request"},
                                }
                            },
                        }
                    ],
                )
                for i in range(len(portfolios))
            ],
        )
