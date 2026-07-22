/**
 * Page shell for the lesson reading experience.
 *
 *   ┌───────────────────────────────────────────────────────────┐
 *   │ container (mx-auto, max-w-7xl)                            │
 *   │ ┌─────────────────────────────┬───────────────────────┐  │
 *   │ │ <main>                      │ <aside> (sidebar)     │  │
 *   │ │   hero                      │   sticky on lg+,      │  │
 *   │ │   article                   │   hidden on mobile    │  │
 *   │ │   footer                    │                       │  │
 *   │ └─────────────────────────────┴───────────────────────┘  │
 *   └───────────────────────────────────────────────────────────┘
 *
 * The shell is responsible for spacing, max widths, and scroll comfort.
 * Page components compose hero/footer/article inside it.
 */

"use client";

import { useState } from "react";
import { Menu, X } from "lucide-react";
import type { ReactNode } from "react";

type Props = {
  children: ReactNode;
  sidebar?: ReactNode;
};

export default function LessonShell({ children, sidebar }: Props) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <div className="mx-auto w-full max-w-7xl px-5 py-16 sm:px-8 sm:py-24">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          <main className="lg:col-span-8 min-w-0">{children}</main>
          {sidebar && <div className="hidden lg:block lg:col-span-4">{sidebar}</div>}
        </div>
      </div>

      {sidebar && (
        <>
          {/* Mobile Floating Button */}
          <button
            onClick={() => setIsOpen(true)}
            className="lg:hidden fixed bottom-6 right-6 z-40 flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white shadow-glow hover:bg-accent-hover active:scale-95 transition-all"
          >
            <Menu size={20} />
          </button>

          {/* Mobile Overlay Drawer */}
          {isOpen && (
            <div className="lg:hidden fixed inset-0 z-50 flex justify-end">
              <div
                className="absolute inset-0 bg-black/60 backdrop-blur-sm transition-opacity"
                onClick={() => setIsOpen(false)}
              />
              <div className="relative h-full w-[85%] max-w-sm overflow-y-auto bg-background p-6 shadow-2xl">
                <button
                  onClick={() => setIsOpen(false)}
                  className="absolute right-4 top-4 rounded-full border border-border bg-card p-2 text-muted hover:text-foreground transition-colors"
                >
                  <X size={18} />
                </button>
                <div className="mt-8">{sidebar}</div>
              </div>
            </div>
          )}
        </>
      )}
    </>
  );
}
