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

See each skill's `references/setup.md` for MCP connection snippets. MIT licensed.

## Claude Code one-step install

```text
/plugin install timetopost-social-scheduler --marketplace MelMayssonOwen/agent-skills
/plugin install timetopost-autoseo-blog --marketplace MelMayssonOwen/agent-skills
/plugin install toolfound-launch-kit --marketplace MelMayssonOwen/agent-skills
/plugin install sheetfolk-budget-builder --marketplace MelMayssonOwen/agent-skills
/plugin install amazon-listing-checker --marketplace MelMayssonOwen/agent-skills
/plugin install clef-music-tools --marketplace MelMayssonOwen/agent-skills
/plugin install ambassly-affiliate-program --marketplace MelMayssonOwen/agent-skills
/plugin install makeirl-release-gate --marketplace MelMayssonOwen/agent-skills
```

The TimeToPost, Toolfound, Clef and MakeIRL plugins also register their hosted MCP servers. TimeToPost and MakeIRL sign you in through your browser (OAuth); never paste an API token into chat.
