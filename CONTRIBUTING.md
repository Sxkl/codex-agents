# 贡献指南

这个仓库欢迎围绕 Codex 工作流、共享资产、案例沉淀进行扩展，但不建议把它重新做回“角色很多、边界很虚”的旧式多 Agent 集合。

## 建议优先贡献的内容

- 新的 stack-specific reference
- 新的 incident example
- 现有 skill 的共享 schema / checklist / workflow preset
- 真实使用后沉淀出的复盘模板和验证模板

## 不建议的方向

- 只增加一个新名字，但没有配套资产
- 一个 skill 同时承担分析、修复、评审、发布四种职责
- 强绑定某个私有模型习惯，导致默认 Codex 模型不可复用
- 没有 example 或 checklist 支撑的“概念型升级”

## 提交前自检

1. 这个改动解决的是哪个高频问题？
2. 是不是应该补资产，而不是新建 skill？
3. 新增内容是否能被现有 workflow 组合复用？
4. 输出结构是否仍然兼容 `summary / evidence / confidence / next_action / risk`？
5. 是否提供了示例、模板或 reference，证明它真的可用？

## 推荐贡献路径

1. 先提 issue，说明问题场景和预期收益。
2. 如果是新 skill，同时补一类共享资产。
3. 如果是改进现有 skill，优先扩展 references / examples / workflows。
4. PR 描述中写清楚：
   - 适用场景
   - 新增资产
   - 对现有 workflow 的影响
   - 未覆盖的边界
