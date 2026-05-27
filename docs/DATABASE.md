# 数据库设计

## ER 关系图

```
users ||--o{ user_lesson_progress : tracks
users ||--o{ user_exercise_attempts : submits
users ||--o{ user_project_progress : works_on
users ||--o{ code_submissions : submits
users ||--o{ wrong_questions : has

courses ||--|{ lessons : contains
lessons ||--|{ exercises : has
lessons ||--o{ code_submissions : referenced_by

projects ||--|{ project_tasks : contains
project_tasks ||--o{ code_submissions : referenced_by

exercises ||--o{ user_exercise_attempts : answered
exercises ||--o{ wrong_questions : recorded_in
exercises ||--o{ code_submissions : referenced_by
```

## 表结构

### users
用户表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| username | String(50) | unique, not null | 用户名 |
| email | String(100) | unique, not null | 邮箱 |
| password_hash | String(255) | not null | bcrypt 哈希 |
| avatar_url | String(255) | nullable | 头像 URL |
| learning_goal | String(50) | default "python_basic" | 学习目标 |
| level | String(20) | default "beginner" | 当前等级 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### courses
课程表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| title | String(100) | not null | 课程标题 |
| description | Text | nullable | 课程简介 |
| category | String(50) | not null | 分类 |
| level | String(20) | not null | 难度等级 |
| order_index | Integer | default 0 | 排序 |
| estimated_minutes | Integer | default 0 | 预计学习时间 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### lessons
课时表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| course_id | Integer | FK → courses.id, not null | |
| title | String(100) | not null | 课时标题 |
| summary | Text | nullable | 课程简介 |
| objectives | JSON | default [] | 学习目标列表 |
| content | Text | not null | 教程正文（Markdown） |
| analogy | Text | nullable | 生活类比 |
| example_code | Text | nullable | 代码示例 |
| line_by_line_explanation | JSON | default [] | 逐行解释 [{line, explanation}] |
| common_errors | JSON | default [] | 常见错误 [{error, explanation}] |
| order_index | Integer | default 0 | 排序 |
| estimated_minutes | Integer | default 15 | 预计学习时间 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### exercises
练习题表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| lesson_id | Integer | FK → lessons.id, not null | |
| type | String(20) | not null | 题型：choice, judge, fill_blank, code_completion, code_fix, programming |
| title | String(200) | not null | 题目标题 |
| description | Text | not null | 题目描述 |
| options | JSON | nullable | 选择题选项 [{label, text}] |
| answer | String(500) | not null | 正确答案 |
| explanation | Text | not null | 答案解析 |
| starter_code | Text | nullable | 初始代码 |
| reference_code | Text | nullable | 参考代码 |
| test_cases | JSON | nullable | 测试用例 [{input, expected_output}] |
| difficulty | String(20) | default "easy" | 难度 |
| tags | JSON | default [] | 标签 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### projects
项目表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| title | String(100) | not null | 项目标题 |
| description | Text | not null | 项目介绍 |
| difficulty | String(20) | not null | 难度 |
| category | String(50) | not null | 分类 |
| estimated_minutes | Integer | default 60 | 预计完成时间 |
| final_result | Text | nullable | 最终效果描述 |
| knowledge_points | JSON | default [] | 涉及知识点 |
| order_index | Integer | default 0 | 排序 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### project_tasks
项目任务表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| project_id | Integer | FK → projects.id, not null | |
| title | String(100) | not null | 任务标题 |
| description | Text | not null | 任务说明 |
| starter_code | Text | nullable | 初始代码 |
| hint | Text | nullable | 提示 |
| answer_code | Text | nullable | 参考答案 |
| test_cases | JSON | nullable | 测试用例 |
| order_index | Integer | default 0 | 排序 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

### user_lesson_progress
用户课时进度表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| user_id | Integer | FK → users.id, not null | |
| lesson_id | Integer | FK → lessons.id, not null | |
| status | String(20) | default "not_started" | 状态：not_started, in_progress, completed |
| progress_percent | Integer | default 0 | 进度百分比 |
| completed_at | DateTime | nullable | 完成时间 |
| last_studied_at | DateTime | nullable | 最近学习时间 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

**唯一约束：** (user_id, lesson_id)

### user_exercise_attempts
用户练习提交记录表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| user_id | Integer | FK → users.id, not null | |
| exercise_id | Integer | FK → exercises.id, not null | |
| user_answer | String(500) | nullable | 用户答案（选择/判断/填空） |
| user_code | Text | nullable | 用户代码 |
| is_correct | Boolean | nullable | 是否正确 |
| score | Integer | nullable | 得分 |
| run_output | Text | nullable | 代码运行输出 |
| run_error | Text | nullable | 代码运行错误 |
| ai_feedback | Text | nullable | AI 点评 |
| created_at | DateTime | default now | |

### user_project_progress
用户项目进度表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| user_id | Integer | FK → users.id, not null | |
| project_id | Integer | FK → projects.id, not null | |
| current_task_id | Integer | FK → project_tasks.id, nullable | 当前任务 |
| status | String(20) | default "not_started" | |
| progress_percent | Integer | default 0 | |
| completed_at | DateTime | nullable | |
| updated_at | DateTime | default now, onupdate | |

**唯一约束：** (user_id, project_id)

### code_submissions
代码提交记录表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| user_id | Integer | FK → users.id, not null | |
| lesson_id | Integer | FK → lessons.id, nullable | 关联课时 |
| exercise_id | Integer | FK → exercises.id, nullable | 关联练习 |
| project_task_id | Integer | FK → project_tasks.id, nullable | 关联项目任务 |
| code | Text | not null | 代码 |
| language | String(20) | default "python" | |
| stdout | Text | nullable | 标准输出 |
| stderr | Text | nullable | 标准错误 |
| exit_code | Integer | nullable | 退出码 |
| execution_time_ms | Integer | nullable | 执行时间 |
| ai_feedback | Text | nullable | AI 反馈 |
| created_at | DateTime | default now | |

### wrong_questions
错题本表

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | Integer | PK, auto | |
| user_id | Integer | FK → users.id, not null | |
| exercise_id | Integer | FK → exercises.id, not null | |
| wrong_count | Integer | default 1 | 错误次数 |
| last_wrong_at | DateTime | default now | 最近错误时间 |
| mastered | Boolean | default False | 是否已掌握 |
| created_at | DateTime | default now | |
| updated_at | DateTime | default now, onupdate | |

**唯一约束：** (user_id, exercise_id)

## 索引设计

```sql
-- 用户查询
CREATE INDEX idx_users_email ON users(email);

-- 课程排序
CREATE INDEX idx_lessons_course_order ON lessons(course_id, order_index);
CREATE INDEX idx_exercises_lesson ON exercises(lesson_id);
CREATE INDEX idx_project_tasks_project ON project_tasks(project_id, order_index);

-- 进度查询
CREATE INDEX idx_user_lesson_progress_user ON user_lesson_progress(user_id);
CREATE INDEX idx_user_exercise_user ON user_exercise_attempts(user_id, created_at DESC);
CREATE INDEX idx_user_project_user ON user_project_progress(user_id);

-- 错题本
CREATE INDEX idx_wrong_questions_user ON wrong_questions(user_id, mastered);
```
