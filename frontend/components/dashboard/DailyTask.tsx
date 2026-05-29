"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, Sparkles } from "lucide-react";

interface DailyTaskProps {
  title?: string;
  lessonId?: number;
}

export function DailyTask({ title, lessonId }: DailyTaskProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-xl border border-primary/20 bg-gradient-to-r from-primary/10 to-cyan-500/10 p-6 transition-all duration-300 hover:from-primary/15 hover:to-cyan-500/15"
    >
      <div className="flex items-center gap-2 text-primary">
        <motion.span
          animate={{ rotate: 360 }}
          transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
          className="inline-flex"
        >
          <Sparkles className="h-5 w-5" />
        </motion.span>
        <span className="text-sm font-semibold">今日学习任务</span>
      </div>
      {title ? (
        <div className="mt-3 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-bold">{title}</h3>
            <p className="text-sm text-muted-foreground">继续你的学习之旅</p>
          </div>
          <Link
            href={`/lesson/${lessonId}`}
            className="flex items-center gap-1 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90"
          >
            继续学习
            <motion.span whileHover={{ x: [0, 3, -3, 0] }} transition={{ duration: 0.4 }}>
              <ArrowRight className="h-4 w-4" />
            </motion.span>
          </Link>
        </div>
      ) : (
        <div className="mt-3">
          <p className="text-sm text-muted-foreground">还没有今日任务，去课程页选一节开始吧！</p>
          <Link
            href="/learn"
            className="mt-2 inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline"
          >
            浏览课程 <ArrowRight className="h-3 w-3" />
          </Link>
        </div>
      )}
    </motion.div>
  );
}
