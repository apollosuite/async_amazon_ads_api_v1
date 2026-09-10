"""Discovery resource namespace — v0 Discovery APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .locations import Locations
from .targetable_entities import TargetableEntities


class Discovery:
    """Lazy Discovery resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__locations: Locations | None = None
        self.__targetable_entities: TargetableEntities | None = None

    @property
    def locations(self) -> Locations:
        if self.__locations is None:
            self.__locations = Locations(self._ctx)
        return self.__locations

    @property
    def targetable_entities(self) -> TargetableEntities:
        if self.__targetable_entities is None:
            self.__targetable_entities = TargetableEntities(self._ctx)
        return self.__targetable_entities
