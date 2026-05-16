import { cn } from "@/lib/utils";

export default function ProgressBar({ value = 0, className, showLabel = false }) {
  const clamped = Math.max(0, Math.min(100, value));
  return (
    <div className={cn("w-full", className)}>
      <div className="h-1.5 w-full overflow-hidden rounded-full bg-black/40">
        <div
          className="h-full rounded-full bg-gradient-to-r from-accent to-accent-hover transition-all duration-700"
          style={{ width: `${clamped}%` }}
        />
      </div>
      {showLabel && (
        <div className="mt-1.5 flex items-center justify-between text-xs text-muted">
          <span>Progress</span>
          <span className="font-medium text-foreground">{Math.round(clamped)}%</span>
        </div>
      )}
    </div>
  );
}
