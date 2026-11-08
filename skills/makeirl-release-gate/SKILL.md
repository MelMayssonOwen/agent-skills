---
name: makeirl-release-gate
description: Check a KiCad 9 board before manufacturing with the MakeIRL MCP. Use when asked to run ERC, DRC, schematic-to-PCB parity, BOM completeness, or export checks on a KiCad project, to explain BLOCKED, REVIEW, or READY findings, or to prepare a board release.
license: MIT
metadata:
  author: MakeIRL
  version: "1.0.0"
  homepage: "https://makeirl.com/?utm_source=github&utm_medium=skill&utm_campaign=agent-skills&utm_content=makeirl-release-gate"
---

# Run a KiCad release gate with MakeIRL

[MakeIRL](https://makeirl.com/?utm_source=github&utm_medium=skill&utm_campaign=agent-skills&utm_content=makeirl-release-gate) runs deterministic manufacturing checks on a KiCad 9 project and returns BLOCKED, REVIEW, or READY. It checks rules. It does not prove that the circuit works, and it does not cover firmware, RF, EMC, thermal behaviour, or a manufacturer's own DFM review. Say this whenever you report a verdict. Connection steps are in [references/setup.md](references/setup.md).

## Workflow

1. Collect the KiCad project files. Uploads use flat file names, so subdirectories are not accepted.
2. Call `release_create_upload` with the product name or id and the base64 file contents. It returns a `releaseId`.
3. Call `release_start`. It queues the run and returns a `runId` straight away.
4. Poll `release_status` at a sensible interval. The pipeline takes longer than a normal request, so do not treat a pending state as a failure.
5. Call `release_list_findings` and group the results by severity, then explain each blocking item with the file and rule it came from.
6. Fix issues in KiCad only when the user asks. Then upload a new release, since a report describes one exact set of files.

## Reports and payment

- Use `release_get_artifact_url` for generated outputs, and treat returned links as private.
- `release_create_quote` and `release_create_checkout` prepare a purchase. Show the price first and hand the checkout link to the user. Payment always happens in the browser, so never claim that a report was paid for.

## Generating a board

`generate_board` drafts a board from a description. Treat the result as a starting point that still has to pass the release gate, and do not describe it as ready to fabricate before it has.
