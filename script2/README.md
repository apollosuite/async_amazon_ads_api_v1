# Ads API v1 代码生成

从 `data/api-spec-v1/` 的 per-entity OpenAPI 生成 `src/ads_api/client/v1` 与 `src/ads_api/models/v1`。不依赖旧的 `scripts/`。runtime（`config` / `base` / `models/_core`）与 v0 共用 `src/ads_api`。

## 命令

```bash
# 下载 spec
uv run python script2/download_toc.py
uv run python script2/download_reference.py
uv run python script2/download_openapi.py

# 生成
uv run python script2/generate.py
```

生成始终覆盖全部实体。同一产品下跨实体完全相同的 schema，会抽到 `models/v1/_shared/<product>.py`，实体模块再导出。

## 目录对应

| 输入 | 输出 |
|------|------|
| `data/api-spec-v1/<entity>/` | `src/ads_api/models/v1/<entity>/<product>.py` |
| 同上（SP/SB/SD/…） | `src/ads_api/client/v1/<product>/<entity>.py` |
| 同上（ALL 独有操作） | `src/ads_api/client/v1/<entity>.py` |
| OpenAPI tag（如 `Campaigns`） | 实体模块名 snake_case（`campaigns`） |
| spec 文件名中的产品 | client 包名 / models 模块名 |

产品从文件名解析：`AmazonAdsAPI(ALL\|SPGLOBAL\|SP\|SB\|SD\|DSP\|ST)…`

| 产品 | 模块 | 资源类 | 模型前缀 |
|------|------|--------|----------|
| ALL | `general`（models） | `BrandStores` | 无（模块路径已区分） |
| SP | `sp` | `SPCampaigns` | `SP`（无前缀 schema 如 `Error` → `SPError`） |
| SPGLOBAL | `sp_global` | `SPGlobalCampaigns` | `SPGlobal` |
| SB / SD / DSP / ST | 同名 | `SBCampaigns` … | 同左 |

spec 里的 `ALL` 不是广告产品，client **不建** `client/v1/all/`：

- 有对应广告产品的操作：只生成 `client/v1/<product>/<entity>.py`
- 无产品归属的接口：写成 `client/v1/<entity>.py`，直接挂在 `AdsClientV1` 上（`ads.v1.selling_accounts`）

`SPGLOBAL` 必须排在 `SP` 前面匹配。广告产品会给**未带该产品前缀**的 schema 补前缀；ALL 不加前缀。

## ALL 去重

ALL spec 中与**任一产品 spec** 相同的 `(HTTP method, path)` 一律删除。

- 删完后若 ALL 无剩余操作：不生成该实体的 ALL 模块
- campaigns 即为此情况（create/delete/query/update 都被产品 spec 覆盖）
- 若某实体 ALL 有独有操作：models 写到 `models/v1/<entity>/general.py`，client 写到 `client/v1/<entity>.py`

## 命名

- 方法名：`operationId` 去掉产品前缀再转 snake_case  
  `SPCreateCampaign` → `create_campaign`
- 访问顺序：广告产品为 **产品 → 实体**；无产品归属的接口挂在 `AdsClientV1` 顶层

```python
from ads_api import AdsClient, AmazonAdsConfig, Region
from ads_api.models.v1.campaigns.sp import SPCreateCampaignRequest

async with AdsClient(config) as ads:
    await ads.v1.sp.campaigns.create_campaign(body)
    await ads.v1.selling_accounts.query_selling_account(body)
```

只需要 v1 时可用 `AdsClientV1(config)`。

- `AdsClientV1` 扫描 `client/v1/` 下已有产品包自动挂属性（生成 dsp 实体后会多出 `.dsp`）
- 无产品归属的实体作为顶层属性（`.selling_accounts`、`.brand_stores` …）
- 产品若只有部分实体，命名空间只暴露实际生成的模块（如 SP 无 brand_stores 则没有 `.brand_stores`）

## 模型规则

请求严格、响应向前兼容：

| | `extra` | 未知枚举 | 字段类型 |
|--|---------|----------|----------|
| 请求（INPUT） | `forbid`（`StrictModel`） | 严格校验拒绝 | `EnumLiteral`（数组为 `list[EnumLiteral \| str]`） |
| 响应（OUTPUT） | `allow`（`LenientModel`） | 容忍未知字符串 | `EnumLiteral \| str` |

- 同 schema 同时出现在请求和响应闭包：请求保留原名，响应加 `Out`
- mutation result（含 `code`+`details` 且非实体字段）：名加 `Result`
- 成功响应只取 `200` / `201` / `207`
- Header 参数不进方法签名（`ClientId` / `Scope` / `AccountId` 由 `AmazonAdsConfig` + `BaseResource` 注入）
- `__all__` 包含请求和响应模型
- 枚举生成为 Python 3.12+ `type Name = Literal[...]`，成员说明附带行内注释与 Docstring
- 多变体 `oneOf` 拆成子 model + `type` 别名；单变体仍 flatten

## 生成器结构

```
script2/
  download_*.py      # 拉 TOC / reference / OpenAPI
  generate.py        # 入口
  codegen/
    spec.py          # 产品解析、ALL 过滤、前缀
    schema.py        # 请求/响应闭包、命名、跨实体共享
    emit.py          # Pydantic + client 源码
  data/api-spec-v1/<entity>/meta.json
```
