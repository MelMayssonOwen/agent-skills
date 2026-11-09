#!/usr/bin/env python3
"""Copy root LICENSE and skills/<skill>/ into each plugins/<plugin>/ folder as regular files.

Root skills/ stays the source of truth. The plugin-to-skill mapping lives in scripts/plugins.json.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = json.loads((Path(__file__).parent / "plugins.json").read_text(encoding="utf-8"))
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {".DS_Store"}


def copy_tree(src, dst):
    dst.mkdir(parents=True, exist_ok=True)
    for item in sorted(src.iterdir()):
        if item.name in SKIP_DIRS or item.name in SKIP_FILES or item.suffix == ".pyc":
            continue
        if item.is_dir():
            copy_tree(item, dst / item.name)
        else:
            shutil.copyfile(item, dst / item.name)


def main():
    for plugin, cfg in MAPPING.items():
        folder = ROOT / "plugins" / plugin
        skill = cfg["skill"]
        target = folder / "skills" / skill
        if target.exists():
            shutil.rmtree(target)
        copy_tree(ROOT / "skills" / skill, target)
        shutil.copyfile(ROOT / "LICENSE", folder / "LICENSE")
        print(f"plugins/{plugin}/skills/{skill}")


if __name__ == "__main__":
    main()
