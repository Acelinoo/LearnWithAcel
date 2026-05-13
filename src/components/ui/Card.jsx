import { cn } from "@/lib/utils";

export function Card({ className, children, hover = true, ...rest }) {
  return (
    <div
      className={cn(
        "card-base p-6",
        hover && "card-hover",
        className
      )}
      {...rest}
    >
      {children}
    </div>
  );
}
