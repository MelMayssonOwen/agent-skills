# Twinpost Crosspost

Check your X mirrors, preview how a post reads on each network, save crosspost drafts, and publish or retry only after you confirm. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Twinpost](https://go.twinpo.st/mkt-github).

## Use it

After installing, ask Claude in plain words. Examples:

- Show what my mirrors posted today and what failed.
- Preview this post for Bluesky, Threads and LinkedIn, then save it as a draft.
- Retry the mirrored post that failed.

## Data

This plugin registers the hosted Twinpost MCP server at https://twinpo.st/mcp. You sign in to your Twinpost account in the browser (OAuth); the plugin never sees your password and there is no API key. When Claude uses a Twinpost tool, the request goes to that server. Drafts never publish on their own: anything that reaches an audience needs your yes in the chat. The plugin has no scripts that run on your machine and sends nothing anywhere else.

Privacy policy: https://twinpo.st/privacy

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install twinpost-crosspost@opsibyte-skills
```
