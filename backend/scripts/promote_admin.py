"""
Promote a registered user to admin.

Usage:
    python -m scripts.promote_admin user@example.com

The user must already be registered via the /auth/register endpoint.
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from prisma import Prisma


async def promote(email: str) -> None:
    db = Prisma()
    await db.connect()
    try:
        user = await db.user.find_unique(where={"email": email})
        if user is None:
            print(f"❌ No user found with email: {email}")
            return

        if user.is_admin:
            print(f"ℹ️  {email} is already an admin.")
            return

        await db.user.update(where={"email": email}, data={"is_admin": True})
        print(f"✅ {email} has been promoted to admin.")
    finally:
        await db.disconnect()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.promote_admin <email>")
        sys.exit(1)
    asyncio.run(promote(sys.argv[1]))
