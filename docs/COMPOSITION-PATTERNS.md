# 组合式工作流

这份文档定义在 Codex 中如何把多个 skill 组合成稳定工作流，而不是每次都临时发挥。

## 模式 1：标准故障排查

适用：

- 线上报错
- 请求超时
- 零星失败但影响未知

推荐顺序：

1. `service-context-loader`
2. `log-analysis`
3. `root-cause-analysis`
4. `jira-writer`

关键原则：

- 先装载服务背景，避免盲查
- 先降噪，再做因果链
- 没有可信因果链，不进入修复

## 模式 2：热修闭环

适用：

- 已有明确影响面
- 需要尽快给出补丁和验证结论

推荐顺序：

1. `service-context-loader`
2. `root-cause-analysis`
3. `code-fix`
4. `code-review`
5. `verification-regression`
6. `jira-writer`

关键原则：

- patch 必须绑定到根因，而不是绑定到症状
- review 和 verification 不可跳过
- 输出必须能支持 operator / reviewer / owner 三方协作

## 模式 3：高优先级故障快线

适用：

- P0 / P1
- 已经明确要热修
- 需要同步 incident summary

推荐顺序：

1. `hotfix-fastlane`
2. `incident-workflow-coordinator`
3. `incident-retro-writer`

关键原则：

- 快线是压缩路径，不是跳过证据
- 复盘必须把未解决风险和后续动作补齐

## 模式 4：评审驱动修复

适用：

- PR review 暴露风险
- 代码能运行但存在隐患

推荐顺序：

1. `code-review`
2. `root-cause-analysis`
3. `code-fix`
4. `verification-regression`

关键原则：

- review 找到的是风险，不一定是根因
- 要验证问题是否真的可触发，再决定修复范围

## 组合设计原则

- 一个 workflow 里必须有一个证据构建节点。
- 一个 workflow 里最好有一个结构化输出节点。
- skill 之间尽量通过共享 schema、example、pattern 交接，而不是靠长篇自然语言。
- 如果新增 workflow 不能复用现有资产，优先补资产，不要先造新名字。
