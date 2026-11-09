# Toolfound Launch Kit

Research a category on Toolfound, prepare a product submission, and follow verification and launch tracking. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Toolfound](https://go.toolfound.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Check which Toolfound category fits my app and prepare the listing.
- Walk me through the pre-launch checklist.
- Track how my launch is doing.

## Data

This plugin registers the hosted Toolfound MCP server at https://toolfound.com/api/mcp. When Claude uses a Toolfound tool, the request goes to that server on the Toolfound domain. No account or sign-in is needed to browse. Submitting a listing sends the product details you confirm to Toolfound. The plugin has no scripts that run on your machine and sends nothing anywhere else.

Privacy policy: https://toolfound.com/legal/privacy

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install toolfound-launch-kit@opsibyte-skills
```
