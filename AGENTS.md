# AGENTS

## Git network policy

- For this repository, all future `git pull` and `git push` operations must use an HTTP remote, not SSH.
- All fetch, pull, push, and other remote Git operations must be executed through a configured HTTP/HTTPS proxy.
- When checking or updating the remote URL, prefer the HTTP form of the repository address.
- If a proxy is required for the current shell session, set `http.proxy` and `https.proxy` before running remote Git commands.
