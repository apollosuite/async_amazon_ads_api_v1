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
│   ├── generate_file_structure.py      # OpenAPI schema 分类器（无硬编码）
│   └── generate_models.py              # 从 JSON Schema 生成 models/
└── src/amazon_ads_sdk/
    ├── __init__.py                     # 公开 API 导出
    ├── config.py                       # AmazonAdsConfig / Region
    ├── py.typed                        # PEP 561 类型标记
    ├── client/                          # 异步 HTTP 客户端
    │   ├── __init__.py                 # AmazonAdsClient 主类
    │   ├── _context.py                 # ClientContext（共享 HTTP 状态）
    │   ├── _resource.py                # _ResourceBase + _ResourceSpec
    │   ├── _campaigns.py               # Campaigns 资源（继承 _ResourceBase）
    │   ├── _ad_groups.py               # AdGroups 资源
    │   ├── _ads.py                     # Ads 资源
    │   ├── _targets.py                 # Targets 资源
    │   └── _ad_extensions.py           # AdExtensions 资源
    └── models/                          # Pydantic v2 模型（自动生成）
        ├── __init__.py                 # 导出全部模型 + model_rebuild
        ├── _enums.py                   # 枚举（ErrorCode, SPState 等）
        ├── _campaigns.py               # Campaign 模型
        ├── _ad_groups.py               # AdGroup 模型
        ├── _ads.py                     # Ad 模型
        ├── _targets.py                 # Target 模型
        ├── _ad_extensions.py           # AdExtension 模型
        ├── _errors.py                  # HTTP 错误响应模型
        └── _shared.py                  # 跨资源共用模型
```

## 项目概述

核心使用 **httpx** 构建 Amazon Ads API 纯异步 SDK，必须遵守最简必要规则，避免过度设计。

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

`scripts/generate_models.py` 从 `AmazonAdsAPISPMerged_prod_3p.json` 自动生成 `src/amazon_ads_sdk/models/`（内部调用 `generate_file_structure.py` 完成 schema 分类）。

```bash
uv run python scripts/generate_models.py --output-dir src/amazon_ads_sdk/models/
uv run ruff check --fix src/
uv run black src/
```

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
from amazon_ads_sdk import AmazonAdsClient, Region
from amazon_ads_sdk.config import AmazonAdsConfig

config = AmazonAdsConfig(
    access_token="YOUR_ACCESS_TOKEN",
    region=Region.NA,
)

async with AmazonAdsClient(config) as client:
    # 嵌套式 API：client.<resource>.<operation>()
    resp = await client.campaign.query({"stateFilter": {"include": ["enabled"]}})
    print(resp.model_dump_json(indent=2))
```
