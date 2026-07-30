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
│   ├── generate_models.py                  # SP/SB/SD 模型 + Client 生成入口
│   ├── _codegen_runner.py                  # 代码生成编排（OpenAPI → Pydantic + Client）
│   ├── _openapi_schema.py                  # OpenAPI 解析、请求/响应 schema 分流
│   ├── _pydantic_emit.py                   # Pydantic 模型源码发射
│   ├── CODEGEN_FORWARD_COMPAT.md           # 向前兼容设计详解（改造参考）
│   └── generate_*.py                       # 各 API 域的独立生成脚本
├── pyproject.toml                          # uv 项目配置
└── src/async_amazon_ads_api_v1/
    ├── __init__.py                         # 导出所有公开 API
    ├── _base.py                            # ClientContext + BaseResource
    ├── errors.py                           # 共享 HTTP 错误模型
    ├── config/
    │   ├── region.py                       # Region 枚举 + ENDPOINT_MAP
    │   ├── settings.py                     # AmazonAdsConfig / CacheBackend
    │   ├── token_cache.py                  # BaseTokenCache / FileTokenCache / RedisTokenCache
    │   └── token_manager.py               # TokenManager / TokenCredentials
    ├── models/
    │   ├── _core/lenient_enum.py           # 枚举向前兼容 validator
    │   ├── sp/                             # SP 模型（自动生成）
    │   ├── sb/                             # SB 模型（自动生成）
    │   ├── sd/                             # SD 模型（自动生成）
    │   ├── general/                        # General API 模型（自动生成）
    │   └── legacy/                         # Legacy API 模型（自动生成）
    └── client/
        ├── sp/                             # SPClient + 5 资源类
        ├── sb/                             # SBClient + 11 资源类
        └── sd/                             # SDClient + 4 资源类
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
- Lint: `uv run ruff check --fix src/ scripts/`
- 格式化: `uv run black src/ scripts/`
- 类型检查: `uv run mypy src/`

## 代码生成

模型基于 OpenAPI 规范自动生成：

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
- 枚举使用 `StrEnum`，可选字段使用 `X | None` 语法
- 详细改造指南见 `scripts/CODEGEN_FORWARD_COMPAT.md`

### 核心设计：请求严格 / 响应向前兼容

Amazon Ads API 的响应可能在 OpenAPI schema 之外变化（新增字段、未知枚举值、缺失字段）。SDK 采用**请求严格、响应宽松**策略：

| 场景 | `extra` | 必填字段 | 未知枚举 |
|------|---------|---------|---------|
| 请求模型 | `forbid` | 保留 OpenAPI `required` | 拒绝（`ValidationError`） |
| 响应模型 | `allow` | 全部可选 | 保留为 `str`（`lenient_enum`） |

**响应三层容忍**（仅响应模型）：

1. `extra="allow"` — 保留 API 新增字段
2. 字段全可选 — 容忍响应体缺失字段
3. `lenient_enum` + `model_validate_json` — 容忍未知枚举值

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
- **字段规则**：`is_required = fname in required and extra == "forbid"` — 仅请求模型保留 OpenAPI `required`

### 运行时解析

`_base.py` 的 `_response()` 必须使用 `model_validate_json(resp.text)`（**禁止** `model_construct` 或 `model_validate(**resp.json())`），以便 JSON 模式下 `lenient_enum` 将未知枚举值保留为 `str`。

枚举字段声明（生成器自动输出）：

```python
state: Annotated[SPState | str, lenient_enum(SPState)] | None = Field(default=None)
```

Client 发出请求走 `body.model_dump(exclude_none=True)`，不经过 `_response`，请求校验不受影响。

## 使用示例

所有 API 方法仅接受 Pydantic model 实例，不支持 dict：

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
