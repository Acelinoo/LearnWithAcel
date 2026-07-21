"use client";

import { useState } from "react";
import { Briefcase, Wrench, Code2 } from "lucide-react";
import { ROLE_CATEGORIES } from "@/lib/constants";

export default function RoadmapFilter({ categories, panels, defaultMainCategory, defaultRole }) {
  const [activeMainCategory, setActiveMainCategory] = useState(defaultMainCategory || ROLE_CATEGORIES[0].id);
  const [activeRole, setActiveRole] = useState(defaultRole || ROLE_CATEGORIES[0].roles[0].slug);

  const handleMainCategoryChange = (catId) => {
    setActiveMainCategory(catId);
    const mainCat = ROLE_CATEGORIES.find(c => c.id === catId);
    if (mainCat && mainCat.roles.length > 0) {
      setActiveRole(mainCat.roles[0].slug);
    }
  };

  const activeMainCatData = ROLE_CATEGORIES.find(c => c.id === activeMainCategory);
  
  // Find the role data from the backend categories array
  const activeRoleData = categories.find(c => c.id === activeRole);

  return (
    <div>
      {/* Step 1: Main Category Filter */}
      <div className="mb-6 flex flex-wrap gap-2 border-b border-border pb-6">
        {ROLE_CATEGORIES.map((cat) => {
          const Icon = cat.icon;
          return (
            <button
              key={cat.id}
              onClick={() => handleMainCategoryChange(cat.id)}
              className={`flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-medium transition-all ${
                activeMainCategory === cat.id
                  ? "bg-accent/20 text-accent-hover border border-accent/30"
                  : "border border-border bg-black/30 text-muted hover:border-border-strong hover:text-foreground"
              }`}
            >
              {Icon && <Icon size={16} />}
              {cat.title}
            </button>
          );
        })}
      </div>

      {/* Step 2: Role Filter */}
      {activeMainCatData && (
        <div className="flex flex-wrap gap-2">
          {activeMainCatData.roles.map((role) => (
            <button
              key={role.slug}
              onClick={() => setActiveRole(role.slug)}
              className={`flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-medium transition-all ${
                activeRole === role.slug
                  ? "bg-accent/20 text-accent-hover border border-accent/30"
                  : "border border-border bg-black/30 text-muted hover:border-border-strong hover:text-foreground"
              }`}
            >
              {role.name}
            </button>
          ))}
        </div>
      )}

      {/* Role Info Card */}
      {activeRoleData && (
        <div className="mt-6 rounded-2xl border border-border bg-black/30 p-5 sm:p-6">
          <div className="flex items-center gap-2">
            <Briefcase size={14} className="text-accent-hover" />
            <span className="font-mono text-[11px] uppercase tracking-[0.14em] text-accent-hover">
              {activeRoleData.role}
            </span>
            <span className="text-xs text-muted">
              ({activeRoleData.side})
            </span>
          </div>

          <p className="mt-3 text-sm leading-relaxed text-foreground/85">
            {activeRoleData.description}
          </p>

          <div className="mt-4 flex items-start gap-2">
            <Wrench size={13} className="mt-0.5 shrink-0 text-muted" />
            <div>
              <span className="text-xs font-medium uppercase tracking-wider text-muted">
                Tugas Utama
              </span>
              <p className="mt-1 text-sm leading-relaxed text-foreground/80">
                {activeRoleData.tasks}
              </p>
            </div>
          </div>

          {activeRoleData.techs && activeRoleData.techs.length > 0 && (
            <div className="mt-4 flex items-start gap-2">
              <Code2 size={13} className="mt-0.5 shrink-0 text-muted" />
              <div>
                <span className="text-xs font-medium uppercase tracking-wider text-muted">
                  Teknologi Utama
                </span>
                <div className="mt-2 space-y-2">
                  {activeRoleData.techs.map((group) => (
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

      {/* Panels content */}
      <div className="mt-8">
        {panels.map((panel) => (
          <div
            key={panel.id}
            className={activeRole === panel.id ? "block" : "hidden"}
          >
            {panel.content}
          </div>
        ))}
      </div>
    </div>
  );
}
