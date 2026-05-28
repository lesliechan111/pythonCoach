"use client";

import { useEffect, useState, useCallback } from "react";
import { useParams, useRouter } from "next/navigation";
import { motion } from "framer-motion";
import {
  Play,
  Lightbulb,
  CheckCircle2,
  XCircle,
  ChevronRight,
  HelpCircle,
  Loader2,
  ArrowLeft,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { useAuth } from "@/hooks/useAuth";
import { CodeEditor } from "@/components/ui/CodeEditor";
import { Toast } from "@/components/ui/Toast";

interface ExerciseData {
  id: number;
  lesson_id: number;
  type: string;
  title: string;
  description: string;
  options: { label: string; text: string }[] | null;
  difficulty: string;
  tags: string[];
  starter_code: string | null;
}

interface SubmitResult {
  is_correct: boolean;
  score: number;
  run_output: string | null;
  run_error: string | null;
  explanation: string | null;
}

interface CodeRunResult {
  stdout: string;
  stderr: string;
  exit_code: number;
  execution_time_ms: number;
}

const ANSWER_TYPES = ["choice", "judge", "fill_blank"];
const CODE_TYPES = ["code_fix", "code_completion", "programming"];

export default function ExercisePage() {
  const params = useParams();
  const router = useRouter();
  const { token } = useAuth();
  const id = Number(params.id);

  const [exercise, setExercise] = useState<ExerciseData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Answer state
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [code, setCode] = useState("");
  const [judgeAnswer, setJudgeAnswer] = useState<boolean | null>(null);
  const [fillAnswer, setFillAnswer] = useState("");

  // UI state
  const [stdin, setStdin] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [running, setRunning] = useState(false);
  const [runResult, setRunResult] = useState<CodeRunResult | null>(null);
  const [submitResult, setSubmitResult] = useState<SubmitResult | null>(null);
  const [showHint, setShowHint] = useState(false);
  const [exerciseIds, setExerciseIds] = useState<number[]>([]);
  const [currentIndex, setCurrentIndex] = useState(-1);
  const [toast, setToast] = useState<{ show: boolean; isCorrect: boolean; message: string }>({ show: false, isCorrect: false, message: "" });
  const [completedIds, setCompletedIds] = useState<Set<number>>(() => {
    if (typeof window === "undefined") return new Set<number>();
    try {
      const stored = sessionStorage.getItem("completedExerciseIds");
      return stored ? new Set(JSON.parse(stored)) : new Set<number>();
    } catch { return new Set<number>(); }
  });
  const isCompleted = completedIds.has(id) || submitResult?.is_correct;

  useEffect(() => {
    setLoading(true);
    setError("");
    setSubmitResult(null);
    setRunResult(null);
    setSelectedAnswer("");
    setStdin("");
    setCode("");
    setJudgeAnswer(null);
    setFillAnswer("");
    setShowHint(false);

    fetch(`/api/v1/exercises/${id}`)
      .then((r) => r.json())
      .then((json) => {
        if (!json.data) { setError("题目不存在"); return; }
        const d = json.data;
        setExercise({
          ...d,
          options: d.options ? (typeof d.options === "string" ? JSON.parse(d.options) : d.options) : null,
          tags: d.tags ? (typeof d.tags === "string" ? JSON.parse(d.tags) : d.tags) : [],
        });
        if (CODE_TYPES.includes(d.type)) {
          setCode(d.starter_code || "");
        }
        // If already completed in this session, show completed state
        let alreadyCompleted = false;
        try {
          const stored = sessionStorage.getItem("completedExerciseIds");
          if (stored) {
            const ids: number[] = JSON.parse(stored);
            alreadyCompleted = ids.includes(id);
          }
        } catch {}
        if (alreadyCompleted) {
          setSubmitResult({ is_correct: true, score: 100, run_output: null, run_error: null, explanation: null });
        }
        // Fetch all exercises for this lesson for navigation
        return fetch(`/api/v1/lessons/${d.lesson_id}/exercises`);
      })
      .then((res) => res?.json())
      .then((listJson) => {
        if (listJson?.data) {
          const ids: number[] = listJson.data.map((e: any) => e.id);
          setExerciseIds(ids);
          setCurrentIndex(ids.indexOf(id));
        }
      })
      .catch(() => setError("加载失败"))
      .finally(() => setLoading(false));
  }, [id]);

  const handleRun = useCallback(async () => {
    if (!code.trim()) return;
    setRunning(true);
    setRunResult(null);
    try {
      const res = await fetch("/api/v1/code/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ language: "python", code, stdin }),
      });
      const json = await res.json();
      setRunResult(json);
    } catch {
      setRunResult({ stdout: "", stderr: "运行失败", exit_code: -1, execution_time_ms: 0 });
    } finally {
      setRunning(false);
    }
  }, [code, stdin]);

  const handleSubmit = useCallback(async () => {
    if (!token) {
      router.push("/auth/login");
      return;
    }
    setSubmitting(true);
    setSubmitResult(null);

    let answer: string | undefined;
    let userCode: string | undefined;

    if (exercise?.type === "choice") answer = selectedAnswer;
    else if (exercise?.type === "judge") answer = judgeAnswer !== null ? (judgeAnswer ? "true" : "false") : undefined;
    else if (exercise?.type === "fill_blank") answer = fillAnswer;
    else if (CODE_TYPES.includes(exercise?.type || "")) userCode = code;

    try {
      const body: Record<string, string> = {};
      if (answer !== undefined) body.answer = answer;
      if (userCode !== undefined) body.code = userCode;

      const res = await fetch(`/api/v1/exercises/${id}/submit`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(body),
      });
      const json = await res.json();
      const data = json.data || json;
      setSubmitResult(data);
      setToast({ show: true, isCorrect: data.is_correct, message: data.explanation || "" });
      if (data.is_correct) {
        setCompletedIds((prev) => {
          const next = new Set(prev).add(id);
          sessionStorage.setItem("completedExerciseIds", JSON.stringify(Array.from(next)));
          return next;
        });
      }
    } catch {
      setSubmitResult({ is_correct: false, score: 0, run_output: null, run_error: "提交失败", explanation: null });
      setToast({ show: true, isCorrect: false, message: "提交失败，请检查网络后重试。" });
    } finally {
      setSubmitting(false);
    }
  }, [token, exercise, selectedAnswer, judgeAnswer, fillAnswer, code, id, router]);

  const handleRetry = useCallback(() => {
    setSubmitResult(null);
    setSelectedAnswer("");
    setJudgeAnswer(null);
    setFillAnswer("");
    setCode(exercise?.starter_code || "");
  }, [exercise]);

  // --- Render ---

  if (loading) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-muted-foreground" />
      </div>
    );
  }

  if (error || !exercise) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <p className="text-muted-foreground">{error || "题目不存在"}</p>
      </div>
    );
  }

  const canSubmit = ANSWER_TYPES.includes(exercise.type)
    ? (exercise.type === "choice" && selectedAnswer) ||
      (exercise.type === "judge" && judgeAnswer !== null) ||
      (exercise.type === "fill_blank" && fillAnswer.trim())
    : code.trim();

  return (
    <div className="mx-auto max-w-4xl p-4 pb-12">
      {/* Back link */}
      <a
        href={`/lesson/${exercise.lesson_id}`}
        className="mb-4 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground transition-colors"
      >
        <ArrowLeft className="h-3.5 w-3.5" />
        返回课程
      </a>

      {/* Header */}
      <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="mb-6">
        <div className="flex items-center gap-2 text-sm text-muted-foreground">
          <span>第 {exercise.lesson_id} 课</span>
          <span className="text-border">|</span>
          <span
            className={cn(
              "rounded-full px-2 py-0.5 text-xs font-medium",
              exercise.difficulty === "easy"
                ? "bg-emerald-500/10 text-emerald-400"
                : exercise.difficulty === "medium"
                ? "bg-yellow-500/10 text-yellow-400"
                : "bg-red-500/10 text-red-400"
            )}
          >
            {exercise.difficulty === "easy" ? "简单" : exercise.difficulty === "medium" ? "中等" : "困难"}
          </span>
          {exercise.tags.map((tag) => (
            <span key={tag} className="rounded-full bg-muted px-2 py-0.5 text-xs">{tag}</span>
          ))}
        </div>
        <h1 className="mt-2 text-xl font-bold">{exercise.title}</h1>
        <p className="mt-1 text-muted-foreground">{exercise.description}</p>
        {(completedIds.has(id) || submitResult?.is_correct) && (
          <div className="mt-3 inline-flex items-center gap-1.5 rounded-full bg-emerald-500/10 px-3 py-1 text-sm font-medium text-emerald-400">
            <CheckCircle2 className="h-4 w-4" />
            已完成
          </div>
        )}
      </motion.div>

      {/* Exercise Content */}
      {exercise.type === "choice" && exercise.options && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="space-y-3">
          {exercise.options.map((option) => {
            const isCorrectAnswer = submitResult?.is_correct && selectedAnswer === option.label;
            const isWrongAnswer = submitResult && !submitResult.is_correct && selectedAnswer === option.label;
            return (
              <button
                key={option.label}
                onClick={() => !submitResult && setSelectedAnswer(option.label)}
                className={cn(
                  "w-full rounded-xl border p-4 text-left transition-all",
                  !submitResult && selectedAnswer === option.label && "border-primary/50 bg-primary/5",
                  isCorrectAnswer && "border-emerald-500/50 bg-emerald-500/10",
                  isWrongAnswer && "border-red-500/50 bg-red-500/10",
                  !submitResult && selectedAnswer !== option.label && "border-border hover:border-primary/30",
                  submitResult && !isCorrectAnswer && !isWrongAnswer && "border-border opacity-60"
                )}
              >
                <span className="font-mono text-sm text-primary">{option.label}.</span>{" "}
                {option.text}
              </button>
            );
          })}
        </motion.div>
      )}

      {exercise.type === "judge" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex gap-4">
          {[true, false].map((val) => {
            const label = val ? "正确" : "错误";
            const isCorrectAnswer = submitResult?.is_correct && judgeAnswer === val;
            const isWrongAnswer = submitResult && !submitResult.is_correct && judgeAnswer === val;
            return (
              <button
                key={label}
                onClick={() => !submitResult && setJudgeAnswer(val)}
                className={cn(
                  "flex-1 rounded-xl border p-6 text-center text-lg font-medium transition-all",
                  !submitResult && judgeAnswer === val && "border-primary/50 bg-primary/5",
                  isCorrectAnswer && "border-emerald-500/50 bg-emerald-500/10 text-emerald-400",
                  isWrongAnswer && "border-red-500/50 bg-red-500/10 text-red-400",
                  !submitResult && judgeAnswer !== val && "border-border hover:border-primary/30",
                  submitResult && !isCorrectAnswer && !isWrongAnswer && "border-border opacity-60"
                )}
              >
                {label}
              </button>
            );
          })}
        </motion.div>
      )}

      {exercise.type === "fill_blank" && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
          <input
            type="text"
            value={fillAnswer}
            onChange={(e) => !submitResult && setFillAnswer(e.target.value)}
            placeholder="请输入你的答案..."
            className={cn(
              "w-full rounded-xl border bg-background px-4 py-3 text-sm outline-none transition-colors",
              submitResult
                ? submitResult.is_correct
                  ? "border-emerald-500/50"
                  : "border-red-500/50"
                : "border-border focus:border-primary"
            )}
            disabled={!!submitResult}
          />
        </motion.div>
      )}

      {CODE_TYPES.includes(exercise.type) && (
        <div className="space-y-4">
          <div className="overflow-hidden rounded-xl border border-zinc-800 bg-zinc-950">
            <CodeEditor
              value={code}
              onChange={setCode}
              readOnly={!!submitResult}
              height="300px"
              showBorder={false}
            />
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center sm:justify-between gap-2 border-t border-zinc-800 px-4 py-2">
              <div className="flex items-center gap-2">
                <input
                  type="text"
                  value={stdin}
                  onChange={(e) => setStdin(e.target.value)}
                  placeholder="标准输入 (每行一个 input)"
                  className="flex-1 sm:flex-none bg-zinc-800 text-xs text-zinc-300 px-2 py-1 rounded border border-zinc-700 focus:border-zinc-500 focus:outline-none font-mono"
                />
              </div>
              <button
                onClick={handleRun}
                disabled={running || !code.trim()}
                className="inline-flex items-center justify-center gap-1.5 rounded-lg bg-emerald-600 px-3 py-1.5 text-xs font-medium text-white hover:bg-emerald-500 transition-colors disabled:opacity-50"
              >
                {running ? <Loader2 className="h-3 w-3 animate-spin" /> : <Play className="h-3 w-3" />}
                运行
              </button>
            </div>
          </div>

          {/* Run output */}
          {runResult && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              className="rounded-xl border border-border bg-card p-4"
            >
              <div className="text-sm text-muted-foreground mb-2">运行结果</div>
              {runResult.stdout && (
                <pre className="font-mono text-sm text-emerald-400 overflow-x-auto whitespace-pre-wrap">{runResult.stdout}</pre>
              )}
              {runResult.stderr && (
                <pre className="font-mono text-sm text-red-400 overflow-x-auto whitespace-pre-wrap">{runResult.stderr}</pre>
              )}
              {!runResult.stdout && !runResult.stderr && (
                <p className="text-sm text-muted-foreground">无输出</p>
              )}
            </motion.div>
          )}
        </div>
      )}

      {/* Hint - only for seed data tasks that have hints. Exercise model doesn't have hint field, so only show generic hint */}
      {!submitResult && (
        <div className="mt-4">
          <button
            onClick={() => setShowHint(!showHint)}
            className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
          >
            <Lightbulb className="h-3.5 w-3.5" />
            {showHint ? "隐藏提示" : "给我一点提示"}
          </button>
          {showHint && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              className="mt-2 rounded-lg border border-yellow-500/20 bg-yellow-500/5 p-3 text-sm text-muted-foreground"
            >
              {exercise.type === "choice" && "仔细阅读每个选项，选择最符合题目描述的答案。"}
              {exercise.type === "judge" && "判断题只有正确和错误两个选项，仔细想想题目描述是否准确。"}
              {exercise.type === "fill_blank" && "注意空格和标点符号，答案需要和预期完全一致。"}
              {exercise.type === "code_fix" && "先运行代码看看报错信息，然后思考哪里写错了。"}
              {exercise.type === "code_completion" && "根据题目要求，在已有代码的基础上补充缺少的部分。"}
              {exercise.type === "programming" && "先理清思路，把大问题拆成小步骤，一步一步完成。"}
            </motion.div>
          )}
        </div>
      )}

      {/* Actions */}
      <div className="mt-6 flex items-center gap-3">
        {!submitResult && (
          <>
            <button
              onClick={handleSubmit}
              disabled={!canSubmit || submitting}
              className="rounded-lg bg-primary px-6 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90 disabled:opacity-50"
            >
              {submitting ? (
                <span className="flex items-center gap-2">
                  <Loader2 className="h-4 w-4 animate-spin" /> 提交中...
                </span>
              ) : (
                "提交答案"
              )}
            </button>
            <button className="flex items-center gap-1 rounded-lg border border-border px-4 py-2.5 text-sm text-muted-foreground hover:bg-muted transition-colors">
              <HelpCircle className="h-4 w-4" />
              AI 帮忙
            </button>
          </>
        )}

        {submitResult?.is_correct && (
          <>
            <button
              disabled
              className="flex items-center gap-2 rounded-lg bg-emerald-600 px-6 py-2.5 text-sm font-medium text-white"
            >
              <CheckCircle2 className="h-4 w-4" />
              已完成
            </button>
            <button
              onClick={() => router.push(`/lesson/${exercise.lesson_id}`)}
              className="flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
            >
              返回课程
              <ChevronRight className="h-4 w-4" />
            </button>
          </>
        )}

        {submitResult && !submitResult.is_correct && (
          <>
            <button
              onClick={handleSubmit}
              disabled={!canSubmit || submitting}
              className="rounded-lg bg-primary px-6 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90 disabled:opacity-50"
            >
              {submitting ? (
                <span className="flex items-center gap-2">
                  <Loader2 className="h-4 w-4 animate-spin" /> 提交中...
                </span>
              ) : (
                "重新提交"
              )}
            </button>
            <button
              onClick={handleRetry}
              className="rounded-lg border border-border px-4 py-2.5 text-sm text-muted-foreground hover:bg-muted transition-colors"
            >
              再试一次
            </button>
          </>
        )}
      </div>

      {/* Submit result */}
      {submitResult && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className={cn(
            "mt-6 rounded-xl border p-4",
            submitResult.is_correct
              ? "border-emerald-500/20 bg-emerald-500/5"
              : "border-red-500/20 bg-red-500/5"
          )}
        >
          <div className="flex items-start gap-3">
            {submitResult.is_correct ? (
              <CheckCircle2 className="h-5 w-5 text-emerald-400 shrink-0 mt-0.5" />
            ) : (
              <XCircle className="h-5 w-5 text-red-400 shrink-0 mt-0.5" />
            )}
            <div>
              <h3 className="font-semibold">
                {submitResult.is_correct ? "回答正确！" : "回答错误"}
              </h3>
              {submitResult.explanation && (
                <p className="mt-1 text-sm text-muted-foreground">{submitResult.explanation}</p>
              )}
              {submitResult.run_error && (
                <pre className="mt-2 font-mono text-xs text-red-400 overflow-x-auto whitespace-pre-wrap">
                  {submitResult.run_error}
                </pre>
              )}
              {submitResult.run_output && (
                <pre className="mt-2 font-mono text-xs text-muted-foreground overflow-x-auto whitespace-pre-wrap">
                  {submitResult.run_output}
                </pre>
              )}
            </div>
          </div>
        </motion.div>
      )}

      {/* Toast */}
      <Toast
        show={toast.show}
        isCorrect={toast.isCorrect}
        message={toast.message}
        onClose={() => setToast({ show: false, isCorrect: false, message: "" })}
      />

      {/* Exercise navigation */}
      {exerciseIds.length > 1 && (
        <div className="mt-8 flex items-center justify-between">
          <button
            onClick={() => currentIndex > 0 && router.push(`/exercise/${exerciseIds[currentIndex - 1]}`)}
            disabled={currentIndex <= 0}
            className="flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground transition-colors disabled:opacity-30 disabled:pointer-events-none"
          >
            <ArrowLeft className="h-4 w-4" />
            上一题
          </button>
          <div className="flex items-center gap-1.5">
            {exerciseIds.map((eid, i) => {
              const isCompleted = completedIds.has(eid) || (eid === id && submitResult?.is_correct);
              const isCurrent = eid === id;
              return (
                <button
                  key={eid}
                  onClick={() => router.push(`/exercise/${eid}`)}
                  className={cn(
                    "flex items-center justify-center rounded-full transition-all",
                    isCurrent ? "h-7 w-7 text-xs font-bold" : "h-5 w-5",
                    isCompleted
                      ? "bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30"
                      : isCurrent
                      ? "bg-primary text-primary-foreground"
                      : "bg-muted text-muted-foreground hover:bg-muted/70"
                  )}
                >
                  {isCompleted ? <CheckCircle2 className="h-3.5 w-3.5" /> : isCurrent ? i + 1 : ""}
                </button>
              );
            })}
          </div>
          <button
            onClick={() => currentIndex < exerciseIds.length - 1 && router.push(`/exercise/${exerciseIds[currentIndex + 1]}`)}
            disabled={currentIndex >= exerciseIds.length - 1}
            className="flex items-center gap-1.5 text-sm text-muted-foreground hover:text-foreground transition-colors disabled:opacity-30 disabled:pointer-events-none"
          >
            下一题
            <ChevronRight className="h-4 w-4" />
          </button>
        </div>
      )}
    </div>
  );
}
