"""Amazon Ads API v0 synchronous client."""

from __future__ import annotations

from typing import Any, overload

from ads_api.base import ClientContext
from ads_api.client.v0.accounts import Accounts
from ads_api.client.v0.ads_data_manager import AdsDataManager
from ads_api.client.v0.discovery import Discovery
from ads_api.client.v0.exports import Exports
from ads_api.client.v0.portfolios import Portfolios
from ads_api.client.v0.products import Products
from ads_api.client.v0.reporting import Reporting
from ads_api.client.v0.sb_v4 import SBV4
from ads_api.client.v0.sd import SD
from ads_api.client.v0.sp_v3 import SPV3
from ads_api.config.settings import AmazonAdsConfig
from ads_api.errors import MissingConfigError


class AdsClientV0:
    """Synchronous client for Amazon Ads API v0.

    with AdsClientV0(config) as ads:
        ads.accounts.profiles.list_profiles()
        ads.reporting.reports.create_async_report(body)
        ads.portfolios.list_portfolios(body)
        ads.sp_v3.campaigns.create_sponsored_products_campaigns(body)
        ads.sd.campaigns.list_campaigns()
    """

    @overload
    def __init__(self, config: AmazonAdsConfig) -> None: ...

    @overload
    def __init__(self, *, ctx: ClientContext) -> None: ...

    def __init__(
        self,
        config: AmazonAdsConfig | None = None,
        *,
        ctx: ClientContext | None = None,
    ) -> None:
        if ctx is not None:
            self._ctx = ctx
            self._owns_ctx = False
        elif config is not None:
            self._ctx = ClientContext(config)
            self._owns_ctx = True
        else:
            raise MissingConfigError()
        self.__accounts: Accounts | None = None
        self.__reporting: Reporting | None = None
        self.__ads_data_manager: AdsDataManager | None = None
        self.__exports: Exports | None = None
        self.__discovery: Discovery | None = None
        self.__portfolios: Portfolios | None = None
        self.__products: Products | None = None
        self.__sp_v3: SPV3 | None = None
        self.__sb_v4: SBV4 | None = None
        self.__sd: SD | None = None

    def __enter__(self) -> AdsClientV0:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        if self._owns_ctx:
            self._ctx.close()

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
    def discovery(self) -> Discovery:
        if self.__discovery is None:
            self.__discovery = Discovery(self._ctx)
        return self.__discovery

    @property
    def portfolios(self) -> Portfolios:
        if self.__portfolios is None:
            self.__portfolios = Portfolios(self._ctx)
        return self.__portfolios

    @property
    def products(self) -> Products:
        if self.__products is None:
            self.__products = Products(self._ctx)
        return self.__products

    @property
    def sp_v3(self) -> SPV3:
        if self.__sp_v3 is None:
            self.__sp_v3 = SPV3(self._ctx)
        return self.__sp_v3

    @property
    def sb_v4(self) -> SBV4:
        if self.__sb_v4 is None:
            self.__sb_v4 = SBV4(self._ctx)
        return self.__sb_v4

    @property
    def sd(self) -> SD:
        if self.__sd is None:
            self.__sd = SD(self._ctx)
        return self.__sd
