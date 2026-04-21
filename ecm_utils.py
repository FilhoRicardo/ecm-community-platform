
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ECM_ROOT = Path(__file__).resolve().parent / "ecms"

BUILDING_TYPE_LABELS = {
    "office_zero_energy": "Office (Zero Energy)",
    "highway_lodging": "Highway Lodging",
    "small_healthcare": "Small Healthcare",
    "zero_k12": "K-12 (Zero Energy)",
    "med_big_box_retail": "Retail (Medium / Big Box)",
    "large_hospitals": "Large Hospitals",
    "k12_50": "K-12 (50%)",
    "grocery": "Grocery",
    "small_warehouse": "Small Warehouse / Self-Storage",
}

USER_FACING_BUILDING_TYPES = list(BUILDING_TYPE_LABELS.values())


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", text.strip().lower()).strip("_")
    return text or "ecm"


def first_markdown_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return fallback


def excerpt_from_content(content: str, max_len: int = 320) -> str:
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    # Skip YAML front matter
    cleaned: list[str] = []
    in_frontmatter = False
    first_line = True
    for line in lines:
        if first_line and line == "---":
            in_frontmatter = True
            first_line = False
            continue
        first_line = False
        if in_frontmatter:
            if line == "---":
                in_frontmatter = False
            continue
        # Skip lines that are markdown headings: one or more # followed by a space
        if re.match(r"#+ ", line.lstrip()):
            continue
        cleaned.append(line)
    text = " ".join(cleaned)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_len]


def load_ecms() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for building_slug, label in BUILDING_TYPE_LABELS.items():
        folder = ECM_ROOT / building_slug
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            content = path.read_text(encoding="utf-8")
            title = first_markdown_title(content, path.stem.replace("_", " "))
            ecm_id = f"{building_slug}:{path.stem}"
            items.append(
                {
                    "id": ecm_id,
                    "filename": f"{building_slug}/{path.name}",
                    "title": title,
                    "building_type": label,
                    "building_slug": building_slug,
                    "content": content,
                    "excerpt": excerpt_from_content(content),
                }
            )
    return items
