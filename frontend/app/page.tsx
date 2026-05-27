"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { WelcomeBanner } from "@/components/dashboard/WelcomeBanner";
import { ContinueLearning } from "@/components/dashboard/ContinueLearning";
import { ProgressCard } from "@/components/dashboard/ProgressCard";
import { StatsGrid } from "@/components/dashboard/StatsGrid";
import { DailyTask } from "@/components/dashboard/DailyTask";
import { RecentActivity } from "@/components/dashboard/RecentActivity";
import { CourseCard } from "@/components/ui/CourseCard";
import { useAuth } from "@/hooks/useAuth";
import type { DashboardStats } from "@/types";

interface Course {
  id: number;
  title: string;
  description: string;
  category: string;
  level: string;
  lesson_count: number;
  estimated_minutes: number;
  progress_percent: number;
}

export default function DashboardPage() {
  const { user, token } = useAuth();
  const [courses, setCourses] = useState<Course[]>([]);
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
  const [loading, setLoading] = useState(true);
  const [continueLessonId, setContinueLessonId] = useState<number | null>(null);

  useEffect(() => {
    async function load() {
      try {
        const headers: Record<string, string> = {};
        if (token) headers["Authorization"] = `Bearer ${token}`;

        const [coursesRes, dashRes] = await Promise.all([
          fetch("/api/v1/courses"),
          token ? fetch("/api/v1/users/me/dashboard", { headers }) : Promise.resolve(null),
        ]);

        const coursesJson = await coursesRes.json();
        if (coursesJson.data) {
          setCourses(
            coursesJson.data.map((c: any) => ({
              ...c,
              lesson_count: c.lesson_count || 0,
              progress_percent: 0,
            }))
          );
        }

        if (dashRes) {
          const dashJson = await dashRes.json();
          if (dashJson.data) {
            setStats(dashJson.data.stats);
            setContinueLessonId(dashJson.data.continue_lesson_id);
          }
        }
      } catch (err) {
        console.error("Failed to fetch dashboard:", err);
      } finally {
        setLoading(false);
      }
    }
    load();
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

  const isAuthenticated = !!user;

  return (
    <div className="mx-auto max-w-7xl space-y-6 p-4 pb-12">
      <WelcomeBanner username={user?.username} studyDays={stats.study_days} />

      <div className="grid gap-6 lg:grid-cols-3">
        <div className="space-y-6 lg:col-span-2">
          {isAuthenticated && continueLessonId && (
            <ContinueLearning
              lessonTitle={`第 ${continueLessonId} 课`}
              lessonId={continueLessonId}
              courseTitle="Python 零基础入门"
              progressPercent={lessonPercent}
            />
          )}

          {isAuthenticated ? (
            <>
              <div className="grid gap-4 sm:grid-cols-3">
                <ProgressCard percent={lessonPercent} completed={stats.completed_lessons} total={stats.total_lessons} label="课程" />
                <ProgressCard percent={exercisePercent} completed={stats.completed_exercises} total={stats.total_exercises} label="题目" />
                <ProgressCard percent={projectPercent} completed={stats.completed_projects} total={stats.total_projects} label="项目" />
              </div>
              <StatsGrid stats={stats} />
            </>
          ) : (
            <div className="rounded-2xl border border-border bg-gradient-to-br from-primary/5 to-cyan-500/5 p-8 text-center">
              <h2 className="text-lg font-semibold">开始你的 Python 学习之旅</h2>
              <p className="mt-2 text-sm text-muted-foreground max-w-md mx-auto">
                注册账号后可以追踪学习进度、记录错题、完成项目实战。每天进步一点点！
              </p>
            </div>
          )}

          <div>
            <h2 className="mb-4 text-lg font-semibold">我的课程</h2>
            {loading ? (
              <p className="text-sm text-muted-foreground">加载中...</p>
            ) : (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {courses.map((course, i) => (
                  <CourseCard key={course.id} course={course} index={i} />
                ))}
              </div>
            )}
          </div>
        </div>

        <div className="space-y-6">
          {isAuthenticated && continueLessonId && (
            <DailyTask title={`第 ${continueLessonId} 课`} lessonId={continueLessonId} />
          )}
          <RecentActivity activities={[]} />
        </div>
      </div>
    </div>
  );
}
