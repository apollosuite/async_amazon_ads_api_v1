"""Accounts resource namespace — v0 Accounts APIs."""

from __future__ import annotations

from ads_api.base import ClientContext

from .advertising_accounts import AdvertisingAccounts
from .dsp_advertisers import DSPAdvertisers
from .manager_accounts import ManagerAccounts
from .profiles import Profiles
from .terms_token import TermsToken
from .test_accounts import TestAccounts
from .user_invitations import UserInvitations
from .user_permissions import UserPermissions


class Accounts:
    """Lazy Accounts resources."""

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx = ctx
        self.__advertising_accounts: AdvertisingAccounts | None = None
        self.__dsp_advertisers: DSPAdvertisers | None = None
        self.__manager_accounts: ManagerAccounts | None = None
        self.__profiles: Profiles | None = None
        self.__terms_token: TermsToken | None = None
        self.__test_accounts: TestAccounts | None = None
        self.__user_invitations: UserInvitations | None = None
        self.__user_permissions: UserPermissions | None = None

    @property
    def advertising_accounts(self) -> AdvertisingAccounts:
        if self.__advertising_accounts is None:
            self.__advertising_accounts = AdvertisingAccounts(self._ctx)
        return self.__advertising_accounts

    @property
    def dsp_advertisers(self) -> DSPAdvertisers:
        if self.__dsp_advertisers is None:
            self.__dsp_advertisers = DSPAdvertisers(self._ctx)
        return self.__dsp_advertisers

    @property
    def manager_accounts(self) -> ManagerAccounts:
        if self.__manager_accounts is None:
            self.__manager_accounts = ManagerAccounts(self._ctx)
        return self.__manager_accounts

    @property
    def profiles(self) -> Profiles:
        if self.__profiles is None:
            self.__profiles = Profiles(self._ctx)
        return self.__profiles

    @property
    def terms_token(self) -> TermsToken:
        if self.__terms_token is None:
            self.__terms_token = TermsToken(self._ctx)
        return self.__terms_token

    @property
    def test_accounts(self) -> TestAccounts:
        if self.__test_accounts is None:
            self.__test_accounts = TestAccounts(self._ctx)
        return self.__test_accounts

    @property
    def user_invitations(self) -> UserInvitations:
        if self.__user_invitations is None:
            self.__user_invitations = UserInvitations(self._ctx)
        return self.__user_invitations

    @property
    def user_permissions(self) -> UserPermissions:
        if self.__user_permissions is None:
            self.__user_permissions = UserPermissions(self._ctx)
        return self.__user_permissions
