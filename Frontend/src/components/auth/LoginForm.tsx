"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { ArrowRight, Lock, Mail } from "lucide-react";
import { login } from "@/lib/api/auth";
import { ApiError } from "@/lib/api/client";
import { useAuth } from "@/components/providers/AuthProvider";
import { loginSchema, type LoginInput } from "@/lib/validators/auth";
import { friendlyAuthError } from "@/lib/auth/errors";
import FormField from "@/components/auth/FormField";
import SubmitButton from "@/components/auth/SubmitButton";
import AuthAlert from "@/components/auth/AuthAlert";

export default function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const redirectTo = searchParams.get("redirectTo") || "/dashboard";
  const { setSession } = useAuth();

  const [serverError, setServerError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginInput>({
    resolver: zodResolver(loginSchema),
    defaultValues: { email: "", password: "", remember: true },
    mode: "onBlur",
  });

  const onSubmit = async (values: LoginInput) => {
    setServerError(null);
    try {
      const { access_token } = await login({
        email: values.email,
        password: values.password,
      });
      await setSession(access_token);
      router.replace(redirectTo);
      router.refresh();
    } catch (e) {
      const msg =
        e instanceof ApiError
          ? e.message
          : e instanceof Error
            ? e.message
            : "Gagal masuk.";
      setServerError(friendlyAuthError(msg));
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4" noValidate>
      <AuthAlert type="error" message={serverError} />

      <FormField
        label="Email"
        type="email"
        autoComplete="email"
        placeholder="kamu@email.com"
        icon={<Mail size={15} />}
        error={errors.email?.message}
        {...register("email")}
      />

      <FormField
        label="Password"
        type="password"
        autoComplete="current-password"
        placeholder="••••••••"
        icon={<Lock size={15} />}
        error={errors.password?.message}
        {...register("password")}
      />

      <div className="flex items-center justify-between pt-1">
        <label className="flex cursor-pointer items-center gap-2 text-[13px] text-muted">
          <input
            type="checkbox"
            className="h-4 w-4 rounded border-white/20 bg-white/[0.04] text-accent accent-accent focus:ring-accent/40"
            {...register("remember")}
          />
          Ingat saya
        </label>
        <Link
          href="/register"
          className="text-[13px] text-muted transition-colors hover:text-accent-hover"
        >
          Belum punya akun?
        </Link>
      </div>

      <SubmitButton loading={isSubmitting} loadingText="Masuk...">
        Masuk
        <ArrowRight size={15} />
      </SubmitButton>
    </form>
  );
}
