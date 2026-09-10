"""ST resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_groups import STAdGroups
from .ads import STAds
from .campaigns import STCampaigns
from .targets import STTargets


class ST:
    """Lazy entity-specific ST resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_groups: STAdGroups | None = None
        self.__ads: STAds | None = None
        self.__campaigns: STCampaigns | None = None
        self.__targets: STTargets | None = None

    @property
    def ad_groups(self) -> STAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = STAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> STAds:
        if self.__ads is None:
            self.__ads = STAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> STCampaigns:
        if self.__campaigns is None:
            self.__campaigns = STCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> STTargets:
        if self.__targets is None:
            self.__targets = STTargets(self._ctx)
        return self.__targets
