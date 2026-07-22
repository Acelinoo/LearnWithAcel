"""
Database seed script.

Loads category, level, and lesson content from `scripts.content.*` and
upserts everything into PostgreSQL via Prisma.

Idempotent — safe to run multiple times. Existing rows are updated
(by unique slug), new rows created.

Usage:
    python -m scripts.seed              # upsert content (no destructive ops)
    python -m scripts.seed --prune      # also delete levels/lessons whose
                                        # slugs are NOT in the current
                                        # content modules (cleans up rows
                                        # left over from old seeds).
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any, Iterable

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Allow running from the backend/ directory
sys.path.insert(0, str(Path(__file__).parent.parent))

from prisma import Prisma  # noqa: E402

from scripts.content import CATEGORIES, LEVELS_BY_CATEGORY  # noqa: E402


# Fields that the Prisma schema expects for each model. Anything beyond
# these is forward-compat metadata (read_time, word_count, xp_reward,
# is_project, …) — we strip it before talking to Prisma.
LEVEL_DB_FIELDS = {
    "number",
    "slug",
    "title",
    "subtitle",
    "description",
    "duration",
    "difficulty",
    "accent_color",
    "mini_project",
    "quiz_count",
    "tags",
    "coming_soon",
}

LESSON_DB_FIELDS = {
    "slug",
    "title",
    "summary",
    "content",
    "duration",
    "order_index",
}


def _select(fields: set[str], data: dict) -> dict[str, Any]:
    return {k: v for k, v in data.items() if k in fields}


def _normalize_tags(value: Any) -> str:
    """Tags can arrive as list[str] or already JSON-encoded. Normalize to JSON."""
    if isinstance(value, str):
        return value
    return json.dumps(value)


async def _upsert_category(db: Prisma, payload: dict) -> Any:
    return await db.category.upsert(
        where={"slug": payload["slug"]},
        data={
            "create": payload,
            "update": {k: v for k, v in payload.items() if k != "slug"},
        },
    )


async def _upsert_level(db: Prisma, category_id: str, payload: dict) -> Any:
    db_payload = _select(LEVEL_DB_FIELDS, payload)
    db_payload["tags"] = _normalize_tags(db_payload.get("tags", []))
    db_payload.setdefault("quiz_count", 0)
    db_payload.setdefault("coming_soon", False)

    return await db.level.upsert(
        where={
            "category_id_slug": {
                "category_id": category_id,
                "slug": db_payload["slug"],
            }
        },
        data={
            "create": {**db_payload, "category_id": category_id},
            "update": {k: v for k, v in db_payload.items() if k != "slug"},
        },
    )


async def _upsert_lesson(db: Prisma, level_id: str, payload: dict) -> Any:
    db_payload = _select(LESSON_DB_FIELDS, payload)

    return await db.lesson.upsert(
        where={
            "level_id_slug": {
                "level_id": level_id,
                "slug": db_payload["slug"],
            }
        },
        data={
            "create": {**db_payload, "level_id": level_id},
            "update": {k: v for k, v in db_payload.items() if k != "slug"},
        },
    )


async def _prune_orphans(
    db: Prisma,
    category_id: str,
    keep_level_slugs: Iterable[str],
    levels_data: list[dict],
) -> None:
    """Delete levels under `category_id` whose slug is not in `keep_level_slugs`,
    and delete lessons under each kept level whose slug is not in the
    expected set. Cascade in the schema removes child rows.
    """
    keep_set = set(keep_level_slugs)
    levels = await db.level.find_many(where={"category_id": category_id})
    for lv in levels:
        if lv.slug not in keep_set:
            await db.level.delete(where={"id": lv.id})
            print(f"    × Pruned orphan level: {lv.title} ({lv.slug})")

    # Also prune orphan lessons inside levels we keep
    for level_data in levels_data:
        keep_lessons = {l["slug"] for l in level_data.get("lessons", [])}
        # Find the level row we just upserted
        level_row = await db.level.find_unique(
            where={
                "category_id_slug": {
                    "category_id": category_id,
                    "slug": level_data["slug"],
                }
            }
        )
        if not level_row:
            continue
        existing_lessons = await db.lesson.find_many(where={"level_id": level_row.id})
        for ls in existing_lessons:
            if ls.slug not in keep_lessons:
                await db.lesson.delete(where={"id": ls.id})
                print(f"      × Pruned orphan lesson: {ls.title} ({ls.slug})")


async def seed(prune: bool = False) -> None:
    db = Prisma()
    await db.connect()

    print("🌱 Starting database seed...")
    if prune:
        print("   (prune mode: orphan levels/lessons will be deleted)")

    for cat_data in CATEGORIES:
        category = await _upsert_category(db, cat_data)
        print(f"  ✓ Category: {category.name}")

        levels_data = LEVELS_BY_CATEGORY.get(cat_data["slug"], [])
        for level_data in levels_data:
            level = await _upsert_level(db, category.id, level_data)
            print(f"    ✓ Level {level.number}: {level.title}")

            for lesson_data in level_data.get("lessons", []):
                lesson = await _upsert_lesson(db, level.id, lesson_data)
                print(f"      ✓ Lesson: {lesson.title}")

        if prune:
            await _prune_orphans(
                db,
                category.id,
                keep_level_slugs=[lv["slug"] for lv in levels_data],
                levels_data=levels_data,
            )

    await db.disconnect()
    print("\n✅ Seed completed successfully!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed LearnWithAcel content.")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Delete levels/lessons whose slugs are not in current content modules.",
    )
    args = parser.parse_args()
    asyncio.run(seed(prune=args.prune))


if __name__ == "__main__":
    main()
