import { GraduationCap } from "lucide-react";

export default function Loading() {
  return (
    <div className="container-page py-24 w-full max-w-full overflow-x-hidden px-4">
      <span className="section-eyebrow">
        <GraduationCap size={12} />
        Learning Roadmap
      </span>
      <div className="mt-5 max-w-3xl">
        <div className="h-12 w-3/4 rounded-xl bg-white/5 animate-pulse" />
        <div className="h-12 w-1/2 mt-2 rounded-xl bg-white/5 animate-pulse" />
      </div>
      <div className="mt-5 max-w-2xl space-y-2">
        <div className="h-4 w-full rounded bg-white/5 animate-pulse" />
        <div className="h-4 w-5/6 rounded bg-white/5 animate-pulse" />
      </div>

      <div className="mt-12">
        {/* Tabs skeleton */}
        <div className="flex gap-2 mb-8 overflow-hidden">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="h-10 w-28 rounded-full bg-white/5 animate-pulse shrink-0" />
          ))}
        </div>

        {/* Content skeleton */}
        <div className="relative">
          <div className="absolute left-[26px] top-6 bottom-6 w-px bg-white/5 md:left-[30px]" />
          <div className="space-y-5">
            {[1, 2, 3].map((level) => (
              <div key={level} className="relative pl-16 md:pl-20 w-full max-w-full overflow-hidden">
                <div className="absolute left-0 top-6 flex h-[52px] w-[52px] items-center justify-center rounded-2xl bg-white/5 animate-pulse md:h-[60px] md:w-[60px]" />
                
                <div className="card-base p-6 sm:p-8 w-full flex-1 min-w-0">
                  <div className="flex flex-col gap-4">
                    <div className="h-3 w-16 rounded bg-white/5 animate-pulse" />
                    <div className="h-8 w-1/2 rounded bg-white/5 animate-pulse" />
                    <div className="h-4 w-3/4 rounded bg-white/5 animate-pulse mt-4" />
                    <div className="h-4 w-full rounded bg-white/5 animate-pulse" />
                    
                    <div className="mt-6 grid grid-cols-1 sm:grid-cols-3 gap-3">
                      {[1, 2, 3].map((m) => (
                        <div key={m} className="h-16 rounded-xl bg-white/5 animate-pulse" />
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
