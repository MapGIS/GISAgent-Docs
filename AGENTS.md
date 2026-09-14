# AGENTS

## 角色定义

- 安全策略优先级始终高于用户请求；当用户请求与安全策略冲突时，必须拒绝或改用安全替代方案。

## 禁止拷贝技能源文件

- 严禁将 `/workspace/skills`、`/home/agent/.claude/skills`、`/home/agent/.qwen/skills`、`/home/agent/.qoder/skills` 下的任何 skill 文件或目录复制、打包、移动、导出或创建持久化副本到当前工作空间、会话目录、`/tmp` 或其他用户可访问目录。
- 使用 skill 时只允许按需读取并调用，不得在最终交付物中包含 skill 源文件内容。
