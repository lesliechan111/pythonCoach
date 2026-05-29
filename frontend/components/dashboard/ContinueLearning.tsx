"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, BookOpen, PlayCircle } from "lucide-react";

interface ContinueLearningProps {
  lessonTitle?: string;
  lessonId?: number;
  courseTitle?: string;
  progressPercent?: number;
}

export function ContinueLearning({
  lessonTitle,
  lessonId,
  courseTitle,
  progressPercent = 0,
}: ContinueLearningProps) {
  if (!lessonTitle) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="rounded-2xl border border-border bg-card p-6"
      >
        <h3 className="font-semibold">开始学习</h3>
        <p className="mt-1 text-sm text-muted-foreground">选择一门课程，开启你的 Python 学习之旅</p>
        <Link
          href="/learn"
          className="mt-4 inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90 hover:-translate-y-0.5"
        >
          浏览课程 <ArrowRight className="h-4 w-4" />
        </Link>
      </motion.div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -2 }}
      className="rounded-2xl border border-border bg-card p-6 transition-shadow hover:shadow-lg"
    >
      <div className="flex items-center gap-2 text-sm text-muted-foreground">
        <BookOpen className="h-4 w-4" />
        <span>{courseTitle || "Python 零基础入门"}</span>
      </div>

      <h3 className="mt-2 text-xl font-bold">{lessonTitle}</h3>

      <div className="mt-4">
        <div className="flex items-center justify-between text-xs mb-1.5">
          <span className="text-muted-foreground">课程总进度</span>
          <span className="font-medium">{progressPercent}%</span>
        </div>
        <div className="relative h-2 w-full overflow-visible rounded-full bg-muted">
          <motion.div
            className="h-full rounded-full bg-primary relative"
            initial={{ width: 0 }}
            animate={{ width: `${progressPercent}%` }}
            transition={{ duration: 0.8 }}
          >
            {progressPercent > 0 && (
              <span className="absolute -right-1 -top-0.5 block h-3 w-3 rounded-full bg-primary animate-pulse" />
            )}
          </motion.div>
        </div>
      </div>

      <Link
        href={`/lesson/${lessonId}`}
        className="mt-5 inline-flex w-full items-center justify-center gap-2 rounded-lg bg-primary px-4 py-2.5 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90 hover:-translate-y-0.5"
      >
        <PlayCircle className="h-4 w-4" />
        继续学习
      </Link>
    </motion.div>
  );
}
