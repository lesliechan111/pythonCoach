"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { FolderGit2, Clock, Star, Loader2 } from "lucide-react";
import { DifficultyBadge } from "@/components/ui/DifficultyBadge";
import { Tag } from "@/components/ui/Tag";
import { EmptyState } from "@/components/ui/EmptyState";

interface ProjectData {
  id: number;
  title: string;
  description: string;
  difficulty: string;
  estimated_minutes: number;
  knowledge_points: string[];
  order_index: number;
}

export default function ProjectPage() {
  const [projects, setProjects] = useState<ProjectData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/v1/projects")
      .then((r) => r.json())
      .then((json) => {
        if (json.data) {
          setProjects(
            json.data.map((p: any) => ({
              ...p,
              knowledge_points: p.knowledge_points
                ? typeof p.knowledge_points === "string"
                  ? JSON.parse(p.knowledge_points)
                  : p.knowledge_points
                : [],
            }))
          );
        }
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="mx-auto max-w-5xl p-4 pb-12">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8"
      >
        <h1 className="text-2xl font-bold md:text-3xl">项目实战</h1>
        <p className="mt-2 text-muted-foreground">
          通过动手做小项目，把学到的知识真正用起来。
        </p>
      </motion.div>

      {loading ? (
        <div className="flex items-center justify-center py-20">
          <Loader2 className="h-8 w-8 animate-spin text-muted-foreground" />
        </div>
      ) : projects.length === 0 ? (
        <EmptyState
          icon={<FolderGit2 className="h-12 w-12" />}
          title="暂无项目"
          description="项目实战内容正在准备中，先完成前面的课程吧！"
        />
      ) : (
        <div className="space-y-4">
          {projects.map((project, index) => (
            <motion.div
              key={project.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <Link
                href={`/project/${project.id}`}
                className="block overflow-hidden rounded-2xl border border-border bg-card p-6 transition-all hover:border-primary/30"
              >
                <div className="flex items-start gap-4">
                  <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-primary/10 text-primary">
                    <FolderGit2 className="h-6 w-6" />
                  </div>

                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <h3 className="text-lg font-bold">{project.title}</h3>
                      <DifficultyBadge difficulty={project.difficulty} />
                    </div>

                    <p className="mt-1 text-sm text-muted-foreground">
                      {project.description}
                    </p>

                    <div className="mt-3 flex flex-wrap items-center gap-2">
                      {project.knowledge_points.map((point) => (
                        <Tag key={point} variant="secondary">{point}</Tag>
                      ))}
                    </div>

                    <div className="mt-4 flex items-center gap-4 text-xs text-muted-foreground">
                      <span className="flex items-center gap-1">
                        <Clock className="h-3.5 w-3.5" />
                        预计 {project.estimated_minutes} 分钟
                      </span>
                      <span className="flex items-center gap-1">
                        <Star className="h-3.5 w-3.5" />
                        {project.knowledge_points.length} 个知识点
                      </span>
                    </div>
                  </div>
                </div>
              </Link>
            </motion.div>
          ))}
        </div>
      )}
    </div>
  );
}
