import { listCategories, getRoadmap } from "@/lib/api/content";
import { JALUR_META } from "@/lib/jalur-data";

export default async function sitemap() {
  const base = "https://learnwithacel.dev";

  const staticRoutes = [
    "",
    "/pilih-jalur",
    "/roadmap",
    "/roadmap/vibe",
    "/dashboard",
    "/about",
    "/donate",
    "/persiapan",
    "/persiapan/vibe",
    "/jalur/manual",
    "/jalur/vibe",
  ].map((path) => ({
    url: `${base}${path}`,
    lastModified: new Date(),
  }));

  // Jalur fundamentals lessons (manual + vibe)
  const jalurLessonRoutes = Object.entries(JALUR_META).flatMap(
    ([path, meta]) =>
      meta.lessons.map((l) => ({
        url: `${base}/jalur/${path}/${l.slug}`,
        lastModified: new Date(),
      })),
  );

  // Placeholder roadmap pages for the four vibe roles
  const vibeRoleRoutes = JALUR_META.vibe.roles.map((r) => ({
    url: `${base}/roadmap/vibe/${r.slug}`,
    lastModified: new Date(),
  }));

  let lessonRoutes = [];
  try {
    const categories = await listCategories();
    const roadmaps = await Promise.all(
      categories.map((c) => getRoadmap(c.slug).catch(() => null)),
    );

    lessonRoutes = roadmaps.flatMap((r) => {
      if (!r) return [];
      const isVibe = r.category.slug === "vibe";
      return r.levels.flatMap((level) =>
        level.lessons.map((lesson) => ({
          url: `${base}${
            isVibe
              ? `/materi/vibe/${level.slug}/${lesson.slug}`
              : `/materi/${level.slug}/${lesson.slug}`
          }`,
          lastModified: new Date(),
        })),
      );
    });
  } catch {
    // backend offline — sitemap will only include static routes
  }

  return [
    ...staticRoutes,
    ...jalurLessonRoutes,
    ...vibeRoleRoutes,
    ...lessonRoutes,
  ];
}
