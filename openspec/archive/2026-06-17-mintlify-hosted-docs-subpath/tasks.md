# 任务：Mintlify 托管与 `/docs` 正式入口

## 1. Mintlify 托管接入

- [x] 使用 GitHub 账号登录 Mintlify
- [x] 为 `MapGIS/GISAgent-Docs` 安装 Mintlify GitHub App
- [x] 完成首次托管部署
- [x] 记录生成的 `*.mintlify.dev` 子域（当前上游为 `mapgis.mintlify.dev`）

## 2. Dashboard 配置

- [ ] 在 Mintlify Dashboard 添加自定义域名 `gisagent.smaryun.com`
- [ ] 开启 `Host at /docs`
- [ ] 获取 TXT 验证要求
- [ ] 获取 CNAME 接入要求

## 3. DNS 配置

- [ ] 配置 Mintlify 要求的 TXT 记录
- [ ] 配置指向 `cname.mintlify.builders` 的 CNAME
- [ ] 确认 Mintlify Dashboard 中域名状态完成验证

## 4. Nginx 反代配置

- [x] 在正式 Nginx 配置中新增 `/docs` 入口
- [x] 将 `/docs` 反代到 `https://<project-subdomain>.mintlify.dev/docs`
- [x] 放行 `/.well-known/` 验证路径
- [x] 按官方要求补齐代理头
- [x] 同步更新本地部署模板目录 `doc/deploy/nginx-20260602_164043`
- [x] 同步更新阿里云目录 `/opt/nginx/nginx-20260602_164043`
- [x] 基于同步后的目录重建阿里云 `gisagent-nginx:latest`
- [x] 在阿里云执行 `docker compose down && docker compose up -d`
- [x] 将健康检查切换为 `Host: gisagent.smaryun.com` 模式
- [x] 将反代 `server` 调整为 `default_server` 并移除 `localhost` 命名依赖

## 5. 公网验证

- [x] 验证 `http://gisagent.smaryun.com/docs`
- [ ] 验证页面刷新与深链接
- [ ] 验证静态资源加载
- [ ] 验证全文搜索
- [ ] 验证 Assistant

## 6. 文档收尾

- [x] 记录最终托管子域与正式入口
- [x] 记录 DNS 与代理配置
- [ ] 记录已知限制与回滚方式
- [ ] 完成 closeout
