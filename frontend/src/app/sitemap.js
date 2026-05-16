import { listCategories, getRoadmap } from "@/lib/api/content";

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
  ].map((path) => ({
    url: `${base}${path}`,
    lastModified: new Date(),
  }));

  let lessonRoutes = [];
  try {
    const categories = await listCategories();
    const roadmaps = await Promise.all(
      categories.map((c) => getRoadmap(c.slug).catch(() => null))
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
        }))
      );
    });
  } catch {
    // backend offline — sitemap will only include static routes
  }

  return [...staticRoutes, ...lessonRoutes];
}
