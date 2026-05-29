"use client";

import { motion } from "framer-motion";
import { BookOpen, CheckCircle2, XCircle, FolderGit2, Calendar, Target } from "lucide-react";
import { useCountUp } from "@/hooks/useCountUp";
import type { DashboardStats } from "@/types";

const icons: Record<string, React.ComponentType<{ className?: string }>> = {
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

function getAccuracyColor(rate: number): string {
  if (rate >= 0.8) return "text-emerald-400";
  if (rate >= 0.6) return "text-amber-400";
  return "";
}

function StatItem({
  statKey,
  value,
  index,
}: {
  statKey: string;
  value: number;
  index: number;
}) {
  const Icon = icons[statKey];
  const isAccuracy = statKey === "accuracy_rate";
  const target = isAccuracy ? Math.round(value * 100) : value;
  const countUpValue = useCountUp(target, 800);
  const accuracyClass = isAccuracy ? getAccuracyColor(value) : "";

  return (
    <motion.div
      initial={{ opacity: 0, x: -10, y: 10 }}
      animate={{ opacity: 1, x: 0, y: 0 }}
      transition={{ delay: index * 0.05 }}
      className="rounded-xl border border-border bg-card p-4 shadow-sm"
    >
      <div className="flex items-center gap-2 text-muted-foreground">
        <motion.span
          whileInView={{ scale: [1, 1.2, 1] }}
          transition={{ type: "spring", stiffness: 300, delay: 0.15 }}
          viewport={{ once: true }}
          className="inline-flex"
        >
          <Icon className="h-4 w-4" />
        </motion.span>
        <span className="text-xs">{labels[statKey]}</span>
      </div>
      <p className={`mt-2 text-2xl font-bold ${accuracyClass}`}>
        {isAccuracy ? `${countUpValue}%` : countUpValue}
      </p>
    </motion.div>
  );
}

export function StatsGrid({ stats }: { stats: DashboardStats }) {
  const entries = Object.entries(stats).filter(([key]) => key in labels);

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
      {entries.map(([key, value], index) => (
        <StatItem key={key} statKey={key} value={value as number} index={index} />
      ))}
    </div>
  );
}
