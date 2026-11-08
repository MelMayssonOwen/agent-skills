# Connect Ambassly MCP

Endpoint: `https://ambassly.com/api/mcp` (Streamable HTTP). Create a scoped key in Dashboard or Portal settings, and store it as `AMBASSLY_API_KEY`.

## Claude Code

```sh
claude mcp add --transport http ambassly https://ambassly.com/api/mcp --header "Authorization: Bearer $AMBASSLY_API_KEY"
```

## Cursor

```json
{"mcpServers":{"ambassly":{"url":"https://ambassly.com/api/mcp","headers":{"Authorization":"Bearer ${env:AMBASSLY_API_KEY}"}}}}
```

Full reference: https://ambassly.com/docs/mcp
