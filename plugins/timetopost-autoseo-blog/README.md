# TimeToPost AutoSEO Blog

Connect a publishing site to TimeToPost AutoSEO, research blog topics, and prepare blog drafts. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [TimeToPost](https://go.timetopost.co/skill-autoseo).

## Use it

After installing, ask Claude in plain words. Examples:

- Connect my site to AutoSEO and propose ten blog topics.
- Write a draft for the second topic and show it to me.
- Which questions are people asking about my niche?

## Data

This plugin registers the hosted TimeToPost MCP server at https://api.timetopost.co/mcp. When Claude uses a TimeToPost tool, the request goes to that server on the TimeToPost domain. You sign in through your browser with OAuth the first time, so no token is ever pasted into chat. The tools can send your draft text, account choices and schedule details to TimeToPost because that is how the work gets done. The plugin has no scripts that run on your machine and sends nothing anywhere else.

Privacy policy: https://timetopost.co/privacy/

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install timetopost-autoseo-blog@opsibyte-skills
```
