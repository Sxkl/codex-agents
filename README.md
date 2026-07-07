# Codex Agents

一套面向 Codex 的公开技能包，聚焦于生产故障排查、根因定位、代码修复、代码审查、验证回归和 Jira 输出。

这个仓库不是把旧 Agent 体系原样搬过来，而是做了一次面向 Codex 的深度重构：

- 更少的技能数量
- 更清晰的职责边界
- 更强的工作流组织能力
- 更统一的输出格式
- 更适合团队协作和长期演进
- 更重的共享资产层（references / shared / workflows / examples）

## 这个仓库解决什么问题

很多旧的多 Agent 方案都有几个典型问题：

- 技能太多，职责重叠
- 强依赖单个模型或模型编排
- 更像“角色集合”，不像“工作流系统”
- 输出格式不统一，难以沉淀和复用

这个仓库的目标是把这些问题收敛掉，形成一套更适合 Codex 的技能体系：

- 用 workflow 取代 role-sprawl
- 用 evidence-first 取代拍脑袋式分析
- 用固定 handoff 取代混乱的多角色串话
- 用统一输出契约支撑 Jira、评审、验证和复盘

## 不只是技能，还包含什么

为了避免“skill 很短但能力很薄”，仓库补了四类资产：

- `references/`
  放具体领域知识、排障模式、审查清单、验证清单
- `shared/`
  放跨 skill 复用的配置，例如服务清单、严重级别矩阵、输出 schema
- `workflows/`
  放工作流配置，描述标准 hotfix 流程和手工接管点
- `examples/`
  放真实风格案例，帮助快速看出这套体系和普通 prompt 的差异

## 当前包含的核心技能

- `incident-workflow-coordinator`
  负责把日志分析、根因定位、修复、审查、验证、输出这条链路组织起来。

- `log-analysis`
  负责对日志进行聚类、识别高风险模式、区分噪音与真正故障，并给出升级建议。

- `root-cause-analysis`
  负责把错误现象、堆栈、日志和代码路径串成因果链，输出证据支撑的根因。

- `code-fix`
  负责在问题明确后做最小、安全、可验证的代码修复。

- `code-review`
  负责面向 bug、回归、安全、事务和测试缺口做高信号审查。

- `verification-regression`
  负责补最小测试、跑最小必要校验，并明确剩余风险。

- `jira-writer`
  负责把分析结果、修复内容和验证结论整理成 Jira 可直接使用的 comment / report / closure。

- `hotfix-fastlane`
  负责把一次生产 hotfix 从日志到修复再到输出整合成标准化闭环。

- `service-context-loader`
  负责按服务名加载技术栈、常见故障模式和分析优先级，减少每次排障都从零建上下文。

- `incident-retro-writer`
  负责把一次故障处理过程整理成复盘摘要、经验结论和后续动作。

## 新增的厚资产能力

这套仓库现在已经不只是 skill 集合，而是补了几层关键资产：

- `shared/`
  - 服务画像
  - 严重级别矩阵
  - 统一 incident 输出 schema
- `references/`
  - Java/Spring incident 模式
  - 审查 checklist
  - 验证 checklist
  - 日志质量 checklist
- `workflows/`
  - hotfix-fastlane 标准流程
- `examples/`
  - timeout、Feign null、Redis lock、retro 示例
- `.github/ISSUE_TEMPLATE/`
  - incident / feature 请求模板
- `docs/BENCHMARKS.md`
  - 对比普通 prompt 和 workflow-first 技能体系的差异
- `docs/CAPABILITY-MATRIX.md`
  - 看当前能力覆盖和下一步扩展缺口
- `docs/COMPOSITION-PATTERNS.md`
  - 定义多 skill 的标准组合方式

## 推荐使用链路

如果你是在处理生产问题，推荐按下面顺序使用：

1. `log-analysis`
2. `root-cause-analysis`
3. `code-fix`
4. `code-review`
5. `verification-regression`
6. `jira-writer`

如果你希望直接走完整热修复流程，优先使用：

- `hotfix-fastlane`

如果你是在做长期团队化落地，建议再配合：

- `docs/CAPABILITY-MATRIX.md`
- `docs/COMPOSITION-PATTERNS.md`

## 仓库结构

```text
CONTRIBUTING.md
skills/
  incident-workflow-coordinator/
  log-analysis/
  root-cause-analysis/
  code-fix/
  code-review/
  verification-regression/
  jira-writer/
  hotfix-fastlane/
  service-context-loader/
  incident-retro-writer/
docs/
  ARCHITECTURE.md
  ROADMAP.md
  BENCHMARKS.md
  CAPABILITY-MATRIX.md
  COMPOSITION-PATTERNS.md
examples/
shared/
.github/
scripts/
  migrate_opencode_agents_to_codex.py
```

如果你打算把这个仓库用于团队协作，先看：

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`

## 设计原则

### 1. 工作流优先

这里不追求堆更多“角色”，而是优先把高频任务链路收敛成稳定流程。

### 2. 证据优先

所有分析型技能都强调：

- 结论必须有证据
- 根因必须能回到代码路径
- 不能只根据日志表象直接拍结论

### 3. 最小修复

修复类技能优先做：

- 最小补丁
- 最小验证
- 明确剩余风险

避免把一次 hotfix 扩大成重构。

### 4. 输出统一

技能输出尽量收敛到统一结构：

- `summary`
- `evidence`
- `confidence`
- `next_action`
- `risk`

这样方便后续沉淀到 Jira、MR、复盘和知识库。

### 5. 主文档短，资产层厚

核心 skill 的 `SKILL.md` 保持短，避免上下文臃肿。

更深的能力来自：

- 引用资料
- 共享规则
- 标准工作流
- 真实案例

## 适合谁使用

这套技能更适合以下场景：

- 生产问题排查
- 团队内标准化 hotfix 流程
- Java / Spring 风格服务排障
- 代码修复后的审查与验证
- 把技术结论整理成团队可读的产物

## 和旧方案的区别

这套公开仓库不是“迁移版遗产合集”，而是“精选后的 Codex 原生技能包”。

它相比旧的偏 DeepSeek / 多模型 / 多角色方案，主要提升在：

- 更清晰的技能边界
- 更少但更强的技能数量
- 更适合 Codex 默认模型行为
- 更容易被团队理解、复用、维护
- 不再靠某个单模型“碰运气”，而是靠流程、资产和验证拉高稳定性

## 后续规划

下一步重点会继续补强：

- `service-context-loader`
- Java / Spring 故障排查 reference
- Redis / Feign / MyBatis / 事务 / 并发检查模板
- incident retro / postmortem 输出能力
- issue template 和 benchmark 示例

详细规划见：

- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`
