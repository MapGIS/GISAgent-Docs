# 设计：同步技能变更与 Mintlify 文档联动

## 设计原则

本次采用“双层记录”：

1. `openspec/changes/sync-skills-from-gitlab`
   - 作为工程事实源
   - 保留 Git 日志、能力归纳和修复记录

2. `doc/docs/*.mdx`
   - 作为文档站消费层
   - 使用 Mintlify frontmatter 和组件

## 页面拆分

文档站侧新增 3 个页面：

- `doc/docs/skills-daily-update-log.mdx`
- `doc/docs/skills-new-capabilities.mdx`
- `doc/docs/skills-frontend-bugfix-log.mdx`

分别对应：

- 每日更新
- 新增能力
- 前端与修复

## 导航设计

在 `doc/docs.json` 的“文档中心”下新增“技能迭代”分组，统一承接这类产品/技能演进记录。

## 链接关系

### 从文档站回链到工程事实

每个 `.mdx` 页面顶部通过说明块指向原始 `openspec` 文件。

### 从工程记录回链到文档站

原始 `openspec/changes/sync-skills-from-gitlab/tasks.md` 增加说明，记录文档站镜像页面与本 change。

## 不做的事

- 不将 `doc/openspec/changes` 直接接入 Mintlify 主导航
- 不把工程执行细节全部搬进文档站
- 不改变原始 openspec change 的事实边界
