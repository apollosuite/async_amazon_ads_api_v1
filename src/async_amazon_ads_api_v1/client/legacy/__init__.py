"""非标准 API 客户端 — 不遵循 /adsApi/v1 通用 CRUD 模式。"""

from async_amazon_ads_api_v1.client.legacy.accounts.account import Accounts
from async_amazon_ads_api_v1.client.legacy.accounts.profiles import Profiles
from async_amazon_ads_api_v1.client.legacy.accounts.terms_token import TermsToken

__all__ = [
    "Accounts",
    "Profiles",
    "TermsToken",
]
