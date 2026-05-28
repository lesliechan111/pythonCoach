"use client";

import { useEffect, useState, useMemo } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { motion } from "framer-motion";
import { ChevronLeft, ChevronRight } from "lucide-react";
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

        // Fetch lesson and exercises first to determine course
        const [lessonRes, exercisesRes] = await Promise.all([
          fetch(`/api/v1/lessons/${id}`),
          fetch(`/api/v1/lessons/${id}/exercises`),
        ]);

        const lessonJson = await lessonRes.json();
        if (!lessonJson.data) { setLoading(false); return; }
        const d = lessonJson.data;
        setLesson({
          ...d,
          objectives: d.objectives ? JSON.parse(d.objectives) : [],
          line_by_line_explanation: d.line_by_line_explanation ? JSON.parse(d.line_by_line_explanation) : [],
          common_errors: d.common_errors ? JSON.parse(d.common_errors) : [],
          is_completed: false,
          next_lesson_id: null, // set below from course sidebar data
        });

        if (exercisesJson.data?.length > 0) {
          setFirstExerciseId(exercisesJson.data[0].id);
        }

        // Fetch the lesson's course for sidebar navigation
        const courseRes = await fetch(`/api/v1/courses/${d.course_id}`);
        const courseJson = await courseRes.json();

        const completedIds = new Set<number>();
        if (token) {
          const progressRes = await fetch("/api/v1/users/me/progress", { headers });
          const progressJson = await progressRes.json();
          for (const cp of progressJson.data?.course_progress || []) {
            for (const l of cp.lessons || []) {
              if (l.status === "completed") completedIds.add(l.lesson_id);
            }
          }
        }

        if (courseJson.data?.lessons) {
          const courseLessons = courseJson.data.lessons;
          const currentIndex = courseLessons.findIndex((l: any) => l.id === id);
          setAllLessons(
            courseLessons.map((l: any) => ({
              id: l.id,
              title: l.title,
              is_completed: completedIds.has(l.id),
            }))
          );
          // Set next lesson ID from course's lesson sequence
          setLesson((prev) => prev ? {
            ...prev,
            next_lesson_id: currentIndex < courseLessons.length - 1 ? courseLessons[currentIndex + 1].id : undefined,
          } : prev);
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

  const currentIndex = useMemo(() => allLessons.findIndex((l) => l.id === id), [allLessons, id]);
  const prevLessonId = currentIndex > 0 ? allLessons[currentIndex - 1].id : null;
  const nextLessonId = currentIndex < allLessons.length - 1 ? allLessons[currentIndex + 1].id : null;

  if (loading) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-2 border-primary border-t-transparent" />
      </div>
    );
  }

  if (!lesson) return <div className="p-8">课程不存在</div>;

  return (
    <div>
      {/* Mobile lesson navigation */}
      <div className="lg:hidden flex items-center justify-between border-b border-border bg-card/50 px-3 py-2">
        <Link
          href={prevLessonId ? `/lesson/${prevLessonId}` : "#"}
          className={`flex items-center gap-1 text-xs font-medium rounded-lg px-2 py-1.5 transition-colors ${
            prevLessonId
              ? "text-muted-foreground hover:text-foreground hover:bg-muted"
              : "text-muted-foreground/30 pointer-events-none"
          }`}
        >
          <ChevronLeft className="h-4 w-4" />
          上一课
        </Link>
        <span className="text-sm font-medium truncate px-2">
          {id}. {lesson.title}
        </span>
        <Link
          href={nextLessonId ? `/lesson/${nextLessonId}` : "#"}
          className={`flex items-center gap-1 text-xs font-medium rounded-lg px-2 py-1.5 transition-colors ${
            nextLessonId
              ? "text-muted-foreground hover:text-foreground hover:bg-muted"
              : "text-muted-foreground/30 pointer-events-none"
          }`}
        >
          下一课
          <ChevronRight className="h-4 w-4" />
        </Link>
      </div>

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
    </div>
  );
}
