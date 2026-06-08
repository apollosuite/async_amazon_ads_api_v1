"""Client configuration — regions and auth."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import time
from enum import StrEnum
from pathlib import Path

import httpx

AMAZON_TOKEN_URL = "https://api.amazon.com/auth/o2/token"

ENDPOINT_MAP: dict[str, str] = {
    "na": "https://advertising-api.amazon.com",
    "eu": "https://advertising-api-eu.amazon.com",
    "fe": "https://advertising-api-fe.amazon.com",
}


class Region(StrEnum):
    """Amazon Ads API region identifiers."""

    NA = "na"
    EU = "eu"
    FE = "fe"


class AmazonAdsConfig:
    """Holds authentication and client-level settings.

    Parameters
    ----------
    endpoints : dict[str, str] | None
        Optional mapping of region values (``"na"``, ``"eu"``, ``"fe"``)
        to custom base URLs. Overrides the default endpoint for the
        selected *region* (useful for local mock servers).
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
    token_cache_dir : str | Path | None
        Directory for persistent token cache across script invocations.
        If set, the access token is written to disk after each refresh and
        reused by subsequent processes, avoiding redundant HTTP calls.
        Defaults to ``None`` (disabled). Set via ``AMAZON_TOKEN_CACHE_DIR``
        environment variable when using ``from_env()``.
    """

    def __init__(
        self,
        *,
        endpoints: dict[str, str] | None = None,
        access_token: str | None = None,
        client_id: str = "",
        region: Region = Region.NA,
        profile_id: str | None = None,
        refresh_token: str | None = None,
        client_secret: str | None = None,
        timeout: float = 60.0,
        max_retries: int = 3,
        raw_response: bool = False,
        token_cache_dir: str | Path | None = None,
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

        self.region = region
        self.base_url = ENDPOINT_MAP[region.value] if endpoints is None else endpoints[region.value]
        self.access_token = access_token
        self.client_id = client_id
        self.profile_id = profile_id
        self.refresh_token = refresh_token
        self.client_secret = client_secret
        self.timeout = timeout
        self.max_retries = max_retries
        self.raw_response = raw_response
        self.token_cache_dir = Path(token_cache_dir) if token_cache_dir else None
        self._token_refresh_lock: asyncio.Lock | None = None
        self._token_expires_at: float | None = None

    async def refresh_access_token(self) -> str:
        """Exchange the refresh token for a new access token.

        Uses ``refresh_token`` + ``client_secret`` to call the Amazon LWA
        token endpoint and updates ``access_token`` in-place.

        The token is cached in memory for the lifetime of this object, and
        optionally persisted to disk when *token_cache_dir* is configured so
        that subsequent script invocations can reuse it without an HTTP call.

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
        if self._is_token_valid():
            return self.access_token  # type: ignore[return-value]
        if self._token_refresh_lock is None:
            self._token_refresh_lock = asyncio.Lock()
        async with self._token_refresh_lock:
            if self._is_token_valid():
                return self.access_token  # type: ignore[return-value]
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
                expires_in = data.get("expires_in", 3600)
                self._token_expires_at = time.time() + expires_in - 60
                if "refresh_token" in data:
                    self.refresh_token = data["refresh_token"]
            self._write_token_cache()
        return self.access_token

    def _is_token_valid(self) -> bool:
        """Return ``True`` if a cached access token is still within its expiry window."""
        if self.access_token is not None and self._token_expires_at is not None:
            if time.time() < self._token_expires_at:
                return True
        self._load_token_cache()
        return (
            self.access_token is not None
            and self._token_expires_at is not None
            and time.time() < self._token_expires_at
        )

    def _cache_file_path(self) -> Path | None:
        if self.token_cache_dir is None or not self.client_id or not self.refresh_token:
            return None
        key = f"{self.client_id}:{self.refresh_token}"
        digest = hashlib.sha256(key.encode()).hexdigest()[:16]
        return self.token_cache_dir / f"token_{digest}.json"

    def _write_token_cache(self) -> None:
        path = self._cache_file_path()
        if path is None or self.access_token is None or self._token_expires_at is None:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "access_token": self.access_token,
            "expires_at": self._token_expires_at,
            "refresh_token": self.refresh_token,
        }
        tmp = path.with_suffix(f".tmp.{os.getpid()}")
        try:
            tmp.write_text(json.dumps(data), encoding="utf-8")
            tmp.chmod(0o600)
            tmp.rename(path)
        finally:
            if tmp.exists():
                tmp.unlink(missing_ok=True)

    def _load_token_cache(self) -> None:
        path = self._cache_file_path()
        if path is None or not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            expires_at = data.get("expires_at")
            if expires_at is not None and data.get("access_token"):
                self.access_token = data["access_token"]
                self._token_expires_at = expires_at
        except OSError, json.JSONDecodeError, KeyError:
            pass

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
        endpoints: dict[str, str] = {}
        for r in Region:
            env_key = f"AMAZON_ENDPOINT_{r.value.upper()}"
            if env_key in os.environ:
                endpoints[r.value] = os.environ[env_key]
        profile_id = os.environ.get("AMAZON_PROFILE_ID")
        refresh_token = os.environ.get("AMAZON_REFRESH_TOKEN") or None
        client_secret = os.environ.get("AMAZON_CLIENT_SECRET") or None
        token_cache_dir = os.environ.get("AMAZON_TOKEN_CACHE_DIR") or None
        return cls(
            endpoints=endpoints or None,
            access_token=access_token,
            client_id=client_id,
            region=region,
            profile_id=profile_id,
            refresh_token=refresh_token,
            client_secret=client_secret,
            token_cache_dir=token_cache_dir,
        )
