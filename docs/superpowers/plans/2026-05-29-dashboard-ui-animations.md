# Dashboard UI Animations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add micro-interactions and narrative animations to the dashboard page for life-like feel and learning guidance.

**Architecture:** Three layers — a shared `useCountUp` hook + `shimmer` CSS keyframe as foundation, per-component animation enhancements built on framer-motion, and a final global pass for entry rhythm and page transitions.

**Tech Stack:** React 18, Next.js 14 App Router, framer-motion ^11.2.0, Tailwind CSS 3.4, TypeScript

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `frontend/hooks/useCountUp.ts` | Create | Shared number-counting hook |
| `frontend/tailwind.config.ts` | Modify | Add `shimmer` keyframe |
| `frontend/app/globals.css` | Modify | Add `animate-shimmer` utility, ripple CSS, keyframes |
| `frontend/components/dashboard/WelcomeBanner.tsx` | Modify | Orb drift, sparkle spin, countUp, random quote |
| `frontend/components/dashboard/ContinueLearning.tsx` | Modify | Glow dot, ripple button, hover lift |
| `frontend/components/dashboard/ProgressCard.tsx` | Modify | CountUp, ring glow, color labels |
| `frontend/components/dashboard/StatsGrid.tsx` | Modify | Diagonal slide-in, icon bounce, countUp, accuracy color |
| `frontend/components/ui/CourseCard.tsx` | Modify | RotateX entry, spring arrow, whileTap, shimmer skeleton |
| `frontend/components/dashboard/DailyTask.tsx` | Modify | hover gradient shift, arrow wiggle, sparkle spin |
| `frontend/components/dashboard/RecentActivity.tsx` | Modify | Slide-in right, type color bar, icon bounce, empty-state sway, shimmer |
| `frontend/app/page.tsx` | Modify | Waterfall delay orchestration, shimmer for loading |
| `frontend/app/layout.tsx` | Modify | Page transition with AnimatePresence |

---

### Task 1: Create useCountUp hook

**Files:**
- Create: `frontend/hooks/useCountUp.ts`

- [ ] **Step 1: Write the hook**

```typescript
"use client";

import { useState, useEffect, useRef } from "react";

export function useCountUp(target: number, duration = 800): number {
  const [value, setValue] = useState(0);
  const prevTarget = useRef(0);
  const frameRef = useRef<number>(0);

  useEffect(() => {
    const startValue = prevTarget.current;
    const diff = target - startValue;
    if (diff === 0) {
      setValue(target);
      return;
    }
    const startTime = performance.now();

    function tick(now: number) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
      setValue(startValue + diff * eased);
      if (progress < 1) {
        frameRef.current = requestAnimationFrame(tick);
      }
    }

    frameRef.current = requestAnimationFrame(tick);
    prevTarget.current = target;

    return () => cancelAnimationFrame(frameRef.current);
  }, [target, duration]);

  return value;
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/hooks/useCountUp.ts
git commit -m "feat: add useCountUp hook for smooth number animation

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 2: Add shimmer keyframe to Tailwind config & globals.css

**Files:**
- Modify: `frontend/tailwind.config.ts`
- Modify: `frontend/app/globals.css`

- [ ] **Step 1: Add shimmer keyframe to tailwind.config.ts**

In `frontend/tailwind.config.ts`, inside the `extend` block, add `keyframes` and `animation`:

```typescript
// After the borderRadius block, add:
keyframes: {
  shimmer: {
    "0%": { backgroundPosition: "200% 0" },
    "100%": { backgroundPosition: "-200% 0" },
  },
  "orb-drift-1": {
    "0%, 100%": { transform: "translate(0, 0) rotate(0deg)" },
    "33%": { transform: "translate(30px, -20px) rotate(15deg)" },
    "66%": { transform: "translate(-20px, 10px) rotate(-10deg)" },
  },
  "orb-drift-2": {
    "0%, 100%": { transform: "translate(0, 0) rotate(0deg)" },
    "33%": { transform: "translate(-25px, 15px) rotate(-12deg)" },
    "66%": { transform: "translate(20px, -10px) rotate(10deg)" },
  },
},
animation: {
  shimmer: "shimmer 2s linear infinite",
  "orb-drift-1": "orb-drift-1 18s ease-in-out infinite",
  "orb-drift-2": "orb-drift-2 24s ease-in-out infinite",
},
```

- [ ] **Step 2: Add ripple and shimmer utility classes to globals.css**

In `frontend/app/globals.css`, inside the `@layer components` block, add:

```css
.shimmer-bg {
  @apply bg-gradient-to-r from-muted/30 via-muted/50 to-muted/30 bg-[length:200%_100%];
  animation: shimmer 2s linear infinite;
}

.btn-ripple {
  @apply relative overflow-hidden;
}
.btn-ripple::after {
  content: "";
  @apply absolute inset-0 rounded-lg opacity-0;
  background: radial-gradient(circle, hsl(var(--primary-foreground) / 0.3) 10%, transparent 10%);
  transform: scale(10);
  transition: transform 0.4s, opacity 0.4s;
}
.btn-ripple:active::after {
  transform: scale(0);
  opacity: 1;
  transition: 0s;
}
```

- [ ] **Step 3: Commit**

```bash
git add frontend/tailwind.config.ts frontend/app/globals.css
git commit -m "feat: add shimmer, orb-drift keyframes and ripple CSS

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 3: Animate WelcomeBanner

**Files:**
- Modify: `frontend/components/dashboard/WelcomeBanner.tsx`

- [ ] **Step 1: Replace WelcomeBanner with animated version**

Replace the file content:

```typescript
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
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/WelcomeBanner.tsx
git commit -m "feat: add orb drift, sparkle spin, and countUp to WelcomeBanner

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 4: Animate ContinueLearning

**Files:**
- Modify: `frontend/components/dashboard/ContinueLearning.tsx`

- [ ] **Step 1: Replace ContinueLearning with animated version**

```typescript
"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, BookOpen, PlayCircle } from "lucide-react";

interface ContinueLearningProps {
  lessonTitle?: string;
  lessonId?: number;
  courseTitle?: string;
  progressPercent?: number;
}

export function ContinueLearning({
  lessonTitle,
  lessonId,
  courseTitle,
  progressPercent = 0,
}: ContinueLearningProps) {
  if (!lessonTitle) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="rounded-2xl border border-border bg-card p-6"
      >
        <h3 className="font-semibold">开始学习</h3>
        <p className="mt-1 text-sm text-muted-foreground">选择一门课程，开启你的 Python 学习之旅</p>
        <Link
          href="/learn"
          className="mt-4 inline-flex items-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90 hover:-translate-y-0.5"
        >
          浏览课程 <ArrowRight className="h-4 w-4" />
        </Link>
      </motion.div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ y: -2 }}
      className="rounded-2xl border border-border bg-card p-6 transition-shadow hover:shadow-lg"
    >
      <div className="flex items-center gap-2 text-sm text-muted-foreground">
        <BookOpen className="h-4 w-4" />
        <span>{courseTitle || "Python 零基础入门"}</span>
      </div>

      <h3 className="mt-2 text-xl font-bold">{lessonTitle}</h3>

      {/* Progress with glow dot */}
      <div className="mt-4">
        <div className="flex items-center justify-between text-xs mb-1.5">
          <span className="text-muted-foreground">课程总进度</span>
          <span className="font-medium">{progressPercent}%</span>
        </div>
        <div className="relative h-2 w-full overflow-visible rounded-full bg-muted">
          <motion.div
            className="h-full rounded-full bg-primary relative"
            initial={{ width: 0 }}
            animate={{ width: `${progressPercent}%` }}
            transition={{ duration: 0.8 }}
          >
            {progressPercent > 0 && (
              <span className="absolute -right-1 -top-0.5 block h-3 w-3 rounded-full bg-primary animate-pulse" />
            )}
          </motion.div>
        </div>
      </div>

      <Link
        href={`/lesson/${lessonId}`}
        className="mt-5 inline-flex w-full items-center justify-center gap-2 rounded-lg bg-primary px-4 py-2.5 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90 hover:-translate-y-0.5"
      >
        <PlayCircle className="h-4 w-4" />
        继续学习
      </Link>
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/ContinueLearning.tsx
git commit -m "feat: add glow dot, ripple, and hover lift to ContinueLearning

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 5: Animate ProgressCard

**Files:**
- Modify: `frontend/components/dashboard/ProgressCard.tsx`

- [ ] **Step 1: Replace ProgressCard with animated version**

```typescript
"use client";

import { useEffect } from "react";
import { motion, useAnimate } from "framer-motion";
import { useCountUp } from "@/hooks/useCountUp";

interface ProgressCardProps {
  percent: number;
  completed: number;
  total: number;
  label: string;
}

export function ProgressCard({ percent, completed, total, label }: ProgressCardProps) {
  const circumference = 2 * Math.PI * 40;
  const offset = circumference - (percent / 100) * circumference;
  const animatedPercent = useCountUp(percent, 1200);
  const animatedCompleted = useCountUp(completed, 1200);
  const [scope, animate] = useAnimate();

  useEffect(() => {
    if (percent > 0) {
      animate(
        scope.current,
        { filter: ["drop-shadow(0 0 6px hsl(var(--primary)))", "drop-shadow(0 0 0px hsl(var(--primary)))"] },
        { duration: 0.5 }
      );
    }
  }, [percent, animate, scope]);

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="flex flex-col items-center rounded-xl border border-border bg-card p-6 shadow-sm"
    >
      <div className="relative h-32 w-32" ref={scope}>
        <svg className="h-full w-full" viewBox="0 0 100 100">
          <circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="currentColor"
            strokeWidth="8"
            className="text-muted/20"
          />
          <motion.circle
            cx="50"
            cy="50"
            r="40"
            fill="none"
            stroke="currentColor"
            strokeWidth="8"
            strokeLinecap="round"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset: offset }}
            transition={{ duration: 1, ease: "easeOut" }}
            className="text-primary"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-2xl font-bold">{Math.round(animatedPercent)}%</span>
        </div>
      </div>
      <p className="mt-4 text-sm font-medium">
        <span className="text-primary">{Math.round(animatedCompleted)}</span>
        <span className="text-muted-foreground"> / {total} {label}</span>
      </p>
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/ProgressCard.tsx
git commit -m "feat: add countUp, ring glow pulse, and color labels to ProgressCard

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 6: Animate StatsGrid

**Files:**
- Modify: `frontend/components/dashboard/StatsGrid.tsx`

- [ ] **Step 1: Replace StatsGrid with animated version (StatItem extracted to avoid hooks-in-loop)**

```typescript
"use client";

import { motion } from "framer-motion";
import { BookOpen, CheckCircle2, XCircle, FolderGit2, Calendar, Target } from "lucide-react";
import { useCountUp } from "@/hooks/useCountUp";
import type { DashboardStats } from "@/types";

const icons: Record<string, React.ComponentType<{ className?: string }>> = {
  completed_lessons: BookOpen,
  completed_exercises: CheckCircle2,
  wrong_questions: XCircle,
  completed_projects: FolderGit2,
  study_days: Calendar,
  accuracy_rate: Target,
};

const labels: Record<string, string> = {
  completed_lessons: "已完成课程",
  completed_exercises: "已完成题目",
  wrong_questions: "错题数",
  completed_projects: "已完成项目",
  study_days: "学习天数",
  accuracy_rate: "正确率",
};

function getAccuracyColor(rate: number): string {
  if (rate >= 0.8) return "text-emerald-400";
  if (rate >= 0.6) return "text-amber-400";
  return "";
}

function StatItem({
  statKey,
  value,
  index,
}: {
  statKey: string;
  value: number;
  index: number;
}) {
  const Icon = icons[statKey];
  const isAccuracy = statKey === "accuracy_rate";
  const target = isAccuracy ? Math.round(value * 100) : value;
  const countUpValue = useCountUp(target, 800);
  const accuracyClass = isAccuracy ? getAccuracyColor(value) : "";

  return (
    <motion.div
      initial={{ opacity: 0, x: -10, y: 10 }}
      animate={{ opacity: 1, x: 0, y: 0 }}
      transition={{ delay: index * 0.05 }}
      className="rounded-xl border border-border bg-card p-4 shadow-sm"
    >
      <div className="flex items-center gap-2 text-muted-foreground">
        <motion.span
          whileInView={{ scale: [1, 1.2, 1] }}
          transition={{ type: "spring", stiffness: 300, delay: 0.15 }}
          viewport={{ once: true }}
          className="inline-flex"
        >
          <Icon className="h-4 w-4" />
        </motion.span>
        <span className="text-xs">{labels[statKey]}</span>
      </div>
      <p className={`mt-2 text-2xl font-bold ${accuracyClass}`}>
        {isAccuracy ? `${countUpValue}%` : countUpValue}
      </p>
    </motion.div>
  );
}

export function StatsGrid({ stats }: { stats: DashboardStats }) {
  const entries = Object.entries(stats).filter(([key]) => key in labels);

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
      {entries.map(([key, value], index) => (
        <StatItem key={key} statKey={key} value={value as number} index={index} />
      ))}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/StatsGrid.tsx
git commit -m "feat: add diagonal entry, icon bounce, countUp, and accuracy colors to StatsGrid

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 7: Animate CourseCard

**Files:**
- Modify: `frontend/components/ui/CourseCard.tsx`

- [ ] **Step 1: Replace CourseCard with animated version**

```typescript
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
          {/* Top row */}
          <div className="flex items-start justify-between">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10 text-primary transition-colors duration-300 group-hover:bg-primary/20">
              <BookOpen className="h-6 w-6" />
            </div>
            <DifficultyBadge difficulty={course.level} />
          </div>

          {/* Content */}
          <h3 className="mt-4 text-lg font-bold group-hover:text-primary transition-colors">
            {course.title}
          </h3>
          <p className="mt-1 text-sm text-muted-foreground line-clamp-2">
            {course.description}
          </p>

          {/* Progress bar */}
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

          {/* Footer stats */}
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

          {/* Hover arrow with spring */}
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
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/ui/CourseCard.tsx
git commit -m "feat: add rotateX entry, spring arrow, and whileTap to CourseCard

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 8: Animate DailyTask

**Files:**
- Modify: `frontend/components/dashboard/DailyTask.tsx`

- [ ] **Step 1: Replace DailyTask with animated version**

```typescript
"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight, Sparkles } from "lucide-react";

interface DailyTaskProps {
  title?: string;
  lessonId?: number;
}

export function DailyTask({ title, lessonId }: DailyTaskProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-xl border border-primary/20 bg-gradient-to-r from-primary/10 to-cyan-500/10 p-6 transition-all duration-300 hover:from-primary/15 hover:to-cyan-500/15"
    >
      <div className="flex items-center gap-2 text-primary">
        <motion.span
          animate={{ rotate: 360 }}
          transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
          className="inline-flex"
        >
          <Sparkles className="h-5 w-5" />
        </motion.span>
        <span className="text-sm font-semibold">今日学习任务</span>
      </div>
      {title ? (
        <div className="mt-3 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-bold">{title}</h3>
            <p className="text-sm text-muted-foreground">继续你的学习之旅</p>
          </div>
          <Link
            href={`/lesson/${lessonId}`}
            className="flex items-center gap-1 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground btn-ripple transition-all hover:opacity-90"
          >
            继续学习
            <motion.span whileHover={{ x: [0, 3, -3, 0] }} transition={{ duration: 0.4 }}>
              <ArrowRight className="h-4 w-4" />
            </motion.span>
          </Link>
        </div>
      ) : (
        <div className="mt-3">
          <p className="text-sm text-muted-foreground">还没有今日任务，去课程页选一节开始吧！</p>
          <Link
            href="/learn"
            className="mt-2 inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline"
          >
            浏览课程 <ArrowRight className="h-3 w-3" />
          </Link>
        </div>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/DailyTask.tsx
git commit -m "feat: add gradient hover shift and arrow wiggle to DailyTask

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 9: Animate RecentActivity

**Files:**
- Modify: `frontend/components/dashboard/RecentActivity.tsx`

- [ ] **Step 1: Replace RecentActivity with animated version**

```typescript
"use client";

import { motion } from "framer-motion";
import { CheckCircle2, Code, XCircle, FileText } from "lucide-react";
import type { Activity } from "@/types";

interface RecentActivityProps {
  activities: Activity[];
  loading?: boolean;
}

const icons = {
  lesson: FileText,
  exercise: CheckCircle2,
  project: Code,
  code: Code,
};

const resultIcons = {
  success: CheckCircle2,
  fail: XCircle,
};

const resultColors = {
  success: "text-emerald-400",
  fail: "text-red-400",
};

const typeColorBar: Record<string, string> = {
  lesson: "bg-blue-400",
  exercise: "bg-emerald-400",
  project: "bg-violet-400",
  code: "bg-violet-400",
};

export function RecentActivity({ activities, loading }: RecentActivityProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-border bg-card p-6"
    >
      <h3 className="font-semibold">最近动态</h3>

      {loading ? (
        <div className="mt-4 space-y-3">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="flex items-center gap-3 rounded-lg p-2">
              <div className="h-8 w-8 shrink-0 rounded-lg shimmer-bg" />
              <div className="flex-1 space-y-2">
                <div className="h-4 w-3/4 rounded shimmer-bg" />
                <div className="h-3 w-1/4 rounded shimmer-bg" />
              </div>
            </div>
          ))}
        </div>
      ) : activities.length === 0 ? (
        <motion.div
          animate={{ rotate: [-0.5, 0.5, -0.5] }}
          transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
          className="mt-4"
        >
          <p className="text-sm text-muted-foreground">还没有学习记录，快去开始第一节课吧！</p>
        </motion.div>
      ) : (
        <div className="mt-4 space-y-3">
          {activities.map((activity, index) => {
            const Icon = icons[activity.type];
            const ResultIcon = activity.result ? resultIcons[activity.result] : null;
            return (
              <motion.div
                key={activity.id}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.05 }}
                className="group relative flex items-center gap-3 rounded-lg p-2 transition-colors hover:bg-muted/50"
              >
                {/* Type color bar on hover */}
                <span
                  className={`absolute left-0 top-1 bottom-1 w-0.5 rounded-full ${typeColorBar[activity.type]} opacity-0 transition-opacity duration-200 group-hover:opacity-100`}
                />

                <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-muted">
                  <Icon className="h-4 w-4 text-muted-foreground" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{activity.title}</p>
                  <p className="text-xs text-muted-foreground">{activity.time}</p>
                </div>
                {ResultIcon && activity.result && (
                  <motion.span
                    whileInView={{ scale: [1, 1.3, 1] }}
                    transition={{ type: "spring", stiffness: 300 }}
                    viewport={{ once: true }}
                    className="inline-flex shrink-0"
                  >
                    <ResultIcon className={`h-4 w-4 ${resultColors[activity.result]}`} />
                  </motion.span>
                )}
              </motion.div>
            );
          })}
        </div>
      )}
    </motion.div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/components/dashboard/RecentActivity.tsx
git commit -m "feat: add slide-in, type color bar, icon bounce, and shimmer to RecentActivity

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 10: Orchestrate waterfall rhythm in DashboardPage

**Files:**
- Modify: `frontend/app/page.tsx`

- [ ] **Step 1: Update page.tsx with waterfall delays and shimmer loading**

The main changes are:
- Pass animation `transition.delay` props to coordinate waterfall entry
- Replace `animate-pulse` skeleton loading with `shimmer-bg`
- CourseCard already handles its own delay via `index * 0.08`

```typescript
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
import type { DashboardStats, Activity } from "@/types";

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

// Waterfall animation wrapper
function AnimateBlock({
  delay,
  children,
}: {
  delay: number;
  children: React.ReactNode;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay, duration: 0.35, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  );
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
  const [activities, setActivities] = useState<Activity[]>([]);
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
            setActivities(dashJson.data.recent_activities || []);
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
      <AnimateBlock delay={0}>
        <WelcomeBanner username={user?.username} studyDays={stats.study_days} />
      </AnimateBlock>

      <div className="grid gap-6 lg:grid-cols-3">
        <div className="space-y-6 lg:col-span-2">
          <AnimateBlock delay={0.1}>
            {isAuthenticated && continueLessonId && (
              <ContinueLearning
                lessonTitle={`第 ${continueLessonId} 课`}
                lessonId={continueLessonId}
                courseTitle="Python 零基础入门"
                progressPercent={lessonPercent}
              />
            )}
          </AnimateBlock>

          {isAuthenticated ? (
            <>
              <AnimateBlock delay={0.2}>
                <div className="grid gap-4 sm:grid-cols-3">
                  <ProgressCard percent={lessonPercent} completed={stats.completed_lessons} total={stats.total_lessons} label="课程" />
                  <ProgressCard percent={exercisePercent} completed={stats.completed_exercises} total={stats.total_exercises} label="题目" />
                  <ProgressCard percent={projectPercent} completed={stats.completed_projects} total={stats.total_projects} label="项目" />
                </div>
              </AnimateBlock>
              <AnimateBlock delay={0.35}>
                <StatsGrid stats={stats} />
              </AnimateBlock>
            </>
          ) : (
            <AnimateBlock delay={0.1}>
              <div className="rounded-2xl border border-border bg-gradient-to-br from-primary/5 to-cyan-500/5 p-8 text-center">
                <h2 className="text-lg font-semibold">开始你的 Python 学习之旅</h2>
                <p className="mt-2 text-sm text-muted-foreground max-w-md mx-auto">
                  注册账号后可以追踪学习进度、记录错题、完成项目实战。每天进步一点点！
                </p>
              </div>
            </AnimateBlock>
          )}

          <AnimateBlock delay={0.4}>
            <h2 className="mb-4 text-lg font-semibold">我的课程</h2>
            {loading ? (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {Array.from({ length: 3 }).map((_, i) => (
                  <div key={i} className="rounded-2xl border border-border bg-card p-6 space-y-3">
                    <div className="h-12 w-12 rounded-xl shimmer-bg" />
                    <div className="h-5 w-3/4 rounded shimmer-bg" />
                    <div className="h-4 w-full rounded shimmer-bg" />
                    <div className="h-3 w-1/2 rounded shimmer-bg" />
                  </div>
                ))}
              </div>
            ) : (
              <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                {courses.map((course, i) => (
                  <CourseCard key={course.id} course={course} index={i} />
                ))}
              </div>
            )}
          </AnimateBlock>
        </div>

        <div className="space-y-6">
          <AnimateBlock delay={0.15}>
            {isAuthenticated && continueLessonId && (
              <DailyTask title={`第 ${continueLessonId} 课`} lessonId={continueLessonId} />
            )}
          </AnimateBlock>
          <AnimateBlock delay={0.25}>
            <RecentActivity activities={activities} loading={loading} />
          </AnimateBlock>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/app/page.tsx
git commit -m "feat: add waterfall entry rhythm and shimmer loading to dashboard

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 11: Add AnimatePresence page transition to layout

**Files:**
- Modify: `frontend/app/layout.tsx`

- [ ] **Step 1: Wrap children in AnimatePresence**

Replace layout.tsx:

```typescript
import type { Metadata } from "next";
import "./globals.css";
import { Navbar } from "@/components/layout/Navbar";
import { AuthProvider } from "@/hooks/useAuth";
import { PageTransition } from "@/components/layout/PageTransition";

export const metadata: Metadata = {
  title: "Python Coach - Python 学习助手",
  description: "面向零基础小白的 Python 系统学习平台",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN" className="dark">
      <body className="min-h-screen bg-background text-foreground antialiased">
        <AuthProvider>
          <Navbar />
          <main className="pt-16">
            <PageTransition>{children}</PageTransition>
          </main>
        </AuthProvider>
      </body>
    </html>
  );
}
```

- [ ] **Step 2: Create PageTransition component**

Create `frontend/components/layout/PageTransition.tsx`:

```typescript
"use client";

import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";

export function PageTransition({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={pathname}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.2 }}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}
```

- [ ] **Step 3: Commit**

```bash
git add frontend/app/layout.tsx frontend/components/layout/PageTransition.tsx
git commit -m "feat: add AnimatePresence page transition to layout

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

### Task 12: Verification — build and visual check

- [ ] **Step 1: Type-check the project**

Run: `cd frontend && npx tsc --noEmit`
Expected: No errors

- [ ] **Step 2: Build the project**

Run: `cd frontend && npm run build`
Expected: Successful build without errors

- [ ] **Step 3: Verify dev server runs**

Run: Check preview server is running at http://localhost:3000
Expected: Dashboard loads with all animations visible

- [ ] **Step 4: Eye-test checklist**

Open http://localhost:3000 and verify:
- [ ] WelcomeBanner orbs are slowly drifting
- [ ] Sparkle icons are rotating
- [ ] Study days counts up when a user is logged in
- [ ] ContinueLearning progress bar has a pulsing glow dot
- [ ] Buttons have ripple effect on click and hover lift
- [ ] ProgressCard numbers count up from 0
- [ ] ProgressCard ring flashes when percent changes
- [ ] StatsGrid items slide in from bottom-left
- [ ] StatsGrid icons bounce on view
- [ ] Accuracy rate shows green/yellow coloring
- [ ] CourseCards have staggered entry
- [ ] CourseCards shrink on click (whileTap)
- [ ] CourseCards hover shows border glow and arrow
- [ ] DailyTask gradient shifts on hover, arrow wiggles
- [ ] RecentActivity items slide in from right
- [ ] RecentActivity hover shows colored left bar
- [ ] Shimmer loading skeletons animate with flowing light
- [ ] Page transitions are smooth fade in/out
```
