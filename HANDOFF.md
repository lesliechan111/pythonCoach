# Handoff — Python Coach 项目交接说明

> 生成时间：2026-05-27
> 会话状态：Phase 1-5 完成，Phase 6-7 未开始

---

## 1. 项目目标

「Python 学习助手」Web 应用，面向零基础小白，帮助用户从 Python 基础语法学到项目实战。

**核心定位：**
- 系统自带教程和题库（不是纯 AI 对话工具）
- AI 只做辅助：答疑、报错解释、代码点评
- 学完即练：每课配套练习，代码可在线运行
- 项目驱动：通过实战项目巩固

**技术栈：**
- 前端：Next.js 14 (App Router) + React + TypeScript + Tailwind CSS + Framer Motion + Monaco Editor
- 后端：FastAPI + Python + SQLModel + SQLite (开发) / PostgreSQL (生产)
- 代码运行：Docker 沙箱 (生产) / subprocess (本地开发)，自动切换
- AI：OpenAI 兼容 Provider 抽象层，支持 OpenAI / DeepSeek 等兼容 API

---

## 2. 已完成功能

### Phase 1 (文档 + 初始化)
- 5 份设计文档（ARCHITECTURE / API / DATABASE / PAGES / MVP_PLAN）
- 后端 20 个文件（FastAPI 入口、11 张表、7 个路由模块、3 个服务、Schema、种子数据）
- 前端 28 个文件（10 页面、14 组件、配置文件）
- docker-compose.yml + code-runner Dockerfile

### Phase 2 (前后端联调 + 用户系统) — **完成**

**后端 API 全部真实实现（0 个桩代码）：**
- `POST /exercises/{id}/submit` — 接入 grader 判题，记录 UserExerciseAttempt，管理 WrongQuestion
- `GET /users/me/wrong-questions` — 未掌握的错题列表
- `POST /project-tasks/{id}/submit` — 运行用户代码，对比输出判题
- `GET /users/me/dashboard` — 聚合 5 张表真实统计
- `GET /users/me/progress` — 课程维度学习进度
- `GET /users/me/submissions` — 最近 20 条提交记录
- `POST /lessons/{id}/complete` — 自动记录课时学习进度

**前端 7 页面 API 对接：** Dashboard、学习路线、课时详情、练习页(6 题型)、项目列表/详情、个人中心

### Phase 3 (编辑器 + 代码沙箱) — **完成**
- Monaco Editor 封装 (`CodeEditor.tsx`)，自定义 `pythoncoach-dark` 主题
- Docker + subprocess 双模式代码运行器，自动回退

### Phase 4 (AI 助手真实对接) — **完成** ✨ 本次新增

**后端 4 个 AI 端点全部接入真实 Provider：**

| 端点 | 文件 | 功能 |
|------|------|------|
| `POST /api/v1/chat` | `routers/ai.py` | 通用 AI 对话（小白友好教学 prompt + 课程上下文 + 历史消息） |
| `POST /api/v1/explain-error` | `routers/ai.py` | 报错解释（生活类比 → 出错原因 → 具体修改方法） |
| `POST /api/v1/review-code` | `routers/ai.py` | 代码点评（先鼓励 → 改进建议 → 具体修改方案） |
| `POST /api/v1/generate-practice` | `routers/ai.py` | 生成练习题（读课程内容 → 生成 N 道指定难度题目 → JSON 返回） |

**AI Provider 改进：**
- `get_ai_provider()` 加 `@lru_cache` 复用 provider 实例
- 支持 `AI_PROVIDER=deepseek`（DeepSeek API 兼容 OpenAI 协议）

**前端 AI 聊天页面：**
- `ai-chat/page.tsx` — `setTimeout` 模拟 → 真实 `fetch /api/v1/chat`
- 传递完整对话历史，支持错误提示
- `lib/api.ts` 新增 `api.ai.chat()` / `explainError()` / `reviewCode()` / `generatePractice()`

**配置修复：**
- `.env` 从项目根目录通过软链接 → `backend/.env`
- `config.py` 加 `extra = "ignore"`，避免前端环境变量被 pydantic 拒绝
- DeepSeek base URL 自动处理（需 `/v1` 后缀）

### Phase 5 (种子数据扩展) — **完成** ✨ 本次新增

| 内容 | 之前 | 之后 |
|------|:--:|:--:|
| 课时 | 2 节 | **20 节** |
| 练习题 | 10 道 | **100 道** (每节 5 道，6 种题型覆盖) |
| 项目 | 1 个 | **3 个** |
| 项目任务 | 3 个 | **10 个** |

**课程结构：**
- Module 1 (1-5): 入门基础 — Python 介绍 / 环境搭建 / 变量与数据类型 / 字符串操作 / 数字与运算符
- Module 2 (6-10): 流程控制 — if 条件判断 / 比较与逻辑运算符 / while 循环 / for 与 range / break/continue 与嵌套
- Module 3 (11-15): 数据结构 — 列表基础 / 列表排序推导式 / 元组 / 字典基础 / 字典方法与嵌套
- Module 4 (16-20): 函数与文件 — 函数定义 / 参数与返回值 / 作用域与 lambda / 模块与 import / 文件读写与综合复习

**新增项目：**
| # | 项目 | 任务数 | 覆盖知识点 |
|---|------|:--:|------|
| 1 | 个人信息卡片 | 3 | 变量、字符串、input/print、f-string |
| 2 | 猜数字游戏 | 4 | random、while 循环、if/elif/else、int() 转换、难度选择 |
| 3 | 待办事项管理器 | 3 | 列表+字典嵌套、while 菜单循环、CRUD 操作 |

### 当前完整数据概览

```
1 Course (Python 零基础入门)
├── 20 Lessons (每节含: Markdown 正文、生活类比、示例代码、逐行解释、常见错误)
│   └── 100 Exercises (每节 5 道, 6 种题型)
└── 3 Projects
    ├── Project 1: 个人信息卡片 (3 tasks)
    ├── Project 2: 猜数字游戏 (4 tasks)
    └── Project 3: 待办事项管理器 (3 tasks)
```

---

## 3. 文件清单

```
pythonCoach/
├── .env                                  # ✨ AI_PROVIDER=deepseek, SQLite, JWT 配置
├── .env.example                          # ✨ 新增 DeepSeek 配置示例
├── docker-compose.yml
├── HANDOFF.md                            # 本文件
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DATABASE.md
│   ├── PAGES.md
│   └── MVP_PLAN.md
├── backend/
│   ├── .env -> ../.env                   # ✨ 软链接指向根目录 .env
│   ├── requirements.txt
│   ├── pythoncoach.db                    # SQLite 数据库（100 练习题 + 20 课时 + 3 项目）
│   ├── venv/                             # Python 3.9 虚拟环境
│   └── app/
│       ├── __init__.py
│       ├── main.py                       # ✨ AI 路由前缀改为 /api/v1
│       ├── config.py                     # ✨ extra = "ignore" 忽略前端 env
│       ├── database.py
│       ├── models/
│       │   ├── user.py
│       │   ├── course.py
│       │   ├── exercise.py
│       │   ├── project.py
│       │   └── submission.py
│       ├── routers/
│       │   ├── auth.py                   # JWT 注册/登录
│       │   ├── users.py                  # Dashboard/进度/统计
│       │   ├── courses.py                # 课程/课时/completeLesson
│       │   ├── exercises.py              # 练习列表/提交判分/错题本
│       │   ├── code.py                   # 代码运行
│       │   ├── ai.py                     # ✨ 4 个 AI 端点全部接入真实 Provider
│       │   └── projects.py               # 项目列表/任务提交
│       ├── schemas/
│       │   ├── user.py
│       │   ├── course.py
│       │   └── exercise.py
│       ├── services/
│       │   ├── ai_provider.py            # ✨ 支持 deepseek provider, @lru_cache
│       │   ├── code_runner.py            # Docker + subprocess 双模式
│       │   └── exercise_grader.py        # 6 种题型判题逻辑
│       └── seed/
│           ├── init_db.py
│           └── data/
│               ├── courses.py            # ✨ 2→20 节课（完整 Markdown 正文）
│               ├── exercises.py          # ✨ 10→100 道练习题
│               └── projects.py           # ✨ 1→3 个项目（10 个任务）
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── tailwind.config.ts
│   ├── tsconfig.json
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── page.tsx                      # Dashboard
│   │   ├── auth/login/page.tsx
│   │   ├── auth/register/page.tsx
│   │   ├── learn/page.tsx
│   │   ├── lesson/[id]/page.tsx
│   │   ├── exercise/[id]/page.tsx
│   │   ├── project/page.tsx
│   │   ├── project/[id]/page.tsx
│   │   ├── ai-chat/page.tsx              # ✨ 真实 API 调用替换 setTimeout 模拟
│   │   └── profile/page.tsx
│   ├── components/
│   │   ├── layout/Navbar.tsx
│   │   ├── layout/Sidebar.tsx
│   │   ├── dashboard/                    # WelcomeBanner, ProgressCard, StatsGrid 等
│   │   ├── learn/LessonCard.tsx
│   │   ├── learn/LessonContent.tsx
│   │   └── ui/
│   │       ├── CodeEditor.tsx            # Monaco Editor 封装
│   │       ├── DifficultyBadge.tsx
│   │       ├── Tag.tsx
│   │       ├── CourseCard.tsx
│   │       └── EmptyState.tsx
│   ├── hooks/
│   │   └── useAuth.tsx
│   ├── lib/
│   │   ├── api.ts                        # ✨ 新增 ai.chat/explainError/reviewCode/generatePractice
│   │   └── utils.ts
│   └── types/
│       └── index.ts
└── code-runner/
    ├── Dockerfile
    └── run.py
```

标注 ✨ 的是本次会话新增或修改的文件。

---

## 4. 未完成项

### Phase 6: Dashboard 真实统计完善

| 任务 | 说明 |
|------|------|
| RecentActivity 组件 | 目前为空，需要从 CodeSubmission / UserExerciseAttempt 聚合真实活动数据 |
| 骨架屏 / Skeleton | 页面加载时显示骨架屏，改善体验 |

### Phase 7: UI 打磨

| 任务 | 说明 |
|------|------|
| 移动端响应式完善 | 部分页面在小屏幕上布局不佳 |
| 错误边界 / ErrorBoundary | 前端无全局错误处理 |

---

## 5. 已知问题

| # | 问题 | 严重度 | 说明 |
|---|------|:----:|------|
| 1 | Python 3.9 兼容 | 中 | 部分文件可能有 `X \| None` 语法，Python 3.9 需改为 `Optional[X]` |
| 2 | npm 安全警告 | 低 | next@14.2.3 有安全漏洞 |
| 3 | LessonCard.isLocked | 低 | `order_index > 5` 硬编码，应从 API/progress 获取 |
| 4 | Sidebar.isLocked | 低 | `id > 5` 硬编码，同上 |
| 5 | SQLite JSON 字段 | 低 | JSON 字段存储为文本，前端需 `JSON.parse()` |
| 6 | seed/init_db.py 不幂等 | 低 | 只检查 Course 表，重复执行不更新 |
| 7 | Docker Desktop 未运行 | 低 | 代码运行用 subprocess 回退，无安全隔离 |
| 8 | RecentActivity 组件为空 | 低 | 需要从提交记录聚合数据 |
| 9 | project task 1/3 判分 | 中 | seed data 中 `answer_code` 含 `input()`，subprocess 模式无 stdin 导致 EOFError。Docker 模式可解决 |
| 10 | TypeScript 错误 | 低 | `RecentActivity.tsx:67` — `Type 'undefined' cannot be used as an index type`（预存问题） |
| 11 | courses.py 引号复杂度 | 低 | example_code 字段混用 `'''`/`"""` 分隔符，编辑时需注意嵌套引号冲突 |

### 问题 11 详解 — 编辑 courses.py 注意事项

`courses.py` 中的 `content` 字段使用 `"""..."""` 作分隔符，`example_code` 字段经修复后使用 `'''...'''` 分隔符。代码示例中的 Python docstring：
- 在 `content`（`"""` 分隔）中 → 必须用 `'''docstring'''`
- 在 `example_code`（`'''` 分隔）中 → 必须用 `"""docstring"""`

新增课程内容时请注意这个规则，否则会语法报错。

---

## 6. 下一步推荐

### 推荐顺序

1. **Phase 6: Dashboard 完善** — RecentActivity 接入真实提交数据，让 Dashboard 更完整
2. **Phase 7: UI 打磨** — 骨架屏、响应式、ErrorBoundary
3. **前端优化** — LessonCard/Sidebar 锁定逻辑接入真实 API
4. **内容扩展** — 继续增加课程（如进阶 Python、数据分析等方向）

---

## 7. 不要重复做 / 不要改动的内容

| 文件/模块 | 原因 |
|------|------|
| `app/models/*` | 数据模型已定，改表需同时改种子数据 |
| `app/services/exercise_grader.py` | 6 种题型判题逻辑完整 |
| `app/services/code_runner.py` | Docker + subprocess 双模式完整 |
| `app/services/ai_provider.py` | Provider 框架已定，deepseek/openai 已支持 |
| `app/routers/auth.py` | JWT 认证完整 |
| `app/routers/exercises.py` | 判题 + 错题本逻辑完整 |
| `app/routers/projects.py` | 任务提交逻辑完整 |
| `app/routers/users.py` | 统计聚合逻辑完整 |
| `app/routers/ai.py` | 4 个 AI 端点已接入真实 Provider |
| `components/ui/CodeEditor.tsx` | Monaco Editor 封装稳定 |
| `hooks/useAuth.tsx` | Auth 状态管理完整 |
| `tailwind.config.ts` | 主题色已定 |
| `app/globals.css` | CSS 变量体系已定 |
| `seed/data/courses.py` | 20 节完整课时（编辑注意引号规则） |
| `seed/data/exercises.py` | 100 道完整练习题 |
| `seed/data/projects.py` | 3 个完整项目 |
| `config.py` | `extra = "ignore"` 不要去掉 |
| `HANDOFF.md` | 本文件 |

---

## 8. 项目命令

### 后端

```bash
cd /Users/lesliechan/project/pythonCoach/backend

# 激活虚拟环境
source venv/bin/activate

# 重新播种（删除数据库并重建）
rm -f pythoncoach.db && PYTHONPATH=. python -m app.seed.init_db

# 启动后端 (http://localhost:8000)
PYTHONPATH=. uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 健康检查
curl http://localhost:8000/health

# API 文档
# http://localhost:8000/docs
```

### 前端

```bash
cd /Users/lesliechan/project/pythonCoach/frontend

# 安装依赖
npm install

# 启动开发服务器 (http://localhost:3000)
npm run dev

# TypeScript 类型检查
npx tsc --noEmit
```

### 本地开发（双终端）

```bash
# 终端 1 — 后端
cd /Users/lesliechan/project/pythonCoach/backend
source venv/bin/activate
PYTHONPATH=. uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 终端 2 — 前端
cd /Users/lesliechan/project/pythonCoach/frontend
npm run dev
```

### Docker

```bash
cd /Users/lesliechan/project/pythonCoach

# 构建代码运行镜像
docker-compose build code-runner

# 启动 PostgreSQL + Redis（生产模式）
docker-compose up -d db redis

# 需要先启动 Docker Desktop
```

### 当前 .env 配置

`.env` 位于项目根目录，`backend/.env` 是软链接。当前配置：
- **数据库**: SQLite (`DATABASE_URL=sqlite:///pythoncoach.db`)
- **AI**: DeepSeek (`AI_PROVIDER=deepseek`, `OPENAI_BASE_URL=https://api.deepseek.com/v1`)
- **JWT**: `SECRET_KEY=change-this-to-a-random-secret-key-at-least-32-chars`
- **代码运行**: subprocess 模式 (`CODE_RUNNER_USE_DOCKER=false`)

```bash
# 查看当前配置
cat /Users/lesliechan/project/pythonCoach/.env
```

---

> 如需在新会话中继续开发，请将本文档提供给 AI 作为上下文。
