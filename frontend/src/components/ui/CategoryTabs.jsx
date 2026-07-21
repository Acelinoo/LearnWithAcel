"use client";

import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { Lock, Briefcase, Wrench, Code2 } from "lucide-react";

/**
 * Tabs for switching between learning paths.
 *
 * The active tab can be preselected via the URL `?path=<id>` query
 * param. That hook is wrapped in its own Suspense boundary so callers
 * don't need to know about the dynamic rendering quirk Next.js 14
 * imposes on `useSearchParams`.
 */
export default function CategoryTabs({ categories, panels }) {
  const fallbackId = categories[0]?.id;
  return (
    <Suspense
      fallback={
        <CategoryTabsBody
          categories={categories}
          panels={panels}
          requested={null}
          fallbackId={fallbackId}
        />
      }
    >
      <CategoryTabsWithSearch
        categories={categories}
        panels={panels}
        fallbackId={fallbackId}
      />
    </Suspense>
  );
}

function CategoryTabsWithSearch({ categories, panels, fallbackId }) {
  const searchParams = useSearchParams();
  const requested = searchParams?.get("path") ?? null;
  return (
    <CategoryTabsBody
      categories={categories}
      panels={panels}
      requested={requested}
      fallbackId={fallbackId}
    />
  );
}

function CategoryTabsBody({ categories, panels, requested, fallbackId }) {
  const initial =
    requested && categories.some((c) => c.id === requested)
      ? requested
      : fallbackId;

  const [active, setActive] = useState(initial);

  useEffect(() => {
    if (requested && categories.some((c) => c.id === requested)) {
      setActive(requested);
    }
  }, [requested, categories]);

  const activeCategory = categories.find((c) => c.id === active);

  return (
    <div>
      <div className="flex flex-wrap gap-2">
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setActive(cat.id)}
            className={`flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-medium transition-all ${
              active === cat.id
                ? "bg-accent/20 text-accent-hover border border-accent/30"
                : "border border-border bg-black/30 text-muted hover:border-border-strong hover:text-foreground"
            }`}
          >
            {cat.label}
            {!cat.available && <Lock size={12} className="text-muted" />}
          </button>
        ))}
      </div>

      {/* Role info card */}
      {activeCategory && (
        <div className="mt-6 rounded-2xl border border-border bg-black/30 p-5 sm:p-6">
          <div className="flex items-center gap-2">
            <Briefcase size={14} className="text-accent-hover" />
            <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-accent-hover">
              {activeCategory.role}
            </span>
            <span className="text-xs text-muted">
              ({activeCategory.side})
            </span>
          </div>

          <p className="mt-3 text-sm leading-relaxed text-foreground/85">
            {activeCategory.description}
          </p>

          <div className="mt-4 flex items-start gap-2">
            <Wrench size={13} className="mt-0.5 shrink-0 text-muted" />
            <div>
              <span className="text-xs font-medium uppercase tracking-wider text-muted">
                Tugas Utama
              </span>
              <p className="mt-1 text-sm leading-relaxed text-foreground/80">
                {activeCategory.tasks}
              </p>
            </div>
          </div>

          {activeCategory.techs && (
            <div className="mt-4 flex items-start gap-2">
              <Code2 size={13} className="mt-0.5 shrink-0 text-muted" />
              <div>
                <span className="text-xs font-medium uppercase tracking-wider text-muted">
                  Teknologi Utama
                </span>
                <div className="mt-2 space-y-2">
                  {activeCategory.techs.map((group) => (
                    <div key={group.label} className="flex flex-wrap items-center gap-1.5">
                      <span className="text-xs text-muted">{group.label}:</span>
                      {group.items.map((item) => (
                        <span
                          key={item}
                          className="rounded-full border border-border bg-black/40 px-2 py-0.5 text-[11px] text-foreground/80"
                        >
                          {item}
                        </span>
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      <div className="mt-8">
        {panels.map((panel) => (
          <div
            key={panel.id}
            className={active === panel.id ? "block" : "hidden"}
          >
            {panel.content}
          </div>
        ))}
      </div>
    </div>
  );
}
