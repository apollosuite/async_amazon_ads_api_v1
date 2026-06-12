# Amazon Ads SDK

Pure async Python SDK for the Amazon Advertising API — Sponsored Products / Sponsored Brands / Sponsored Display.

## 项目结构

```
.
├── scripts/
│   ├── AmazonAdsAPISPMerged_prod_3p.json   # SP OpenAPI 规范（不修改）
│   ├── AmazonAdsAPISBMerged_prod_3p.json   # SB OpenAPI 规范
│   ├── AmazonAdsAPISDMerged_prod_3p.json   # SD OpenAPI 规范
│   ├── download_spec.py                    # 下载 OpenAPI 规范
│   ├── generate_all.py                     # 一键生成所有产品模型
│   ├── generate_file_structure.py          # 通用 schema 分类器（无硬编码）
│   └── generate_models.py                  # 从 JSON Schema 生成 Pydantic 模型
├── README.md
├── AGENTS.md                               # 本文件
├── LICENSE                                 # MIT 许可证
├── pyproject.toml                          # uv 项目配置
├── uv.lock                                 # 依赖锁定
└── src/async_amazon_ads_api_v1/
    ├── __init__.py                         # 导出所有公开 API
    ├── _base.py                            # ClientContext + _ResourceBase + _ResourceSpec
    ├── errors.py                           # 共享 HTTP 错误模型 (ErrorCode, Error, ErrorsIndex ...)
    ├── py.typed                            # PEP 561 类型标记
    ├── config/
    │   ├── __init__.py
    │   ├── loader.py                       # from_toml() 配置加载
    │   ├── region.py                       # Region 枚举 + ENDPOINT_MAP
    │   ├── settings.py                     # AmazonAdsConfig / CacheBackend
    │   ├── token_cache.py                  # BaseTokenCache / FileTokenCache / RedisTokenCache
    │   └── token_manager.py               # TokenManager / TokenCredentials
    ├── models/
    │   ├── base.py
    │   ├── sp/                             # SP 模型（自动生成）
    │   ├── sb/                             # SB 模型（自动生成）
    │   └── sd/                             # SD 模型（自动生成）
    └── client/
        ├── sp/                             # SPClient + 5 资源类
        ├── sb/                             # SBClient + 11 资源类
        └── sd/                             # SDClient + 4 资源类
```

## 项目概述

核心使用 **httpx** 构建 Amazon Ads API 纯异步 SDK，支持三种广告产品。

## 核心环境要求 (CRITICAL)

- **环境管理**: **必须**使用 `uv` 进行依赖管理、虚拟环境创建及任务执行。
- **Python 版本**:
    - 最小支持版本为 **Python 3.13**。
    - **优先兼容 Python 3.13+** 及后续更高版本。
    - **禁止**考虑对 Python 3.12 及以下版本的向后兼容性。
- **特性使用**: 鼓励使用 Python 3.13+ 引入的新特性。

## 代码质量 (MUST)

- **格式化**: 必须使用 `black` 格式化代码。
- **静态检查**: 必须使用 `ruff check --fix` 移除未使用的 imports/variables。
- 保存前执行这两条命令。

## Git 提交规范

- **语言**: `git commit` 信息尽量使用**中文**。
- **术语**: 术语如 `uv`, `Python 3.14`, `asyncio`, `httpx`, `Pydantic` 等保持**英文**。
- **格式示例**: `feat: 使用 uv 同步依赖，支持 Python 3.14 特性`

## 常用命令

- 同步环境: `uv sync`
- 添加依赖: `uv add <package>`
- 执行脚本: `uv run python <script>` — **禁止**直接使用 `python3` / `python` 调用 Python
- 测试: `uv run pytest`
- Lint: `uv run ruff check --fix src/`
- 格式化: `uv run black src/ scripts/`
- 类型检查: `uv run mypy src/`

## 代码生成

模型基于 OpenAPI 规范自动生成：

```bash
uv run python scripts/generate_models.py --product sp --output-dir src/async_amazon_ads_api_v1/models/sp/
uv run python scripts/generate_models.py --product sb --output-dir src/async_amazon_ads_api_v1/models/sb/
uv run python scripts/generate_models.py --product sd --output-dir src/async_amazon_ads_api_v1/models/sd/
uv run ruff check --fix src/
uv run black src/
```

- `generate_file_structure.py` 提供通用的图分类算法，不依赖硬编码
- 每次修改上游 JSON Schema 后，重新运行生成脚本
- 枚举使用 `StrEnum`，可选字段使用 Python 3.14 `X | None` 语法

## 环境变量

```bash
AMAZON_ACCESS_TOKEN     # OAuth bearer token（必填，或使用 refresh_token 自动获取）
AMAZON_CLIENT_ID        # OAuth client ID（使用 refresh_token 时必填）
AMAZON_REFRESH_TOKEN    # OAuth refresh token（可选，用于自动续期）
AMAZON_CLIENT_SECRET    # OAuth client secret（使用 refresh_token 时必填）
AMAZON_REGION           # na | eu | fe（默认 na）
AMAZON_PROFILE_ID       # 可选，数字类型
AMAZON_TOKEN_URL        # 可选，自定义 token 端点
AMAZON_TOKEN_CACHE_DIR  # 可选，token 缓存目录
AMAZON_CACHE_BACKEND    # 可选，file | redis
AMAZON_REDIS_URL        # 可选，Redis 连接 URL（使用 redis 缓存时需要）
AMAZON_ENDPOINT_NA      # 可选，覆盖 NA 端点
AMAZON_ENDPOINT_EU      # 可选，覆盖 EU 端点
AMAZON_ENDPOINT_FE      # 可选，覆盖 FE 端点
```

## 使用示例

```python
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient, SBClient, SDClient

config = AmazonAdsConfig(access_token="...", region=Region.NA)

async with SPClient(config) as sp:
    resp = await sp.campaigns.query({"stateFilter": {"include": ["enabled"]}})
    print(resp.model_dump_json(indent=2))

async with SBClient(config) as sb:
    resp = await sb.campaigns.query({...})
    resp = await sb.advertising_deals.query({...})

async with SDClient(config) as sd:
    resp = await sd.campaigns.query({...})
```

## 公开导出

`__init__.py` 导出以下 API：

```python
from async_amazon_ads_api_v1 import (
    AmazonAdsConfig,      # 核心配置
    Region,               # 区域枚举 (NA/EU/FE)
    CacheBackend,         # 缓存后端枚举 (FILE/REDIS)
    SPClient,             # Sponsored Products 客户端
    SBClient,             # Sponsored Brands 客户端
    SDClient,             # Sponsored Display 客户端
    TokenManager,         # OAuth token 生命周期管理
    TokenCredentials,     # token 刷新凭据
    BaseTokenCache,       # 缓存抽象基类
    FileTokenCache,       # 文件缓存实现
    RedisTokenCache,      # Redis 缓存实现
    close_all_redis,      # 关闭所有 Redis 连接
)
```
