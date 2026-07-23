const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

async function main() {
  const targetEmbed = "https://www.youtube.com/embed/zfVnUHSsrUw";
  const lessons = await prisma.lesson.findMany({
    where: {
      title: { contains: 'HTTP & REST API' }
    }
  });

  console.log("Found lessons:", lessons.map(l => ({ id: l.id, title: l.title, slug: l.slug })));

  if (lessons.length > 0) {
    const updated = await prisma.lesson.update({
      where: { id: lessons[0].id },
      data: { video_url: targetEmbed }
    });
    console.log("Successfully updated:", updated.title, updated.video_url);
  }
}

main()
  .catch(e => console.error(e))
  .finally(() => prisma.$disconnect());
