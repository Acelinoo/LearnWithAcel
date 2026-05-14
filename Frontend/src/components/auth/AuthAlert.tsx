"use client";

import { AnimatePresence, motion } from "framer-motion";
import { AlertCircle, CheckCircle2 } from "lucide-react";
import { cn } from "@/lib/utils";

type Props = {
  type?: "error" | "success";
  message?: string | null;
};

// Framer-motion 11.x has a known typing regression that makes its motion.*
// components reject standard HTML props. Cast once so we still get runtime
// correctness without fighting bad types.
const MDiv = motion.div as unknown as React.FC<
  React.HTMLAttributes<HTMLDivElement> & Record<string, unknown>
>;

export default function AuthAlert({ type = "error", message }: Props) {
  const Icon = type === "error" ? AlertCircle : CheckCircle2;
  return (
    <AnimatePresence initial={false}>
      {message ? (
        <MDiv
          key={message}
          initial={{ opacity: 0, y: -6, height: 0 }}
          animate={{ opacity: 1, y: 0, height: "auto" }}
          exit={{ opacity: 0, y: -6, height: 0 }}
          transition={{ duration: 0.25, ease: [0.22, 1, 0.36, 1] }}
          className={cn(
            "flex items-start gap-2.5 rounded-xl border px-3.5 py-3 text-[13px]",
            type === "error"
              ? "border-red-500/25 bg-red-500/[0.07] text-red-200"
              : "border-emerald-500/25 bg-emerald-500/[0.07] text-emerald-200"
          )}
          role={type === "error" ? "alert" : "status"}
        >
          <Icon size={15} className="mt-0.5 shrink-0" />
          <span className="leading-relaxed">{message}</span>
        </MDiv>
      ) : null}
    </AnimatePresence>
  );
}
