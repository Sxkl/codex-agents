# 能力覆盖矩阵

这个仓库不是追求“技能数量最多”，而是追求在 Codex 里把高频工程任务做深、做稳、做成可以复用的资产包。

## 当前覆盖

| 任务域 | 主要技能 | 辅助资产 | 当前强度 |
| --- | --- | --- | --- |
| 日志分析 | `log-analysis` | `noise-patterns.yaml`、日志质量清单 | 高 |
| 根因定位 | `root-cause-analysis` | Java/Spring + Feign + Redis + MyBatis + 事务并发模式库 | 高 |
| 服务上下文装载 | `service-context-loader` | `shared/known-services.yaml` | 中高 |
| 代码修复 | `code-fix` | incident schema、示例 case | 中高 |
| 代码审查 | `code-review` | Java/Spring review checklist | 中高 |
| 验证回归 | `verification-regression` | verification checklist | 中高 |
| Jira/汇报输出 | `jira-writer` | incident schema、模板化输出约束 | 高 |
| 事故复盘 | `incident-retro-writer` | retro outline、incident schema | 中高 |
| 故障协同 | `incident-workflow-coordinator` | workflow presets、hotfix fastlane | 高 |
| 快速热修 | `hotfix-fastlane` | workflow yaml、severity matrix | 高 |

## 与传统“多 Agent 堆叠”的区别

传统方案常见优点：

- agent 名字多、角色细、看起来很强
- 容易表达复杂编排意图
- 对 Demo 和展示很友好

传统方案常见问题：

- 多数能力停留在 prompt 层，缺少共享资产
- skill 之间知识不互通，容易重复判断
- 迁移模型后不稳定，强依赖旧模型习惯
- 缺少统一输出结构，团队复用成本高

这个仓库的策略是：

- 少一些泛化空壳 skill，多一些可直接复用的参考资产
- 把“思路”沉淀成 schema、pattern、checklist、examples、workflow preset
- 让 Codex 在默认模型下也能稳定执行高价值链路

## 还未补齐的区域

下面这些方向值得继续扩展：

| 方向 | 缺口 | 建议下一步 |
| --- | --- | --- |
| SQL 风险分析 | 目前只有代码侧和 incident 侧 | 增加 SQL review / migration rollback 模板 |
| 发布验证 | 现有验证偏代码回归 | 增加 deploy checklist / smoke template |
| 服务目录 | `known-services.yaml` 还偏轻量 | 增加表、MQ、缓存、下游依赖画像 |
| 复盘闭环 | 复盘已有，但 follow-up 资产不够 | 增加 action item 模板与 owner SLA |
| 团队协作 | issue 模板已加，但 project board 没有 | 增加 GitHub Projects / labels 规范 |

## 判断仓库是否在成长

如果后续升级满足下面任意两项，就说明是在“深度成长”，不是表面扩充：

1. 新 skill 同时附带至少一种共享资产。
2. 旧 skill 的引用面变宽，而不是只增加说明文案。
3. 示例 case 能覆盖新的失败模式。
4. 输出结构更统一，便于团队协作和复盘。
5. 真实 incident 的处理耗时能被这些资产明显缩短。
