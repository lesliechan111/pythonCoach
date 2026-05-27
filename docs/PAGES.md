# 页面结构与组件拆分

## 页面路由（App Router）

| 路径 | 页面 | 说明 |
|------|------|------|
| `/` | 首页 Dashboard | 学习概览、今日任务 |
| `/learn` | 学习路线页 | 课程列表、进度 |
| `/lesson/[id]` | 课程详情页 | 教程正文、练习入口 |
| `/exercise/[id]` | 练习页面 | 做题、代码编辑 |
| `/project` | 项目实战列表 | 项目卡片 |
| `/project/[id]` | 项目详情页 | 任务拆解、编码 |
| `/ai-chat` | AI 答疑页 | 聊天界面 |
| `/profile` | 个人中心 | 统计、错题本、历史 |
| `/auth/login` | 登录页 | |
| `/auth/register` | 注册页 | |

## 布局组件（Layout Components）

### `components/layout/Navbar.tsx`
- 顶部导航栏
- Logo、学习路线、项目实战、AI 助手入口
- 用户头像下拉菜单
- 响应式：移动端折叠为汉堡菜单

### `components/layout/Sidebar.tsx`
- 左侧边栏（仅学习页面）
- 课程章节列表
- 课时完成状态指示
- 当前课时高亮

### `components/layout/Footer.tsx`
- 底部信息
- 极简，不占空间

## 首页 Dashboard 组件

### `components/dashboard/WelcomeBanner.tsx`
- 欢迎语 + 当前时间
- 连续学习天数徽章

### `components/dashboard/ProgressCard.tsx`
- 环形进度条
- 总课程进度百分比
- 已完成/总数

### `components/dashboard/DailyTask.tsx`
- 今日推荐学习任务
- 快速开始按钮

### `components/dashboard/StatsGrid.tsx`
- 统计卡片网格
- 已完成课程数、做题数、正确率、错题数

### `components/dashboard/RecentActivity.tsx`
- 最近学习记录
- 时间线形式

### `components/dashboard/ContinueLearning.tsx`
- 上次学习课程卡片
- 一键继续

## 课程学习组件

### `components/learn/LessonCard.tsx`
- 课时卡片
- 标题、预计时间、完成状态
- 锁定/解锁状态

### `components/learn/LessonContent.tsx`
- 教程正文渲染（Markdown）
- 代码块高亮
- 生活类比卡片（特殊样式）

### `components/learn/CodeExample.tsx`
- 代码示例展示
- 一键复制
- 可点击"运行示例"

### `components/learn/LineExplanation.tsx`
- 逐行解释表格
- 行号 + 代码片段 + 解释

### `components/learn/CommonErrors.tsx`
- 常见错误警示卡片
- 错误代码 + 正确代码对比

### `components/learn/ObjectivesList.tsx`
- 学习目标清单
- 学习前展示

## 练习组件

### `components/exercise/ExerciseCard.tsx`
- 题目卡片（列表中）
- 题型标签、难度标签、完成状态

### `components/exercise/ExerciseContent.tsx`
- 题目描述渲染
- 选择题选项 / 填空题输入框 / 代码题编辑器

### `components/exercise/CodeEditor.tsx`
- Monaco Editor 封装
- Python 语法高亮
- 主题适配（深色模式）
- 字体大小调整

### `components/exercise/ExerciseResult.tsx`
- 提交结果展示
- 正确/错误状态
- 运行输出显示
- 解析展开

### `components/exercise/ExerciseNavigator.tsx`
- 题目导航
- 上一题 / 下一题
- 题目列表快速跳转

## AI 助手组件

### `components/ai/ChatWindow.tsx`
- 聊天消息列表容器
- 自动滚动到底部
- 课程上下文提示

### `components/ai/MessageBubble.tsx`
- 消息气泡
- 用户 / AI 区分样式
- 支持 Markdown 渲染

### `components/ai/CodeBlock.tsx`
- 消息中的代码块
- 语法高亮
- 一键复制
- 一键运行（跳转到代码编辑器）

### `components/ai/ChatInput.tsx`
- 输入框
- 发送按钮
- 快捷问题按钮（"解释报错", "给点提示"）

### `components/ai/SuggestedPrompts.tsx`
- 快捷提问建议
- 根据当前课程动态生成

## 项目实战组件

### `components/project/ProjectCard.tsx`
- 项目卡片
- 难度标签、预计时间、知识点标签
- 进度条

### `components/project/TaskStepper.tsx`
- 任务步骤条
- 当前任务高亮
- 已完成任务打勾

### `components/project/ProjectEditor.tsx`
- 项目代码编辑器
- 左侧任务说明，右侧编辑器
- 运行结果面板

### `components/project/HintAccordion.tsx`
- 提示手风琴
- 逐步展开提示，不直接给答案

## 公共 UI 组件（shadcn/ui 扩展）

### `components/ui/Tag.tsx`
- 标签组件
- 颜色按类型：难度、课程分类

### `components/ui/DifficultyBadge.tsx`
- 难度徽章
- 简单(绿) / 中等(黄) / 困难(红)

### `components/ui/ProgressRing.tsx`
- 环形进度条
- 带动画

### `components/ui/CodeBlock.tsx`
- 通用代码展示块
- 支持行号、复制

## 状态管理

使用 React Hook + Context 方案：

- `AuthContext`：用户登录状态
- `LessonContext`：当前课程学习上下文（供 AI 使用）
- `CodeRunContext`：代码运行状态

## 响应式断点

```
mobile:  < 768px   单列布局，底部固定导航
tablet:  768px+   可折叠侧边栏
desktop: 1024px+  左侧边栏 + 主内容 + 右侧面板
```
