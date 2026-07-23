"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { ArrowRight, AtSign, Lock, Mail } from "lucide-react";
import { login, register as registerApi } from "@/lib/api/auth";
import { ApiError } from "@/lib/api/client";
import { useAuth } from "@/components/providers/AuthProvider";
import { registerSchema, type RegisterInput } from "@/lib/validators/auth";
import { friendlyAuthError } from "@/lib/auth/errors";
import FormField from "@/components/auth/FormField";
import SubmitButton from "@/components/auth/SubmitButton";
import AuthAlert from "@/components/auth/AuthAlert";

type Stage = "idle" | "creating-account" | "signing-in" | "redirecting";

const loadingLabel: Record<Exclude<Stage, "idle">, string> = {
  "creating-account": "Membuat akun...",
  "signing-in": "Masuk ke akun...",
  redirecting: "Mengarahkan ke onboarding...",
};

export default function RegisterForm() {
  const router = useRouter();
  const { setSession } = useAuth();
  const [serverError, setServerError] = useState<string | null>(null);
  const [stage, setStage] = useState<Stage>("idle");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterInput>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    mode: "onBlur",
  });

  const onSubmit = async (values: RegisterInput) => {
    setServerError(null);

    // 1. Create the account.
    setStage("creating-account");
    try {
      await registerApi({
        email: values.email,
        password: values.password,
        full_name: values.username,
      });
    } catch (e) {
      setStage("idle");
      const msg =
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal membuat akun.";
      setServerError(friendlyAuthError(msg));
      return;
    }

    // 2. Auto-login so the user lands on /onboarding already authenticated.
    setStage("signing-in");
    let token = "";
    try {
      const { access_token } = await login({
        email: values.email,
        password: values.password,
      });
      token = access_token;
      await setSession(access_token);
    } catch (e) {
      setStage("idle");
      const msg =
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Akun dibuat, tapi gagal masuk otomatis.";
      setServerError(friendlyAuthError(msg));
      return;
    }

    // 3. Redirect.
    setStage("redirecting");
    if (typeof window !== "undefined" && token) {
      window.localStorage.setItem("lwa_token", token);
    }
    await new Promise((resolve) => setTimeout(resolve, 300));
    router.push("/onboarding");
  };

  const busy = isSubmitting || stage !== "idle";

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4" noValidate>
      <AuthAlert type="error" message={serverError} />

      <FormField
        label="Username"
        type="text"
        autoComplete="username"
        placeholder="username_kamu"
        icon={<AtSign size={15} />}
        error={errors.username?.message}
        hint="3–24 karakter. Huruf, angka, titik, dan underscore."
        disabled={busy}
        {...register("username")}
      />

      <FormField
        label="Email"
        type="email"
        autoComplete="email"
        placeholder="kamu@email.com"
        icon={<Mail size={15} />}
        error={errors.email?.message}
        disabled={busy}
        {...register("email")}
      />

      <FormField
        label="Password"
        type="password"
        autoComplete="new-password"
        placeholder="Min. 8 karakter, huruf & angka"
        icon={<Lock size={15} />}
        error={errors.password?.message}
        disabled={busy}
        {...register("password")}
      />

      <FormField
        label="Konfirmasi password"
        type="password"
        autoComplete="new-password"
        placeholder="Ulangi password"
        icon={<Lock size={15} />}
        error={errors.confirmPassword?.message}
        disabled={busy}
        {...register("confirmPassword")}
      />

      <SubmitButton
        loading={busy}
        loadingText={stage === "idle" ? undefined : loadingLabel[stage]}
      >
        Buat akun
        <ArrowRight size={15} />
      </SubmitButton>

      <p className="pt-1 text-center text-[12px] leading-relaxed text-muted/80">
        Dengan mendaftar, kamu setuju dengan ketentuan penggunaan platform
        LearnWithAcel.
      </p>
    </form>
  );
}
