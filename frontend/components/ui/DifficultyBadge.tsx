"use client";

import { cn } from "@/lib/utils";

interface DifficultyBadgeProps {
  difficulty: "easy" | "medium" | "hard" | string;
  className?: string;
}

const variants = {
  easy: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20",
  medium: "bg-yellow-500/10 text-yellow-400 border-yellow-500/20",
  hard: "bg-red-500/10 text-red-400 border-red-500/20",
};

const labels: Record<string, string> = {
  easy: "简单",
  medium: "中等",
  hard: "困难",
  beginner: "入门",
  intermediate: "进阶",
  advanced: "高级",
};

export function DifficultyBadge({ difficulty, className }: DifficultyBadgeProps) {
  const variant = variants[difficulty as keyof typeof variants] || variants.easy;
  const label = labels[difficulty] || difficulty;

  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium",
        variant,
        className
      )}
    >
      {label}
    </span>
  );
}
