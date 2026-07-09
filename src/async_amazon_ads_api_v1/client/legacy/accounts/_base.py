"""Shared base for Advertising Accounts API clients."""

from __future__ import annotations

from async_amazon_ads_api_v1._base import _ResourceBase


class _AccountsAPIBase(_ResourceBase):
    """Base class for Advertising Accounts API resources.

    Provides the ``Amazon-Advertising-API-ClientId`` header required
    by all endpoints in this API.
    """

    def _client_id_header(self) -> dict[str, str]:
        return {"Amazon-Advertising-API-ClientId": self._ctx.config.client_id}
