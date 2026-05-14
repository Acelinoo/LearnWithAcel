import { redirect } from "next/navigation";
import { Sparkles } from "lucide-react";
import Reveal from "@/components/ui/Reveal";
import AdminCMS from "@/components/admin/AdminCMS";
import { getServerUser, getServerToken } from "@/lib/api/server";
import { listCategories, getRoadmap } from "@/lib/api/content";

export const dynamic = "force-dynamic";

export const metadata = {
  title: "Admin — Content Management",
  description:
    "CMS untuk mengelola category, level, dan lesson di LearnWithAcel.",
};

export default async function AdminPage() {
  const [user, token] = [await getServerUser(), getServerToken()];
  if (!user || !token) {
    redirect("/login?redirectTo=/admin");
  }
  if (!user.is_admin) {
    return (
      <div className="container-page py-24">
        <h1 className="font-display text-3xl font-semibold">
          Akses ditolak
        </h1>
        <p className="mt-4 text-muted">
          Halaman ini hanya untuk admin. Hubungi pemilik platform jika kamu
          merasa seharusnya punya akses.
        </p>
      </div>
    );
  }

  const categories = await listCategories();

  // Fetch full roadmaps for every category so the admin can see/edit
  // levels and lessons without extra round trips.
  const roadmaps = await Promise.all(
    categories.map(async (c) => {
      try {
        return await getRoadmap(c.slug);
      } catch {
        return { category: c, levels: [] };
      }
    })
  );

  return (
    <div className="container-page py-16">
      <Reveal>
        <span className="section-eyebrow">
          <Sparkles size={12} />
          Admin · CMS
        </span>
        <h1 className="mt-5 font-display text-3xl font-semibold tracking-tight sm:text-4xl">
          Kelola konten LearnWithAcel.
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-muted">
          Tambah, ubah, dan hapus category, level, dan lesson langsung lewat
          API. Semua perubahan langsung tercermin di seluruh aplikasi.
        </p>
      </Reveal>

      <Reveal delay={0.08}>
        <div className="mt-10">
          <AdminCMS initialRoadmaps={roadmaps} />
        </div>
      </Reveal>
    </div>
  );
}
