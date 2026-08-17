"""Load configuration from TOML and environment variables."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

from ads_api.config.settings import AmazonAdsConfig

ENV_MAP: dict[str, str] = {
    "client_id": "AMAZON_CLIENT_ID",
    "access_token": "AMAZON_ACCESS_TOKEN",
    "refresh_token": "AMAZON_REFRESH_TOKEN",
    "client_secret": "AMAZON_CLIENT_SECRET",
    "region": "AMAZON_REGION",
    "profile_id": "AMAZON_PROFILE_ID",
    "account_id": "AMAZON_ACCOUNT_ID",
    "token_url": "AMAZON_TOKEN_URL",
    "token_cache_dir": "AMAZON_TOKEN_CACHE_DIR",
    "cache_backend": "AMAZON_CACHE_BACKEND",
    "redis_url": "AMAZON_REDIS_URL",
}


def _merge_env(raw: dict[str, object]) -> None:
    for key, env_var in ENV_MAP.items():
        val = os.environ.get(env_var)
        if val is not None:
            raw[key] = val

    endpoints: dict[str, str] = {}
    for region_code in ("na", "eu", "fe"):
        val = os.environ.get(f"AMAZON_ENDPOINT_{region_code.upper()}")
        if val is not None:
            endpoints[region_code] = val
    if endpoints:
        raw["endpoints"] = endpoints


def from_toml(path: str | Path | None = None) -> AmazonAdsConfig:
    if path is None:
        path = Path.cwd() / "config.toml"
    path = Path(path)

    raw: dict[str, object] = {}
    if path.exists():
        raw = tomllib.loads(path.read_text(encoding="utf-8"))

    _merge_env(raw)
    return AmazonAdsConfig.model_validate(raw)
