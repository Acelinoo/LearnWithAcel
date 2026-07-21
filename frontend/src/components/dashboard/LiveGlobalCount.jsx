"use client";

import { useViewerCountReadOnly } from "@/hooks/useViewerCount";
import { formatCompact } from "@/lib/utils";

export default function LiveGlobalCount({ fallback }) {
  const { count, ready } = useViewerCountReadOnly();
  return (
    <span className="tabular-nums">
      {ready ? formatCompact(count) : formatCompact(fallback)}
    </span>
  );
}
