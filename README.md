# Python Coach — Python 学习助手

面向零基础小白的 Python 系统学习平台。

## 核心定位

- **不是 AI 聊天工具**：系统自带完整教程、题库、项目实战
- **AI 只做辅助**：答疑、报错解释、代码点评、生成额外练习
- **学完即练**：每节课配套练习，代码可在线运行
- **项目驱动**：通过实战项目巩固知识

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Next.js 14 (App Router), React, TypeScript, Tailwind CSS, shadcn/ui, Monaco Editor, Framer Motion |
| 后端 | FastAPI, Python, SQLModel, PostgreSQL |
| 代码运行 | Docker 沙箱，受限 Python 容器 |
| AI | OpenAI 兼容 API，Provider 抽象层 |

## 项目结构

```
pythonCoach/
├── docs/                  # 架构文档
├── backend/               # FastAPI 后端
├── frontend/              # Next.js 前端
├── code-runner/           # Docker 代码执行沙箱
├── scripts/               # 初始化脚本
├── docker-compose.yml
└── .env.example
```

## 快速开始

```bash
# 1. 复制环境变量
cp .env.example .env

# 2. 启动基础设施
docker-compose up -d db redis

# 3. 初始化后端
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python -m app.seed.init_db

# 4. 启动后端
uvicorn app.main:app --reload

# 5. 启动前端（新终端）
cd frontend
npm install
npm run dev
```

## 开发阶段

| 阶段 | 内容 |
|------|------|
| Phase 1 | 架构设计 + 数据库 + API 骨架 + 前端框架（当前） |
| Phase 2 | 用户系统 + 课程模块 + 学习进度 |
| Phase 3 | 练习题系统 + 代码运行沙箱 |
| Phase 4 | AI 助手集成 |
| Phase 5 | 项目实战模块 |
| Phase 6 | 首页 Dashboard + 数据统计 |
| Phase 7 | UI  polish + 响应式 + 深色模式 |
