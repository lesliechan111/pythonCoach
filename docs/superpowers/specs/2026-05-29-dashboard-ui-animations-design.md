# Dashboard UI 动效优化设计文档

**日期：** 2026-05-29
**类型：** UI Enhancement (动效与交互)
**范围：** 前端仪表盘页面及共享组件

---

## 目标

为 Python Coach 仪表盘注入持续的"生命感"和交互反馈，提升学习体验的情感价值和操作感受。以微交互打底 + 叙事动效增强学习引导感，不做过度装饰。

---

## 设计原则

- **不干扰学习** — 动效增强体验而非分散注意
- **性能优先** — 使用 CSS transform/opacity，减少重排；`will-change` 仅用于关键元素
- **可复用** — 通用能力抽为 hooks/组件
- **渐进增强** — 动效是附加值，不影响功能可用性

---

## 共享基础设施

### useCountUp(target: number, duration: number) hook

数字从 0（或前一个值）平滑滚动到目标值。内部用 `requestAnimationFrame` + easing 插值，60fps。支持：

- `target` — 目标数值
- `duration` — 动画时长 ms（默认 800）
- 返回值 `number` — 当前显示值（整数/百分比字符串由调用方格式化）

### 骨架屏 Shimmer（CSS keyframe）

tailwind.config.ts 新增 `shimmer` 动画 keyframe：`0% { background-position: 200% 0 } 100% { background-position: -200% 0 }`。组件使用时添加 className：`bg-gradient-to-r from-muted via-muted/50 to-muted bg-[length:200%_100%] animate-shimmer`。

适用位置：ContinueLearning 未开始状态的骨架、RecentActivity 列表项骨架、CourseCard 列表加载骨架。

### 点击波纹

---

## 组件逐项变更

### 1. WelcomeBanner

| 变更 | 实现 |
|------|------|
| 背景光斑漂移 | CSS `@keyframes`：两个光斑 `translate` + `rotate`，一个 18s 循环，另一个 24s（错开节奏），ease-in-out 往返 |
| Sparkle 旋转 | `motion.div` 每 3s `rotate: 360`，`repeat: Infinity`，ease: "linear" |
| 学习天数递增 | 使用 `useCountUp`，duration 1000ms |
| 鼓励语随机 | 前端维护 8 句数组，按小时 + 随机取模选择 |

### 2. ContinueLearning

| 变更 | 实现 |
|------|------|
| 进度条末端发光 | 进度条 div 末尾绝对定位一个 `w-2 h-2 rounded-full bg-primary` 圆点，`animate-pulse` |
| 按钮 ripple | `whileTap={{ scale: 0.97 }}` + 扩散伪元素（CSS：`.ripple::after { ... }`） |
| hover 抬升 | `hover:-translate-y-0.5` + `shadow-lg transition-shadow` |

### 3. ProgressCard

| 变更 | 实现 |
|------|------|
| 数字递增 | `useCountUp(percent, 1200)` — 因为百分比是 UI 核心，给稍长的 1.2s |
| 环闪 | 当 percent 变化时，用 `animate` 给 circle 添加 `filter: drop-shadow(0 0 6px hsl(var(--primary)))`，500ms 后恢复 |
| 底部分数着色 | `{completed}` 用 primary 色，`{total}` 用 muted-foreground |

### 4. StatsGrid

| 变更 | 实现 |
|------|------|
| 入场方向 | 卡片从**左下角 20px** 滑入（`initial={{ opacity: 0, x: -10, y: 10 }}`），保留 stagger |
| 图标弹跳 | `whileInView` 触发 spring bounce：`{ scale: [1, 1.2, 1], transition: { type: "spring", stiffness: 300, delay: 0.15 } }` |
| 数字递增 | 正确率用 `useCountUp`，formatter: `v => Math.round(v * 100) + "%"`；其余整数直接显示 |
| 正确率着色 | ≥80% 绿色 text-emerald-400，≥60% 黄色 text-amber-400，<60% 保持默认 |

### 5. CourseCard

| 变更 | 实现 |
|------|------|
| 入场 | `initial={{ opacity: 0, rotateX: 3, y: 20 }}`，`animate` 到 normal，轻微翻转增加卡片层次 |
| hover 边框发光 | `hover:border-primary/50 hover:shadow-lg hover:shadow-primary/5` — 已有，强化 transition-duration 到 300ms |
| 点击缩小 | `whileTap={{ scale: 0.97 }}` |
| 箭头弹入 | hover 时箭头 `x: [10, 0, 2, 0]` spring 序列，用 `transition: { type: "spring", stiffness: 300 }` |
| 进度条 | 保持入场展开，加一个 `transition-delay: 200ms` 跟随卡片之后 |

### 6. DailyTask

| 变更 | 实现 |
|------|------|
| hover 背景位移 | `hover:bg-gradient-to-r hover:from-primary/15 hover:to-cyan-500/15`，transition background 300ms |
| 按钮箭头抖动 | hover 时箭头做 `x: [0, 3, -3, 0]` 小幅度 wiggle |
| Sparkle 旋转 | 复用 WelcomeBanner 的旋转脉冲逻辑 |

### 7. RecentActivity

| 变更 | 实现 |
|------|------|
| 入场方向 | 从**右侧 20px** 滑入（`initial={{ opacity: 0, x: 20 }}`），保留 stagger |
| 类型色条 | hover 时左侧出现 `w-0.5` 彩色竖线：课程=blue-400，练习=emerald-400，项目=violet-400。用 `transition-all` + `opacity` 实现 |
| 结果图标弹跳 | SUCCESS/FAIL 图标 `whileInView` spring bounce |
| 空状态 | 整体卡片 `animate={{ rotate: [-0.5, 0.5, -0.5] }}` 慢速微摆，transition 4s infinite ease-in-out |

---

## 全局编排

### 瀑布流入场节奏

当前各组件 `initial/animate` 独立触发。改为统一的 delay 链：

```
WelcomeBanner        delay: 0ms
ContinueLearning     delay: 100ms
ProgressCard ×3      delay: 200ms, 250ms, 300ms
StatsGrid            delay: 350ms (stagger 内部再 50ms/项)
CourseCard ×n        delay: 400ms + idx * 80ms
DailyTask (右侧栏)   delay: 150ms
RecentActivity       delay: 250ms
```

### 骨架屏 Shimmer

ContinueLearning、RecentActivity、CourseCard 列表的 loading 骨架统一替换为 shimmer

### 页面过渡

Layout 增加 `AnimatePresence`，页面切换淡入淡出: `initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}`，duration 200ms。

---

## 实施顺序

1. **基础设施** — `useCountUp` hook、shimmer keyframe、ripple pattern
2. **欢迎横幅 + 继续学习** — 最先看到
3. **进度卡片 + 统计网格** — 核心数据
4. **课程卡片** — 列表区
5. **右侧栏（每日任务 + 动态）** — 辅区
6. **全局编排** — 瀑布流 rhythm + 骨架屏 + 页面过渡

---

## 技术约束

- 所有动画使用 CSS transform/opacity，避免 layout thrashing
- `will-change` 仅用于 WelcomeBanner 光斑和 CourseCard hover（限制数量）
- framer-motion 版本保持 `^11.2.0`，不升级
- `useCountUp` 内部用浏览器 `requestAnimationFrame`，不引入新依赖
