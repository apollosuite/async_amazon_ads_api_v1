"""AdsDataManager resource namespace — v0 Ads data manager APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .audiences import Audiences
from .data_rooms import DataRooms
from .datasets import Datasets
from .identity_deletion import IdentityDeletion
from .sharing_rules import SharingRules
from .terms import Terms


class AdsDataManager:
    """Lazy AdsDataManager resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__audiences: Audiences | None = None
        self.__data_rooms: DataRooms | None = None
        self.__datasets: Datasets | None = None
        self.__identity_deletion: IdentityDeletion | None = None
        self.__sharing_rules: SharingRules | None = None
        self.__terms: Terms | None = None

    @property
    def audiences(self) -> Audiences:
        if self.__audiences is None:
            self.__audiences = Audiences(self._ctx)
        return self.__audiences

    @property
    def data_rooms(self) -> DataRooms:
        if self.__data_rooms is None:
            self.__data_rooms = DataRooms(self._ctx)
        return self.__data_rooms

    @property
    def datasets(self) -> Datasets:
        if self.__datasets is None:
            self.__datasets = Datasets(self._ctx)
        return self.__datasets

    @property
    def identity_deletion(self) -> IdentityDeletion:
        if self.__identity_deletion is None:
            self.__identity_deletion = IdentityDeletion(self._ctx)
        return self.__identity_deletion

    @property
    def sharing_rules(self) -> SharingRules:
        if self.__sharing_rules is None:
            self.__sharing_rules = SharingRules(self._ctx)
        return self.__sharing_rules

    @property
    def terms(self) -> Terms:
        if self.__terms is None:
            self.__terms = Terms(self._ctx)
        return self.__terms
