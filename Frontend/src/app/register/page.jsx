import Link from "next/link";
import AuthShell from "@/components/auth/AuthShell";
import RegisterForm from "@/components/auth/RegisterForm";

export const metadata = {
  title: "Daftar",
  description:
    "Buat akun LearnWithAcel gratis untuk mulai belajar web development dari nol.",
};

export default function RegisterPage() {
  return (
    <AuthShell
      eyebrow="Register"
      title="Mulai perjalanan kamu."
      subtitle="Buat akun gratis untuk menyimpan progress, bookmark, dan history belajar."
      footer={
        <>
          Sudah punya akun?{" "}
          <Link
            href="/login"
            className="font-medium text-accent-hover transition-colors hover:text-accent"
          >
            Masuk di sini
          </Link>
        </>
      }
    >
      <RegisterForm />
    </AuthShell>
  );
}
