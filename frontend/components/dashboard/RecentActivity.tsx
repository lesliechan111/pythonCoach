"use client";

import { motion } from "framer-motion";
import { CheckCircle2, Code, XCircle, FileText } from "lucide-react";

interface Activity {
  id: number;
  type: "lesson" | "exercise" | "project" | "code";
  title: string;
  result?: "success" | "fail";
  time: string;
}

interface RecentActivityProps {
  activities: Activity[];
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

export function RecentActivity({ activities }: RecentActivityProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-border bg-card p-6"
    >
      <h3 className="font-semibold">最近动态</h3>

      {activities.length === 0 ? (
        <p className="mt-4 text-sm text-muted-foreground">还没有学习记录，快去开始第一节课吧！</p>
      ) : (
        <div className="mt-4 space-y-3">
          {activities.map((activity, index) => {
            const Icon = icons[activity.type];
            const ResultIcon = activity.result ? resultIcons[activity.result] : null;
            return (
              <motion.div
                key={activity.id}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.05 }}
                className="flex items-center gap-3 rounded-lg p-2 transition-colors hover:bg-muted/50"
              >
                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-muted">
                  <Icon className="h-4 w-4 text-muted-foreground" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{activity.title}</p>
                  <p className="text-xs text-muted-foreground">{activity.time}</p>
                </div>
                {ResultIcon && (
                  <ResultIcon className={`h-4 w-4 shrink-0 ${resultColors[activity.result]}`} />
                )}
              </motion.div>
            );
          })}
        </div>
      )}
    </motion.div>
  );
}
