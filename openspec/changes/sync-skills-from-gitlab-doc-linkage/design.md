# 设计：同步技能变更与 Mintlify 文档联动

## 设计原则

本次采用“三层联动”：

1. `openspec/changes/sync-skills-from-gitlab`
   - 作为工程事实源
   - 保留 Git 日志、能力归纳和修复记录

2. `doc/update.md`
   - 作为统一汇总稿
   - 固定承接 `clis/` 与 `gisagent/` 两个来源

3. `doc/docs/*.mdx`
   - 作为文档站消费层
   - 使用 Mintlify frontmatter 和组件

## 页面收敛

文档站侧只保留 1 个页面：

- `doc/docs/skills-detailed-update-log.mdx`

该页面统一覆盖：

- 用户摘要
- 每日更新
- 新增能力
- 前端与修复

`doc/update.md` 则作为更稳定的汇总稿，用于后续继续镜像、摘录或重组。

## 导航设计

在 `doc/docs.json` 的“文档中心”下保留“技能迭代”分组，当前只挂 1 个统一页面，避免拆分页继续漂移。

## 链接关系

### 从文档站回链到工程事实

唯一 `.mdx` 页面顶部通过说明块指向原始 `openspec` 文件。

### 从汇总稿到文档页

`doc/update.md` 记录固定来源和统一摘要；`skills-detailed-update-log.mdx` 承接对外阅读结构。

### 从工程记录回链到文档站

原始 `openspec/changes/sync-skills-from-gitlab/tasks.md` 增加说明，记录统一页面、`doc/update.md` 和本 change。

## 不做的事

- 不将 `doc/openspec/changes` 直接接入 Mintlify 主导航
- 不把工程执行细节全部搬进文档站
- 不恢复旧的“三页发布”结构
- 不改变原始 openspec change 的事实边界
