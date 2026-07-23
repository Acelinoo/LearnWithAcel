import asyncio
from prisma import Prisma

async def main() -> None:
    db = Prisma()
    await db.connect()
    
    lesson = await db.lesson.find_first(
        where={
            'slug': 'frontend-developer-lesson-1-1'
        }
    )
    if lesson:
        await db.lesson.update(
            where={'id': lesson.id},
            data={'video_url': 'https://www.youtube.com/embed/UMbbF72vXSM'}
        )
        print(f"Updated lesson '{lesson.title}' with video_url.")
    else:
        print("Lesson not found.")
        
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
