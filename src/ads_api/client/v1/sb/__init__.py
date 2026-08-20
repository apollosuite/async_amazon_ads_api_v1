"""SB resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_extensions import SBAdExtensions
from .ad_groups import SBAdGroups
from .ads import SBAds
from .campaigns import SBCampaigns
from .targets import SBTargets


class SB:
    """Lazy entity-specific SB resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_extensions: SBAdExtensions | None = None
        self.__ad_groups: SBAdGroups | None = None
        self.__ads: SBAds | None = None
        self.__campaigns: SBCampaigns | None = None
        self.__targets: SBTargets | None = None

    @property
    def ad_extensions(self) -> SBAdExtensions:
        if self.__ad_extensions is None:
            self.__ad_extensions = SBAdExtensions(self._ctx)
        return self.__ad_extensions

    @property
    def ad_groups(self) -> SBAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = SBAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> SBAds:
        if self.__ads is None:
            self.__ads = SBAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> SBCampaigns:
        if self.__campaigns is None:
            self.__campaigns = SBCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> SBTargets:
        if self.__targets is None:
            self.__targets = SBTargets(self._ctx)
        return self.__targets
