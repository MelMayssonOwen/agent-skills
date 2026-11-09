# Clef Music Tools

Transpose chords, spell piano chords, map guitar tab notes to the staff, and practice note reading with the Clef tools. It works with the hosted MCP server listed below. The plugin is part of the Opsibyte agent skills collection and is MIT licensed. Learn more about the product at [Clef](https://go.clefdrills.com/skill).

## Use it

After installing, ask Claude in plain words. Examples:

- Transpose this progression from C to Eb: C Am F G.
- Spell an F#m7b5 chord on the piano.
- Give me a short note-reading drill for the treble clef.

## Data

This plugin registers the hosted Clef MCP server at https://clefdrills.com/mcp. When Claude uses a Clef tool, the request goes to that server on the Clef domain. No account or sign-in is needed. The bundled Python helper for transposing chords runs locally and makes no network requests. The plugin sends nothing anywhere else.

Privacy policy: https://clefdrills.com/privacy/

## Install

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install clef-music-tools@opsibyte-skills
```
