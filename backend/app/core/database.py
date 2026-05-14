"""
Prisma client lifecycle management.

The single Prisma client instance is created at startup and closed at shutdown
via FastAPI's lifespan context manager.
"""

from prisma import Prisma

# Module-level singleton — shared across the entire application.
prisma = Prisma()
