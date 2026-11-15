# Connect Twinpost MCP

Endpoint: `https://twinpo.st/mcp` (Streamable HTTP). Sign-in is OAuth in the browser with a Twinpost account; there is no API key. Use a client that supports remote MCP with OAuth.

## Claude Code

```sh
claude mcp add --transport http twinpost https://twinpo.st/mcp
```

## Cursor

```json
{"mcpServers":{"twinpost":{"url":"https://twinpo.st/mcp"}}}
```

## Codex

```toml
[mcp_servers.twinpost]
url = "https://twinpo.st/mcp"
```

## VS Code / Copilot

```json
{"servers":{"twinpost":{"type":"http","url":"https://twinpo.st/mcp"}}}
```

Docs: https://twinpo.st/docs/mcp
