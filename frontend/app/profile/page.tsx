"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { User, Target, Award } from "lucide-react";
import { ProgressCard } from "@/components/dashboard/ProgressCard";
import { StatsGrid } from "@/components/dashboard/StatsGrid";
import { useAuth } from "@/hooks/useAuth";
import type { DashboardStats } from "@/types";

export default function ProfilePage() {
  const { user, token } = useAuth();
  const [stats, setStats] = useState<DashboardStats>({
    completed_lessons: 0,
    total_lessons: 0,
    completed_exercises: 0,
    total_exercises: 0,
    wrong_questions: 0,
    completed_projects: 0,
    total_projects: 0,
    study_days: 0,
    accuracy_rate: 0,
  });

  useEffect(() => {
    if (!token) return;
    fetch("/api/v1/users/me/dashboard", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((json) => {
        if (json.data) setStats(json.data.stats);
      })
      .catch(console.error);
  }, [token]);

  const lessonPercent = stats.total_lessons > 0
    ? Math.round((stats.completed_lessons / stats.total_lessons) * 100)
    : 0;
  const exercisePercent = stats.total_exercises > 0
    ? Math.round((stats.completed_exercises / stats.total_exercises) * 100)
    : 0;
  const projectPercent = stats.total_projects > 0
    ? Math.round((stats.completed_projects / stats.total_projects) * 100)
    : 0;

  return (
    <div className="mx-auto max-w-5xl p-4 pb-12">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8 flex flex-col items-center gap-4 rounded-2xl border border-border bg-card p-8 md:flex-row md:items-start"
      >
        <div className="flex h-20 w-20 items-center justify-center rounded-full bg-primary/10 text-primary">
          <User className="h-10 w-10" />
        </div>
        <div className="text-center md:text-left">
          <h1 className="text-2xl font-bold">{user?.username || "同学"}</h1>
          <p className="mt-1 text-muted-foreground">
            加入 Python Coach {stats.study_days > 0 ? `第 ${stats.study_days} 天` : ""} · 正在学习 Python 零基础入门
          </p>
          <div className="mt-3 flex flex-wrap justify-center gap-2 md:justify-start">
            <span className="inline-flex items-center gap-1 rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
              <Award className="h-3.5 w-3.5" />
              {user?.level === "beginner" ? "初学者" : user?.level || "初学者"}
            </span>
            <span className="inline-flex items-center gap-1 rounded-full bg-muted px-3 py-1 text-xs font-medium text-muted-foreground">
              <Target className="h-3.5 w-3.5" />
              目标：Python 零基础入门
            </span>
          </div>
        </div>
      </motion.div>

      <StatsGrid stats={stats} />

      <div className="mt-8">
        <h2 className="mb-4 text-lg font-semibold">学习概览</h2>
        <div className="grid gap-4 sm:grid-cols-3">
          <ProgressCard percent={lessonPercent} completed={stats.completed_lessons} total={stats.total_lessons} label="课程" />
          <ProgressCard percent={exercisePercent} completed={stats.completed_exercises} total={stats.total_exercises} label="题目" />
          <ProgressCard percent={projectPercent} completed={stats.completed_projects} total={stats.total_projects} label="项目" />
        </div>
      </div>
    </div>
  );
}
