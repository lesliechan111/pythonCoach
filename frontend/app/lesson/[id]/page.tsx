"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { motion } from "framer-motion";
import { LessonContent } from "@/components/learn/LessonContent";
import { Sidebar } from "@/components/layout/Sidebar";
import { useAuth } from "@/hooks/useAuth";
import type { Lesson } from "@/types";

export default function LessonPage() {
  const params = useParams();
  const id = Number(params.id);
  const { token } = useAuth();
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [allLessons, setAllLessons] = useState<Array<{ id: number; title: string; is_completed: boolean }>>([]);
  const [firstExerciseId, setFirstExerciseId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadLesson() {
      try {
        const headers: Record<string, string> = token
          ? { Authorization: `Bearer ${token}` }
          : {};

        const [lessonRes, courseRes, exercisesRes, progressRes] = await Promise.all([
          fetch(`/api/v1/lessons/${id}`),
          fetch(`/api/v1/courses/1`),
          fetch(`/api/v1/lessons/${id}/exercises`),
          token
            ? fetch("/api/v1/users/me/progress", { headers })
            : Promise.resolve(null),
        ]);

        const lessonJson = await lessonRes.json();
        if (lessonJson.data) {
          const d = lessonJson.data;
          setLesson({
            ...d,
            objectives: d.objectives ? JSON.parse(d.objectives) : [],
            line_by_line_explanation: d.line_by_line_explanation ? JSON.parse(d.line_by_line_explanation) : [],
            common_errors: d.common_errors ? JSON.parse(d.common_errors) : [],
            is_completed: false,
            next_lesson_id: id < 20 ? id + 1 : undefined,
          });
        }

        const exercisesJson = await exercisesRes.json();
        if (exercisesJson.data?.length > 0) {
          setFirstExerciseId(exercisesJson.data[0].id);
        }

        const courseJson = await courseRes.json();
        if (courseJson.data?.lessons) {
          const completedIds = new Set<number>();
          if (progressRes) {
            const progressJson = await progressRes.json();
            for (const cp of progressJson.data?.course_progress || []) {
              for (const l of cp.lessons || []) {
                if (l.status === "completed") completedIds.add(l.lesson_id);
              }
            }
          }
          setAllLessons(
            courseJson.data.lessons.map((l: any) => ({
              id: l.id,
              title: l.title,
              is_completed: completedIds.has(l.id),
            }))
          );
        }

        // Record lesson progress
        if (token) {
          fetch(`/api/v1/lessons/${id}/complete`, {
            method: "POST",
            headers: { Authorization: `Bearer ${token}` },
          }).catch(() => {});
        }
      } catch (err) {
        console.error("Failed to fetch lesson:", err);
      } finally {
        setLoading(false);
      }
    }
    loadLesson();
  }, [id, token]);

  if (loading) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-2 border-primary border-t-transparent" />
      </div>
    );
  }

  if (!lesson) return <div className="p-8">课程不存在</div>;

  return (
    <div className="flex">
      <Sidebar lessons={allLessons} />
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex-1 p-4 pb-12 md:p-8"
      >
        <div className="mx-auto max-w-3xl">
          <LessonContent lesson={lesson} firstExerciseId={firstExerciseId} />
        </div>
      </motion.div>
    </div>
  );
}
