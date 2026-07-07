# Changelog

## v0.6.0 (2026-07-08)

### feat — 新功能
- 基于 OpenAPI 规范重写所有 Legacy API，模型自动生成：
  - **SP BudgetRules**: 预算规则关联（创建、查询、更新、删除）
  - **SB BudgetRules**: 预算规则关联（创建、查询、更新、删除）
  - **SD BudgetRules**: 预算规则关联（创建、查询、更新、删除）
  - **SD Creatives**: 创意管理
  - **Portfolios**: 投资组合管理
- `generate_all.py` 集成所有 legacy 生成脚本，一键生成

### refactor — 重构
- `TokenManager` 直接判断 token 过期，不再依赖异常捕获
- 默认请求超时从 60s 提升到 600s
- 模型层移除所有 `import *`，改用显式子模块导入
- 清理已废弃的旧版 `BudgetRules` 客户端和模型
- 提取共享函数到 `scripts/_gen_utils.py`，消除代码重复
