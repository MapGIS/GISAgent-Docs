# 统一更新日志

## 汇总说明

- 汇总日期：2026-07-20
- 状态截止：2026-07-20
- 来源文件：
  - `openspec/changes/sync-skills-from-gitlab/clis-detailed-update-log.md`
  - `gisagent/CHANGELOG.md`
  - `/home/maptex/Code/xcsmartdatabase/skills` Git 提交与实际文件变更
- 说明：
  - 本文件是 `sync-skills-from-gitlab` 当前固定产物。
  - 汇总范围固定为 `clis/`、`gisagent/` 与 `skills/`。
  - 这不是逐个 `SKILL.md` 自动生成的全量更新日志。
  - 若某个来源在本轮无新增条目，必须显式写明。

## 本轮结论

- `clis/`：
  - 截至 2026-07-20，当前固定来源仍是 `clis-detailed-update-log.md`。
  - 既有整理稿覆盖范围为 **2026-06-10 至 2026-06-25**。
  - **2026-06-25 之后，本轮有新增提交条目。**
  - 新增内容主要集中在 `3dtiles_cli`、`knowledge_cli`、`postgis_service_cli`，并新增 `geomoder_cli`。
- `gisagent/`：
  - 截至 2026-07-20，当前固定来源仍是 `gisagent/CHANGELOG.md`。
  - 当前最新版本记录仍为 `0.1.3`。
  - **本轮没有看到高于 `0.1.3` 的新增版本条目。**
- `skills/`：
  - 截至 2026-07-20，当前固定来源已纳入 `/home/maptex/Code/xcsmartdatabase/skills`。
  - **本轮有 2026-07-20 的新增提交条目。**
  - 这批更新集中在代理约束、运行环境、打包脚本和忽略规则整理。

## 更新概览

- **3D Tiles 工具链已经成型**：`clis/` 侧已补齐生成、发布、自动发现和前端预览这一条主链路。
- **知识图谱能力继续收敛**：知识图谱渲染质量提升，技能触发规则更严格，误调用更少。
- **`clis/` 在 2026-07-20 前仍持续演进**：3D Tiles 增加 OBJ 分片与地质网格支持，知识图谱补入海事知识，PostGIS 3D Tiles 自动发现与目录工具继续扩展。
- **GIS Agent 已进入可运维阶段**：会话持久化、停止生成、路由调整和管理界面能力已经落地。
- **`skills/` 工作区在 2026-07-20 有明确增量**：代理仓库补写 Git 路由规则，补齐环境文件、部署脚本模板和运行时刷新脚本。
- **`gisagent/` 截至 2026-07-20 无新的版本增量**：本轮增量主要来自 `clis/` 和 `/skills` 工作区。

---

## clis/

### 本轮状态

- 来源文件：`openspec/changes/sync-skills-from-gitlab/clis-detailed-update-log.md`
- 已整理稿覆盖区间：2026-06-10 至 2026-06-25
- 截至 2026-07-20 的结论：
  - **本轮有新增条目**
  - `clis-detailed-update-log.md` 还没有吸收 2026-06-26 至 2026-07-20 的增量
  - 新增重点包括 3D Tiles 建模增强、知识图谱与海事知识扩展、PostGIS 3D Tiles 自动发现增强，以及 `geomoder_cli` 新增

### 2026-06-26 至 2026-07-20 增量摘要

#### `3dtiles_cli`

- `2026-06-26`：
  - `7373887` 使用 `ogr2ogr` 处理 shapefile 矢量
  - `14ad61d` 更新 Docker 环境
- `2026-07-03`：
  - `92b46e9` 新增 OBJ 分片制瓦与地质网格支持
- `2026-07-16`：
  - `12ff913` 修复无纹理 OBJ 的 UV 坐标保留问题

#### `knowledge_cli`

- `2026-06-29`：
  - `94aa42b` 更新 `knowledge-mcp` 和 `graph-g6-render`
- `2026-07-08`：
  - `3676308` 补入海事知识数据与相关技能内容
- `2026-07-20`：
  - `779bd86` 同步本地变更

#### `postgis_service_cli`

- `2026-06-26`：
  - `e6ce584` 同步 PostGIS 服务技能与 3D Tiles 指引
- `2026-06-29`：
  - `a354325` 更新 materials catalog 和 `postgres-3dtiles-source`
- `2026-07-08`：
  - `b6ec828` 扩展 3D Tiles 自动发现与 catalog tooling
  - 同日连续提交补齐 `hk260702` 管线/阀门 3D Tiles 数据准备与显示修正
- `2026-07-20`：
  - `b7225d8` 同步本地变更

#### `geomoder_cli`

- `2026-07-03`：
  - `0ed380a` 初始导入 `geomoder_cli`
- `2026-07-16`：
  - `1341aca` 改进地质体建模流水线
- `2026-07-17`：
  - `7559bce` 修复可选 Docker 依赖

#### `postgiscli`

- `2026-06-29`：
  - `d4fd258` 更新 Dockerfile 与技能文档
- `2026-07-20`：
  - `14e33a3` 同步本地变更

### 最近一次已整理更新

#### 2026-06-25

**完善「3D Tiles 工具链」**：新增独立 CLI、默认导出优化和 Docker 构建环境补齐。3D Tiles 相关能力从零散脚本整理为稳定工具入口。

**扩展「3D Tiles 自动发现与预览」**：地图服务继续补齐自动发现、目录入口和前端预览链路，减少手工配置成本。

#### 2026-06-24

**新建「3D Tiles 独立工具链」**：`3dtiles_cli` 初始化完成，后续 3D Tiles 能力可以独立迭代和调用。

#### 2026-06-23

**收紧「知识技能触发规则」**：非知识查询场景下降低误触发，技能路由更稳定。

#### 2026-06-17

**新增「3D Tiles 可重复导入流水线」**：面向大陆城市数据建立可重复导入流程，便于批量三维数据准备。

#### 2026-06-16

**上线「3D Tiles 发布与 Cesium 预览」**：地图服务支持发布 3D Tiles 并直接预览，同时补上安全校验和测试链路。

#### 2026-06-14

**优化「知识图谱渲染与校验」**：增强技能路由约束并补齐结果校验，知识图谱输出更一致。

#### 2026-06-11

**优化「知识图谱 G6 渲染」**：图谱展示质量提升，更适合直接生成 HTML 结果。

**收敛「地图样式指引」**：统一 MapLibre 网关样式和 sprite 路径说明，减少配置漂移。

#### 2026-06-10

**修复「Docker 环境变量配置」**：修正容器内变量和样式资源引用，降低部署偏差。

## gisagent/

### 本轮状态

- 来源文件：`gisagent/CHANGELOG.md`
- 截至 2026-07-20 的结论：
  - **本轮无新增版本条目**
  - 当前最新版本仍为 `0.1.3`

### 当前最新版本摘要

#### 0.1.3

**完善「Web 路由与双界面入口」**：根路径默认跳转到 `/gis/`，管理界面迁移到 `/manager/`，用户侧 GIS 页面和管理页分工更清晰。

**新增「对话停止与会话持久化」**：支持停止生成、会话 SQLite 持久化、会话重连与流式快照恢复，长会话更可控。

**补齐「管理与 GIS 工作台能力」**：新增 agent 预设持久化、会话重命名置顶、Web 管理界面、GIS 地图预览和文件浏览。

#### 0.1.2

**新增「思考过程转发控制」**：可选把 agent thinking 实时转发到微信，并保留终端调试输出。

#### 0.1.1

**优化「会话存活与输入反馈」**：默认空闲超时延长到 24 小时，并补齐 typing indicator 的开始与结束控制。

#### 0.1.0

**上线「基础微信 Agent 运行框架」**：支持微信扫码登录、按用户隔离 agent 会话、后台守护、配置文件和内置 agent 预设。

## skills/

### 本轮状态

- 来源：`/home/maptex/Code/xcsmartdatabase/skills`
- 检查方式：Git 提交记录 + 实际变更文件
- 截至 2026-07-20 的结论：
  - **本轮有新增条目**
  - 最近一组更新集中在 `2026-07-20`
  - 重点不是新增单个地图技能，而是收紧运行约束、补齐环境与打包链路

### 2026-07-20

#### `7956a68` `docs: declare proxy 7897 and code.maptex.top route`

- 在 `agents/qoder/AGENTS.md` 中补写 Git 网络约定：
  - Git 访问统一走 `proxy 7897`
  - 远端默认走 `http://code.maptex.top`
- 同步调整工作区级 `config` / `doc` 入口引用，减少多仓协作时的路由漂移

#### `29ca6a0` `feat:update env`

- 新增 `.env`，补齐地形、3D Tiles 自动发布和覆盖配置
- 扩展 `docker-compose.yml`、`package.sh` 和打包模板，补齐部署入口
- 新增并增强以下运行脚本：
  - `scripts/package-templates/deploy.sh`
  - `scripts/package-templates/refresh-agent-prompts.sh`
  - `scripts/refresh-postgis-gateway.sh`
  - `scripts/sync-skills-from-gitlab.sh`
- 这组变更的直接意义是：
  - 技能工作区的运行环境不再只靠人工约定
  - 打包、部署、网关刷新和 skillpacks 同步有了更完整的脚本骨架

#### `dfb4a47` `feat:update gitignore`

- 调整 `.gitignore`
- 目标是收敛工作区噪声，避免环境产物和无关文件持续进入版本控制视野
