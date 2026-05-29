"use client";

import { motion } from "framer-motion";
import { CheckCircle2, Code, XCircle, FileText } from "lucide-react";
import type { Activity } from "@/types";

interface RecentActivityProps {
  activities: Activity[];
  loading?: boolean;
}

const icons = {
  lesson: FileText,
  exercise: CheckCircle2,
  project: Code,
  code: Code,
};

const resultIcons = {
  success: CheckCircle2,
  fail: XCircle,
};

const resultColors = {
  success: "text-emerald-400",
  fail: "text-red-400",
};

const typeColorBar: Record<string, string> = {
  lesson: "bg-blue-400",
  exercise: "bg-emerald-400",
  project: "bg-violet-400",
  code: "bg-violet-400",
};

export function RecentActivity({ activities, loading }: RecentActivityProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-border bg-card p-6"
    >
      <h3 className="font-semibold">最近动态</h3>

      {loading ? (
        <div className="mt-4 space-y-3">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="flex items-center gap-3 rounded-lg p-2">
              <div className="h-8 w-8 shrink-0 rounded-lg shimmer-bg" />
              <div className="flex-1 space-y-2">
                <div className="h-4 w-3/4 rounded shimmer-bg" />
                <div className="h-3 w-1/4 rounded shimmer-bg" />
              </div>
            </div>
          ))}
        </div>
      ) : activities.length === 0 ? (
        <motion.div
          animate={{ rotate: [-0.5, 0.5, -0.5] }}
          transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
          className="mt-4"
        >
          <p className="text-sm text-muted-foreground">还没有学习记录，快去开始第一节课吧！</p>
        </motion.div>
      ) : (
        <div className="mt-4 space-y-3">
          {activities.map((activity, index) => {
            const Icon = icons[activity.type];
            const ResultIcon = activity.result ? resultIcons[activity.result] : null;
            return (
              <motion.div
                key={activity.id}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.05 }}
                className="group relative flex items-center gap-3 rounded-lg p-2 transition-colors hover:bg-muted/50"
              >
                <span
                  className={`absolute left-0 top-1 bottom-1 w-0.5 rounded-full ${typeColorBar[activity.type]} opacity-0 transition-opacity duration-200 group-hover:opacity-100`}
                />

                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-muted">
                  <Icon className="h-4 w-4 text-muted-foreground" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{activity.title}</p>
                  <p className="text-xs text-muted-foreground">{activity.time}</p>
                </div>
                {ResultIcon && activity.result && (
                  <motion.span
                    whileInView={{ scale: [1, 1.3, 1] }}
                    transition={{ type: "spring", stiffness: 300 }}
                    viewport={{ once: true }}
                    className="inline-flex shrink-0"
                  >
                    <ResultIcon className={`h-4 w-4 ${resultColors[activity.result]}`} />
                  </motion.span>
                )}
              </motion.div>
            );
          })}
        </div>
      )}
    </motion.div>
  );
}
