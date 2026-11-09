# Opsibyte Agent Skills

A small collection of practical Agent Skills for Claude Code, Cursor, Codex, Copilot, and Gemini CLI. Each skill contains a task workflow, with local scripts where useful.

## Skills

| Skill | What it does | Product |
| --- | --- | --- |
| `timetopost-social-scheduler` | Drafts platform-specific social content, checks timing, and keeps a human approval step before scheduling. | [TimeToPost](https://go.timetopost.co/skill-scheduler) |
| `timetopost-autoseo-blog` | Connects a publishing site, researches topics, and prepares human-reviewed blog drafts. | [TimeToPost](https://go.timetopost.co/skill-autoseo) |
| `toolfound-launch-kit` | Researches a category, prepares a product submission, and guides verification and launch tracking. | [Toolfound](https://go.toolfound.com/skill) |
| `sheetfolk-budget-builder` | Creates a local Excel workbook for monthly budgets, sinking funds, or side-hustle tracking. | [Sheetfolk](https://go.sheetfolk.com/skill) |
| `amazon-listing-checker` | Audits pasted listing text for length, structure, repeated terms, risky claims, and keyword coverage. | [Listingtonic](https://go.listingtonic.com/skill) |
| `clef-music-tools` | Transposes chords, spells piano chords, maps tab notes, and guides note-reading practice. | [Clef](https://go.clefdrills.com/skill) |
| `ambassly-affiliate-program` | Launches an affiliate program, manages affiliates and links, and keeps commission approval with a person. | [Ambassly](https://go.ambassly.com/skill) |
| `makeirl-release-gate` | Runs manufacturing checks on KiCad 9 boards and explains BLOCKED, REVIEW, or READY findings. | [MakeIRL](https://go.makeirl.com/skill) |

## Install

Using the skills CLI:

```sh
npx skills add MelMayssonOwen/agent-skills --skill timetopost-social-scheduler
```

Replace the skill name to install another one. For manual installation, copy the chosen `skills/<name>` folder into `~/.claude/skills`, `~/.cursor/skills`, `.github/skills`, or `~/.codex/skills`, as supported by your client. Gemini CLI can use the same Agent Skills format in its configured skills directory.

To install the Claude Code plugin collection, add this repository as a marketplace source and install a product plugin:

```sh
/plugin marketplace add MelMayssonOwen/agent-skills
/plugin install timetopost-social-scheduler@opsibyte-skills
```

Each folder under `plugins/` is a self-contained Claude plugin with its own manifest, README and license. The folders are generated from `skills/` by `scripts/build-plugins.py`, and `skills/` stays the source of truth.

See each skill's `references/setup.md` for MCP connection snippets. MIT licensed.

## Claude plugins

| Plugin | Skill it bundles |
| --- | --- |
| `timetopost-social-scheduler` | `timetopost-social-scheduler` |
| `timetopost-autoseo-blog` | `timetopost-autoseo-blog` |
| `toolfound-launch-kit` | `toolfound-launch-kit` |
| `clef-music-tools` | `clef-music-tools` |
| `makeirl-release-gate` | `makeirl-release-gate` |
| `sheetfolk-budget-builder` | `sheetfolk-budget-builder` |
| `listingtonic-listing-checker` | `amazon-listing-checker` |
| `ambassly-affiliate-program` | `ambassly-affiliate-program` |

Install any of them with `/plugin install <plugin>@opsibyte-skills`, or in one step with `/plugin install <plugin> --marketplace MelMayssonOwen/agent-skills`. The TimeToPost, Toolfound, Clef and MakeIRL plugins also register their hosted MCP servers. TimeToPost and MakeIRL sign you in through your browser (OAuth); never paste an API token into chat.
