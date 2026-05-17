"use client";

/**
 * Drop-in component that fires a single view track on mount.
 *
 * Use anywhere a page/section should be counted toward an entity's
 * view total. Renders nothing.
 *
 *   <ViewTracker entityType="lesson" entityId={lesson.id} />
 *   <ViewTracker entityType="level"  entityId={level.id}  />
 *   <ViewTracker entityType="page"   entityId="homepage"  />
 *
 * Behaviour delegates to `useViewTracker` so all the usual debounce /
 * cooldown / anonymous-friendly logic applies uniformly.
 */

import { useViewTracker } from "@/lib/hooks/useViewTracker";
import type { EntityType } from "@/lib/api/views";

type Props = {
  entityType: EntityType;
  entityId: string | null | undefined;
  pathname?: string;
  enabled?: boolean;
  cooldownMinutes?: number;
};

export default function ViewTracker(props: Props) {
  useViewTracker(props);
  return null;
}
