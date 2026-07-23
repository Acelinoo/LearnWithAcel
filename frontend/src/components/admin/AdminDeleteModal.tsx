"use client";

import { X } from "lucide-react";
import { cn } from "@/lib/utils";

type Props = {
  isOpen: boolean;
  title: string;
  description: string;
  onConfirm: () => void;
  onCancel: () => void;
  confirmText?: string;
  cancelText?: string;
};

export default function AdminDeleteModal({
  isOpen,
  title,
  description,
  onConfirm,
  onCancel,
  confirmText = "Hapus",
  cancelText = "Batal",
}: Props) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/60 backdrop-blur-sm transition-opacity" 
        onClick={onCancel} 
      />
      
      {/* Modal */}
      <div className="relative z-10 w-full max-w-sm overflow-hidden rounded-2xl border border-border bg-[#0a0a0a] p-6 text-left align-middle shadow-xl">
        <button
          onClick={onCancel}
          className="absolute right-4 top-4 rounded-full p-1.5 text-muted transition-colors hover:bg-white/10 hover:text-foreground"
        >
          <X size={16} />
        </button>

        <h3 className="font-display text-lg font-semibold text-foreground">
          {title}
        </h3>
        <p className="mt-2 text-sm text-muted">
          {description}
        </p>

        <div className="mt-6 flex flex-row-reverse gap-3">
          <button
            type="button"
            className="inline-flex items-center justify-center rounded-xl bg-rose-500 px-4 py-2 text-sm font-medium text-white transition-all hover:bg-rose-600 focus:outline-none focus:ring-2 focus:ring-rose-500 focus:ring-offset-2 focus:ring-offset-[#0a0a0a]"
            onClick={onConfirm}
          >
            {confirmText}
          </button>
          <button
            type="button"
            className="inline-flex items-center justify-center rounded-xl border border-border bg-transparent px-4 py-2 text-sm font-medium text-muted transition-all hover:bg-white/5 hover:text-foreground focus:outline-none focus:ring-2 focus:ring-accent focus:ring-offset-2 focus:ring-offset-[#0a0a0a]"
            onClick={onCancel}
          >
            {cancelText}
          </button>
        </div>
      </div>
    </div>
  );
}
