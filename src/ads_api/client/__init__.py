"""Amazon Ads API async clients."""

from __future__ import annotations

from typing import Any, overload

from ads_api.base import ClientContext
from ads_api.client.v0 import AdsClientV0
from ads_api.client.v1 import AdsClientV1
from ads_api.config.settings import AmazonAdsConfig

__all__ = ["AdsClient", "AdsClientV0", "AdsClientV1"]


class AdsClient:
    """Unified async client for Amazon Ads API v0 and v1.

    v0 and v1 share one HTTP session and token. Use the version clients
    directly when you only need one API generation:

        async with AdsClient(config) as ads:
            await ads.v0.accounts.profiles.list_profiles()
            await ads.v1.sp.campaigns.create_campaign(body)
    """

    @overload
    def __init__(self, config: AmazonAdsConfig) -> None: ...

    @overload
    def __init__(self, *, ctx: ClientContext) -> None: ...

    def __init__(self, config: AmazonAdsConfig | None = None, *, ctx: ClientContext | None = None) -> None:
        if ctx is not None:
            self._ctx = ctx
            self._owns_ctx = False
        elif config is not None:
            self._ctx = ClientContext(config)
            self._owns_ctx = True
        else:
            raise ValueError("Either 'config' or 'ctx' must be provided.")
        self.__v0: AdsClientV0 | None = None
        self.__v1: AdsClientV1 | None = None

    async def __aenter__(self) -> AdsClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._owns_ctx:
            await self._ctx.close()

    @property
    def v0(self) -> AdsClientV0:
        if self.__v0 is None:
            self.__v0 = AdsClientV0(ctx=self._ctx)
        return self.__v0

    @property
    def v1(self) -> AdsClientV1:
        if self.__v1 is None:
            self.__v1 = AdsClientV1(ctx=self._ctx)
        return self.__v1
