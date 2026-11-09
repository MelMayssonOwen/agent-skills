# Ambassly Affiliate Program

Launch and run a Stripe-based affiliate program with Ambassly: set up the program, manage affiliates and links, and keep commission approval with a person. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Ambassly](https://go.ambassly.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Create an affiliate program for my product with a 20 percent commission.
- List my affiliates and their latest clicks.
- Generate a tracked link for a new partner.

## Data

This plugin contains instructions only and registers no MCP server and runs no scripts. If you choose to connect the Ambassly MCP server at https://ambassly.com/api/mcp, follow the setup reference in the skill folder: you create a scoped key in your Ambassly settings and paste it into your MCP client's own secret or header setting. Requests then go to ambassly.com. The key is never read from your environment by this plugin.

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install ambassly-affiliate-program@opsibyte-skills
```
