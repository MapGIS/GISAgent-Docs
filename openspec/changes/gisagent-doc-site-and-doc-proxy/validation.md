# 验证记录：GIS Agent 文档站与 `/doc` 本机代理

## 验证范围

本次验证仅覆盖：

1. `doc/` 文档工程是否可本地运行
2. 本机 `nginx-proxy` 是否能将 `/doc` 代理到 Mintlify 预览

本次**未覆盖**：

1. 阿里云服务器公网入口
2. 真实公网 DNS 解析落点
3. 正式静态部署后的公网验收

## 已完成验证

### A. 文档站本地运行

启动后确认：

- 本地地址：`http://localhost:3000`
- 页面可返回 `200`
- 页面标题与内容更新生效

补充验证：

- `http://127.0.0.1:3000/` 返回 Mintlify 文档首页
- `http://127.0.0.1/doc/` 通过本机 `nginx-proxy` 返回改写后的 `/doc` 文档首页

### B. 本机 Nginx 容器到宿主机上游联通

在 `nginx-proxy` 容器内验证：

- `http://172.17.0.1:3000/` 返回 `200`

### C. 本机 Host 头代理验证

以下链路已在本机验证通过：

```bash
curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/
curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/system-overview
curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/_next/static/chunks/9ffc684b9a12d113.css
```

验证结果：

- `/doc/` 返回 `200`
- `/doc/system-overview` 返回文档页面
- `/doc/_next/static/...` 返回 `200`

### D. `server.maptex.top` 参考入口差异

当前观察到两种不同结果：

1. 本机回环验证：
   - `curl -H 'Host: server.maptex.top' http://127.0.0.1/doc/`
   - 可返回文档页
2. 直接请求公网 HTTPS：
   - `https://server.maptex.top/gis/`
   - `https://server.maptex.top/doc/`
   - 当前终端环境下都返回“贝锐花生壳”访问限制页

这说明：

- 本机 Nginx `/doc` 规则已就位
- 但公网 HTTPS 入口前仍存在额外访问控制或上层代理策略

### E. `server.maptex.top` 专用 block 修复后验证

新增验证结果：

1. 原始请求：
   - `GET /doc` with `Host: server.maptex.top`
   - 返回 `301 Location: https://server.maptex.top/doc/`
2. 文档首页：
   - `GET /doc/` with `Host: server.maptex.top`
   - 返回 Mintlify 文档首页 HTML
3. 文档页面：
   - `GET /doc/system-overview` with `Host: server.maptex.top`
   - 返回 `200`
4. 静态资源：
   - `GET /doc/_next/static/chunks/9ffc684b9a12d113.css` with `Host: server.maptex.top`
   - 返回 `200`

修复后可确认：

- `server.maptex.top` 本机实际生效的专用 server block 已正确接入文档站
- 本机 `/doc` 不再误转发到 `gisagent`

### F. 用户确认

用户已确认：

- `https://server.maptex.top/doc/`

当前可正常访问。

## 未通过或未确认项

### 1. 公网域名入口

用户实测：

- `http://gisagent.smaryun.com/doc`

仍然进入：

- `/manager/login?forbidden=1&redirect=/doc/`

这说明至少有一种情况成立：

1. 公网请求并未进入当前工作机的 `nginx-proxy`
2. 公网 `443` 入口与本机 `80` 入口不是同一套配置
3. 阿里云侧存在另一层代理、网关或容器链路

### 2. OpenSpec closeout 要求

按 `openspec/project.md` 的规则，涉及跨入口与运行时链路的 change，在 closeout 前应完成真实链路集成验收。

本次尚未满足这一条，因此不能标记为最终完成。

## 当前结论

本次 change 的状态应视为：

- 文档站工程：已完成
- 本机开发态代理：已完成
- `server.maptex.top` 本机 `/doc` 接入：已完成
- 公网真实入口验证：未完成
