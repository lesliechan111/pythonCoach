"use client";

import Link from "next/link";
import { CheckCircle2, Circle, Clock, Lock, PlayCircle } from "lucide-react";
import type { Lesson } from "@/types";
import { cn } from "@/lib/utils";

interface LessonCardProps {
  lesson: Lesson;
  isLocked?: boolean;
  isCurrent?: boolean;
}

export function LessonCard({ lesson, isLocked = false, isCurrent = false }: LessonCardProps) {

  let statusIcon;
  let statusClass;

  if (lesson.is_completed) {
    statusIcon = <CheckCircle2 className="h-5 w-5 text-primary" />;
    statusClass = "border-primary/30 bg-primary/5";
  } else if (isCurrent) {
    statusIcon = (
      <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground">
        <PlayCircle className="h-4 w-4" />
      </div>
    );
    statusClass = "border-primary/50 bg-primary/5 shadow-sm";
  } else if (isLocked) {
    statusIcon = <Lock className="h-5 w-5 text-muted-foreground/50" />;
    statusClass = "opacity-50";
  } else {
    statusIcon = <Circle className="h-5 w-5 text-muted-foreground/50" />;
    statusClass = "";
  }

  return (
    <Link href={isLocked ? "#" : `/lesson/${lesson.id}`}>
      <div
        className={cn(
          "group relative flex items-start gap-4 rounded-xl border border-border bg-card p-5 transition-all",
          !isLocked && "hover:border-primary/50 hover:shadow-md",
          statusClass
        )}
      >
        {/* Status indicator */}
        <div className="mt-0.5 shrink-0">{statusIcon}</div>

        <div className="min-w-0 flex-1">
          <div className="flex items-center justify-between gap-2">
            <h3
              className={cn(
                "font-semibold",
                lesson.is_completed && "text-muted-foreground line-through decoration-primary/50"
              )}
            >
              {lesson.order_index}. {lesson.title}
            </h3>
            {!isLocked && !lesson.is_completed && (
              <span className="shrink-0 rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">
                {isCurrent ? "继续" : "未开始"}
              </span>
            )}
          </div>
          {lesson.summary && (
            <p className="mt-1 text-sm text-muted-foreground">{lesson.summary}</p>
          )}
          <div className="mt-2 flex items-center gap-3 text-xs text-muted-foreground">
            <span className="flex items-center gap-1">
              <Clock className="h-3 w-3" />
              {lesson.estimated_minutes} 分钟
            </span>
            <span>5 道练习题</span>
          </div>
        </div>
      </div>
    </Link>
  );
}
