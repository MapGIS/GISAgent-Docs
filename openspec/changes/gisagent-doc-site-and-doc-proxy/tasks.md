# 任务：GisAgent 文档站与 `/doc` 本机代理

## 1. 文档站初始化

- [x] 确认 `bakup/meoo` 不是源码仓库，而是 Mintlify 导出页面
- [x] 确认 Mintlify 最新工程格式使用 `docs.json`
- [x] 基于官方 starter 结构在 `doc/` 下创建最小文档站
- [x] 创建首页、快速开始页、系统总览页

## 2. 架构内容迁移

- [x] 将现有 AGENTS.md 中的系统说明迁移到文档站
- [x] 拆分为多页结构，避免单页过长
- [x] 补齐架构类页面导航

## 3. 品牌与视觉调整

- [x] 站点标题改为 `GisAgent`
- [x] 页面文案中文化
- [x] 导航改为多 Tab 结构
- [x] logo 改为蓝色地球图标
- [x] favicon 改为同一套图形
- [x] 主色调从绿色改为 `#2979ff`

## 4. 本地运行与验证

- [x] 启动 `mint dev --no-open`
- [x] 验证本地地址 `http://localhost:3000`
- [x] 验证局域网地址输出

## 5. 仓库内 Nginx 预期配置

- [x] 在仓库 `nginx/nginx/gisagent.conf` 中补 `/doc` 代理规则
- [x] 在仓库 `nginx/docker-compose.yml` 中补 `host.docker.internal` 访问方式
- [x] 说明该路径是“预期配置更新”，未直接成为当前公网生效入口

## 6. 当前工作机实际生效代理

- [x] 确认真实对外容器为 `nginx-proxy`
- [x] 确认实际生效配置文件为 `/home/maptex/docker/nginx/conf.d/main.conf`
- [x] 在 `main.conf` 中加入 `/doc` 与 `/doc/` 代理
- [x] 将 `/doc/...` 改写到上游根路径
- [x] 将 HTML 根路径资源改写到 `/doc/...`
- [x] 热重载 `nginx-proxy`

## 7. 本机验证

- [x] 验证 `curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/` 返回 `200`
- [x] 验证 `curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/_next/...` 返回 `200`
- [x] 验证 `curl -H 'Host: gisagent.smaryun.com' http://127.0.0.1/doc/system-overview` 命中文档页

## 8. 未完成项

- [ ] 确认 `gisagent.smaryun.com` 公网流量是否实际进入当前工作机
- [ ] 确认阿里云侧是否存在另一套 Nginx / Docker / 网关配置
- [ ] 完成 `/doc` 静态正式部署
- [ ] 按 openspec 最终 closeout 口径完成公网集成验收
