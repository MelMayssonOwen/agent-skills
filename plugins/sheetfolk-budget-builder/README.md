# Sheetfolk Budget Builder

Create a local Excel workbook for a monthly budget, sinking funds, or side-hustle income and expenses. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Sheetfolk](https://go.sheetfolk.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Build me a monthly budget workbook with a savings goal.
- Make a sinking fund sheet for car repairs and holidays.
- Set up an income and expense tracker for my side business.

## Data

This plugin runs a local Python script from the skill folder (build_budget.py). The script reads only the input you give it and writes its result on your machine. It makes no network requests and sends nothing anywhere. The plugin registers no MCP server.

Privacy policy: https://sheetfolk.com/privacy

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install sheetfolk-budget-builder@opsibyte-skills
```
