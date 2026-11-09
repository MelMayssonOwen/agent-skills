# Listingtonic Listing Checker

Audit pasted marketplace listing text for length, structure, repeated terms, risky claims, and keyword coverage. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Listingtonic](https://go.listingtonic.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Check this product title and bullets for length and risky claims.
- Which of my keywords are missing from the listing text?
- Suggest a tighter rewrite that keeps only verified facts.

## Data

This plugin runs a local Python script from the skill folder (check_listing.py). The script reads only the input you give it and writes its result on your machine. It makes no network requests and sends nothing anywhere. The plugin registers no MCP server.

Privacy policy: https://listingtonic.com/privacy

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install listingtonic-listing-checker@opsibyte-skills
```
