"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Folders, GraduationCap, NotebookPen, Users, Activity, Target } from "lucide-react";
import { useAuth } from "@/components/providers/AuthProvider";
import type { ApiRoadmap } from "@/lib/api/content";
import { getAdminStats, type AdminStats } from "@/lib/api/admin";
import { cn } from "@/lib/utils";
import CategoryManager from "./CategoryManager";
import LevelManager from "./LevelManager";
import LessonManager from "./LessonManager";
import UserManager from "./UserManager";

type Tab = "categories" | "levels" | "lessons" | "users";

const TABS: { id: Tab; label: string; icon: React.ComponentType<{ size?: number; className?: string }> }[] = [
  { id: "categories", label: "Categories", icon: Folders },
  { id: "levels", label: "Levels", icon: GraduationCap },
  { id: "lessons", label: "Lessons", icon: NotebookPen },
  { id: "users", label: "Manajemen User", icon: Users },
];

type Props = {
  initialRoadmaps: ApiRoadmap[];
};

export default function AdminCMS({ initialRoadmaps }: Props) {
  const router = useRouter();
  const { token } = useAuth();
  const [tab, setTab] = useState<Tab>("categories");
  const [stats, setStats] = useState<AdminStats | null>(null);

  const refresh = () => router.refresh();

  useEffect(() => {
    if (token) {
      getAdminStats(token)
        .then(setStats)
        .catch((err) => console.error("Failed to load stats", err));
    }
  }, [token]);

  if (!token) {
    return (
      <p className="text-sm text-muted">
        Token tidak tersedia. Coba login ulang.
      </p>
    );
  }

  return (
    <div className="space-y-8">
      {/* Stat Cards */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        <div className="card-base flex items-center gap-4 p-5">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-accent/20 text-accent">
            <Users size={20} />
          </div>
          <div>
            <p className="text-sm font-medium text-muted">Total User Terdaftar</p>
            <p className="font-display text-2xl font-semibold">
              {stats ? stats.total_users : "..."}
            </p>
          </div>
        </div>
        <div className="card-base flex items-center gap-4 p-5">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-accent/20 text-accent">
            <Target size={20} />
          </div>
          <div>
            <p className="text-sm font-medium text-muted">Total Lesson Selesai</p>
            <p className="font-display text-2xl font-semibold">
              {stats ? stats.completed_lessons : "..."}
            </p>
          </div>
        </div>
      </div>

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
          {tab === "users" && <UserManager token={token} />}
        </div>
      </div>
    </div>
  );
}
