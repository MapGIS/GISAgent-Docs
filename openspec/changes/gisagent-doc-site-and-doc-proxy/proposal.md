# 提案：GIS Agent 文档站与 `/doc` 反向代理接入

## 背景

当前 `/home/maptex/Code/xcsmartdatabase/doc` 目录原先为空，缺少一个可持续维护的文档站工程。

同时，已有域名入口中存在以下现实需求：

1. 需要基于最新 Mintlify 工程结构搭建一个文档站
2. 需要把站点品牌统一为 `GIS Agent`
3. 需要支持中文化与多 Tab 导航
4. 需要让 `http://gisagent.smaryun.com/doc` 可以访问当前文档站

在执行过程中还发现一个重要事实：

- 当前工作机上真正对外接流量的 Nginx 容器并不是仓库内 `nginx/docker-compose.yml` 对应的 `gisagent-nginx`
- 实际运行的是本机 Docker 容器 `nginx-proxy`
- 其生效配置来自宿主机路径 `/home/maptex/docker/nginx/conf.d/main.conf`

因此，这次工作实际上分成两个部分：

1. 在仓库 `doc/` 下创建并调整 Mintlify 文档站
2. 在当前工作机上把 `/doc` 路由接到本地 Mintlify 预览进程

## 问题陈述

当前系统缺少以下正式能力：

- 缺少 `GIS Agent` 对应的文档站工程
- 缺少文档站品牌资源、中文导航和多 Tab 信息架构
- 缺少针对 `/doc` 子路径的本机代理配置记录
- 缺少对“仓库内 Nginx 配置”和“当前机器实际生效配置”差异的明确说明

## 目标

本 change 的目标是：

1. 在 `doc/` 下建立最新 Mintlify 工程结构
2. 将站点标题统一为 `GIS Agent`
3. 完成主要页面中文化
4. 把左侧导航重组为多 Tab 模式
5. 统一 logo、favicon 与主色调
6. 记录 `/doc` 反向代理的本机接入过程与已知限制

## 范围内

- `doc/docs.json`
- `doc/*.mdx`
- `doc/logo/*`
- `doc/favicon.svg`
- 文档站本地预览启动
- 当前工作机 `nginx-proxy` 的 `/doc` 本机接入记录
- 仓库内 `nginx/` 相关配置更新记录

## 范围外

- 阿里云公网服务器实际配置修改确认
- `gisagent.smaryun.com` 域名公网入口的最终归属排查
- `/doc` 的静态正式部署
- 最终 closeout 所需的公网集成验收

## 成功标准

1. `doc/` 下存在可运行的 Mintlify 文档工程
2. 文档站标题为 `GIS Agent`
3. 主体页面完成中文化
4. 导航切换为多 Tab
5. logo / favicon / 主色调统一
6. 本机 `Host: gisagent.smaryun.com` 条件下，`/doc/` 可以命中文档站
7. 文档明确记录：当前验证仅覆盖本机，不代表阿里云公网入口已同步完成
