import { Loader2 } from "lucide-react";

export default function Loading() {
  return (
    <div className="flex min-h-[calc(100vh-5rem)] items-center justify-center">
      <div className="flex items-center gap-2 text-sm text-muted">
        <Loader2 size={16} className="animate-spin text-accent-hover" />
        Menyiapkan onboarding...
      </div>
    </div>
  );
}
