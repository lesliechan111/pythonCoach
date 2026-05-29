"use client";

import { useMemo } from "react";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import { useCountUp } from "@/hooks/useCountUp";

interface WelcomeBannerProps {
  username?: string;
  studyDays?: number;
}

const QUOTES = [
  "每天坚持学习一点点，你也能成为 Python 高手。今天继续加油！",
  "编程不是记住语法，而是学会用代码思考问题。",
  "伟大的程序员不是一天练成的，都是一行行代码堆出来的。",
  "学编程最好的时间是昨天，其次就是现在。",
  "不积跬步无以至千里，不积代码无以成大神。",
  "错误是学习的一部分，每次报错都是一次成长的机会。",
  "写代码就像解谜题，享受解决问题的过程吧！",
  "今天的努力，就是明天的技能。坚持下去！",
];

export function WelcomeBanner({ username, studyDays = 0 }: WelcomeBannerProps) {
  const greeting = getGreeting();
  const animatedDays = useCountUp(studyDays, 1000);

  const quote = useMemo(() => {
    const idx = (new Date().getHours() + studyDays * 7) % QUOTES.length;
    return QUOTES[idx];
  }, [studyDays]);

  return (
    <motion.div
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      className="relative overflow-hidden rounded-2xl border border-primary/20 bg-gradient-to-br from-primary/10 via-background to-cyan-500/5 p-6 md:p-8"
    >
      {/* Drifting orbs */}
      <div
        className="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-primary/5 blur-3xl animate-orb-drift-1"
        style={{ willChange: "transform" }}
      />
      <div
        className="absolute -bottom-10 -left-10 h-40 w-40 rounded-full bg-cyan-500/5 blur-3xl animate-orb-drift-2"
        style={{ willChange: "transform" }}
      />

      <div className="relative">
        <div className="flex items-center gap-2 text-primary">
          <motion.span
            animate={{ rotate: 360 }}
            transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
            className="inline-flex"
          >
            <Sparkles className="h-5 w-5" />
          </motion.span>
          <span className="text-sm font-medium">
            {studyDays > 0 ? `已连续学习 ${Math.round(animatedDays)} 天` : "开始你的 Python 之旅"}
          </span>
        </div>
        <h1 className="mt-2 text-3xl font-bold md:text-4xl">
          {greeting}，{username || "同学"}！
        </h1>
        <p className="mt-2 max-w-lg text-muted-foreground">
          {quote}
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
