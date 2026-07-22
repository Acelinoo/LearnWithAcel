"use client";

import { useState } from "react";
import { TrendingUp, Flame, ChevronDown } from "lucide-react";
import ProgressByLevel from "./ProgressByLevel";

export default function DashboardProgressCard({ stats, categories, roadmapMap, defaultRole }) {
  const [activeRole, setActiveRole] = useState(defaultRole);

  const activeCategory = categories.find(c => c.slug === activeRole) || categories[0];
  
  // Calculate role-specific stats
  let roleTotalLessons = 0;
  let roleCompletedLessons = 0;
  const roleLevels = roadmapMap[activeRole] || [];
  
  // Extract completed lesson IDs from stats if available
  const completedIds = new Set(stats?.completed_lesson_ids || []);
  
  const roleByLevel = [];
  
  roleLevels.forEach(level => {
    const totalLevelLessons = level.lessons?.length || 0;
    if (totalLevelLessons === 0) return; // Skip levels with no lessons
    
    let completedLevelLessons = 0;
    level.lessons.forEach(lesson => {
      if (completedIds.has(lesson.id)) {
        completedLevelLessons++;
      }
    });
    
    roleTotalLessons += totalLevelLessons;
    roleCompletedLessons += completedLevelLessons;
    
    // Calculate percentage
    const percentage = totalLevelLessons > 0 ? (completedLevelLessons / totalLevelLessons) * 100 : 0;
    
    roleByLevel.push({
      level_id: level.id,
      level_title: level.title,
      level_slug: level.slug,
      total_lessons: totalLevelLessons,
      completed_lessons: completedLevelLessons,
      percentage
    });
  });

  const rolePercentage = roleTotalLessons > 0 ? (roleCompletedLessons / roleTotalLessons) * 100 : 0;
  
  // Filter out levels with 0% progress if we have many levels, or just show them all and let ProgressByLevel handle the top 3
  // Wait, backend's by_level only includes levels with >0% progress typically, but it's fine to include all here, ProgressByLevel handles slicing.
  // Actually, we should only pass levels that have > 0 completed or are the next immediate level to tackle.
  // We can sort them by percentage descending or just keep the original order and filter those with completed > 0 or the first one with 0.
  const activeRoleLevels = roleByLevel.filter(l => l.completed_lessons > 0);
  if (activeRoleLevels.length === 0 && roleByLevel.length > 0) {
    activeRoleLevels.push(roleByLevel[0]); // Show at least the first level if no progress
  }

  return (
    <div className="card-base relative h-full overflow-hidden p-4 sm:p-6 md:p-8 flex flex-col justify-between">
      <div className="pointer-events-none absolute -right-16 -top-16 h-48 w-48 rounded-full bg-accent/20 blur-3xl" />
      <div className="relative">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2 text-xs uppercase tracking-[0.14em] text-muted">
            <TrendingUp size={12} />
            Progress kamu
          </div>
          
          <div className="relative group">
            <select 
              value={activeRole}
              onChange={(e) => setActiveRole(e.target.value)}
              className="appearance-none bg-white/[0.03] border border-white/10 rounded-lg pl-3 pr-8 py-1.5 text-xs font-medium text-foreground hover:bg-white/[0.05] transition-colors focus:outline-none focus:ring-1 focus:ring-accent cursor-pointer"
            >
              {categories.map(cat => (
                <option key={cat.slug} value={cat.slug} className="bg-black text-foreground">
                  {cat.name}
                </option>
              ))}
            </select>
            <ChevronDown size={14} className="absolute right-2.5 top-1/2 -translate-y-1/2 text-muted pointer-events-none" />
          </div>
        </div>
        
        <div className="mt-5 flex flex-wrap items-end justify-between gap-4 sm:gap-6">
          <div>
            <div className="font-display text-5xl font-semibold tabular-nums">
              {stats ? `${roleCompletedLessons} / ${roleTotalLessons}` : "-"}
            </div>
            <div className="mt-2 text-sm text-muted">
              materi sudah kamu selesaikan
            </div>
          </div>
          <div className="flex items-center gap-1.5 rounded-full border border-emerald-400/30 bg-emerald-400/10 px-3 py-1 text-xs font-medium text-emerald-300">
            <Flame size={12} />
            {stats ? `${rolePercentage.toFixed(0)}%` : "0%"}
          </div>
        </div>

        {stats && (
          <div className="mt-8">
            <ProgressByLevel byLevel={activeRoleLevels} />
          </div>
        )}
      </div>
    </div>
  );
}
