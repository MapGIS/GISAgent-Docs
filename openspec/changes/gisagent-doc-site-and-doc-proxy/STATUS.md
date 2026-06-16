---
name: "gisagent-doc-site-and-doc-proxy"
description: "`doc/` 下 GIS Agent Mintlify 文档站建设与 `/doc` 本机代理接入记录"
metadata:
  type: project
status: in_progress
updated: 2026-06-12
---

# GIS Agent 文档站与 `/doc` 代理状态

## 当前结论

本 change 已完成文档站建设、`server.maptex.top/doc/` 本机入口接入，并获得用户访问确认，但尚未完成其它公网入口的最终验收。

## 已完成

- `doc/` 下创建 Mintlify 文档工程
- 站点标题改为 `GIS Agent`
- 页面中文化
- 导航改为多 Tab
- logo、favicon、主色调统一为蓝色系
- 架构文档迁移为多页结构
- 本地 `mint dev` 预览可运行
- 当前工作机 `nginx-proxy` 到本地文档站的 `/doc` 代理已验证可用
- `server.maptex.top` 专用 server block 的 `/doc` 误转发问题已修复
- 用户已确认 `https://server.maptex.top/doc/` 可正常访问

## 未完成

- `gisagent.smaryun.com` 公网请求真实落点确认
- `server.maptex.top` HTTPS 上层访问控制策略确认
- 阿里云或其他公网入口层配置同步确认
- `/doc` 正式静态部署
- OpenSpec 要求的真实链路集成验收

## 证据入口

- `proposal.md`: 目标、范围和成功标准
- `design.md`: Mintlify 方案与 `/doc` 代理设计
- `tasks.md`: 分阶段任务完成情况
- `execution.md`: 实际执行动作
- `validation.md`: 本机验证结果与公网未通过项
- `closeout.md`: 为什么当前不能标记最终收尾

## 建议状态

- 文档工程: 已完成
- 本机开发态代理: 已完成
- `server.maptex.top/doc/`: 已完成并已确认
- 公网入口链路: 阻塞中
- closeout: 暂不关闭
