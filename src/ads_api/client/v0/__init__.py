"""Amazon Ads API v0 async client."""

from __future__ import annotations

from typing import Any

from ads_api.base import ClientContext
from ads_api.client.v0.accounts import Accounts
from ads_api.client.v0.ads_data_manager import AdsDataManager
from ads_api.client.v0.exports import Exports
from ads_api.client.v0.reporting import Reporting
from ads_api.client.v0.sp_v3 import SPV3
from ads_api.config.settings import AmazonAdsConfig


class AdsClientV0:
    """Async client for Amazon Ads API v0.

    async with AdsClientV0(config) as ads:
        await ads.accounts.profiles.list_profiles()
        await ads.reporting.reports.create_async_report(body)
        await ads.sp_v3.campaigns.create_sponsored_products_campaigns(body)
    """

    def __init__(self, config: AmazonAdsConfig, *, ctx: ClientContext | None = None) -> None:
        self._ctx = ctx if ctx is not None else ClientContext(config)
        self._owns_ctx = ctx is None
        self.__accounts: Accounts | None = None
        self.__reporting: Reporting | None = None
        self.__ads_data_manager: AdsDataManager | None = None
        self.__exports: Exports | None = None
        self.__sp_v3: SPV3 | None = None

    async def __aenter__(self) -> AdsClientV0:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        if self._owns_ctx:
            await self._ctx.close()

    @property
    def accounts(self) -> Accounts:
        if self.__accounts is None:
            self.__accounts = Accounts(self._ctx)
        return self.__accounts

    @property
    def reporting(self) -> Reporting:
        if self.__reporting is None:
            self.__reporting = Reporting(self._ctx)
        return self.__reporting

    @property
    def ads_data_manager(self) -> AdsDataManager:
        if self.__ads_data_manager is None:
            self.__ads_data_manager = AdsDataManager(self._ctx)
        return self.__ads_data_manager

    @property
    def exports(self) -> Exports:
        if self.__exports is None:
            self.__exports = Exports(self._ctx)
        return self.__exports

    @property
    def sp_v3(self) -> SPV3:
        if self.__sp_v3 is None:
            self.__sp_v3 = SPV3(self._ctx)
        return self.__sp_v3
