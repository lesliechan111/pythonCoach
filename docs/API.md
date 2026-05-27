# API 接口设计

## 基础约定

- 基础路径：`/api/v1`
- 认证方式：`Bearer <JWT>`
- 响应格式：统一 JSON，`{ "data": ..., "error": null }` 或 `{ "data": null, "error": { "code": "...", "message": "..." } }`
- 分页参数：`?page=1&page_size=20`

## 1. 认证相关

### POST /api/v1/auth/register
用户注册

**请求体：**
```json
{
  "username": "python_newbie",
  "email": "user@example.com",
  "password": "min8chars"
}
```

**响应：**
```json
{
  "data": {
    "id": 1,
    "username": "python_newbie",
    "email": "user@example.com",
    "token": "eyJhbGciOiJIUzI1NiIs..."
  }
}
```

### POST /api/v1/auth/login
用户登录

**请求体：**
```json
{
  "email": "user@example.com",
  "password": "min8chars"
}
```

**响应：** 同 register

### GET /api/v1/users/me
获取当前用户信息

**响应：**
```json
{
  "data": {
    "id": 1,
    "username": "python_newbie",
    "email": "user@example.com",
    "avatar_url": null,
    "learning_goal": "python_basic",
    "level": "beginner",
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

## 2. 课程相关

### GET /api/v1/courses
获取课程列表（按路线分类）

**查询参数：**
- `category` (可选): `python_basic`, `automation`, `crawler`, `data_analysis`, `backend`, `ai_tools`

**响应：**
```json
{
  "data": [
    {
      "id": 1,
      "title": "Python 零基础入门",
      "description": "从零开始学习 Python",
      "category": "python_basic",
      "level": "beginner",
      "lesson_count": 20,
      "estimated_minutes": 600,
      "progress_percent": 35
    }
  ]
}
```

### GET /api/v1/courses/:id
获取课程详情（含课时列表）

**响应：**
```json
{
  "data": {
    "id": 1,
    "title": "Python 零基础入门",
    "lessons": [
      {
        "id": 1,
        "title": "Python 是什么，能做什么",
        "order_index": 1,
        "estimated_minutes": 15,
        "is_completed": true
      }
    ]
  }
}
```

### GET /api/v1/lessons/:id
获取课时详情

**响应：**
```json
{
  "data": {
    "id": 1,
    "course_id": 1,
    "title": "Python 是什么，能做什么",
    "summary": "了解 Python 的应用场景",
    "objectives": ["知道 Python 是什么", "了解 Python 能做什么"],
    "content": "...",
    "analogy": "Python 就像乐高积木...",
    "example_code": "print('Hello, World!')",
    "line_by_line_explanation": [{"line": 1, "explanation": "输出文字到屏幕"}],
    "common_errors": [{"error": "拼写错误 prnit", "explanation": "注意拼写"}],
    "order_index": 1,
    "exercise_count": 5,
    "is_completed": true,
    "next_lesson_id": 2
  }
}
```

### POST /api/v1/lessons/:id/complete
标记课时完成

**响应：**
```json
{
  "data": {
    "progress_percent": 5,
    "completed_at": "2024-01-01T12:00:00Z"
  }
}
```

## 3. 练习相关

### GET /api/v1/lessons/:id/exercises
获取课时练习列表

**响应：**
```json
{
  "data": [
    {
      "id": 1,
      "lesson_id": 1,
      "type": "choice",
      "title": "Python 的创始人是谁？",
      "difficulty": "easy",
      "is_completed": false
    }
  ]
}
```

### GET /api/v1/exercises/:id
获取练习详情

**响应：**
```json
{
  "data": {
    "id": 1,
    "lesson_id": 1,
    "type": "choice",
    "title": "Python 的创始人是谁？",
    "description": "选择正确答案",
    "options": [
      {"label": "A", "text": "Guido van Rossum"},
      {"label": "B", "text": "Linus Torvalds"}
    ],
    "difficulty": "easy",
    "tags": ["history"],
    "starter_code": null,
    "is_completed": false
  }
}
```

### POST /api/v1/exercises/:id/submit
提交练习答案

**请求体：**
```json
{
  "answer": "A",
  "code": null
}
```

或编程题：
```json
{
  "answer": null,
  "code": "print('hello')"
}
```

**响应：**
```json
{
  "data": {
    "is_correct": true,
    "score": 100,
    "run_output": "hello",
    "run_error": null,
    "explanation": "正确！Guido van Rossum 是 Python 的创始人。",
    "ai_feedback": null
  }
}
```

### GET /api/v1/users/me/wrong-questions
获取错题本

**响应：**
```json
{
  "data": [
    {
      "exercise_id": 5,
      "title": "...",
      "wrong_count": 2,
      "last_wrong_at": "2024-01-01T12:00:00Z",
      "mastered": false
    }
  ]
}
```

## 4. 代码运行

### POST /api/v1/code/run
运行代码

**请求体：**
```json
{
  "language": "python",
  "code": "print('hello')",
  "stdin": ""
}
```

**响应：**
```json
{
  "data": {
    "stdout": "hello\n",
    "stderr": "",
    "exit_code": 0,
    "execution_time_ms": 35
  }
}
```

## 5. AI 相关

### POST /api/v1/ai/chat
AI 答疑

**请求体：**
```json
{
  "message": "变量是什么意思？",
  "lesson_id": 4,
  "history": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

**响应：**
```json
{
  "data": {
    "reply": "变量就像是一个盒子...",
    "suggested_practice": "试着定义一个变量 name = '小明'，然后打印它。"
  }
}
```

### POST /api/v1/ai/explain-error
解释代码错误

**请求体：**
```json
{
  "code": "print('hello",
  "error": "SyntaxError: unterminated string literal",
  "lesson_id": 3
}
```

### POST /api/v1/ai/review-code
代码点评

**请求体：**
```json
{
  "code": "...",
  "lesson_id": 5,
  "exercise_id": 12
}
```

### POST /api/v1/ai/generate-practice
生成额外练习

**请求体：**
```json
{
  "lesson_id": 4,
  "difficulty": "easy",
  "count": 3
}
```

## 6. 项目相关

### GET /api/v1/projects
获取项目列表

**响应：**
```json
{
  "data": [
    {
      "id": 1,
      "title": "个人信息卡片",
      "difficulty": "beginner",
      "category": "python_basic",
      "estimated_minutes": 30,
      "task_count": 3,
      "progress_percent": 0
    }
  ]
}
```

### GET /api/v1/projects/:id
获取项目详情

**响应：**
```json
{
  "data": {
    "id": 1,
    "title": "个人信息卡片",
    "description": "创建一个展示个人信息的程序",
    "difficulty": "beginner",
    "knowledge_points": ["变量", "字符串", "print"],
    "tasks": [
      {
        "id": 1,
        "title": "定义个人信息变量",
        "order_index": 1,
        "is_completed": false
      }
    ]
  }
}
```

### POST /api/v1/project-tasks/:id/submit
提交项目任务

**请求体：**
```json
{
  "code": "name = '小明'\nprint(name)"
}
```

## 7. 学习统计

### GET /api/v1/users/me/dashboard
首页 Dashboard 数据

**响应：**
```json
{
  "data": {
    "welcome_message": "欢迎回来，python_newbie！",
    "today_task": {
      "type": "lesson",
      "title": "变量",
      "id": 4
    },
    "stats": {
      "completed_lessons": 3,
      "total_lessons": 20,
      "completed_exercises": 15,
      "total_exercises": 100,
      "wrong_questions": 2,
      "completed_projects": 0,
      "total_projects": 3,
      "study_days": 5,
      "accuracy_rate": 0.88
    },
    "recent_submissions": [...],
    "continue_lesson_id": 4
  }
}
```

### GET /api/v1/users/me/progress
学习进度

**响应：**
```json
{
  "data": {
    "course_progress": [
      {
        "course_id": 1,
        "completed_lessons": 3,
        "total_lessons": 20,
        "progress_percent": 15
      }
    ]
  }
}
```
