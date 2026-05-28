"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { BookOpen, Trophy } from "lucide-react";
import { LessonCard } from "@/components/learn/LessonCard";
import { DifficultyBadge } from "@/components/ui/DifficultyBadge";
import { useAuth } from "@/hooks/useAuth";
import type { Lesson } from "@/types";

export default function LearnPage() {
  const params = useParams();
  const courseId = Number(params.courseId);
  const { token } = useAuth();
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [courseMeta, setCourseMeta] = useState<{
    title: string;
    description: string;
    level: string;
    estimated_minutes: number;
    lesson_count: number;
  } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const headers: Record<string, string> = token
          ? { Authorization: `Bearer ${token}` }
          : {};

        const [courseRes, progressRes] = await Promise.all([
          fetch(`/api/v1/courses/${courseId}`),
          token
            ? fetch("/api/v1/users/me/progress", { headers })
            : Promise.resolve(null),
        ]);

        const courseJson = await courseRes.json();
        if (!courseJson.data?.lessons) return;

        const course = courseJson.data;
        setCourseMeta({
          title: course.title,
          description: course.description,
          level: course.level,
          estimated_minutes: course.estimated_minutes,
          lesson_count: course.lessons.length,
        });

        const completedIds = new Set<number>();
        if (progressRes) {
          const progressJson = await progressRes.json();
          for (const cp of progressJson.data?.course_progress || []) {
            for (const l of cp.lessons || []) {
              if (l.status === "completed") completedIds.add(l.lesson_id);
            }
          }
        }

        const rawLessons: Lesson[] = course.lessons.map((l: any) => ({
          ...l,
          is_completed: completedIds.has(l.id),
        }));

        const firstIncomplete = rawLessons.find((l) => !l.is_completed);
        const firstIncompleteIndex = firstIncomplete
          ? rawLessons.indexOf(firstIncomplete)
          : -1;

        setLessons(
          rawLessons.map((l, i) => ({
            ...l,
            _isLocked: i > 0 && !rawLessons[i - 1].is_completed,
            _isCurrent: i === firstIncompleteIndex,
          }))
        );
      } catch (err) {
        console.error("Failed to fetch lessons:", err);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, [courseId, token]);

  const completedCount = lessons.filter((l) => l.is_completed).length;
  const totalLessons = lessons.length || 0;
  const progressPercent = totalLessons > 0 ? Math.round((completedCount / totalLessons) * 100) : 0;
  const estimatedHours = courseMeta ? Math.round(courseMeta.estimated_minutes / 60) : 0;

  return (
    <div className="mx-auto max-w-5xl p-4 pb-12">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8 rounded-2xl border border-border bg-card p-6 md:p-8"
      >
        <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
          <div>
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <BookOpen className="h-4 w-4" />
              <span>学习路线</span>
              <span className="text-border">|</span>
              <DifficultyBadge difficulty={courseMeta?.level || "beginner"} />
            </div>
            <h1 className="mt-2 text-2xl font-bold md:text-3xl">
              {courseMeta?.title || "加载中..."}
            </h1>
            <p className="mt-2 max-w-xl text-muted-foreground">
              {courseMeta?.description || ""}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-primary/10">
              <Trophy className="h-7 w-7 text-primary" />
            </div>
            <div>
              <p className="text-2xl font-bold">{progressPercent}%</p>
              <p className="text-xs text-muted-foreground">总进度</p>
            </div>
          </div>
        </div>

        <div className="mt-6">
          <div className="flex items-center justify-between text-sm mb-2">
            <span className="text-muted-foreground">
              已完成 {completedCount} / {totalLessons} 节课
            </span>
            <span className="text-muted-foreground">预计总时长 {estimatedHours} 小时</span>
          </div>
          <div className="h-3 w-full overflow-hidden rounded-full bg-muted">
            <motion.div
              className="h-full rounded-full bg-primary"
              initial={{ width: 0 }}
              animate={{ width: `${progressPercent}%` }}
              transition={{ duration: 0.8 }}
            />
          </div>
        </div>

        <div className="mt-6 grid grid-cols-3 gap-4 border-t border-border pt-6">
          <div className="text-center">
            <p className="text-xl font-bold">{totalLessons}</p>
            <p className="text-xs text-muted-foreground">课时</p>
          </div>
          <div className="text-center">
            <p className="text-xl font-bold">{totalLessons * 5}</p>
            <p className="text-xs text-muted-foreground">练习题</p>
          </div>
          <div className="text-center">
            <p className="text-xl font-bold">{courseId === 2 ? 5 : 3}</p>
            <p className="text-xs text-muted-foreground">实战项目</p>
          </div>
        </div>
      </motion.div>

      {loading ? (
        <p className="text-muted-foreground">加载中...</p>
      ) : (
        <div className="relative">
          <div className="absolute left-6 top-0 bottom-0 w-px bg-border md:left-7" />
          <div className="space-y-4">
            {lessons.map((lesson, index) => (
              <motion.div
                key={lesson.id}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.05 }}
              >
                <LessonCard
                  lesson={lesson}
                  isLocked={(lesson as any)._isLocked}
                  isCurrent={(lesson as any)._isCurrent}
                />
              </motion.div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
