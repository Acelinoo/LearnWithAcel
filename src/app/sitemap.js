import { levels } from "@/lib/roadmap";

export default function sitemap() {
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

  const lessonRoutes = levels.flatMap((level) =>
    level.lessons.map((lesson) => ({
      url: `${base}/materi/${level.slug}/${lesson.slug}`,
      lastModified: new Date(),
    }))
  );

  return [...staticRoutes, ...lessonRoutes];
}
