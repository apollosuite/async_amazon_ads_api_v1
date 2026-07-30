# 代码生成向前兼容改造指南

本文档总结 `generate_brandstores.py` 及相关运行时改动的设计，供后续改造 `generate_models.py`（SP/SB/SD）及其他生成脚本时参考。

## 背景与目标

Amazon Ads API 的响应可能在 OpenAPI schema 之外发生变化：

| 变化类型 | 示例 | 旧行为问题 |
|---------|------|-----------|
| 新增字段 | API 返回 `newField` | `extra="forbid"` + `model_construct` 会静默丢弃 |
| 新增枚举值 | `publishState: "FUTURE_STATE"` | 严格枚举校验导致 `ValidationError` |
| 缺失字段 | 响应体字段少于 schema `required` | 响应模型保留 OpenAPI `required`，缺失时 `ValidationError` |

改造目标：

- **请求**：保持严格校验（`extra="forbid"`、必填字段、未知枚举拒绝）
- **响应**：容忍 API 变动（多余字段、未知枚举），但保留 OpenAPI `required` 字段

---

## 改动文件一览（暂存区）

| 文件 | 改动性质 |
|------|---------|
| `scripts/generate_brandstores.py` | 生成器核心逻辑 |
| `src/async_amazon_ads_api_v1/_base.py` | 运行时响应解析 |
| `src/async_amazon_ads_api_v1/models/general/*.py` | 重新生成的模型 |
| `tests/test_base.py` | 响应解析测试 |

---

## 一、运行时：`_base.py`

### 变更

```python
# 旧
def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
    return model_cls.model_construct(**resp.json())

# 新
def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
    return model_cls.model_validate_json(resp.text)
```

### 原因

| 方式 | 多余字段 | 未知枚举 | 缺失字段 | 类型校验 |
|------|---------|---------|---------|---------|
| `model_construct` | 取决于 `extra` | 不跑 validator | 不校验 | 无 |
| `model_validate(**dict)` | 取决于 `extra` | Python 模式严格 | 校验 required | 有 |
| `model_validate_json(text)` | 取决于 `extra` | JSON 模式宽松（配合 `lenient_enum`） | 校验 required | 有 |

**必须使用 `model_validate_json(resp.text)`**，才能让 `lenient_enum` 在 API 响应场景下将未知枚举值保留为 `str`。

> 注意：`model_validate(**resp.json())` 写法是错误的，会把 JSON key 当作 `model_validate` 的参数。

### 与 `lenient_enum` 的配合

已有实现：`src/async_amazon_ads_api_v1/models/_core/lenient_enum.py`

```python
# 字段声明（生成器已输出）
state: Annotated[AdState | str, lenient_enum(AdState)] | None = Field(default=None)
```

| 模式 | 已知枚举值 | 未知枚举值 |
|------|-----------|-----------|
| Python（构造请求） | `AdState.ENABLED` | `ValidationError` |
| JSON（解析响应） | `AdState.ENABLED` | `"UNKNOWN"`（`str`） |

调用方处理未知枚举：

```python
if isinstance(state, AdState):
    ...
else:
    logger.warning("unknown state: %s", state)
```

---

## 二、生成器：Schema 分流

### 新增函数

将原先单一的 `discover_schemas` BFS 拆为请求/响应两套闭包：

```python
def _collect_schema_seeds(endpoints, *, from_request: bool, from_response: bool) -> set[str]: ...

def _bfs_schema_closure(all_schemas, seeds) -> set[str]: ...

def discover_schema_sets(spec, endpoints) -> tuple[request_schemas, response_schemas, all_needed]:
    request_seeds = _collect_schema_seeds(endpoints, from_request=True, from_response=False)
    response_seeds = _collect_schema_seeds(endpoints, from_request=False, from_response=True)
    # 分别 BFS，返回两个字典 + 并集
```

- **请求种子**：`requestBody` 中的 `$ref`
- **响应种子**：`200` / `201` / `207` 响应中的 `$ref`
- **不遍历**非 2xx 错误 schema（4xx `*ResponseContent` 暂不生成）

### 判定规则

```python
response_schema_names = {_rename_schema(n) for n in response_schemas}
request_schema_names = {_rename_schema(n) for n in request_schemas}

for name, schema in models:
    extra = "allow" if name in response_schema_names else "forbid"
    emit_model(name, schema, schemas, extra=extra)
```

---

## 三、生成器：模型字段规则

### `generate_model(..., extra: str = "forbid")`

```python
# 请求/响应模型均保留 OpenAPI required
is_required = fname in required

# 非必填字段添加 | None 与 default=None
if not is_required and typ not in ("Any",):
    typ = f"{typ} | None"
# 并添加 default=None
```

### 生成结果对比

**请求模型**（`AdAssociationCreate`）：

```python
class AdAssociationCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    adGroupId: str = Field(...)
    state: Annotated[CreateState | str, lenient_enum(CreateState)]
```

**响应模型**（`AdAssociation`）：

```python
class AdAssociation(BaseModel):
    model_config = ConfigDict(extra="allow")
    adAssociationId: str = Field(...)
    adGroupId: str = Field(...)
    adId: str = Field(...)
    state: Annotated[AdState | str, lenient_enum(AdState)]
    endDateTime: datetime | None = Field(default=None, ...)
```

### 两层容忍策略（仅响应）

1. `extra="allow"` — 保留 API 新增字段
2. `lenient_enum` + `model_validate_json` — 容忍未知枚举值

---

## 四、请求校验是否受影响

### 不受影响

- 纯请求 schema（`*Request`、`*Create`、`*Update`、`*Filter`）仍为 `extra="forbid"` + 原始 required
- Client 发出请求走 `body.model_dump(exclude_none=True)`，不经过 `_response`
- 用户构造请求对象时仍为 Python 模式严格校验

### 边界情况：请求 ∩ 响应共用 schema

若同一 schema 同时出现在两个闭包中，生成器会按**响应规则**处理（`allow` + 全可选）。

**当前 general API 扫描结果**（均为 enum，无共用 model）：

```
BrandStoreEditionPublishVersions: StorePublishState, StorePublishStatus
AdvertiserAccounts: CurrencyCode, IndustryVertical, SellingProgram, TimeZoneIana
SellingAccounts: SellingProgram
GeoLocations: DistanceUnit
LocationIndexes: CountryCode
```

enum 不受 `extra` / 字段可选影响，实际风险极低。若未来出现共用 model，应考虑拆分或单独处理。

### 诊断输出

生成器已内置公用 schema 打印：

```
Shared schemas (request ∩ response): N
  SchemaName (enum|model)
...
Shared schemas summary (request ∩ response)
  TagName: Schema1, Schema2
```

---

## 五、Client 生成（无逻辑变化，附带修复）

响应仍返回 Pydantic 模型：

```python
return self._response(BrandStoreSuccessResponse, resp)
```

附带修复：非 GET 请求使用实际 `http_method`，而非硬编码 `"POST"`。

---

## 六、测试要求

在 `tests/test_base.py` 中覆盖以下场景：

### 1. 基础 JSON 解析

```python
resp.text = json.dumps({"name": "x", "value": 2})
result = resource._response(DummyModel, resp)
```

### 2. 未知枚举值透传

```python
resp.text = json.dumps({..., "publishState": "FUTURE_STATE", ...})
result = resource._response(BrandStoreEditionPublishVersion, resp)
assert result.publishState == "FUTURE_STATE"  # str，非枚举
```

### 3. 缺失响应字段

```python
resp.text = json.dumps({"adAssociations": [{"state": "123"}]})
with pytest.raises(ValidationError):
    resource._response(AdAssociationSuccessResponse, resp)
```

已有参考：`tests/test_lenient_enum.py`

---

## 七、改造其他脚本 Checklist

以 `generate_models.py`（SP/SB/SD）为例：

### 生成器

- [ ] 引入 `discover_schema_sets`（或复用共享模块）
- [ ] `generate_model` 增加 `extra` 参数
- [ ] 响应 schema：`extra="allow"` + `is_required = fname in required`
- [ ] 请求 schema：保持 `extra="forbid"`
- [ ] 枚举字段继续使用 `Annotated[Enum | str, lenient_enum(Enum)]`
- [ ] 添加公用 schema 诊断打印
- [ ] 重新生成模型并执行 `black` / `ruff`

### 运行时

- [ ] 确认 `_base.py` 的 `_response` 使用 `model_validate_json(resp.text)`（全局生效，改一次即可）

### 测试

- [ ] 更新 mock `resp.text`（替代 `resp.json.return_value`）
- [ ] 添加未知枚举 + 缺失字段的响应测试
- [ ] 确认请求模型严格性测试仍通过

### 不建议的方案

| 方案 | 原因 |
|------|------|
| 响应返回 `dict` + `TypedDict` | 失去属性访问；与现有 SDK 风格不一致 |
| 响应返回 `resp.json()` 裸 dict | 无类型校验、无 datetime 等自动转换 |
| 全局 `model_construct` | 不跑 validator，枚举/类型不转换 |
| 响应仍用 `extra="forbid"` | 丢弃 API 新增字段 |

---

## 八、迁移命令

```bash
# 重新生成 general 模型
uv run python scripts/generate_brandstores.py

# 格式化与检查
uv run black src/ scripts/
uv run ruff check --fix src/ scripts/

# 测试
uv run pytest tests/test_base.py tests/test_lenient_enum.py -q
```

---

## 九、设计决策记录

| 决策 | 选择 | 备选 |
|------|------|------|
| 响应类型 | Pydantic + `extra="allow"` | TypedDict / 裸 dict |
| 响应解析 | `model_validate_json` | `model_construct` |
| 缺失字段 | 响应保留 OpenAPI `required` | 响应字段全可选 |
| 请求/响应分流 | 按 BFS 闭包来源 | 按命名约定（`*Response`） |
| 枚举 | 已有 `lenient_enum` | 纯 `StrEnum` |

---

## 十、相关文件

- 生成器参考实现：`scripts/generate_brandstores.py`
- 枚举 validator：`src/async_amazon_ads_api_v1/models/_core/lenient_enum.py`
- 运行时基类：`src/async_amazon_ads_api_v1/_base.py`
- 测试：`tests/test_base.py`、`tests/test_lenient_enum.py`
