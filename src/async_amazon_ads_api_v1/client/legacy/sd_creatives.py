"""SD Creatives resource operations."""

from __future__ import annotations

from typing import Any

from async_amazon_ads_api_v1._base import _ResourceBase
from async_amazon_ads_api_v1.models.legacy import SDCreativeItem, SDCreativesResponse


class SDCreatives(_ResourceBase):
    """Sponsored Display Creatives API."""

    async def create(self, creatives: list[dict[str, Any]]) -> SDCreativesResponse:
        """批量创建创意。"""
        resp = await self._request("POST", "/sd/creatives", json=creatives)

        if resp.status_code in (200, 207):
            result = SDCreativesResponse()
            for i, item in enumerate(resp.json()):
                sd_item = SDCreativeItem(
                    index=i,
                    code=item.get("code"),
                    details=item.get("details"),
                    creativeId=item.get("creativeId"),
                )
                if item.get("code") in ("200", "SUCCESS"):
                    result.success.append(sd_item)
                else:
                    result.error.append(sd_item)
            return result

        return SDCreativesResponse(
            success=[],
            error=[
                SDCreativeItem(
                    creative=c,
                    description=f"{resp.status_code}:{resp.text}",
                    index=i,
                )
                for i, c in enumerate(creatives)
            ],
        )
