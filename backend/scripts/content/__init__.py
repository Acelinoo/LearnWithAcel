"""
Content modules for the LearnWithAcel seed script.

The seed script (`scripts.seed`) is orchestration-only — it imports the
manifests from here and writes them to the database via Prisma.
"""

from .categories import CATEGORIES
from .dummy_content import generate_dummy_levels

LEVELS_BY_CATEGORY = {
    cat["slug"]: generate_dummy_levels(cat["name"], cat["slug"])
    for cat in CATEGORIES
}

__all__ = [
    "CATEGORIES",
    "LEVELS_BY_CATEGORY",
]
