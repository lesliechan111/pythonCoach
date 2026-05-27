"use client";

import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";

interface WelcomeBannerProps {
  username?: string;
  studyDays?: number;
}

export function WelcomeBanner({ username, studyDays = 0 }: WelcomeBannerProps) {
  const greeting = getGreeting();

  return (
    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className="relative overflow-hidden rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/10 via-background to-cyan-500/5 p-6 md:p-8"
    >
      {/* Decorative elements */}
      <div className="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-primary/5 blur-3xl" />
      <div className="absolute -bottom-10 -left-10 h-40 w-40 rounded-full bg-cyan-500/5 blur-3xl" />

      <div className="relative">
        <div className="flex items-center gap-2 text-primary">
          <Sparkles className="h-5 w-5" />
          <span className="text-sm font-medium">
            {studyDays > 0 ? `已连续学习 ${studyDays} 天` : "开始你的 Python 之旅"}
          </span>
        </div>
        <h1 className="mt-2 text-3xl font-bold md:text-4xl">
          {greeting}，{username || "同学"}！
        </h1>
        <p className="mt-2 max-w-lg text-muted-foreground">
          每天坚持学习一点点，你也能成为 Python 高手。今天继续加油！
        </p>
      </div>
    </motion.div>
  );
}

function getGreeting() {
  const hour = new Date().getHours();
  if (hour < 6) return "夜深了";
  if (hour < 9) return "早上好";
  if (hour < 12) return "上午好";
  if (hour < 14) return "中午好";
  if (hour < 18) return "下午好";
  return "晚上好";
}
