"use client";

import { useEffect, useState, useCallback } from "react";
import { useParams, useRouter } from "next/navigation";
import { motion } from "framer-motion";
import {
  FolderGit2,
  Clock,
  CheckCircle2,
  Circle,
  Play,
  Lightbulb,
  ChevronRight,
  Star,
  ArrowLeft,
  Loader2,
  XCircle,
} from "lucide-react";
import { DifficultyBadge } from "@/components/ui/DifficultyBadge";
import { Tag } from "@/components/ui/Tag";
import { EmptyState } from "@/components/ui/EmptyState";
import { cn } from "@/lib/utils";
import { useAuth } from "@/hooks/useAuth";
import { CodeEditor } from "@/components/ui/CodeEditor";

interface TaskData {
  id: number;
  project_id: number;
  title: string;
  description: string;
  starter_code: string | null;
  hint: string | null;
  answer_code: string | null;
  order_index: number;
}

interface ProjectData {
  id: number;
  title: string;
  description: string;
  difficulty: string;
  estimated_minutes: number;
  knowledge_points: string[];
  tasks: TaskData[];
}

interface CodeRunResult {
  stdout: string;
  stderr: string;
  exit_code: number;
  execution_time_ms: number;
}

interface SubmitResult {
  is_correct: boolean;
  stdout: string;
  stderr: string;
  exit_code: number;
  execution_time_ms: number;
}

export default function ProjectDetailPage() {
  const params = useParams();
  const router = useRouter();
  const { token } = useAuth();
  const projectId = Number(params.id);

  const [project, setProject] = useState<ProjectData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [currentTask, setCurrentTask] = useState(0);
  const [code, setCode] = useState("");
  const [showHint, setShowHint] = useState(false);

  const [stdin, setStdin] = useState("");
  const [running, setRunning] = useState(false);
  const [runResult, setRunResult] = useState<CodeRunResult | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [submitResult, setSubmitResult] = useState<SubmitResult | null>(null);
  const [completedTasks, setCompletedTasks] = useState<Set<number>>(new Set());

  useEffect(() => {
    setLoading(true);
    setError("");
    fetch(`/api/v1/projects/${projectId}`)
      .then((r) => r.json())
      .then((json) => {
        if (!json.data) { setError("项目不存在"); return; }
        const d = json.data;
        setProject({
          ...d,
          knowledge_points: d.knowledge_points
            ? typeof d.knowledge_points === "string"
              ? JSON.parse(d.knowledge_points)
              : d.knowledge_points
            : [],
        });
        if (d.tasks?.length > 0) {
          setCode(d.tasks[0].starter_code || "");
        }
      })
      .catch(() => setError("加载失败"))
      .finally(() => setLoading(false));
  }, [projectId]);

  const switchTask = useCallback(
    (index: number) => {
      setCurrentTask(index);
      setCode(project?.tasks[index]?.starter_code || "");
      setStdin("");
      setRunResult(null);
      setSubmitResult(null);
      setShowHint(false);
    },
    [project]
  );

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
    if (!token || !project) { router.push("/auth/login"); return; }
    const task = project.tasks[currentTask];
    if (!task) return;

    setSubmitting(true);
    setSubmitResult(null);
    try {
      const res = await fetch(`/api/v1/project-tasks/${task.id}/submit`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ code }),
      });
      const json = await res.json();
      const data = json.data || json;
      setSubmitResult(data);
      if (data.is_correct) {
        setCompletedTasks((prev) => new Set(prev).add(currentTask));
      }
    } catch {
      setSubmitResult({ is_correct: false, stdout: "", stderr: "提交失败", exit_code: -1, execution_time_ms: 0 });
    } finally {
      setSubmitting(false);
    }
  }, [token, project, currentTask, code, router]);

  // --- Render ---

  if (loading) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <Loader2 className="h-8 w-8 animate-spin text-muted-foreground" />
      </div>
    );
  }

  if (error || !project) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center">
        <p className="text-muted-foreground">{error || "项目不存在"}</p>
      </div>
    );
  }

  if (project.tasks.length === 0) {
    return (
      <div className="mx-auto max-w-5xl p-4">
        <a href="/project" className="mb-4 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground">
          <ArrowLeft className="h-3.5 w-3.5" />
          返回项目列表
        </a>
        <EmptyState
          icon={<FolderGit2 className="h-12 w-12" />}
          title="暂无任务"
          description="该项目还没有添加任务，请稍后再来。"
        />
      </div>
    );
  }

  const task = project.tasks[currentTask];
  const isLastTask = currentTask >= project.tasks.length - 1;

  return (
    <div className="mx-auto max-w-5xl p-4 pb-12">
      {/* Back link */}
      <a href="/project" className="mb-4 inline-flex items-center gap-1 text-sm text-muted-foreground hover:text-foreground transition-colors">
        <ArrowLeft className="h-3.5 w-3.5" />
        返回项目列表
      </a>

      {/* Project Header */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8 rounded-2xl border border-border bg-card p-6"
      >
        <div className="flex flex-wrap items-center gap-2">
          <FolderGit2 className="h-6 w-6 text-primary" />
          <h1 className="text-2xl font-bold">{project.title}</h1>
          <DifficultyBadge difficulty={project.difficulty} />
        </div>
        <p className="mt-3 text-muted-foreground">{project.description}</p>
        <div className="mt-4 flex flex-wrap items-center gap-2">
          {project.knowledge_points.map((kp) => (
            <Tag key={kp} variant="secondary">{kp}</Tag>
          ))}
        </div>
        <div className="mt-4 flex items-center gap-4 text-xs text-muted-foreground">
          <span className="flex items-center gap-1">
            <Clock className="h-3.5 w-3.5" />预计 {project.estimated_minutes} 分钟
          </span>
          <span className="flex items-center gap-1">
            <Star className="h-3.5 w-3.5" />{project.knowledge_points.length} 个知识点
          </span>
        </div>
      </motion.div>

      {/* Task Stepper */}
      <div className="mb-8">
        <div className="flex items-center gap-2 overflow-x-auto pb-2">
          {project.tasks.map((t, i) => (
            <div key={t.id} className="flex items-center shrink-0">
              <button
                onClick={() => switchTask(i)}
                className={cn(
                  "flex items-center gap-2 rounded-full px-3 py-1.5 text-xs font-medium transition-colors",
                  i === currentTask
                    ? "bg-primary text-primary-foreground"
                    : completedTasks.has(i)
                    ? "bg-emerald-500/10 text-emerald-400"
                    : "bg-muted text-muted-foreground"
                )}
              >
                {completedTasks.has(i) ? (
                  <CheckCircle2 className="h-3.5 w-3.5" />
                ) : (
                  <Circle className="h-3.5 w-3.5" />
                )}
                {t.order_index}
              </button>
              {i < project.tasks.length - 1 && (
                <div className="mx-1 h-px w-6 bg-border" />
              )}
            </div>
          ))}
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-5">
        {/* Task description */}
        <div className="lg:col-span-2">
          <motion.div
            key={`desc-${currentTask}`}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            className="rounded-xl border border-border bg-card p-5"
          >
            <h3 className="font-bold text-lg">{task.title}</h3>
            <p className="mt-3 text-sm text-muted-foreground leading-relaxed">
              {task.description}
            </p>

            {task.hint && (
              <div className="mt-4">
                <button
                  onClick={() => setShowHint(!showHint)}
                  className="flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Lightbulb className="h-3.5 w-3.5" />
                  {showHint ? "隐藏提示" : "我需要提示"}
                </button>
                {showHint && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    className="mt-2 rounded-lg border border-yellow-500/20 bg-yellow-500/5 p-3 text-sm text-muted-foreground"
                  >
                    {task.hint}
                  </motion.div>
                )}
              </div>
            )}
          </motion.div>
        </div>

        {/* Code editor */}
        <div className="lg:col-span-3 space-y-4">
          <motion.div
            key={`editor-${currentTask}`}
            initial={{ opacity: 0, x: 10 }}
            animate={{ opacity: 1, x: 0 }}
          >
            <div className="overflow-hidden rounded-xl border border-zinc-800 bg-zinc-950">
              <CodeEditor
                value={code}
                onChange={setCode}
                readOnly={!!submitResult?.is_correct}
                height="300px"
                showBorder={false}
              />
              <div className="flex items-center justify-between border-t border-zinc-800 px-4 py-2">
                <div className="flex-1 flex items-center gap-2">
                  <input
                    type="text"
                    value={stdin}
                    onChange={(e) => setStdin(e.target.value)}
                    placeholder="标准输入 (每行一个 input)"
                    className="flex-1 bg-zinc-800 text-xs text-zinc-300 px-2 py-1 rounded border border-zinc-700 focus:border-zinc-500 focus:outline-none font-mono"
                  />
                </div>
                <div className="flex items-center gap-2">
                  <button
                    onClick={handleRun}
                    disabled={running || !code.trim()}
                    className="inline-flex items-center gap-1.5 rounded-lg bg-emerald-600 px-3 py-1.5 text-xs font-medium text-white hover:bg-emerald-500 transition-colors disabled:opacity-50"
                  >
                    {running ? <Loader2 className="h-3 w-3 animate-spin" /> : <Play className="h-3 w-3" />}
                    运行
                  </button>
                  {!submitResult?.is_correct && (
                    <button
                      onClick={handleSubmit}
                      disabled={submitting || !code.trim()}
                      className="inline-flex items-center gap-1.5 rounded-lg bg-primary px-3 py-1.5 text-xs font-medium text-primary-foreground hover:opacity-90 transition-opacity disabled:opacity-50"
                    >
                      {submitting ? <Loader2 className="h-3 w-3 animate-spin" /> : null}
                      提交
                    </button>
                  )}
                </div>
              </div>
            </div>
          </motion.div>

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

          {/* Submit result */}
          {submitResult && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className={cn(
                "rounded-xl border p-4",
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
                <div className="flex-1 min-w-0">
                  <h3 className="font-semibold">
                    {submitResult.is_correct ? "任务完成！" : "尚未通过"}
                  </h3>
                  {submitResult.stdout && (
                    <pre className="mt-1 font-mono text-xs text-emerald-400 overflow-x-auto whitespace-pre-wrap">{submitResult.stdout}</pre>
                  )}
                  {submitResult.stderr && (
                    <pre className="mt-1 font-mono text-xs text-red-400 overflow-x-auto whitespace-pre-wrap">{submitResult.stderr}</pre>
                  )}
                </div>
              </div>
            </motion.div>
          )}

          {/* Next task button */}
          {submitResult?.is_correct && !isLastTask && (
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex justify-end">
              <button
                onClick={() => switchTask(currentTask + 1)}
                className="flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2.5 text-sm font-medium text-primary-foreground transition-opacity hover:opacity-90"
              >
                下一任务
                <ChevronRight className="h-4 w-4" />
              </button>
            </motion.div>
          )}
        </div>
      </div>
    </div>
  );
}
