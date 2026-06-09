# ads_v1 e2e 行为契约测试 — 执行进度跟踪

> 目标：为 `async-amazon-ads-api-v1` 增加面向 `ads_v1_server` 的真实 HTTP e2e 测试，验证 SDK 行为是否符合 Amazon Ads API v1 的业务契约。
> 工作目录：`/Users/jack/codex/ads_v1/tests/e2e/`
> 依赖服务：`/Users/jack/codex/ads_v1_server`
> 默认服务地址：`http://127.0.0.1:8000`

## 状态图例

| 状态 | 含义 |
|---|---|
| DONE | 已完成 |
| IN_PROGRESS | 正在执行 |
| PENDING | 待执行 |
| BLOCKED | 被外部条件阻塞 |

## 阶段与状态

| 阶段 | 描述 | 状态 | 完成时间 | 备注 |
|---|---|---|---|---|
| S1 | 建立 `tests/e2e/` 文档与进度跟踪 | DONE | 2026-06-09 | 已创建 README 与 PROGRESS |
| S2 | 创建 e2e 配置与 fixtures | DONE | 2026-06-09 | 健康检查、seed 配置、唯一 campaign 名称 |
| S3 | 实现 SP campaigns 生命周期 e2e | DONE | 2026-06-09 | create/query/update/delete + 归档验证 |
| S4 | 实现 SP campaigns 负向契约测试 | DONE | 2026-06-09 | client id、scope 错误 |
| S5 | 实现 profile 隔离测试 | DONE | 2026-06-09 | 同 token 下不同 profile 不共享资源 |
| S6 | 实现父子资源关系测试 | PENDING |  | adGroups 必须引用同 profile campaign |
| S7 | 增加 pytest marker 与运行说明 | PENDING |  | 可选：`e2e` marker |
| S8 | 跑通并记录首次结果 | PENDING |  | `ruff` + `pytest tests/e2e -v` |

## 本轮执行日志

### 2026-06-09 创建 e2e 跟踪文档

**做了什么**：

- 参考 `ads_v1_server/tests/e2e/README.md` 与 `PROGRESS.md` 的组织方式。
- 在 `ads_v1/tests/e2e/` 下创建 e2e 说明文档和进度文档。
- 明确 e2e 完成标准：必须验证 Amazon 行为契约，不能仅以接口不报错为通过标准。

**当前结论**：

- 先从 SP campaigns 生命周期开始落地。
- 后续逐步覆盖鉴权错误、profile 隔离、父子资源关系。
- e2e 不导入服务端代码，只通过真实 HTTP 调用 `ads_v1_server`。

### 2026-06-09 创建 e2e 配置与 fixtures

**做了什么**：

- 新增 `config.py`，集中读取 `ADS_V1_E2E_*` 环境变量，并提供 `ads_v1_server` seed 默认值。
- 新增 `conftest.py`，提供 `/health` 健康检查、`AmazonAdsConfig`、`SPClient` 和唯一名称 fixture。
- 服务不可用时使用 `pytest.skip`，避免本地 e2e 环境问题污染单元测试结果。

**当前结论**：

- e2e 默认通过 refresh token 自动换取 access token，覆盖 SDK 的 token refresh 链路。
- 后续测试文件可直接使用 `sp_client` 与 `e2e_settings` fixture。

### 2026-06-09 实现 SP campaigns 生命周期 e2e

**做了什么**：

- 新增 `test_sp_campaigns_lifecycle_contract`。
- 覆盖 `sp.campaigns.create/query/update/delete` 的完整生命周期。
- 断言 MultiStatus、`campaignId`、profile currency、query filters、update 持久化和 delete 归档语义。

**验证结果**：

- `uv run --frozen ruff check tests/e2e`：通过。
- `uv run --frozen pytest tests/e2e/test_sp_campaigns.py -v`：1 passed。

**当前结论**：

- 当前 `ads_v1_server` 在 SP campaigns 生命周期上符合已记录的 Amazon 行为契约。
- 未发现需要修改服务端代码的业务偏差。

### 2026-06-09 实现请求上下文负向契约

**做了什么**：

- 新增 `access_token` fixture，直接校验 refresh token 响应中的 `token_type`、`expires_in` 和 refresh token 不轮换。
- 新增缺失 `Amazon-Ads-ClientId` 的协议探针，验证 Amazon Ads 错误体。
- 新增 SDK 场景：有效 access token + 错误 client id，验证 `UNAUTHORIZED`。
- 新增 SDK 场景：有效 access token + 非数字 profile scope，验证 `BAD_REQUEST`。

**当前结论**：

- 当前 `ads_v1_server` 的请求上下文错误格式与已记录 Amazon 行为契约一致。
- 缺失 client id 无法由 SDK 正常构造，因此使用裸 HTTP 作为 e2e 协议探针。

**验证结果**：

- `uv run --frozen ruff check tests/e2e`：通过。
- `uv run --frozen pytest tests/e2e/test_ads_api_context.py -v`：3 passed。

### 2026-06-09 实现 profile 隔离测试

**做了什么**：

- 新增 `helpers.py`，沉淀 SP campaign payload 与 query body。
- 新增 `test_sp_campaigns_are_isolated_by_profile_scope`。
- 使用同一个 refresh token 的两个 profile：默认 `111111115` 创建资源，`111111116` 查询不到该资源。
- 测试结束时通过 owner profile delete 归档清理测试资源。

**当前结论**：

- 当前 `ads_v1_server` 的资源隔离符合已记录的 profile scope 行为契约。

**验证结果**：

- `uv run --frozen ruff check tests/e2e`：通过。
- `uv run --frozen pytest tests/e2e/test_profile_isolation.py tests/e2e/test_sp_campaigns.py -v`：2 passed。

## 行为契约检查清单

### OAuth 与请求上下文

| 编号 | 检查项 | 状态 | 说明 |
|---|---|---|---|
| C-001 | refresh token 可换取 access token | DONE | SDK 配置不传 access_token 时应自动刷新 |
| C-002 | 资源请求携带 `Amazon-Ads-ClientId` | DONE | 通过缺失 header 错误路径验证 |
| C-003 | 资源请求携带 `Amazon-Advertising-API-Scope` | DONE | 通过非数字 scope 错误路径验证 |
| C-004 | client_id mismatch 返回 `UNAUTHORIZED` | DONE | 验证 Amazon Ads 错误体 |
| C-005 | 非数字 scope 返回 `BAD_REQUEST` | DONE | 验证错误 message |

### SP campaigns

| 编号 | 检查项 | 状态 | 说明 |
|---|---|---|---|
| C-101 | create 返回 MultiStatus | DONE | `success/error`，成功项包含 `campaign` 与 `index` |
| C-102 | create 响应使用 `campaignId` | DONE | 不接受仅有通用 `id` |
| C-103 | budget 响应补齐 profile currency | DONE | profile `111111115` 预期 `GBP` |
| C-104 | query 返回 `campaigns` 与 `nextToken` | DONE | `nextToken` 当前预期为 `None` |
| C-105 | `campaignIdFilter` 精确过滤 | DONE | 只返回目标 campaign |
| C-106 | `stateFilter` 按状态过滤 | DONE | ENABLED/ARCHIVED |
| C-107 | `adProductFilter` 按广告产品过滤 | DONE | SPONSORED_PRODUCTS |
| C-108 | update 返回 MultiStatus 且持久化 | DONE | query 后字段已更新 |
| C-109 | delete 是归档语义 | DONE | state 变为 `ARCHIVED` |
| C-110 | delete 后资源仍可查询 | DONE | `stateFilter=ARCHIVED` |

### 隔离与父子关系

| 编号 | 检查项 | 状态 | 说明 |
|---|---|---|---|
| C-201 | profile 间资源隔离 | DONE | 一个 profile 创建，另一个 profile 查不到 |
| C-202 | adGroup 缺失 parent campaign 返回 MultiStatus error | PENDING | `RESOURCE_DOES_NOT_BELONG_TO_PARENT` |
| C-203 | adGroup 跨 profile parent 返回 MultiStatus error | PENDING | 不创建孤儿资源 |
| C-204 | adGroup 同 profile parent 可创建成功 | PENDING | success 项含 parent campaignId |

## 首次实现建议

优先实现以下最小闭环：

1. `config.py`：读取 e2e 环境变量并提供 seed 默认值。
2. `conftest.py`：健康检查，不可用时 skip；提供 `AmazonAdsConfig` fixture。
3. `test_sp_campaigns.py`：覆盖 C-001、C-101 至 C-110。
4. 运行 `ruff` 与 `pytest tests/e2e -v`。

## 运行记录

| 时间 | 命令 | 结果 | 备注 |
|---|---|---|---|
| 2026-06-09 | `uv run --frozen ruff check tests/e2e` | DONE | S3 静态检查通过 |
| 2026-06-09 | `uv run --frozen pytest tests/e2e/test_sp_campaigns.py -v` | DONE | 1 passed |
| 2026-06-09 | `uv run --frozen ruff check tests/e2e` | DONE | S4 静态检查通过 |
| 2026-06-09 | `uv run --frozen pytest tests/e2e/test_ads_api_context.py -v` | DONE | 3 passed |
| 2026-06-09 | `uv run --frozen ruff check tests/e2e` | DONE | S5 静态检查通过 |
| 2026-06-09 | `uv run --frozen pytest tests/e2e/test_profile_isolation.py tests/e2e/test_sp_campaigns.py -v` | DONE | 2 passed |
