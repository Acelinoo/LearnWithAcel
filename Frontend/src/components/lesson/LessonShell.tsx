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

import type { ReactNode } from "react";

type Props = {
  children: ReactNode;
  sidebar?: ReactNode;
};

export default function LessonShell({ children, sidebar }: Props) {
  return (
    <div className="mx-auto w-full max-w-7xl px-5 py-12 sm:px-8 sm:py-16">
      <div className="lg:grid lg:grid-cols-[minmax(0,1fr)_19rem] lg:gap-12 xl:gap-16">
        <main className="min-w-0">{children}</main>
        {sidebar}
      </div>
    </div>
  );
}
