"use client";

import { Loader2 } from "lucide-react";
import type { ButtonHTMLAttributes, ReactNode } from "react";
import { cn } from "@/lib/utils";

type Props = ButtonHTMLAttributes<HTMLButtonElement> & {
  loading?: boolean;
  children: ReactNode;
  loadingText?: string;
};

export default function SubmitButton({
  loading,
  disabled,
  className,
  children,
  loadingText,
  ...rest
}: Props) {
  return (
    <button
      type="submit"
      disabled={loading || disabled}
      className={cn(
        "group relative inline-flex w-full items-center justify-center gap-2 overflow-hidden rounded-xl bg-accent px-5 py-3 text-sm font-medium text-white shadow-glow transition-all",
        "hover:bg-accent-hover hover:shadow-glow-lg active:scale-[0.99]",
        "disabled:cursor-not-allowed disabled:opacity-60 disabled:hover:shadow-glow",
        className
      )}
      {...rest}
    >
      {/* Sheen */}
      <span
        aria-hidden
        className="pointer-events-none absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/25 to-transparent transition-transform duration-700 group-hover:translate-x-full"
      />
      {loading ? (
        <>
          <Loader2 size={15} className="animate-spin" />
          <span>{loadingText ?? "Memproses..."}</span>
        </>
      ) : (
        children
      )}
    </button>
  );
}
