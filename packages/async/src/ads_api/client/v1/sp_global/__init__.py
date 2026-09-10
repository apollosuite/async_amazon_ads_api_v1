"""SPGlobal resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_extensions import SPGlobalAdExtensions
from .ad_groups import SPGlobalAdGroups
from .ads import SPGlobalAds
from .campaigns import SPGlobalCampaigns
from .targets import SPGlobalTargets


class SPGlobal:
    """Lazy entity-specific SPGlobal resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_extensions: SPGlobalAdExtensions | None = None
        self.__ad_groups: SPGlobalAdGroups | None = None
        self.__ads: SPGlobalAds | None = None
        self.__campaigns: SPGlobalCampaigns | None = None
        self.__targets: SPGlobalTargets | None = None

    @property
    def ad_extensions(self) -> SPGlobalAdExtensions:
        if self.__ad_extensions is None:
            self.__ad_extensions = SPGlobalAdExtensions(self._ctx)
        return self.__ad_extensions

    @property
    def ad_groups(self) -> SPGlobalAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = SPGlobalAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> SPGlobalAds:
        if self.__ads is None:
            self.__ads = SPGlobalAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> SPGlobalCampaigns:
        if self.__campaigns is None:
            self.__campaigns = SPGlobalCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> SPGlobalTargets:
        if self.__targets is None:
            self.__targets = SPGlobalTargets(self._ctx)
        return self.__targets
