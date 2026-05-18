# Amazon Ads SDK

Pure async Python SDK for the Amazon Advertising API — Sponsored Products / Sponsored Brands / Sponsored Display.

## 项目结构

```
.
├── scripts/
│   ├── AmazonAdsAPISPMerged_prod_3p.json   # SP OpenAPI 规范（不修改）
│   ├── AmazonAdsAPISBMerged_prod_3p.json   # SB OpenAPI 规范
│   ├── AmazonAdsAPISDMerged_prod_3p.json   # SD OpenAPI 规范
│   ├── generate_file_structure.py          # 通用 schema 分类器（无硬编码）
│   └── generate_models.py                  # 从 JSON Schema 生成 Pydantic 模型
├── README.md
├── CLAUDE.md                               # 本文件
├── pyproject.toml                          # uv 项目配置
├── uv.lock                                 # 依赖锁定
└── src/async_amazon_ads_api_v1/
    ├── __init__.py                         # 导出 AmazonAdsConfig, Region, SPClient, SBClient, SDClient
    ├── config.py                           # AmazonAdsConfig / Region
    ├── errors.py                           # 共享 HTTP 错误模型 (ErrorCode, Error, ErrorsIndex ...)
    ├── _base.py                            # ClientContext + _ResourceBase + _ResourceSpec
    ├── py.typed                            # PEP 561 类型标记
    ├── models/
    │   ├── __init__.py
    │   ├── sp/                             # SP 模型（自动生成，8 文件 / 195 模型）
    │   ├── sb/                             # SB 模型（自动生成，14 文件 / 294 模型）
    │   └── sd/                             # SD 模型（自动生成，6 文件 / 165 模型）
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
    - 最小支持版本为 **Python 3.14**。
    - **优先兼容 Python 3.14+** 及后续更高版本。
    - **禁止**考虑对 Python 3.12 及以下版本的向后兼容性。
- **特性使用**: 鼓励使用 Python 3.14 引入的新特性。

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
AMAZON_ACCESS_TOKEN   # OAuth bearer token（必填）
AMAZON_REGION         # na | eu | fe（默认 na）
AMAZON_PROFILE_ID     # 可选，数字类型
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
