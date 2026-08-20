# Amazon Ads SDK

> [!WARNING]
> **废弃与迁移说明 (Deprecation & Migration)**:
> `async_amazon_ads_api_v1` 包即将废弃，项目正在逐步迁移到全新的统一包 **`ads_api`**。
> - **`ads_api` (推荐)**：统一多版本（v0 与 v1）、全实体（SP、SB、SD、DSP、ST、SP Global、Accounts、Reporting、Ads Data Manager、Exports 等）的纯异步 Python SDK。
> - **`async_amazon_ads_api_v1` (即将废弃)**：旧版 v1 SDK，仅保留用于向后兼容，后续所有新特性与维护均迁移至 `ads_api`。

## 项目结构

```
.
├── script4/                                # Ads API v1 自动代码生成器 (基于 Merged OpenAPI)
│   ├── download_openapi.py                 # 下载 v1 Merged OpenAPI spec
│   ├── generate.py                         # 生成 src/ads_api/client/v1 与 models/v1
│   └── codegen/                            # v1 代码生成实现
├── script3/                                # Ads API v0 自动代码生成器
│   ├── download_openapi.py                 # 下载 v0 OpenAPI spec
│   ├── generate.py                         # 生成 src/ads_api/client/v0 与 models/v0
│   └── codegen/                            # v0 代码生成实现
├── script2/                                # [已废弃] 旧版 v1 分散式 OpenAPI 代码生成 (已由 script4 替代)
├── scripts/                                # [已废弃] 旧版 async_amazon_ads_api_v1 代码生成
│   ├── specs/                              # 旧版 OpenAPI 规范文件
│   └── generate_all.py                     # 旧版生成脚本
├── pyproject.toml                          # uv 项目配置
└── src/
    ├── ads_api/                            # 【全新统一包】Amazon Ads API (v0 + v1)
    │   ├── __init__.py                     # 导出 AdsClient, AdsClientV0, AdsClientV1 等
    │   ├── base.py                         # ClientContext + BaseResource + RequestRunner
    │   ├── config/                         # Region, AmazonAdsConfig, TokenManager, TokenCache
    │   ├── client/
    │   │   ├── v0/                         # v0 API 客户端 (accounts, reporting, sp_v3, exports...)
    │   │   └── v1/                         # v1 API 客户端 (sp, sb, sd, dsp, st, sp_global...)
    │   └── models/
    │       ├── _core/                      # lenient_enum, base model
    │       ├── v0/                         # v0 Pydantic 模型
    │       └── v1/                         # v1 Pydantic 模型
    └── async_amazon_ads_api_v1/             # 【即将废弃】旧版 SDK (逐步迁移至 ads_api)
        ├── __init__.py
        ├── _base.py
        ├── config/
        ├── client/                         # sp, sb, sd
        └── models/                         # sp, sb, sd, general, legacy
```

## 核心环境要求 (CRITICAL)

- **环境管理**: **必须**使用 `uv` 进行依赖管理、虚拟环境创建及任务执行。
- **Python 版本**: 最小 **Python 3.13**，禁止向后兼容 3.12 及以下。
- **特性使用**: 鼓励使用 Python 3.13+ 新特性。

## 代码质量 (MUST)

- **格式化**: 必须使用 `black` 格式化代码。
- **静态检查**: 必须使用 `ruff check --fix` 移除未使用的 imports/variables。
- 保存前执行这两条命令。

## Git 提交规范

- **语言**: `git commit` 信息尽量使用**中文**。
- **术语**: 术语如 `uv`, `asyncio`, `httpx`, `Pydantic` 等保持**英文**。
- **格式示例**: `feat: 使用 uv 同步依赖，支持 Python 3.14 特性`

## 常用命令

- 同步环境: `uv sync`
- 添加依赖: `uv add <package>`
- 执行脚本: `uv run python <script>` — **禁止**直接使用 `python3` / `python`
- 测试: `uv run pytest`
- Lint: `uv run ruff check --fix src/ scripts/ script4/ script3/`
- 格式化: `uv run black src/ scripts/ script4/ script3/`
- 类型检查: `uv run mypy src/`

## 代码生成

### 1. `ads_api` 代码生成（推荐）

- **v1 代码生成**（`script4/`）：
  ```bash
  uv run python script4/download_openapi.py
  uv run python script4/generate.py
  ```
  生成 `src/ads_api/client/v1` 与 `src/ads_api/models/v1`。

- **v0 代码生成**（`script3/`）：
  ```bash
  uv run python script3/download_openapi.py
  uv run python script3/generate.py
  ```
  生成 `src/ads_api/client/v0` 与 `src/ads_api/models/v0`。

### 2. 旧版 `async_amazon_ads_api_v1` 代码生成（已废弃）

```bash
uv run python scripts/generate_all.py
# 或单独生成某一产品：
uv run python scripts/generate_models.py --product sp --output-dir src/async_amazon_ads_api_v1/models/sp/
uv run python scripts/generate_models.py --product sb --output-dir src/async_amazon_ads_api_v1/models/sb/
uv run python scripts/generate_models.py --product sd --output-dir src/async_amazon_ads_api_v1/models/sd/
uv run ruff check --fix src/ scripts/
uv run black src/ scripts/
```

- 每次修改上游 JSON Schema 后，重新运行生成脚本
- 跨 tag 共用枚举写入各产品包的 `enums.py`，并加产品前缀（如 `SPErrorCode`、`SBErrorCode`、`GeneralCountryCode`）
- 跨 tag 共用 model 写入各产品包的 `shared.py`（如 `SPError`、`SPErrorsIndex`、`SPTag`），并加产品前缀
- 枚举使用 `StrEnum`，可选字段使用 `X | None` 语法
- 详细改造指南见 `scripts/CODEGEN_FORWARD_COMPAT.md`

### 核心设计：请求严格 / 响应向前兼容

Amazon Ads API 的响应可能在 OpenAPI schema 之外变化（新增字段、未知枚举值）。SDK 采用**请求严格、响应向前兼容**策略：

| 场景 | `extra` | 必填字段 | 未知枚举 |
|------|---------|---------|---------|
| 请求模型 | `forbid` | 保留 OpenAPI `required` | 拒绝（`ValidationError`） |
| 响应模型 | `allow` | 保留 OpenAPI `required` | 保留为 `str`（`lenient_enum`） |

**响应两层容忍**（仅响应模型）：

1. `extra="allow"` — 保留 API 新增字段
2. `lenient_enum` + `model_validate_json` — 容忍未知枚举值

### 生成器架构

```
OpenAPI spec
  → _openapi_schema.discover_schema_sets()   # 按 requestBody / 2xx 响应分别 BFS
  → _openapi_schema.split_shared_response_schemas()  # 拆分 request∩response 共用 model
  → _pydantic_emit.emit_model(extra=...)     # 按来源决定 forbid / allow
  → _codegen_runner.generate_models_for_tag() # 编排 + 写文件
```

- **Schema 分流**：`discover_schema_sets()` 将 schema 分为请求闭包与响应闭包（种子来自 `requestBody` 与 `200/201/207` 响应），据此决定 `extra` 与字段必填性
- **共用 schema 拆分**：若同一 model 同时出现在请求和响应闭包，生成器自动复制为 `FooForResponse`（重命名为 `FooResponse`）；请求侧保留原名。enum / type alias 允许共用；model 共用且未拆分会抛 `SharedModelSchemaError`
- **字段规则**：`is_required = fname in required` — 请求/响应模型均保留 OpenAPI `required`

### 运行时解析

`_base.py` / `base.py` 的 `_response()` 必须使用 `model_validate_json(resp.text)`（**禁止** `model_construct` 或 `model_validate(**resp.json())`），以便 JSON 模式下 `lenient_enum` 将未知枚举值保留为 `str`。

枚举字段声明（生成器自动输出）：

```python
state: Annotated[SPState | str, lenient_enum(SPState)] | None = Field(default=None)
```

Client 发出请求走 `self.dump_json(body)`（内部 `model_dump(mode="json", exclude_unset/exclude_none)`），不经过 `_response`，请求校验不受影响。

## 使用示例

所有 API 方法仅接受 Pydantic model 实例，不支持 dict。

### 推荐方式：使用全新 `ads_api`

```python
from ads_api import AdsClient, AmazonAdsConfig, Region


async def main() -> None:
    config = AmazonAdsConfig(access_token="...", region=Region.NA)

    async with AdsClient(config) as ads:
        # v1 接口
        resp = await ads.v1.sp.campaigns.query_campaigns(body)
        print(resp.model_dump_json(indent=2))

        # v0 接口
        profiles = await ads.v0.accounts.profiles.list_profiles()
```

### 旧版兼容：`async_amazon_ads_api_v1`（即将废弃）

```python
from async_amazon_ads_api_v1 import AmazonAdsConfig, Region, SPClient, SBClient, SDClient
from async_amazon_ads_api_v1.models.sp import SPQueryCampaignRequest


async def main() -> None:
    config = AmazonAdsConfig(access_token="...", region=Region.NA)
    body = SPQueryCampaignRequest(
        adProductFilter={"include": ["SPONSORED_PRODUCTS"]},
        stateFilter={"include": ["ENABLED"]},
    )

    async with SPClient(config) as sp:
        resp = await sp.campaigns.query(body)
        print(resp.model_dump_json(indent=2))

    async with SBClient(config) as sb:
        resp = await sb.campaigns.query(body)

    async with SDClient(config) as sd:
        resp = await sd.campaigns.query(body)
```
