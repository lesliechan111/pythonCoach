"use client";

import { motion } from "framer-motion";

interface ProgressCardProps {
  percent: number;
  completed: number;
  total: number;
  label: string;
}

export function ProgressCard({ percent, completed, total, label }: ProgressCardProps) {
  const circumference = 2 * Math.PI * 40;
  const offset = circumference - (percent / 100) * circumference;

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="flex flex-col items-center rounded-xl border border-border bg-card p-6 shadow-sm"
    >
      <div className="relative h-32 w-32">
        <svg className="h-full w-full" viewBox="0 0 100 100">
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="currentColor"
            strokeWidth="8"
            className="text-muted/20"
          />
          <motion.circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="currentColor"
            strokeWidth="8"
            strokeLinecap="round"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset: offset }}
            transition={{ duration: 1, ease: "easeOut" }}
            className="text-primary"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-2xl font-bold">{percent}%</span>
        </div>
      </div>
      <p className="mt-4 text-sm font-medium text-muted-foreground">
        {completed} / {total} {label}
      </p>
    </motion.div>
  );
}
