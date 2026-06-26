# 执行记录：同步技能变更与 Mintlify 文档联动

## 已执行动作

### 1. 文档站页面落地

新增以下 Mintlify 页面：

- `doc/docs/skills-daily-update-log.mdx`
- `doc/docs/skills-new-capabilities.mdx`
- `doc/docs/skills-frontend-bugfix-log.mdx`

### 2. 导航接入

在 `doc/docs.json` 中新增“技能迭代”分组，将上述 3 个页面接入文档中心导航。

### 3. 文档侧 change 建立

新增：

- `doc/openspec/changes/sync-skills-from-gitlab-doc-linkage/`

用于记录本次从工程记录到文档站页面的联动关系。

### 4. 工程侧回链

在：

- `openspec/changes/sync-skills-from-gitlab/tasks.md`

中补充文档站镜像页面与文档侧 change 的说明。

## 当前结果

当前已经形成两层稳定入口：

1. 工程事实入口：`openspec/changes/sync-skills-from-gitlab`
2. 文档站阅读入口：`doc/docs/*.mdx`
