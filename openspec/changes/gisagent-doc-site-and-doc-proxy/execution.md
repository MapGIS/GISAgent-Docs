# 执行记录：GIS Agent 文档站与 `/doc` 本机代理

## 执行日期

- 2026-06-12

## 实际执行内容

### 1. 分析 `bakup/meoo`

确认该目录只包含保存下来的页面和打包资源，不是可继续开发的前端源码工程。

判断结论：

- Mintlify
- Next.js
- React
- MDX
- Tailwind CSS

### 2. 初始化 `doc/` 文档站

在 `doc/` 下创建：

- `docs.json`
- `index.mdx`
- `quickstart.mdx`
- `system-overview.mdx`
- `component-roles.mdx`
- `runtime-flow.mdx`
- `constraints-and-direction.mdx`
- `logo/light.svg`
- `logo/dark.svg`
- `favicon.svg`

### 3. 文案与结构调整

完成：

- 全站中文化
- 站点标题改为 `GIS Agent`
- 导航从普通 `pages` 调整为 `tabs`

### 4. 本地 Mintlify 预览

启动命令：

```bash
cd /home/maptex/Code/xcsmartdatabase/doc
npx -y mint@4.2.616 dev --no-open
```

本地预览输出：

- `http://localhost:3000`

### 5. 仓库内 Nginx 配置尝试

在仓库内修改了：

- `nginx/nginx/gisagent.conf`
- `nginx/docker-compose.yml`

并尝试构建：

- `gisagent-nginx:latest`

期间发现：

- 当前端口 `80` 已被已有容器占用
- 新建 `gisagent-nginx` 并不是当前外部入口

因此改动仅作为仓库内预期配置保留。

### 6. 实际生效入口定位

通过 Docker 检查确认：

- 当前承接 `80/443` 的是 `nginx-proxy`
- 其挂载配置目录为：
  - `/home/maptex/docker/nginx/conf.d/main.conf`

于是后续把 `/doc` 代理改动直接落到了这份宿主机配置。

### 7. `/doc` 本机代理落地

在 `/home/maptex/docker/nginx/conf.d/main.conf` 中加入：

- `location = /doc`
- `location /doc/`

核心处理包括：

- `/doc/...` -> 上游 `/...`
- 上游 `proxy_pass http://172.17.0.1:3000/`
- `sub_filter` 改写 HTML 中的根路径静态资源
- 注入 `<base href="/doc/">`

### 8. 本机链路验证

本机验证成功项：

- `/doc/` 返回 `200`
- `/doc/_next/static/...` 返回 `200`
- `/doc/system-overview` 返回文档页面

### 9. 问题定位结果

用户随后反馈公网访问 `http://gisagent.smaryun.com/doc` 仍然进入登录页。

排查结论：

- 我当前修改的是**本机 Docker / 本机 Nginx**
- 不是阿里云侧公网服务配置
- 本机验证成功，不代表公网实际入口已同步

### 10. `server.maptex.top` 本机入口确认

后续按用户要求，改为以本机 `server.maptex.top` 入口为准确认 `/doc` 接入关系。

确认结果：

- `/home/maptex/Code/xcsmartdatabase/gisagent` 仍对应主站入口能力
- `/home/maptex/Code/xcsmartdatabase/doc` 对应文档站
- 当前本机实际生效 Nginx 配置 `/home/maptex/docker/nginx/conf.d/main.conf` 已包含 `/doc` 代理规则
- 仓库参考配置 `nginx/nginx/gisagent.conf` 已同步补充 `server.maptex.top` Host 语义

### 11. `server.maptex.top` 专用 server block 修复

进一步排查后确认：

- `main.conf` 后半段存在单独的 `server_name server.maptex.top` server block
- 该 block 原先把所有请求直接代理到 `http://192.168.11.24:17076/`

这导致：

- `https://server.maptex.top/doc`

并不会命中前面的通用 `/doc` 规则，而是落到 `gisagent`，随后被前端跳转到：

- `/manager/login?redirect=/doc`

实际修复动作：

- 在 `server_name server.maptex.top` 专用 block 中新增：
  - `location = /doc`
  - `location ^~ /doc/`
- 将 `/doc` 明确重定向到 `/doc/`
- 将 `/doc/` 代理到宿主机文档站 `http://172.23.0.1:3000/`
- 保留 HTML 子路径改写与 `<base href="/doc/">` 注入
- 重载 `nginx-proxy`

## 涉及文件

仓库内文件：

- `/home/maptex/Code/xcsmartdatabase/doc/*`
- `/home/maptex/Code/xcsmartdatabase/nginx/nginx/gisagent.conf`
- `/home/maptex/Code/xcsmartdatabase/nginx/docker-compose.yml`

本机运行态文件：

- `/home/maptex/docker/nginx/conf.d/main.conf`

本机运行态容器：

- `nginx-proxy`
