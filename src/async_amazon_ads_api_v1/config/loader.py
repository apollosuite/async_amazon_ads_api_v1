"""Configuration loader — reads TOML config files with environment variable overrides."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path

from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig

ENV_MAP: dict[str, str] = {
    "client_id": "AMAZON_CLIENT_ID",
    "access_token": "AMAZON_ACCESS_TOKEN",
    "refresh_token": "AMAZON_REFRESH_TOKEN",
    "client_secret": "AMAZON_CLIENT_SECRET",
    "region": "AMAZON_REGION",
    "profile_id": "AMAZON_PROFILE_ID",
    "token_url": "AMAZON_TOKEN_URL",
    "token_cache_dir": "AMAZON_TOKEN_CACHE_DIR",
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
    """Load configuration from environment variables and a TOML file.

    Resolution order (higher wins):
    1. **Project-level TOML** — ``./config.toml`` (or *path* if provided)
    2. **Environment variables** — ``AMAZON_CLIENT_ID``, ``AMAZON_REGION``,
       ``AMAZON_ACCESS_TOKEN``, ``AMAZON_REFRESH_TOKEN``,
       ``AMAZON_CLIENT_SECRET``, ``AMAZON_PROFILE_ID``,
       ``AMAZON_TOKEN_URL``, ``AMAZON_TOKEN_CACHE_DIR``,
       ``AMAZON_ENDPOINT_NA``, ``AMAZON_ENDPOINT_EU``,
       ``AMAZON_ENDPOINT_FE``.

    The TOML file is optional — if it does not exist, configuration is
    sourced entirely from environment variables.

    Parameters
    ----------
    path : str | Path | None
        Path to the TOML configuration file. Defaults to ``./config.toml``
        in the current working directory.

    Returns
    -------
    AmazonAdsConfig
        Populated configuration instance.

    Raises
    ------
    pydantic.ValidationError
        If required fields are missing or have invalid values.
    """

    if path is None:
        path = Path.cwd() / "config.toml"
    path = Path(path)

    raw: dict[str, object] = {}
    if path.exists():
        raw = tomllib.loads(path.read_text(encoding="utf-8"))

    _merge_env(raw)

    return AmazonAdsConfig.model_validate(raw)
