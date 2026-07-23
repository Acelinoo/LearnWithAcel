import { Loader2 } from "lucide-react";

export default function LessonSkeleton() {
  return (
    <div className="container-page py-12 md:py-16 w-full max-w-full overflow-x-hidden px-4 md:px-8 lg:px-12">
      <div className="mx-auto max-w-4xl">
        <div className="mb-8 flex flex-wrap items-center gap-2 md:mb-10 text-sm">
          <div className="h-5 w-20 rounded bg-white/5 animate-pulse" />
          <span className="text-muted/50">/</span>
          <div className="h-5 w-32 rounded bg-white/5 animate-pulse" />
        </div>

        <div className="space-y-10 pb-16">
          <div className="relative overflow-hidden rounded-2xl border border-white/10 bg-white/5 p-6 sm:p-8 min-h-[200px] flex flex-col justify-center">
            <div className="mb-4 h-8 w-3/4 rounded-lg bg-white/10 animate-pulse" />
            <div className="h-4 w-1/2 rounded bg-white/10 animate-pulse mt-2" />
            <div className="h-4 w-2/3 rounded bg-white/10 animate-pulse mt-2" />
          </div>

          <section className="space-y-4">
            <div className="h-6 w-1/3 rounded bg-white/5 animate-pulse" />
            <div className="space-y-2">
              <div className="h-4 w-full rounded bg-white/5 animate-pulse" />
              <div className="h-4 w-[90%] rounded bg-white/5 animate-pulse" />
              <div className="h-4 w-[95%] rounded bg-white/5 animate-pulse" />
              <div className="h-4 w-[85%] rounded bg-white/5 animate-pulse" />
            </div>
            <div className="space-y-2 pt-4">
              <div className="h-4 w-full rounded bg-white/5 animate-pulse" />
              <div className="h-4 w-[80%] rounded bg-white/5 animate-pulse" />
              <div className="h-4 w-[88%] rounded bg-white/5 animate-pulse" />
            </div>
          </section>

          <section className="mt-12 rounded-2xl border border-white/10 bg-white/5 p-6 text-center sm:p-10 flex flex-col items-center justify-center">
            <div className="h-16 w-16 rounded-full bg-white/10 animate-pulse mb-6 flex items-center justify-center">
              <Loader2 className="h-8 w-8 text-white/20 animate-spin" />
            </div>
            <div className="h-6 w-48 rounded bg-white/10 animate-pulse mb-4" />
            <div className="h-10 w-40 rounded-full bg-white/10 animate-pulse" />
          </section>
        </div>
      </div>
    </div>
  );
}
