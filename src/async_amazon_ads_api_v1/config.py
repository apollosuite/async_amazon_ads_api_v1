"""Client configuration — regions and auth."""

from __future__ import annotations

import asyncio
import os
from enum import StrEnum

import httpx

AMAZON_TOKEN_URL = "https://api.amazon.com/auth/o2/token"

_REGION_ENDPOINTS: dict[str, str] = {
    "na": "https://advertising-api.amazon.com",
    "eu": "https://advertising-api-eu.amazon.com",
    "fe": "https://advertising-api-fe.amazon.com",
}


class Region(StrEnum):
    """Amazon Ads API region identifiers.

    Each region resolves to a default production endpoint, but the
    mapping can be overridden at runtime (e.g. for local mock servers)
    via :meth:`set_endpoint`.
    """

    NA = "na"
    EU = "eu"
    FE = "fe"

    def resolve(self) -> str:
        """Return the effective API base URL for this region."""
        return _REGION_ENDPOINTS[self.value]

    @classmethod
    def set_endpoint(cls, region: Region, url: str) -> None:
        """Override the base URL that *region* resolves to."""
        if not url:
            raise ValueError("url must be a non-empty string")
        _REGION_ENDPOINTS[region.value] = url


class AmazonAdsConfig:
    """Holds authentication and client-level settings.

    Parameters
    ----------
    access_token : str | None
        OAuth 2.0 bearer token. If not provided, ``refresh_token`` and
        ``client_secret`` must be set to obtain one automatically.
    client_id : str
        Client identifier associated with a 'Login with Amazon' account.
        Sent as the ``Amazon-Ads-ClientId`` header.
    region : Region
        Which regional endpoint to target. Defaults to NA.
    profile_id : str | None
        Optional profile ID (for multi-profile accounts).
        Sent as the ``Amazon-Advertising-API-Scope`` header.
    refresh_token : str | None
        Refresh token for obtaining new access tokens automatically.
        Required when ``access_token`` is not provided.
    client_secret : str | None
        Client secret associated with the 'Login with Amazon' application.
        Required when ``access_token`` is not provided.
    timeout : float
        Request timeout in seconds. Defaults to 60.
    max_retries : int
        Number of automatic retries on transient errors (429 / 5xx).
    raw_response : bool
        If True, returns raw JSON dict instead of Pydantic model instances.
    """

    def __init__(
        self,
        *,
        access_token: str | None = None,
        client_id: str = "",
        region: Region = Region.NA,
        profile_id: str | None = None,
        refresh_token: str | None = None,
        client_secret: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3,
        raw_response: bool = False,
    ) -> None:
        if not client_id:
            raise ValueError("client_id is required and cannot be empty")
        if not access_token and not (refresh_token and client_secret):
            raise ValueError(
                "Either access_token or both refresh_token and client_secret must be provided"
            )
        if timeout <= 0:
            raise ValueError("timeout must be a positive number")
        if max_retries < 0:
            raise ValueError("max_retries cannot be negative")
        self.access_token = access_token
        self.client_id = client_id
        self.region = region
        self.profile_id = profile_id
        self.refresh_token = refresh_token
        self.client_secret = client_secret
        self.timeout = timeout
        self.max_retries = max_retries
        self.raw_response = raw_response
        self._token_refresh_lock: asyncio.Lock | None = None

    async def refresh_access_token(self) -> str:
        """Exchange the refresh token for a new access token.

        Uses ``refresh_token`` + ``client_secret`` to call the Amazon LWA
        token endpoint and updates ``access_token`` in-place.

        Returns
        -------
        str
            The new access token.

        Raises
        ------
        RuntimeError
            If ``refresh_token`` or ``client_secret`` are not configured.
        httpx.HTTPError
            If the token endpoint request fails.
        """
        if not self.refresh_token or not self.client_secret:
            raise RuntimeError(
                "refresh_token and client_secret must be set to refresh the access token"
            )
        if self._token_refresh_lock is None:
            self._token_refresh_lock = asyncio.Lock()
        async with self._token_refresh_lock:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    AMAZON_TOKEN_URL,
                    data={
                        "grant_type": "refresh_token",
                        "refresh_token": self.refresh_token,
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                self.access_token = data["access_token"]
                if "refresh_token" in data:
                    self.refresh_token = data["refresh_token"]
        return self.access_token

    @classmethod
    def from_env(cls) -> AmazonAdsConfig:
        access_token = os.environ.get("AMAZON_ACCESS_TOKEN") or None
        client_id = os.environ.get("AMAZON_CLIENT_ID")
        if not client_id:
            raise OSError("AMAZON_CLIENT_ID environment variable is not set")
        if not access_token:
            refresh_token = os.environ.get("AMAZON_REFRESH_TOKEN") or None
            client_secret = os.environ.get("AMAZON_CLIENT_SECRET") or None
            if not refresh_token or not client_secret:
                raise OSError(
                    "Either AMAZON_ACCESS_TOKEN or both AMAZON_REFRESH_TOKEN "
                    "and AMAZON_CLIENT_SECRET must be set"
                )
        region_str = os.environ.get("AMAZON_REGION", "na").lower()
        region_map = {"na": Region.NA, "eu": Region.EU, "fe": Region.FE}
        region = region_map.get(region_str)
        if region is None:
            raise ValueError(
                f"Unsupported AMAZON_REGION: {region_str!r}. Expected one of: {', '.join(region_map)}"
            )
        for r in Region:
            env_key = f"AMAZON_ENDPOINT_{r.value.upper()}"
            if env_key in os.environ:
                Region.set_endpoint(r, os.environ[env_key])
        profile_id = os.environ.get("AMAZON_PROFILE_ID")
        refresh_token = os.environ.get("AMAZON_REFRESH_TOKEN") or None
        client_secret = os.environ.get("AMAZON_CLIENT_SECRET") or None
        return cls(
            access_token=access_token,
            client_id=client_id,
            region=region,
            profile_id=profile_id,
            refresh_token=refresh_token,
            client_secret=client_secret,
        )
