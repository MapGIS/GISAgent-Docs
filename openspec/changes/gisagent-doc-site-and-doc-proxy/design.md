# 设计：GisAgent 文档站与 `/doc` 本机代理链路

## 摘要

本设计将此次工作拆成两条主线：

1. **文档站主线**：使用最新 Mintlify `docs.json` 工程结构，在 `doc/` 下创建可维护的 `GisAgent` 文档站
2. **代理接入主线**：在当前工作机本机 Nginx 运行态中把 `/doc` 接到本地 `mint dev` 预览

## 当前观察结论

### 1. `bakup/meoo` 的前端技术判断

通过导出页面反推，`bakup/meoo` 使用的是：

- Mintlify
- Next.js
- React
- MDX
- Tailwind CSS
- Turbopack

因此文档站复刻方向应优先使用 Mintlify，而不是手写一套普通静态站。

### 2. Mintlify 当前工程格式

本次以当前官方 starter 结构为准，核心格式为：

- `docs.json`
- `.mdx` 页面
- `logo/`、`favicon.svg` 等静态资源

### 3. 当前工作机上的真实代理入口

本机验证时发现：

- 仓库内 `nginx/docker-compose.yml` 对应的 `gisagent-nginx` 容器并未占用公网 `80/443`
- 当前实际承接外部 `80/443` 的容器是 `nginx-proxy`
- 该容器挂载了：
  - `/home/maptex/docker/nginx/conf.d`
  - `/home/maptex/docker/nginx/nginx.conf`

因此：

- 修改仓库内 `nginx/` 配置只能作为“预期配置更新”
- 真正影响当前本机访问链路的，是 `/home/maptex/docker/nginx/conf.d/main.conf`

## 文档站设计

### 信息架构

站点名称：

- `GisAgent`

导航采用 `navigation.tabs`：

1. `开始使用`
2. `架构设计`

页面包括：

- `index.mdx`
- `quickstart.mdx`
- `system-overview.mdx`
- `component-roles.mdx`
- `runtime-flow.mdx`
- `constraints-and-direction.mdx`

### 视觉设计

品牌统一为蓝色系：

- `primary`: `#2979ff`
- `light`: `#5aa0ff`
- `dark`: `#1565c0`

logo 与 favicon 统一采用蓝色地球图标。

## `/doc` 代理设计

### 上游

本地 Mintlify 预览：

- `http://localhost:3000`

从 Docker Nginx 容器访问宿主机时使用：

- `http://172.17.0.1:3000`

### 路由处理

由于 Mintlify 预览运行在根路径 `/`，而对外需要挂到 `/doc`，因此本机代理需要做两件事：

1. 把请求路径 `/doc/...` 改写为上游根路径 `/...`
2. 将 HTML 中的根路径静态资源引用改写为 `/doc/...`

### 当前实现方式

在本机实际生效配置里，对 `/doc` 使用了：

- `rewrite ^/doc/(.*)$ /$1 break;`
- `proxy_pass http://172.17.0.1:3000/;`
- `sub_filter` 处理 `href="/`、`src="/`、`content="/``
- 注入 `<base href="/doc/">`

### 已知限制

这套 `/doc` 代理目前依赖：

- 本地 `mint dev` 进程必须持续运行

因此它更像“开发预览接入”，不是正式静态部署。

## 验收边界

按 openspec 的严格口径，本 change 目前只完成了：

- 本机开发态验证
- 本机 Docker/Nginx 链路验证

尚未完成：

- 公网真实域名链路验证
- 阿里云服务器侧一致性验证
- 静态正式部署验收
