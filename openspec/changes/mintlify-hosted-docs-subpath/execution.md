# 执行记录：Mintlify 托管与 `/docs` 正式入口

## 执行日期

- 2026-06-16

## 当前执行内容

### 1. 方案确认

确认本次正式方案采用：

- Mintlify 托管
- 自定义域名
- `Host at /docs`
- `gisagent.smaryun.com/docs`

而不再沿用：

- 本机 `mint dev` + `/doc` 开发代理
- `mint export` 静态站直接承载 Mintlify 搜索 / Assistant

### 2. 与既有 change 的关系判断

确认当前已有 change：

- `gisagent-doc-site-and-doc-proxy`

主要记录：

- 文档站建设
- 本机 `/doc` 开发代理
- 历史公网入口排查

不适合直接扩展为 Mintlify 正式托管方案，因此新建独立 change。

### 3. 确认 Mintlify 实际托管上游

在当前托管状态下确认：

- `https://mapgis.mintlify.app/` 可正常访问当前仓库内容

因此将当前 `/docs` 反代目标统一确定为：

- `mapgis.mintlify.app`

### 4. 同步本地部署模板目录

已对本地目录：

- `/home/maptex/Code/xcsmartdatabase/doc/deploy/nginx-20260602_164043`

执行以下调整：

- 将旧的 `/doc -> 本地 docs_backend` 配置改为 `/docs -> mapgis.mintlify.app`
- 新增 `/.well-known/` 反代规则
- 在 `nginx.conf` 中增加 `resolver`
- 更新 `README.md`、`manifest.txt`、`deploy.sh`
- 删除旧备份文件 `nginx/gisagent.conf~`

### 5. 同步阿里云目录

已将以下文件同步到阿里云：

- `/opt/nginx/nginx-20260602_164043/nginx/gisagent.conf`
- `/opt/nginx/nginx-20260602_164043/nginx/nginx.conf`
- `/opt/nginx/nginx-20260602_164043/README.md`
- `/opt/nginx/nginx-20260602_164043/manifest.txt`
- `/opt/nginx/nginx-20260602_164043/deploy.sh`

并删除远端旧备份文件：

- `/opt/nginx/nginx-20260602_164043/nginx/gisagent.conf~`

### 6. 当前关键状态说明

当前远端目录内容已经更新，但尚未自动生效到运行中的 Nginx 容器。

原因是：

- 当前阿里云 `docker-compose.yml` 使用的是镜像内配置
- 并未通过 volume 挂载宿主机目录中的 `nginx/*.conf`

因此后续仍必须执行：

1. 基于新目录重建 `gisagent-nginx:latest`
2. 在阿里云执行 `docker compose down && docker compose up -d`

### 7. 阿里云重启后的现场现象

后续已在阿里云目录中执行现有 `deploy.sh`，完成：

- 镜像加载
- `docker compose` 重启

现场验证结果显示：

- `Host: gisagent.smaryun.com` 条件下，`GET /docs` 可返回 `200`
- 但 `localhost/nginx-health` 与 `localhost/docs` 会落到默认站点并返回 `404`

进一步判断原因为：

- 站点配置中包含 `localhost`
- 且容器内仍有默认站点配置参与匹配
- 导致基于 `localhost` 的健康检查和本地验证不稳定

因此补充修正为：

1. 反代 server 使用 `default_server`
2. 移除 `server_name` 中的 `localhost`
3. 所有健康检查与验证命令统一带 `Host: gisagent.smaryun.com`

### 8. 同步最后一轮运行态修正

已将以下最新文件再次同步到阿里云：

- `/opt/nginx/nginx-20260602_164043/nginx/gisagent.conf`
- `/opt/nginx/nginx-20260602_164043/docker-compose.yml`
- `/opt/nginx/nginx-20260602_164043/deploy.sh`

本轮同步的关键修正为：

- `listen 80 default_server`
- `listen [::]:80 default_server`
- `server_name` 去除 `localhost`
- `docker-compose.yml` 健康检查强制带 `Host: gisagent.smaryun.com`
- `deploy.sh` 的 `/nginx-health`、`/`、`/martin/`、`/docs` 验证全部改为 Host 头校验

### 9. 阿里云重建与重启

已在阿里云执行：

1. `cd /opt/nginx/nginx-20260602_164043`
2. `bash deploy.sh`

执行结果：

- 成功加载 `images/docker-images.tar.gz`
- 成功重建并启动 `gisagent-nginx`
- 容器状态从 `health: starting` 转为 `healthy`

### 10. 本轮现场验证结果

阿里云主机内验证：

- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/nginx-health` 返回 `200 OK`
- `curl -I -H 'Host: gisagent.smaryun.com' http://127.0.0.1/docs` 返回 `200 OK`
- `docker compose -f /opt/nginx/nginx-20260602_164043/docker-compose.yml ps` 显示 `healthy`

公网验证：

- `curl -I http://gisagent.smaryun.com/docs` 返回 `200 OK`

### 11. 新一轮线上故障与修正

后续再次观察到公网 `http://gisagent.smaryun.com/docs` 被跳转到：

- `/manager/login?forbidden=1&redirect=/docs`

该现象最终确认不是 Mintlify 引起，而是运行中的 `gisagent-nginx` 容器仍使用镜像内旧版 `gisagent.conf`，导致 `/docs` 实际回落到了主站 `/` 代理。

本轮处理分为三步：

1. 将 `docker-compose.yml` 改为直接挂载宿主机 `nginx.conf` 与 `gisagent.conf`
2. 强制 `docker compose down && docker compose up -d --force-recreate`
3. 校正 Mintlify 上游与 `proxy_pass` 写法

### 12. 上游与转发路径修正

现场进一步确认：

- `mapgis.mintlify.dev/docs` 返回 `404`
- `mapgis.mintlify.app/docs` 才是当前真实可访问的托管站入口

因此将：

- `set $mintlify_docs_host mapgis.mintlify.dev;`

改为：

- `set $mintlify_docs_host mapgis.mintlify.app;`

同时发现旧写法：

- `proxy_pass $mintlify_docs_origin/docs;`
- `proxy_pass $mintlify_docs_origin/docs/;`

会导致 `/docs` 与 `/docs/product-overview` 间的循环跳转，因此统一修正为保留原始 URI 的：

- `proxy_pass $mintlify_docs_origin;`

### 13. 主应用 `/` 路径修正

后续又确认主应用站点必须继续由阿里云上的主应用容器承载：

- 容器名：`mapgis-ai-gisagent`
- 镜像：`mapgis-ai-gisagent:latest`
- 端口：`3000`

此前 `/` 发生 `502 Bad Gateway` 的原因有两点：

1. Nginx 上游名称误写为 `gisagent:3000`
2. `/` 路由使用变量 `proxy_pass $gisagent_upstream`，触发了全局 `resolver` 通过公网 DNS 解析 `gisagent`

因此将主应用上游修正为：

- `upstream gisagent_backend { server mapgis-ai-gisagent:3000; }`

并将 `/` 代理修正为：

- `proxy_pass http://gisagent_backend;`

这样可确保：

- `http://gisagent.smaryun.com/` 继续进入主应用
- `http://gisagent.smaryun.com/docs` 独立进入 Mintlify 托管文档

### 14. Mintlify 根路径静态资源修正

浏览器侧进一步发现：

- 文档页 HTML 中输出的 CSS / JS / favicon 资源并不位于 `/docs/...`
- 而是使用绝对根路径：
  - `/mintlify-assets/...`
  - `/llms.txt`
  - `/llms-full.txt`
  - `/sitemap.xml`

此前这些路径未单独代理时，会落入主应用 `/` 代理，导致资源类型错误或页面资源缺失。

因此补充以下 Nginx 转发：

1. `location ^~ /mintlify-assets/`
2. `location = /llms.txt`
3. `location = /llms-full.txt`
4. `location = /sitemap.xml`

以上路径统一反代到：

- `https://mapgis.mintlify.app`

### 15. HTTPS 现状确认

针对浏览器报错中的：

- `https://gisagent.smaryun.com/... ERR_CONNECTION_REFUSED`

现场确认阿里云当前仅监听：

- `0.0.0.0:80`
- `[::]:80`

尚未监听：

- `443`

因此当前结论是：

- `http://gisagent.smaryun.com/...` 已修复可用
- `https://gisagent.smaryun.com/...` 仍不可用，原因是当前未配置 TLS 监听与证书

### 16. HTTPS 证书与 443 监听落地

随后已在阿里云主机执行：

1. 安装 `certbot`
2. 短暂停止 `gisagent-nginx`
3. 使用 `certbot certonly --standalone --preferred-challenges http -d gisagent.smaryun.com`
4. 成功签发证书：
   - `/etc/letsencrypt/live/gisagent.smaryun.com/fullchain.pem`
   - `/etc/letsencrypt/live/gisagent.smaryun.com/privkey.pem`

证书有效期至：

- `2026-09-14`

随后对部署模板补充：

1. `docker-compose.yml` 增加 `443:443` 端口映射
2. 挂载 `/etc/letsencrypt:/etc/letsencrypt:ro`
3. `gisagent.conf` 增加：
   - `listen 443 ssl http2`
   - `ssl_certificate`
   - `ssl_certificate_key`
   - 基础 TLS 会话参数

完成后重新启动 `gisagent-nginx`，阿里云现场确认：

- `0.0.0.0:443` 已监听
- `[::]:443` 已监听
- 容器状态为 `healthy`

## 后续待执行

- Mintlify Dashboard 自定义域名配置
- DNS 验证
- 页面刷新 / 深链接验收
- 静态资源加载验收
- 公网搜索 / Assistant 验收
