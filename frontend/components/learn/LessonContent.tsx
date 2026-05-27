"use client";

import Link from "next/link";
import { ArrowLeft, ArrowRight, BookOpen, Lightbulb, AlertTriangle, Play } from "lucide-react";
import type { Lesson } from "@/types";
import { cn } from "@/lib/utils";

interface LessonContentProps {
  lesson: Lesson;
  firstExerciseId?: number | null;
}

function MarkdownContent({ content }: { content: string }) {
  // Simple markdown renderer for MVP
  const lines = content.split("\n");
  const elements: React.ReactNode[] = [];
  let inCode = false;
  let codeContent = "";
  let codeLang = "";

  lines.forEach((line, i) => {
    if (line.startsWith("```")) {
      if (inCode) {
        elements.push(
          <pre key={`code-${i}`} className="code-block my-4">
            <code>{codeContent.trim()}</code>
          </pre>
        );
        codeContent = "";
        inCode = false;
      } else {
        inCode = true;
        codeLang = line.replace("```", "").trim();
      }
      return;
    }

    if (inCode) {
      codeContent += line + "\n";
      return;
    }

    if (line.startsWith("## ")) {
      elements.push(
        <h2 key={i} className="mt-8 mb-4 text-xl font-bold">
          {line.replace("## ", "")}
        </h2>
      );
    } else if (line.startsWith("### ")) {
      elements.push(
        <h3 key={i} className="mt-6 mb-3 text-lg font-semibold">
          {line.replace("### ", "")}
        </h3>
      );
    } else if (line.startsWith("1. ") || line.startsWith("2. ") || line.startsWith("3. ")) {
      elements.push(
        <li key={i} className="ml-5 list-decimal text-muted-foreground">
          {line.replace(/^\d+\. /, "")}
        </li>
      );
    } else if (line.trim() === "") {
      elements.push(<div key={i} className="h-2" />);
    } else {
      // Inline code
      const parts = line.split(/(`[^`]+`)/g);
      elements.push(
        <p key={i} className="leading-relaxed text-foreground/90">
          {parts.map((part, j) =>
            part.startsWith("`") && part.endsWith("`") ? (
              <code key={j} className="rounded bg-muted px-1 py-0.5 text-sm font-mono text-primary">
                {part.slice(1, -1)}
              </code>
            ) : (
              part
            )
          )}
        </p>
      );
    }
  });

  return <>{elements}</>;
}

export function LessonContent({ lesson, firstExerciseId }: LessonContentProps) {
  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="border-b border-border pb-6">
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <BookOpen className="h-4 w-4" />
          <span>第 {lesson.order_index} 课</span>
          <span className="text-border">|</span>
          <span>{lesson.estimated_minutes} 分钟</span>
        </div>
        <h1 className="mt-2 text-3xl font-bold">{lesson.title}</h1>
        {lesson.summary && (
          <p className="mt-2 text-muted-foreground">{lesson.summary}</p>
        )}
      </div>

      {/* Objectives */}
      {lesson.objectives && lesson.objectives.length > 0 && (
        <div className="rounded-xl bg-secondary/50 p-5">
          <h3 className="mb-3 font-semibold">学习目标</h3>
          <ul className="space-y-2">
            {lesson.objectives.map((obj, i) => (
              <li key={i} className="flex items-center gap-2 text-sm text-muted-foreground">
                <div className="h-1.5 w-1.5 rounded-full bg-primary" />
                {obj}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Main Content */}
      <div className="prose prose-invert max-w-none">
        <MarkdownContent content={lesson.content} />
      </div>

      {/* Analogy */}
      {lesson.analogy && (
        <div className="rounded-xl border border-yellow-500/20 bg-yellow-500/5 p-5">
          <div className="flex items-center gap-2 text-yellow-500">
            <Lightbulb className="h-5 w-5" />
            <span className="font-semibold">生活类比</span>
          </div>
          <p className="mt-2 text-muted-foreground">{lesson.analogy}</p>
        </div>
      )}

      {/* Code Example */}
      {lesson.example_code && (
        <div>
          <h3 className="mb-3 font-semibold">代码示例</h3>
          <div className="relative">
            <pre className="code-block">
              <code>{lesson.example_code}</code>
            </pre>
            <button className="absolute right-3 top-3 rounded bg-muted px-2 py-1 text-xs hover:bg-muted/80">
              运行示例
            </button>
          </div>
        </div>
      )}

      {/* Line by line explanation */}
      {lesson.line_by_line_explanation && lesson.line_by_line_explanation.length > 0 && (
        <div>
          <h3 className="mb-3 font-semibold">逐行解释</h3>
          <div className="overflow-hidden rounded-xl border border-border">
            <table className="w-full text-sm">
              <thead className="bg-muted/50">
                <tr>
                  <th className="px-4 py-2 text-left font-medium text-muted-foreground">行</th>
                  <th className="px-4 py-2 text-left font-medium text-muted-foreground">代码</th>
                  <th className="px-4 py-2 text-left font-medium text-muted-foreground">解释</th>
                </tr>
              </thead>
              <tbody>
                {lesson.line_by_line_explanation.map((item, i) => {
                  const codeLines = lesson.example_code?.split("\n") || [];
                  return (
                    <tr key={i} className="border-t border-border">
                      <td className="px-4 py-3 text-muted-foreground">{item.line}</td>
                      <td className="px-4 py-3 font-mono text-primary">
                        <code>{codeLines[item.line - 1]}</code>
                      </td>
                      <td className="px-4 py-3 text-muted-foreground">{item.explanation}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Common Errors */}
      {lesson.common_errors && lesson.common_errors.length > 0 && (
        <div className="rounded-xl border border-red-500/20 bg-red-500/5 p-5">
          <div className="flex items-center gap-2 text-red-400">
            <AlertTriangle className="h-5 w-5" />
            <span className="font-semibold">常见错误</span>
          </div>
          <div className="mt-3 space-y-3">
            {lesson.common_errors.map((err, i) => (
              <div key={i} className="rounded-lg bg-background/50 p-3">
                <code className="text-sm text-red-300">{err.error}</code>
                <p className="mt-1 text-sm text-muted-foreground">{err.explanation}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Navigation */}
      <div className="flex items-center justify-between border-t border-border pt-6">
        <Link
          href={lesson.order_index > 1 ? `/lesson/${lesson.order_index - 1}` : "#"}
          className={cn(
            "flex items-center gap-2 text-sm",
            lesson.order_index <= 1 ? "pointer-events-none opacity-50" : "text-muted-foreground hover:text-foreground"
          )}
        >
          <ArrowLeft className="h-4 w-4" />
          上一节
        </Link>

        <Link
          href={`/exercise/${firstExerciseId || lesson.id}`}
          className="flex items-center gap-2 rounded-lg bg-primary px-5 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
        >
          <Play className="h-4 w-4" />
          去做练习
        </Link>

        <Link
          href={lesson.next_lesson_id ? `/lesson/${lesson.next_lesson_id}` : "#"}
          className={cn(
            "flex items-center gap-2 text-sm",
            !lesson.next_lesson_id ? "pointer-events-none opacity-50" : "text-muted-foreground hover:text-foreground"
          )}
        >
          下一节
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  );
}
