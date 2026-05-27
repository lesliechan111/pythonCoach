"use client";

import { motion } from "framer-motion";
import { BookOpen, CheckCircle2, XCircle, FolderGit2, Calendar, Target } from "lucide-react";
import type { DashboardStats } from "@/types";

const icons = {
  completed_lessons: BookOpen,
  completed_exercises: CheckCircle2,
  wrong_questions: XCircle,
  completed_projects: FolderGit2,
  study_days: Calendar,
  accuracy_rate: Target,
};

const labels: Record<string, string> = {
  completed_lessons: "已完成课程",
  completed_exercises: "已完成题目",
  wrong_questions: "错题数",
  completed_projects: "已完成项目",
  study_days: "学习天数",
  accuracy_rate: "正确率",
};

export function StatsGrid({ stats }: { stats: DashboardStats }) {
  const entries = Object.entries(stats).filter(([key]) => key in labels);

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
      {entries.map(([key, value], index) => {
        const Icon = icons[key as keyof typeof icons];
        const displayValue = key === "accuracy_rate" ? `${Math.round((value as number) * 100)}%` : value;
        return (
          <motion.div
            key={key}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className="rounded-xl border border-border bg-card p-4 shadow-sm"
          >
            <div className="flex items-center gap-2 text-muted-foreground">
              <Icon className="h-4 w-4" />
              <span className="text-xs">{labels[key]}</span>
            </div>
            <p className="mt-2 text-2xl font-bold">{displayValue}</p>
          </motion.div>
        );
      })}
    </div>
  );
}
