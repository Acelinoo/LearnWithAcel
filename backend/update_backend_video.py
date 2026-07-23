import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    try:
        lesson1 = await prisma.lesson.find_first(where={"slug": "backend-developer-lesson-1-1"})
        if lesson1:
            updated_lesson = await prisma.lesson.update(
                where={"id": lesson1.id},
                data={"video_url": "https://www.youtube.com/embed/zfVnUHSsrUw"}
            )
            print(f"Updated {updated_lesson.title} video_url to {updated_lesson.video_url}")

        lesson3 = await prisma.lesson.find_first(where={"slug": "backend-developer-lesson-1-3"})
        if lesson3:
            await prisma.lesson.update(
                where={"id": lesson3.id},
                data={"video_url": None}
            )
            print("Reverted lesson 3")

    finally:
        await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
