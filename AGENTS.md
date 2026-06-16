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
├── pyproject.toml                          # uv 项目配置
└── src/async_amazon_ads_api_v1/
    ├── __init__.py                         # 导出所有公开 API
    ├── _base.py                            # ClientContext + _ResourceBase + _ResourceSpec
    ├── errors.py                           # 共享 HTTP 错误模型
    ├── config/
    │   ├── region.py                       # Region 枚举 + ENDPOINT_MAP
    │   ├── settings.py                     # AmazonAdsConfig / CacheBackend
    │   ├── token_cache.py                  # BaseTokenCache / FileTokenCache / RedisTokenCache
    │   └── token_manager.py               # TokenManager / TokenCredentials
    ├── models/
    │   ├── sp/                             # SP 模型（自动生成）
    │   ├── sb/                             # SB 模型（自动生成）
    │   └── sd/                             # SD 模型（自动生成）
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

- 每次修改上游 JSON Schema 后，重新运行生成脚本
- 枚举使用 `StrEnum`，可选字段使用 `X | None` 语法

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
