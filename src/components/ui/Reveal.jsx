"use client";

import { motion } from "framer-motion";

export default function Reveal({
  children,
  delay = 0,
  y = 20,
  as: Tag = "div",
  className,
  once = true,
}) {
  const MotionTag = motion[Tag] || motion.div;
  return (
    <MotionTag
      initial={{ opacity: 0, y }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once, margin: "-80px" }}
      transition={{ duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] }}
      className={className}
    >
      {children}
    </MotionTag>
  );
}
