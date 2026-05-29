"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Clock, BookOpen, ChevronRight } from "lucide-react";
import { DifficultyBadge } from "./DifficultyBadge";
import type { Course } from "@/types";

interface CourseCardProps {
  course: Course;
  index?: number;
}

export function CourseCard({ course, index = 0 }: CourseCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, rotateX: 3, y: 20 }}
      animate={{ opacity: 1, rotateX: 0, y: 0 }}
      transition={{ delay: index * 0.08, duration: 0.4 }}
      whileTap={{ scale: 0.97 }}
    >
      <Link href={`/learn/${course.id}`}>
        <div
          className="group relative overflow-hidden rounded-2xl border border-border bg-card p-6 transition-all duration-300 hover:border-primary/50 hover:shadow-lg hover:shadow-primary/5"
          style={{ willChange: "transform" }}
        >
          <div className="flex items-start justify-between">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors duration-300 group-hover:bg-primary/20">
              <BookOpen className="h-6 w-6" />
            </div>
            <DifficultyBadge difficulty={course.level} />
          </div>

          <h3 className="mt-4 text-lg font-bold group-hover:text-primary transition-colors">
            {course.title}
          </h3>
          <p className="mt-1 text-sm text-muted-foreground line-clamp-2">
            {course.description}
          </p>

          {course.progress_percent !== undefined && course.progress_percent > 0 && (
            <div className="mt-4">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="text-muted-foreground">学习进度</span>
                <span className="font-medium text-primary">{course.progress_percent}%</span>
              </div>
              <div className="h-2 w-full overflow-hidden rounded-full bg-muted">
                <motion.div
                  className="h-full rounded-full bg-primary"
                  initial={{ width: 0 }}
                  animate={{ width: `${course.progress_percent}%` }}
                  transition={{ duration: 0.8, delay: 0.2 }}
                />
              </div>
            </div>
          )}

          <div className="mt-4 flex items-center gap-4 text-xs text-muted-foreground">
            <span className="flex items-center gap-1">
              <BookOpen className="h-3.5 w-3.5" />
              {course.lesson_count} 节课
            </span>
            <span className="flex items-center gap-1">
              <Clock className="h-3.5 w-3.5" />
              {course.estimated_minutes} 分钟
            </span>
          </div>

          <motion.div
            className="absolute bottom-6 right-6"
            initial={{ opacity: 0, x: 10 }}
            whileHover={{ opacity: 1, x: 0 }}
          >
            <ChevronRight className="h-5 w-5 text-primary" />
          </motion.div>
        </div>
      </Link>
    </motion.div>
  );
}
