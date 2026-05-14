"use client";

import { forwardRef, type InputHTMLAttributes, type TextareaHTMLAttributes } from "react";
import { cn } from "@/lib/utils";

type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
  error?: string;
  hint?: string;
};

export const TextField = forwardRef<HTMLInputElement, InputProps>(
  function TextField({ label, error, hint, className, id, ...rest }, ref) {
    const inputId = id ?? `f-${label.toLowerCase().replace(/\s+/g, "-")}`;
    return (
      <div className="space-y-1.5">
        <label
          htmlFor={inputId}
          className="block text-[12px] font-medium text-foreground/80"
        >
          {label}
        </label>
        <input
          id={inputId}
          ref={ref}
          className={cn(
            "w-full rounded-xl border border-white/10 bg-white/[0.02] px-3 py-2.5 text-sm text-foreground outline-none transition-all placeholder:text-muted/60",
            "focus:border-accent/60 focus:bg-white/[0.04] focus:shadow-[0_0_0_3px_rgba(78,186,236,0.1)]",
            error && "border-rose-500/50",
            className
          )}
          {...rest}
        />
        {error ? (
          <p className="text-[11px] font-medium text-rose-400">{error}</p>
        ) : hint ? (
          <p className="text-[11px] text-muted/80">{hint}</p>
        ) : null}
      </div>
    );
  }
);

type TextareaProps = TextareaHTMLAttributes<HTMLTextAreaElement> & {
  label: string;
  error?: string;
  hint?: string;
};

export const TextArea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  function TextArea({ label, error, hint, className, id, ...rest }, ref) {
    const inputId = id ?? `f-${label.toLowerCase().replace(/\s+/g, "-")}`;
    return (
      <div className="space-y-1.5">
        <label
          htmlFor={inputId}
          className="block text-[12px] font-medium text-foreground/80"
        >
          {label}
        </label>
        <textarea
          id={inputId}
          ref={ref}
          className={cn(
            "w-full rounded-xl border border-white/10 bg-white/[0.02] px-3 py-2.5 text-sm text-foreground outline-none transition-all placeholder:text-muted/60 font-mono",
            "focus:border-accent/60 focus:bg-white/[0.04] focus:shadow-[0_0_0_3px_rgba(78,186,236,0.1)]",
            error && "border-rose-500/50",
            className
          )}
          {...rest}
        />
        {error ? (
          <p className="text-[11px] font-medium text-rose-400">{error}</p>
        ) : hint ? (
          <p className="text-[11px] text-muted/80">{hint}</p>
        ) : null}
      </div>
    );
  }
);

type CheckboxProps = InputHTMLAttributes<HTMLInputElement> & {
  label: string;
};

export function CheckBox({ label, ...rest }: CheckboxProps) {
  return (
    <label className="flex cursor-pointer items-center gap-2 text-[13px] text-foreground/85">
      <input
        type="checkbox"
        className="h-4 w-4 rounded border-white/20 bg-white/[0.04] accent-accent"
        {...rest}
      />
      {label}
    </label>
  );
}
