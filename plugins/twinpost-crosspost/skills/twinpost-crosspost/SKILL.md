---
name: twinpost-crosspost
description: Check X mirrors, preview and draft crossposts, and publish or retry through the Twinpost MCP. Use when asked to crosspost a post to Bluesky, Threads, Telegram or LinkedIn, see what a mirror posted or why it failed, pause a mirror, or retry a failed mirrored post.
license: MIT
metadata:
  author: Twinpost
  version: "1.0.0"
  homepage: "https://go.twinpo.st/mkt-clawhub"
---

# Crosspost from chat with Twinpost

Use the Twinpost MCP at `https://twinpo.st/mcp` to look at the user's mirrors, preview how a post reads on each network, save drafts and, only after the user says yes, publish or retry. [Twinpost](https://go.twinpo.st/mkt-clawhub) mirrors posts from X to other networks; connecting is free and what the tools can do follows the user's plan.

## Workflow

1. Call `whoami` first and confirm the workspace is the one the user means. Stop before any write if it is not.
2. Call `list_accounts` and `list_mirrors` to see which networks are connected and which mirrors are on. Use only the accounts returned.
3. To answer "what happened to my last post", call `list_mirror_activity` and report, per network, whether the post landed or failed and the reason given. Do not guess a reason the tool did not return.
4. To crosspost new text, call `preview_crosspost` first and show the user how it reads on each network. Adjust length and tone per network when the preview shows a problem; do not paste identical text everywhere.
5. Save with `draft_crosspost`. A draft never publishes. Use `list_drafts` and `list_scheduled_posts` to show what is waiting.
6. Show the final text, the networks and the time. Call `publish_draft` or `retry_mirror_post` only after the user confirms those exact details in the chat, then pass `confirm: true`. Never publish on inference.
7. `pause_mirror` pauses a mirror at once. Resuming reaches an audience again, so ask before resuming and pass `confirm: true` only after a yes.

## Limits

- Publishing a draft directly needs a Twinpost plan that includes direct posts. If the tool returns a plan message, relay it plainly and leave the draft saved.
- Sign-in is browser OAuth with the user's Twinpost account. Never ask for a password or an API key, and never put a token in chat.
- The user can disconnect the app at any time in Twinpost under Connected apps.

Setup snippets for each client are in [references/setup.md](references/setup.md).
