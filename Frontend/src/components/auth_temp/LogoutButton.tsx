"use client";

import { useState } from "react";
import { LogOut, Loader2 } from "lucide-react";
import { useAuth } from "@/components/providers/AuthProvider";
import { cn } from "@/lib/utils";

type Props = {
  className?: string;
  variant?: "primary" | "secondary" | "ghost";
  label?: string;
};

export default function LogoutButton({
  className,
  variant = "secondary",
  label = "Keluar",
}: Props) {
  const { signOut } = useAuth();
  const [loading, setLoading] = useState(false);

  const handle = async () => {
    if (loading) return;
    setLoading(true);
    try {
      await signOut();
    } finally {
      setLoading(false);
    }
  };

  const base =
    variant === "primary"
      ? "btn-primary"
      : variant === "ghost"
        ? "btn-ghost"
        : "btn-secondary";

  return (
    <button
      type="button"
      onClick={handle}
      disabled={loading}
      className={cn(base, "disabled:cursor-not-allowed disabled:opacity-60", className)}
    >
      {loading ? (
        <Loader2 size={15} className="animate-spin" />
      ) : (
        <LogOut size={15} />
      )}
      {label}
    </button>
  );
}
