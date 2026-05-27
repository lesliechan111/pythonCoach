# 架构设计文档

## 1. 系统架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        前端层 (Next.js)                      │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ Dashboard│ │ 课程学习 │ │ 练习做题 │ │ AI 答疑 │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                       │
│  │ 项目实战 │ │ 代码编辑 │ │ 个人中心 │                       │
│  └─────────┘ └─────────┘ └─────────┘                       │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP / REST
┌────────────────────▼────────────────────────────────────────┐
│                        后端层 (FastAPI)                      │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ 认证路由 │ │ 课程路由 │ │ 练习路由 │ │ 代码路由 │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                       │
│  │ AI 路由  │ │ 项目路由 │ │ 用户路由 │                       │
│  └─────────┘ └─────────┘ └─────────┘                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                       │
│  │ 权限校验 │ │ 业务逻辑 │ │ 数据访问 │                       │
│  └─────────┘ └─────────┘ └─────────┘                       │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
┌───────▼─────┐ ┌────▼────┐ ┌────▼─────┐
│  PostgreSQL  │ │  Redis  │ │  Docker  │
│  (主数据库)   │ │ (缓存)  │ │ (代码沙箱)│
└─────────────┘ └─────────┘ └──────────┘
                     │
            ┌────────▼────────┐
            │   AI Provider   │
            │ (OpenAI / 其他)  │
            └─────────────────┘
```

## 2. 分层设计

### 前端分层

| 层级 | 职责 | 示例 |
|------|------|------|
| Page | 页面组装，数据获取 | `app/lesson/[id]/page.tsx` |
| Layout | 页面布局框架 | `app/layout.tsx` |
| Component | 业务组件 | `LessonContent`, `CodeEditor` |
| Hook | 状态与副作用逻辑 | `useAuth`, `useLesson` |
| Lib | 工具函数、API 封装 | `api.ts`, `utils.ts` |
| Types | TypeScript 类型定义 | `types/index.ts` |

### 后端分层

| 层级 | 职责 | 示例 |
|------|------|------|
| Router | 路由定义、参数校验、权限检查 | `routers/courses.py` |
| Service | 业务逻辑编排 | `services/code_runner.py` |
| Model | 数据模型、表关系 | `models/lesson.py` |
| Schema | Pydantic 请求/响应模型 | `schemas/course.py` |
| Seed | 种子数据 | `seed/data/courses.py` |

## 3. 核心模块设计

### 3.1 认证模块

- JWT Token 认证
- 密码 bcrypt 哈希
- 注册 / 登录 / 获取当前用户

### 3.2 课程模块

- 课程与课时两级结构
- 学习进度追踪（user_lesson_progress）
- 课程内容 JSON 存储，支持富文本

### 3.3 练习模块

- 6 种题型：选择、判断、填空、代码补全、代码纠错、编程题
- 编程题通过代码沙箱运行测试用例判题
- 错题本自动收集答错题目

### 3.4 代码运行模块

- 独立 Docker 容器运行用户代码
- 资源限制：CPU、内存、执行时间
- 网络隔离（默认禁用）
- 敏感目录禁止访问
- 只暴露 stdout/stderr/exit_code

### 3.5 AI 模块

- Provider 抽象接口，支持多模型切换
- 上下文携带当前课程信息
- 系统提示词固定教学风格
- 功能：答疑、报错解释、代码点评、生成练习

### 3.6 项目实战模块

- 项目 -> 任务拆解结构
- 分步引导，不一次性给答案
- 每个任务含 starter_code、hint、answer_code

## 4. 安全设计

### 代码沙箱安全

1. **容器隔离**：每个请求新建容器，运行后销毁
2. **资源限制**：
   - 执行时间 <= 5 秒
   - 内存 <= 128MB
   - CPU <= 0.5 核
3. **系统调用过滤**：禁止 `exec`, `fork`, `open` 敏感路径
4. **网络隔离**：容器 `--network none`
5. **文件系统**：只读挂载，除 tmp 外无写权限
6. **环境纯净**：无敏感环境变量，无宿主机文件访问

### API 安全

1. JWT 认证保护私有接口
2. 输入参数 Pydantic 严格校验
3. SQL 注入防护：SQLModel 参数化查询
4. CORS 限制前端域名

## 5. 扩展性设计

### AI Provider 扩展

```python
class BaseAIProvider(ABC):
    @abstractmethod
    async def chat(self, messages: list, context: dict) -> str: ...

class OpenAIProvider(BaseAIProvider): ...
class ClaudeProvider(BaseAIProvider): ...
class LocalLLMProvider(BaseAIProvider): ...
```

### 新题型扩展

练习模块的判题逻辑按题型分发：
```python
def grade_exercise(exercise: Exercise, submission: Submission) -> GradeResult:
    graders = {
        ExerciseType.CHOICE: grade_choice,
        ExerciseType.CODE_COMPLETION: grade_code_completion,
        ExerciseType.PROGRAMMING: grade_programming,
        # 新增题型在此注册
    }
    return graders[exercise.type](exercise, submission)
```

### 新学习路线扩展

课程表有 `category` 和 `level` 字段，新增路线只需添加课程数据，无需改表结构。
