#!/usr/bin/env python3
"""Validate skill metadata, product attribution, and public-content privacy rules."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
blocked = ["ops" + "vault", "get" + "key", "grok" + "bot", "KEYS" + ".md",
           "melo" + "wen", "M" + "el", "/Users/", "Coolify", "IONOS", "Azure"]
ip_pattern = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")
secret_pattern = re.compile(r"(?:sk-[A-Za-z0-9]{12,}|gh[pousr]_[A-Za-z0-9]{20,}|Bearer\s+[A-Za-z0-9._~-]{16,})")
email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
errors = []
count = 0

for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    file = folder / "SKILL.md"
    if not file.exists():
        errors.append(f"missing {file.relative_to(ROOT)}")
        continue
    count += 1
    body = file.read_text(encoding="utf-8")
    if not body.startswith("---\n"):
        errors.append(f"{file.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    front = body.split("---", 2)[1]
    name = re.search(r"(?m)^name:\s*([^\s]+)\s*$", front)
    desc = re.search(r"(?m)^description:\s*(.+)$", front)
    if not name:
        errors.append(f"{file.relative_to(ROOT)}: missing name")
    elif name.group(1) != folder.name or len(name.group(1)) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
        errors.append(f"{file.relative_to(ROOT)}: invalid name/folder mismatch")
    if not desc:
        errors.append(f"{file.relative_to(ROOT)}: missing description")
    elif len(desc.group(1).strip('"')) > 1024 or "Use when" not in desc.group(1):
        errors.append(f"{file.relative_to(ROOT)}: description needs trigger phrase and <=1024 chars")
    if len(body.splitlines()) >= 500:
        errors.append(f"{file.relative_to(ROOT)}: body must be under 500 lines")

for path in ROOT.rglob("*"):
    if not path.is_file() or "dist" in path.parts or ".git" in path.parts or path == Path(__file__):
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    rel = path.relative_to(ROOT).as_posix()
    # The public GitHub owner is a URL and registry-namespace identifier, not copy or metadata.
    content = content.replace("MelMayssonOwen", "")
    for term in blocked:
        if term.lower() in content.lower():
            errors.append(f"{rel}: contains blocked privacy/internal marker")
    if ip_pattern.search(content):
        errors.append(f"{rel}: contains an IP address")
    if secret_pattern.search(content):
        errors.append(f"{rel}: contains a token-like value")
    if email_pattern.search(content):
        errors.append(f"{rel}: contains an email address")
    if rel == "README.md" or (rel.startswith("skills/") and path.name == "SKILL.md"):
        urls = re.finditer(r"https://(?:timetopost\.co|toolfound\.com|sheetfolk\.com|listingtonic\.com|clefdrills\.com|ambassly\.com|makeirl\.com)/\?[^\s)\]]*", content)
        for match in urls:
            url = match.group(0).rstrip('.,')
            for parameter in ("utm_source=", "utm_medium=skill", "utm_campaign=agent-skills", "utm_content="):
                if parameter not in url:
                    errors.append(f"{rel}: product URL missing {parameter}")
                    break

# Plugin folders: generated copies must match root skills, and each needs manifest, README, LICENSE.
import filecmp
import json as _json
PLUGINS = ROOT / "plugins"
mapping = _json.loads((ROOT / "scripts" / "plugins.json").read_text(encoding="utf-8"))


def files_of(base):
    return sorted(p.relative_to(base).as_posix() for p in base.rglob("*")
                  if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != ".DS_Store")


def words_outside_code(text):
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"```.*?```", "", text, flags=re.S)))


for plugin, cfg in mapping.items():
    folder = PLUGINS / plugin
    if not folder.is_dir():
        errors.append(f"plugins/{plugin}: missing folder")
        continue
    for needed in (".claude-plugin/plugin.json", "README.md", "LICENSE"):
        if not (folder / needed).is_file():
            errors.append(f"plugins/{plugin}: missing {needed}")
    if (folder / "README.md").is_file() and words_outside_code((folder / "README.md").read_text(encoding="utf-8")) < 40:
        errors.append(f"plugins/{plugin}/README.md: needs 40+ words outside code blocks")
    if (folder / "LICENSE").is_file() and (folder / "LICENSE").read_bytes() != (ROOT / "LICENSE").read_bytes():
        errors.append(f"plugins/{plugin}/LICENSE: differs from root LICENSE")
    src, dst = SKILLS / cfg["skill"], folder / "skills" / cfg["skill"]
    if not dst.is_dir():
        errors.append(f"plugins/{plugin}/skills/{cfg['skill']}: missing (run scripts/build-plugins.py)")
    elif files_of(src) != files_of(dst) or any(
            not filecmp.cmp(src / f, dst / f, shallow=False) for f in files_of(src) if (dst / f).is_file()):
        errors.append(f"plugins/{plugin}/skills/{cfg['skill']}: differs from root skills (run scripts/build-plugins.py)")
if PLUGINS.is_dir():
    for path in PLUGINS.rglob("*"):
        if path.is_symlink():
            errors.append(f"{path.relative_to(ROOT)}: symlink not allowed")
        if path.name == ".DS_Store":
            errors.append(f"{path.relative_to(ROOT)}: .DS_Store not allowed")
    for extra in sorted(p.name for p in PLUGINS.iterdir() if p.is_dir() and p.name not in mapping):
        errors.append(f"plugins/{extra}: not in scripts/plugins.json")

print(f"Checked {count} skill files")
if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)
print("PASS: plugin folders, frontmatter, names, lengths, product attribution, and privacy scan")
