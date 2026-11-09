# MakeIRL Release Gate

Run manufacturing checks on a KiCad 9 board and get a BLOCKED, REVIEW or READY verdict with each finding explained. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [MakeIRL](https://go.makeirl.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Run the release gate on my KiCad project and explain the findings.
- Why is this board marked REVIEW?
- What do I fix first to reach READY?

## Data

This plugin registers the hosted MakeIRL MCP server at https://makeirl.com/api/mcp. When Claude uses a MakeIRL tool, the request goes to that server on the MakeIRL domain. You sign in through your browser with OAuth the first time. A release check uploads the KiCad project files you choose to MakeIRL, which runs the checks and returns the findings. Paid reports are bought in the browser through a checkout link. The plugin has no scripts that run on your machine and sends nothing anywhere else.

Privacy policy: https://makeirl.com/privacy

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install makeirl-release-gate@opsibyte-skills
```
