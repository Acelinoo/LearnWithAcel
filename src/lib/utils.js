export function cn(...classes) {
  return classes.filter(Boolean).join(" ");
}

export function formatNumber(n) {
  if (typeof n !== "number" || Number.isNaN(n)) return "0";
  return new Intl.NumberFormat("en-US").format(n);
}

export function formatCompact(n) {
  if (typeof n !== "number" || Number.isNaN(n)) return "0";
  if (n < 1000) return String(n);
  if (n < 10000) return `${(n / 1000).toFixed(1)}K`;
  if (n < 1_000_000) return `${Math.round(n / 1000)}K`;
  return `${(n / 1_000_000).toFixed(1)}M`;
}
