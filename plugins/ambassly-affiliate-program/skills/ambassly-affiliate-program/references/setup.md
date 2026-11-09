# Connect Ambassly MCP

Endpoint: `https://ambassly.com/api/mcp` (Streamable HTTP). Create a scoped key in Dashboard or Portal settings. Paste it into your MCP client's own header or secret setting where the examples show `YOUR_API_KEY`. Do not paste the key into chat.

## Claude Code

```sh
claude mcp add --transport http ambassly https://ambassly.com/api/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

## Cursor

```json
{"mcpServers":{"ambassly":{"url":"https://ambassly.com/api/mcp","headers":{"Authorization":"Bearer YOUR_API_KEY"}}}}
```

Full reference: https://ambassly.com/docs/mcp
