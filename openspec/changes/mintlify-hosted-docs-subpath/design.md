# 设计：Mintlify 托管与 `gisagent.smaryun.com/docs` 正式接入

## 摘要

本设计将正式部署方案拆成四个阶段：

1. **托管接入阶段**：将当前 GitHub 仓库接入 Mintlify
2. **域名阶段**：在 Mintlify Dashboard 配置自定义域名并启用 `Host at /docs`
3. **反代阶段**：通过现有 Nginx 将 `/docs` 反代到 `*.mintlify.dev`
4. **验收阶段**：在公网验证页面、搜索、Assistant 和资源加载链路

## 当前观察结论

### 1. 当前静态导出方案的能力边界

当前 `mint export` + `nginx` 方案适合：

- 静态浏览
- Docker 独立部署
- 内网分发

但不适合直接承载：

- Mintlify 平台搜索
- Mintlify Assistant
- Dashboard 驱动的托管能力

### 2. Mintlify `/docs` 子路径的官方能力边界

Mintlify 官方支持通过：

- 自定义域名
- `Host at /docs`
- 反向代理到 `*.mintlify.dev`

来提供 `/docs` 子路径的正式站点。

而自定义非标准子路径（例如 `/doc`）属于另一类能力，不在本次方案内。

### 3. 当前正式目标路径

本次正式目标路径统一为：

- `https://gisagent.smaryun.com/docs`

而不是：

- `https://gisagent.smaryun.com/doc`

## 托管设计

### 上游形态

Mintlify 托管完成后，将获得一个托管子域：

- `https://<project-subdomain>.mintlify.dev`

该地址作为反向代理的唯一上游。

### 内容来源

内容继续以当前仓库为准：

- GitHub 仓库：`MapGIS/GISAgent-Docs`

后续流程为：

1. 提交文档变更到仓库
2. Mintlify 自动触发部署
3. 托管站点自动更新

## 域名与 DNS 设计

### 域名目标

- 正式域名：`gisagent.smaryun.com`
- 正式子路径：`/docs`

### Dashboard 配置

在 Mintlify Dashboard 中执行：

1. 添加自定义域名 `gisagent.smaryun.com`
2. 开启 `Host at /docs`
3. 获取 TXT 验证记录
4. 获取 CNAME 指向 `cname.mintlify.builders`

### DNS 目标

预期需要：

- TXT 记录用于域名验证
- CNAME 记录用于接入 Mintlify

## Nginx 反代设计

### 反代目标

将：

- `https://gisagent.smaryun.com/docs`

转发到：

- `https://<project-subdomain>.mintlify.dev/docs`

### 核心要求

代理配置必须满足：

1. 使用 `.mintlify.dev` 上游
2. 放行 `/.well-known/` 验证路径
3. 不透传自定义 `Host` 到上游
4. 传递 `Origin`、`X-Forwarded-For`、`X-Forwarded-Proto`、`X-Real-IP`、`User-Agent`

### 参考结构

建议提供三类 location：

1. `location = /docs`
2. `location /docs/`
3. `location ^~ /.well-known/`

## 验收设计

### 页面链路

需要验证：

- `/docs`
- `/docs/`
- `/docs/quickstart`
- `/docs/_next/...`

### 功能链路

需要验证：

- 顶部搜索可用
- Assistant 可用
- 跳转与刷新可用
- 页面资源不丢失

### 非目标

本 change 不负责：

- `/doc` 与 `/docs` 双路径兼容
- 本地静态 Docker 方案搜索增强

