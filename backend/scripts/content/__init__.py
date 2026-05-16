"""
Content modules for the LearnWithAcel seed script.

Each path (frontend, backend, fullstack, vibe) is a sub-package whose
`LEVELS` constant exposes a flat list of level dicts. Every level dict
carries its own list of lessons with full Markdown content.

The seed script (`scripts.seed`) is orchestration-only — it imports the
manifests from here and writes them to the database via Prisma.

Splitting per level (not per category) keeps each file under ~600 lines
and makes copy review/diffs ergonomic. New levels can be added by
dropping a new module and registering it in the path's `__init__.py`.
"""

from .categories import CATEGORIES
from .frontend import LEVELS as FRONTEND_LEVELS
from .backend_path import LEVELS as BACKEND_LEVELS
from .fullstack import LEVELS as FULLSTACK_LEVELS
from .vibe import LEVELS as VIBE_LEVELS

LEVELS_BY_CATEGORY = {
    "frontend": FRONTEND_LEVELS,
    "backend": BACKEND_LEVELS,
    "fullstack": FULLSTACK_LEVELS,
    "vibe": VIBE_LEVELS,
}

__all__ = [
    "CATEGORIES",
    "FRONTEND_LEVELS",
    "BACKEND_LEVELS",
    "FULLSTACK_LEVELS",
    "VIBE_LEVELS",
    "LEVELS_BY_CATEGORY",
]
