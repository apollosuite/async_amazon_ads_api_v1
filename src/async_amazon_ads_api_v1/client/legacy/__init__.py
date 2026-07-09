"""非标准 API 客户端 — 不遵循 /adsApi/v1 通用 CRUD 模式。"""

from async_amazon_ads_api_v1.client.legacy.accounts.account import Accounts
from async_amazon_ads_api_v1.client.legacy.accounts.profiles import Profiles
from async_amazon_ads_api_v1.client.legacy.accounts.terms_token import TermsToken
from async_amazon_ads_api_v1.client.legacy.portfolios import Portfolios
from async_amazon_ads_api_v1.client.legacy.sb_budget_rules import SBBudgetRules
from async_amazon_ads_api_v1.client.legacy.sb_rules import SBOptimizationRules
from async_amazon_ads_api_v1.client.legacy.sd_budget_rules import SDBudgetRules
from async_amazon_ads_api_v1.client.legacy.sd_creatives import SDCreatives
from async_amazon_ads_api_v1.client.legacy.sd_rules import SDOptimizationRules
from async_amazon_ads_api_v1.client.legacy.sp_budget_rules import SPBudgetRules

__all__ = [
    "Accounts",
    "Portfolios",
    "Profiles",
    "SBBudgetRules",
    "SBOptimizationRules",
    "SDBudgetRules",
    "SDCreatives",
    "SDOptimizationRules",
    "SPBudgetRules",
    "TermsToken",
]
