import { Suspense } from "react";
import Link from "next/link";
import AuthShell from "@/components/auth/AuthShell";
import LoginForm from "@/components/auth/LoginForm";

export const metadata = {
  title: "Masuk",
  description:
    "Masuk ke akun LearnWithAcel kamu untuk melanjutkan progress belajar.",
};

function LoginFormFallback() {
  return (
    <div className="space-y-4">
      {[0, 1].map((i) => (
        <div key={i} className="space-y-1.5">
          <div className="h-4 w-20 animate-pulse rounded bg-black/40" />
          <div className="h-11 animate-pulse rounded-xl border border-border bg-black/30" />
        </div>
      ))}
      <div className="h-11 animate-pulse rounded-xl bg-accent/30" />
    </div>
  );
}

export default function LoginPage() {
  return (
    <AuthShell
      eyebrow="Login"
      title="Selamat datang kembali."
      subtitle="Masuk untuk lanjut belajar dan pantau progress kamu."
      footer={
        <>
          Belum punya akun?{" "}
          <Link
            href="/register"
            className="font-medium text-accent-hover transition-colors hover:text-accent"
          >
            Daftar sekarang
          </Link>
        </>
      }
    >
      <Suspense fallback={<LoginFormFallback />}>
        <LoginForm />
      </Suspense>
    </AuthShell>
  );
}
