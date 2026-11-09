# TimeToPost Social Scheduler

Draft platform-specific social posts, check the best posting times, and schedule them through TimeToPost once you confirm the exact content, accounts and time. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [TimeToPost](https://go.timetopost.co/skill-scheduler).

## Use it

After installing, ask Claude in plain words. Examples:

- Draft a LinkedIn post and an X thread about our new release.
- When is the best time to post this on Instagram this week?
- Schedule the approved draft for Thursday morning.

## Data

This plugin registers the hosted TimeToPost MCP server at https://api.timetopost.co/mcp. When Claude uses a TimeToPost tool, the request goes to that server on the TimeToPost domain. You sign in through your browser with OAuth the first time, so no token is ever pasted into chat. The tools can send your draft text, account choices and schedule details to TimeToPost because that is how the work gets done. The plugin has no scripts that run on your machine and sends nothing anywhere else.

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install timetopost-social-scheduler@opsibyte-skills
```
