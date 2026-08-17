"""SD resource namespace — entity-specific clients."""

from __future__ import annotations

from ads_api.base import ClientContext

from .ad_groups import SDAdGroups
from .ads import SDAds
from .campaigns import SDCampaigns
from .targets import SDTargets


class SD:
    """Lazy entity-specific SD resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__ad_groups: SDAdGroups | None = None
        self.__ads: SDAds | None = None
        self.__campaigns: SDCampaigns | None = None
        self.__targets: SDTargets | None = None

    @property
    def ad_groups(self) -> SDAdGroups:
        if self.__ad_groups is None:
            self.__ad_groups = SDAdGroups(self._ctx)
        return self.__ad_groups

    @property
    def ads(self) -> SDAds:
        if self.__ads is None:
            self.__ads = SDAds(self._ctx)
        return self.__ads

    @property
    def campaigns(self) -> SDCampaigns:
        if self.__campaigns is None:
            self.__campaigns = SDCampaigns(self._ctx)
        return self.__campaigns

    @property
    def targets(self) -> SDTargets:
        if self.__targets is None:
            self.__targets = SDTargets(self._ctx)
        return self.__targets
