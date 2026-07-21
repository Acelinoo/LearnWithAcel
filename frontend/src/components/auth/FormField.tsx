"use client";

import {
  forwardRef,
  useState,
  type InputHTMLAttributes,
  type ReactNode,
} from "react";
import { Eye, EyeOff } from "lucide-react";
import { cn } from "@/lib/utils";

type Props = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
  error?: string;
  icon?: ReactNode;
  hint?: string;
};

const FormField = forwardRef<HTMLInputElement, Props>(function FormField(
  { label, error, icon, hint, type = "text", className, id, ...rest },
  ref
) {
  const [show, setShow] = useState(false);
  const isPassword = type === "password";
  const inputType = isPassword ? (show ? "text" : "password") : type;
  const inputId =
    id ?? `field-${label.toLowerCase().replace(/\s+/g, "-")}`;
  const describedBy = error
    ? `${inputId}-error`
    : hint
      ? `${inputId}-hint`
      : undefined;

  return (
    <div className="space-y-1.5">
      <label
        htmlFor={inputId}
        className="block text-[13px] font-medium text-foreground/90"
      >
        {label}
      </label>

      <div
        className={cn(
          "group relative flex items-center overflow-hidden rounded-xl border bg-black/30 transition-all",
          "border-border focus-within:border-accent/60 focus-within:bg-black/30",
          "focus-within:shadow-[0_0_0_4px_rgba(78,186,236,0.12)]",
          error &&
            "border-red-500/50 focus-within:border-red-400/70 focus-within:shadow-[0_0_0_4px_rgba(239,68,68,0.15)]"
        )}
      >
        {icon && (
          <span className="pointer-events-none flex h-11 w-11 items-center justify-center text-muted group-focus-within:text-accent-hover">
            {icon}
          </span>
        )}
        <input
          id={inputId}
          ref={ref}
          type={inputType}
          aria-invalid={!!error}
          aria-describedby={describedBy}
          className={cn(
            "w-full bg-transparent py-2.5 pr-3 text-sm text-foreground outline-none placeholder:text-muted/60",
            !icon && "pl-4",
            isPassword && "pr-12",
            className
          )}
          {...rest}
        />
        {isPassword && (
          <button
            type="button"
            onClick={() => setShow((v) => !v)}
            aria-label={show ? "Sembunyikan password" : "Tampilkan password"}
            className="absolute right-1.5 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-lg text-muted transition-colors hover:bg-black/40 hover:text-foreground"
            tabIndex={-1}
          >
            {show ? <EyeOff size={15} /> : <Eye size={15} />}
          </button>
        )}
      </div>

      {error ? (
        <p
          id={`${inputId}-error`}
          className="text-[12px] font-medium text-red-400"
        >
          {error}
        </p>
      ) : hint ? (
        <p id={`${inputId}-hint`} className="text-[12px] text-muted/80">
          {hint}
        </p>
      ) : null}
    </div>
  );
});

export default FormField;
