"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { CheckCircle2, Circle, Lock } from "lucide-react";
import { cn } from "@/lib/utils";

interface SidebarLesson {
  id: number;
  title: string;
  is_completed: boolean;
}

interface SidebarProps {
  lessons: SidebarLesson[];
}

function computeLocked(lessons: SidebarLesson[]): Set<number> {
  const sorted = [...lessons].sort((a, b) => a.id - b.id);
  const locked = new Set<number>();
  for (let i = 1; i < sorted.length; i++) {
    if (!sorted[i - 1].is_completed) {
      locked.add(sorted[i].id);
    }
  }
  return locked;
}

export function Sidebar({ lessons }: SidebarProps) {
  const params = useParams();
  const currentLessonId = Number(params.id);
  const lockedIds = computeLocked(lessons);

  return (
    <aside className="hidden w-72 shrink-0 border-r border-border bg-card/50 lg:block">
      <div className="sticky top-16 h-[calc(100vh-4rem)] overflow-y-auto">
        <div className="border-b border-border p-4">
          <h2 className="text-sm font-semibold">Python 零基础入门</h2>
          <p className="mt-1 text-xs text-muted-foreground">{lessons.length} 节课</p>
        </div>

        <nav className="space-y-0.5 p-2">
          {lessons.map((lesson) => {
            const isActive = lesson.id === currentLessonId;
            const isLocked = lockedIds.has(lesson.id);

            return (
              <Link
                key={lesson.id}
                href={isLocked ? "#" : `/lesson/${lesson.id}`}
                className={cn(
                  "flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm transition-colors",
                  isActive
                    ? "bg-primary/10 text-primary font-medium"
                    : "text-muted-foreground hover:bg-muted hover:text-foreground",
                  isLocked && "opacity-50 cursor-not-allowed"
                )}
              >
                <div className="shrink-0">
                  {lesson.is_completed ? (
                    <CheckCircle2 className="h-4 w-4 text-primary" />
                  ) : isLocked ? (
                    <Lock className="h-4 w-4" />
                  ) : (
                    <Circle className="h-4 w-4" />
                  )}
                </div>
                <span className="truncate">
                  {lesson.id}. {lesson.title}
                </span>
              </Link>
            );
          })}
        </nav>
      </div>
    </aside>
  );
}
