# Amazon Ads SDK — Sponsored Products

Pure async Python SDK for the Amazon Advertising API (Sponsored Products).

## 项目结构

```
.
├── AmazonAdsAPISPMerged_prod_3p.json   # 原始 OpenAPI 规范（不修改）
├── CLAUDE.md                           # 本文件
├── README.md
├── pyproject.toml                      # uv 项目配置
├── uv.lock                             # 依赖锁定文件（提交）
├── scripts/
│   └── generate_models.py              # 从 JSON Schema 生成 models.py
└── src/amazon_ads_sdk/
    ├── __init__.py                     # 公开 API 导出
    ├── config.py                       # AmazonAdsConfig / Region
    ├── client.py                       # 异步 HTTP 客户端（httpx）
    └── models.py                       # 208 个 Pydantic v2 模型（自动生成）
```

## 项目概述

核心使用 **httpx** 构建 Amazon Ads API 纯异步 SDK，必须遵守最简必要规则，避免过度设计。

## 核心环境要求 (CRITICAL)

- **环境管理**: **必须**使用 `uv` 进行依赖管理、虚拟环境创建及任务执行。
- **Python 版本**:
    - 最小支持版本为 **Python 3.13**。
    - **优先兼容 Python 3.14+** 及后续更高版本。
    - **禁止**考虑对 Python 3.12 及以下版本的向后兼容性。
- **特性使用**: 鼓励使用 Python 3.13/3.14 引入的新特性。

## 代码质量 (MUST)

- **格式化**: 必须使用 `ruff` 格式化代码，保持风格一致。
- **静态检查**: 必须使用 `ruff check --fix` 移除未使用的 imports/variables。
- 保存前执行这两条命令。

## Git 提交规范

- **语言**: `git commit` 信息尽量使用**中文**。
- **术语**: 术语如 `uv`, `Python 3.14`, `asyncio`, `httpx`, `Pydantic` 等保持**英文**。
- **格式示例**: `feat: 使用 uv 同步依赖，支持 Python 3.14 特性`

## 常用命令

- 同步环境: `uv sync`
- 添加依赖: `uv add <package>`
- 执行脚本: `uv run python <script>`
- 测试: `uv run pytest`
- Lint: `uv run ruff check --fix src/`
- 类型检查: `uv run mypy src/`

## 代码生成

`scripts/generate_models.py` 从 `AmazonAdsAPISPMerged_prod_3p.json` 自动生成 `src/amazon_ads_sdk/models.py`。

- 每次修改上游 JSON Schema 后，重新运行生成脚本
- 生成后执行 `uv run ruff check --fix src/amazon_ads_sdk/models.py`
- 枚举使用 `StrEnum`，可选字段使用 Python 3.14 `X | None` 语法

## 环境变量

```bash
AMAZON_ACCESS_TOKEN   # OAuth bearer token（必填）
AMAZON_REGION         # na | eu | fe（默认 na）
AMAZON_PROFILE_ID     # 可选，数字类型
```

## 使用示例

```python
from amazon_ads_sdk import AmazonAdsClient, Region
from amazon_ads_sdk.config import AmazonAdsConfig

config = AmazonAdsConfig(
    access_token="YOUR_ACCESS_TOKEN",
    region=Region.NA,
)

async with AmazonAdsClient(config) as client:
    resp = await client.query_campaigns({"stateFilter": {"include": ["enabled"]}})
    print(resp.json())
```
