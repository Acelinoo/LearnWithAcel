"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Folders, GraduationCap, NotebookPen } from "lucide-react";
import { useAuth } from "@/components/providers/AuthProvider";
import type { ApiRoadmap } from "@/lib/api/content";
import { cn } from "@/lib/utils";
import CategoryManager from "./CategoryManager";
import LevelManager from "./LevelManager";
import LessonManager from "./LessonManager";

type Tab = "categories" | "levels" | "lessons";

const TABS: { id: Tab; label: string; icon: React.ComponentType<{ size?: number; className?: string }> }[] = [
  { id: "categories", label: "Categories", icon: Folders },
  { id: "levels", label: "Levels", icon: GraduationCap },
  { id: "lessons", label: "Lessons", icon: NotebookPen },
];

type Props = {
  initialRoadmaps: ApiRoadmap[];
};

export default function AdminCMS({ initialRoadmaps }: Props) {
  const router = useRouter();
  const { token } = useAuth();
  const [tab, setTab] = useState<Tab>("categories");

  const refresh = () => router.refresh();

  if (!token) {
    return (
      <p className="text-sm text-muted">
        Token tidak tersedia. Coba login ulang.
      </p>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-2">
        {TABS.map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => setTab(id)}
            className={cn(
              "flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-medium transition-all",
              tab === id
                ? "border border-accent/30 bg-accent/20 text-accent-hover"
                : "border border-border bg-black/30 text-muted hover:border-border hover:text-foreground"
            )}
          >
            <Icon size={14} />
            {label}
          </button>
        ))}
      </div>

      <div className="card-base p-6 sm:p-8">
        {tab === "categories" && (
          <CategoryManager
            roadmaps={initialRoadmaps}
            token={token}
            onChange={refresh}
          />
        )}
        {tab === "levels" && (
          <LevelManager
            roadmaps={initialRoadmaps}
            token={token}
            onChange={refresh}
          />
        )}
        {tab === "lessons" && (
          <LessonManager
            roadmaps={initialRoadmaps}
            token={token}
            onChange={refresh}
          />
        )}
      </div>
    </div>
  );
}
