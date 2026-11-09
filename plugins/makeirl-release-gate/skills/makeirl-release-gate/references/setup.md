# Connect MakeIRL MCP

Endpoint: `https://makeirl.com/api/mcp` (Streamable HTTP, OAuth 2.1). Your client opens a browser sign-in on first use, so there is no API key to copy.

## Claude Code

```sh
claude mcp add --transport http makeirl https://makeirl.com/api/mcp
```

## Cursor

```json
{"mcpServers":{"makeirl":{"url":"https://makeirl.com/api/mcp"}}}
```

## Codex

```toml
[mcp_servers.makeirl]
url = "https://makeirl.com/api/mcp"
```
