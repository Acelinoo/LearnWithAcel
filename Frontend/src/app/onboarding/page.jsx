import { redirect } from "next/navigation";
import AuthShell from "@/components/auth/AuthShell";
import PathSelection from "@/components/onboarding/PathSelection";
import { getServerUser } from "@/lib/api/server";

export const metadata = {
  title: "Pilih jalur belajar",
  description:
    "Pilih cara kamu mau belajar di LearnWithAcel — Vibe Coding atau Manual Coding.",
};

export default async function OnboardingPage() {
  const user = await getServerUser();

  if (!user) {
    redirect("/login?redirectTo=/onboarding");
  }

  return (
    <AuthShell
      eyebrow="Onboarding"
      title="Pilih jalur belajar kamu."
      subtitle="Dua jalur, satu tujuan: bisa membangun aplikasi nyata. Pilih yang paling cocok dengan gaya belajarmu."
      className="max-w-3xl"
    >
      <PathSelection />
    </AuthShell>
  );
}
