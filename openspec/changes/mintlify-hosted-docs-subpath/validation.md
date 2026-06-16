# 验证记录：Mintlify 托管与 `/docs` 正式入口

## 验证范围

本 change 最终需要覆盖：

1. Mintlify 托管部署是否成功
2. `gisagent.smaryun.com/docs` 是否正确反代
3. 搜索与 Assistant 是否在公网正式入口可用

## 当前已完成

### A. 方案层验证

已确认：

- Mintlify 官方支持 `Host at /docs`
- `*.mintlify.dev` 可作为 `/docs` 反代上游
- 自定义非标准子路径 `/doc` 不属于本次目标方案

### B. Mintlify 托管上游确认

已确认：

- `https://mapgis.mintlify.app/` 可访问当前仓库内容

因此当前反代上游已明确为：

- `mapgis.mintlify.app`

### C. 本地与远端目录一致性

已确认以下远端文件内容已同步：

- `nginx/gisagent.conf`
- `nginx/nginx.conf`
- `README.md`
- `manifest.txt`
- `deploy.sh`

同步后的远端配置中已可检出：

- `set $mintlify_docs_host mapgis.mintlify.app;`
- `/docs`
- `resolver 1.1.1.1 8.8.8.8`

### D. 阿里云现场重启后验证

已观察到：

- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/docs` 返回 `200`

也观察到：

- `curl -I http://127.0.0.1/nginx-health` 返回 `404`
- `curl -I http://127.0.0.1/docs` 返回 `404`

当前判断为：

- `/docs` 正常链路需要显式的 `Host: gisagent.smaryun.com`
- 基于 `localhost` 的健康检查方式不可靠，需调整部署模板

### E. 运行态修正后的二次验证

已完成以下修正：

- Nginx `server` 改为 `default_server`
- `server_name` 移除 `localhost`
- Docker 健康检查改为显式发送 `Host: gisagent.smaryun.com`
- 部署脚本验证命令统一改为显式发送 `Host: gisagent.smaryun.com`

修正后二次验证结果：

- `docker compose -f /opt/nginx/nginx-20260602_164043/docker-compose.yml ps`
  显示 `gisagent-nginx` 为 `healthy`
- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/nginx-health`
  返回 `200 OK`
- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/docs`
  返回 `200 OK`
- `curl -I http://gisagent.smaryun.com/docs`
  返回 `200 OK`

### F. 公网登录跳转故障复盘

后续再次发现：

- `http://gisagent.smaryun.com/docs`
  被重定向到
- `/manager/login?forbidden=1&redirect=/docs`

最终验证结论：

- 这不是 Mintlify 的响应
- 而是 Nginx 运行态仍使用镜像内旧配置，导致 `/docs` 落入主站代理

修正后再次验证：

- `docker inspect gisagent-nginx` 已显示宿主机 `nginx.conf` 与 `gisagent.conf` 单文件挂载
- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/docs`
  返回 `307 Temporary Redirect`
- `Location: /docs/product-overview`
- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/docs/product-overview`
  返回 `200 OK`

### G. 当前公网入口状态

当前公网入口验证结果：

- `curl -I -L http://gisagent.smaryun.com/docs`
  首先返回 `307` 到 `/docs/product-overview`
- 随后 `http://gisagent.smaryun.com/docs/product-overview`
  返回 `200 OK`

说明：

- 主站登录拦截已解除
- `/docs` 当前已进入 Mintlify 托管站
- 当前有效上游应以 `mapgis.mintlify.app` 为准，而不是 `mapgis.mintlify.dev`

### H. 主应用与文档并存验证

后续根据阿里云现场容器信息进一步确认：

- 主应用容器名为 `mapgis-ai-gisagent`
- 主应用监听 `3000`

修正主应用上游后验证结果：

- `curl -I -L http://gisagent.smaryun.com/`
  首先返回 `302 Location: /gis/`
- 随后 `http://gisagent.smaryun.com/gis/`
  返回 `200 OK`
- `curl -I -L http://gisagent.smaryun.com/docs`
  返回 Mintlify 文档站跳转到 `/docs/product-overview`
- `curl -I http://gisagent.smaryun.com/docs/product-overview`
  返回 `200 OK`

说明当前行为已经满足：

- 主应用站点 `/` 可访问
- 文档入口 `/docs` 可访问
- 两条路径已由 Nginx 正确分流

### I. Mintlify 静态资源验证

已从文档页 HTML 中确认：

- 资源链接使用绝对根路径 `/mintlify-assets/...`

补充资源代理后验证结果：

- `curl -I http://gisagent.smaryun.com/mintlify-assets/_next/static/chunks/9ffc684b9a12d113.css?...`
  返回 `200 OK`
- `Content-Type: text/css; charset=utf-8`
- `curl -I http://gisagent.smaryun.com/llms.txt`
  返回 `200 OK`

说明：

- 文档页静态 CSS / JS / favicon 链路已切通
- Mintlify 根路径元数据文件已切通

### J. HTTPS 现状验证

已验证：

- `curl -I https://gisagent.smaryun.com/`
  连接失败
- `curl -I https://gisagent.smaryun.com/mintlify-assets/...`
  连接失败

阿里云现场端口监听确认：

- 仅监听 `80`
- 未监听 `443`

因此当前结论为：

- `ERR_CONNECTION_REFUSED` 的直接原因不是 Mintlify 页面资源地址本身
- 而是 `gisagent.smaryun.com` 当前尚未部署 HTTPS 监听

### K. HTTPS 修复后验证

后续已完成 HTTPS 证书与 443 监听配置，再次验证结果：

- `curl -Ik https://gisagent.smaryun.com/`
  返回 `302 Location: /gis/`
- `curl -Ik https://gisagent.smaryun.com/docs`
  返回 `307 Location: /docs/product-overview`
- `curl -Ik https://gisagent.smaryun.com/mintlify-assets/_next/static/chunks/9ffc684b9a12d113.css?...`
  返回 `200 OK`
- 资源响应头包含：
  - `Content-Type: text/css; charset=utf-8`

阿里云端口监听确认：

- `80` 已监听
- `443` 已监听

因此当前结论更新为：

- `https://gisagent.smaryun.com/` 可访问
- `https://gisagent.smaryun.com/docs` 可访问
- `https://gisagent.smaryun.com/mintlify-assets/...` 可访问
- 浏览器中此前的 `ERR_CONNECTION_REFUSED` 已具备被消除的服务端条件

## 当前未完成

### 1. Dashboard 域名验证

尚未完成 `gisagent.smaryun.com` 的域名验证。

### 2. 深链接与静态资源验证

尚未验证：

- `http://gisagent.smaryun.com/docs/_next/...`
- `http://gisagent.smaryun.com/docs/quickstart`
- 浏览器刷新深链接是否稳定

### 3. 功能验证

尚未验证：

- 全文搜索
- Assistant
