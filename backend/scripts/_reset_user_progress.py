"""Reset every user's XP/streak/progress so we can test from scratch."""

import asyncio
import sys

from prisma import Prisma


async def main() -> None:
    db = Prisma()
    await db.connect()
    deleted = await db.userprogress.delete_many()
    sys.stdout.write(f"Deleted {deleted} progress rows.\n")
    users = await db.user.find_many()
    for u in users:
        await db.user.update(
            where={"id": u.id},
            data={
                "xp_total": 0,
                "current_streak": 0,
                "longest_streak": 0,
                "last_activity_at": None,
            },
        )
    sys.stdout.write(f"Reset XP/streak for {len(users)} user(s).\n")
    sys.stdout.flush()
    await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
