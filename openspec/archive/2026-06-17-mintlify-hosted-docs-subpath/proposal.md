# 提案：GIS Agent 文档站接入 Mintlify 托管与 `/docs` 正式入口

## 背景

当前仓库已经具备：

1. 可维护的 Mintlify 文档工程
2. 本地 `mint dev` 预览能力
3. 静态导出与 Docker 部署能力

但实际验证表明：

- `export-site + nginx` 的静态部署不能直接获得 Mintlify 平台搜索与 Assistant 能力
- 现有 `/doc` 本机代理 change 主要面向开发验证，不适合作为正式公网方案

与此同时，当前期望的正式访问形式是：

- `https://gisagent.smaryun.com/docs`

因此需要引入一条新的正式交付路径：

1. 文档内容继续保存在当前 GitHub 仓库
2. 文档站由 Mintlify 托管
3. 通过自定义域名与反向代理，将公网入口统一到 `gisagent.smaryun.com/docs`

## 问题陈述

当前系统缺少以下正式能力：

- 缺少 Mintlify 托管接入记录
- 缺少 Mintlify Dashboard 配置步骤记录
- 缺少 `Host at /docs` 子路径托管方案
- 缺少 `gisagent.smaryun.com/docs` 的 DNS 与 Nginx 反代方案
- 缺少对“正式搜索 / Assistant 可用性”的公网验收标准

## 目标

本 change 的目标是：

1. 将当前文档仓库接入 Mintlify 托管
2. 获取可持续自动部署的 Mintlify 托管子域
3. 为正式入口启用 `Host at /docs`
4. 将 `gisagent.smaryun.com/docs` 反代到 Mintlify 托管子域
5. 在正式入口验证全文搜索与 Assistant 可用

## 范围内

- Mintlify GitHub App 接入步骤记录
- Mintlify Dashboard 域名与 `/docs` 配置
- DNS 验证要求记录
- `gisagent.smaryun.com/docs` 的 Nginx 反代配置
- Mintlify 托管后的公网功能验证

## 范围外

- 旧 `/doc` 开发代理链路替换历史
- 现有静态 Docker 方案下的本地搜索增强实现
- Mintlify Enterprise 的自定义子路径 `/doc` 方案

## 成功标准

1. 当前文档仓库已接入 Mintlify 托管
2. Mintlify Dashboard 中已启用 `Host at /docs`
3. `gisagent.smaryun.com/docs` 可访问托管文档站
4. 公网入口下全文搜索可用
5. 公网入口下 Assistant 可用
6. 文档中明确记录 DNS、代理与验收过程

