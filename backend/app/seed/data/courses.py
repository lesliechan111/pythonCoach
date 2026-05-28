"""
种子数据 - 50 节完整 Python 从入门到精通课程

课程结构:
- Module 1 (1-5): 入门基础
- Module 2 (6-10): 流程控制
- Module 3 (11-15): 数据结构
- Module 4 (16-20): 函数与文件
- Module 5 (21-25): 错误处理与调试
- Module 6 (26-30): 高级数据结构
- Module 7 (31-35): 文件与数据处理
- Module 8 (36-40): 面向对象编程
- Module 9 (41-45): 函数进阶与工程化
- Module 10 (46-50): 实战技能
"""

COURSE = {
    "title": "Python 零基础入门",
    "description": "从零开始系统学习 Python，无需任何编程基础。20 节课涵盖变量、条件、循环、列表、字典、函数、文件读写等核心知识，打好扎实的编程基础。",
    "category": "python_basic",
    "level": "beginner",
    "order_index": 1,
    "estimated_minutes": 600,
}

COURSE_2 = {
    "title": "Python 项目实战进阶",
    "description": "30 节进阶课程，深入学习错误处理、高级数据结构、文件数据处理、面向对象编程、装饰器、API 调用、数据库操作等实用技能，通过项目实战提升编程能力。要求先完成入门课程。",
    "category": "python_advanced",
    "level": "intermediate",
    "order_index": 2,
    "estimated_minutes": 900,
}

# ============================================================
# Module 1: 入门基础 (Lessons 1-5)
# ============================================================

LESSON_1 = {
    "title": "Python 是什么，能做什么",
    "summary": "了解 Python 这门语言和应用场景，为后续学习建立信心",
    "objectives": [
        "知道 Python 是什么",
        "了解 Python 能做什么",
        "理解什么是编程语言",
        "对 Python 产生兴趣",
    ],
    "content": """## Python 是什么？

Python 是一门**编程语言**。你就把它理解成一种和电脑沟通的工具。

我们用中文和人说话，用英语和外国人说话，用 Python 和电脑说话。

### 为什么叫 Python？

这个名字和蛇没有关系（虽然 Python 的 Logo 是一条蛇）。Python 的创始人 Guido van Rossum 是一个英国喜剧迷，他用自己喜欢的剧名「Monty Python's Flying Circus」给这门语言起了名字。

## Python 能做什么？

Python 的应用非常广泛，下面是几个常见领域：

### 1. 自动化办公

每天要处理 100 个 Excel 文件？Python 几行代码帮你搞定。

```python
# 批量给文件名加上日期前缀
import os
for file in os.listdir("报告"):
    os.rename(f"报告/{file}", f"报告/2026-05-27_{file}")
```

### 2. Web 网站开发

你用的 Instagram、YouTube、豆瓣，背后都有 Python 的身影。

### 3. 数据分析和人工智能

Python 是数据科学和 AI 领域最流行的语言。

### 4. 爬虫

自动从网页上收集信息、下载图片和视频。

### 5. 游戏开发

虽然不常见，但 Python 也能做小游戏。

## 为什么学 Python？

- **语法简单**：像写英文一样写代码
- **上手快**：几小时就能写出第一个有用程序
- **就业广**：几乎每个行业都能用到 Python
""",
    "analogy": "Python 就像是一把瑞士军刀：小、轻、功能多。虽然不如大菜刀（C/C++）锋利，但日常使用绰绰有余。",
    "example_code": '''print("Hello, Python!")
print("这是我的第一行 Python 代码")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "print() 是 Python 的输出命令，双引号里写要显示的文字"},
        {"line": 2, "explanation": "第二行 print 会输出另一句话"},
    ],
    "common_errors": [
        {"error": "print(Hello)", "explanation": "文字内容要加引号，正确写法：print('Hello')"},
        {"error": "print（'Hello'）", "explanation": "括号要用英文输入法打，中文括号不识别"},
        {"error": "pritn('Hello')", "explanation": "单词拼写错误，是 print 不是 pritn"},
    ],
    "order_index": 1,
    "estimated_minutes": 15,
}

LESSON_2 = {
    "title": "安装环境与运行第一个程序",
    "summary": "安装 Python 环境，写出并运行你的第一个 Python 程序",
    "objectives": [
        "安装 Python 到电脑",
        "认识代码编辑工具",
        "写出第一个 Python 程序",
        "学会运行 Python 代码",
    ],
    "content": """## 安装 Python

### Windows 用户

1. 打开 Python 官网 https://python.org
2. 点击黄色的 Download 按钮
3. 双击运行下载的文件
4. **重要**：勾选「Add Python to PATH」再点 Install
5. 安装完成后，打开「命令提示符」，输入 `python --version`，看到版本号说明成功了

### Mac 用户

Mac 已经自带了 Python，但版本可能比较老。

1. 打开终端
2. 输入 `python3 --version` 看看有没有
3. 建议去官网下载最新版 Python 安装

## 在哪里写代码？

Python 代码就是普通的文字文件，后缀名是 `.py`。

推荐使用的编辑工具：

| 工具 | 适合谁 | 特点 |
|------|--------|------|
| IDLE | 纯新手 | Python 自带的编辑器，简单但够用 |
| VS Code | 大部分人 | 免费好用，安装 Python 插件即可 |
| PyCharm | 专业开发者 | 功能强大但有点重 |

对于本课程的学习，**推荐使用 VS Code**。

## 第一个程序

打开 VS Code，新建一个文件叫做 `hello.py`，输入：

```python
print("Hello, World!")
```

保存文件，然后在终端里运行：

```bash
python hello.py
```

或者（Mac）：

```bash
python3 hello.py
```

你会看到：

```
Hello, World!
```

🎉 恭喜！你已经成功运行了第一个 Python 程序！

你现在是一个程序员了 ✨
""",
    "analogy": "安装 Python 就像给你的电脑装了一个翻译官，以后你用 Python 写的话，翻译官就帮你翻译成电脑能懂的语言。",
    "example_code": '''print("Hello, World!")
print("我会写 Python 了！")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "print() 把括号里的内容显示到屏幕上"},
        {"line": 2, "explanation": "第二行 print 显示另一句话"},
    ],
    "common_errors": [
        {"error": "python 不是内部或外部命令", "explanation": "安装时没勾选 Add Python to PATH，需要重新安装或者手动配置环境变量"},
        {"error": "SyntaxError: invalid syntax", "explanation": "语法错误，检查是不是用了中文标点符号"},
        {"error": "ModuleNotFoundError", "explanation": "没找到模块，检查文件名是否正确"},
    ],
    "order_index": 2,
    "estimated_minutes": 20,
}

LESSON_3 = {
    "title": "变量与数据类型",
    "summary": "理解变量的概念，认识 Python 的四种基本数据类型",
    "objectives": [
        "理解什么是变量",
        "学会创建变量和赋值",
        "认识数字、字符串、布尔值三种类型",
        "能用 print() 输出变量",
    ],
    "content": """## 什么是变量？

变量，就是一个**贴了标签的盒子**，你可以往里面放东西，也可以随时换里面的东西。

```python
name = "小明"      # 把 "小明" 放进叫 name 的盒子
age = 18           # 把 18 放进叫 age 的盒子
score = 95.5       # 把 95.5 放进叫 score 的盒子
```

等号 `=` 在这里不是"等于"，而是**赋值**——把右边的值装进左边的变量里。

## 三种基本数据类型

Python 会自动识别你放进去的是什么类型：

| 类型 | 名称 | 例子 | 说明 |
|------|------|------|------|
| `int` | 整数 | `18`, `0`, `-5` | 没有小数点的数字 |
| `float` | 浮点数 | `95.5`, `3.14`, `-0.5` | 有小数点的数字 |
| `str` | 字符串 | `"小明"`, `'Hello'` | 文字内容，要加引号 |
| `bool` | 布尔值 | `True`, `False` | 只有对/错两种可能 |

## 变量命名规则

1. 只能用字母、数字、下划线
2. 不能以数字开头
3. 不能是 Python 的关键字（如 `if`、`for`、`print`）
4. 区分大小写（`name` 和 `Name` 是两个不同变量）

```python
# ✅ 合法
user_name = "张三"
score1 = 90
_max = 100

# ❌ 非法
1st_place = "冠军"    # 不能数字开头
my-name = "李四"      # 不能有减号
if = 100              # if 是关键字
```
""",
    "analogy": "变量就像一个快递柜的格子。格子的编号就是变量名，里面放的快递就是变量的值。你可以随时取件（读取变量），也可以放新的快递进去（重新赋值）。不同类型的值就像不同类型的快递：文件（字符串）、包裹（数字）、信封（布尔值）。",
    "example_code": '''name = "小明"
age = 18
is_student = True

print("姓名:", name)
print("年龄:", age)
print("是否是学生:", is_student)
print("明年年龄:", age + 1)''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "创建字符串变量 name，值为 '小明'"},
        {"line": 2, "explanation": "创建整数变量 age，值为 18"},
        {"line": 3, "explanation": "创建布尔变量 is_student，值为 True（注意首字母大写）"},
        {"line": 5, "explanation": "print 可以接收多个参数，用逗号隔开"},
        {"line": 8, "explanation": "可以对变量做运算，age + 1 会得到 19"},
    ],
    "common_errors": [
        {"error": "print(name) → NameError: name 'name' is not defined", "explanation": "变量还没创建就使用，就像还没放快递就去取件"},
        {"error": "name = 小明 → SyntaxError", "explanation": "字符串要加引号，写成 name = '小明'"},
        {"error": "age + '1' → TypeError", "explanation": "不同类型不能直接运算，'1' 是字符串不是数字"},
    ],
    "order_index": 3,
    "estimated_minutes": 25,
}

LESSON_4 = {
    "title": "字符串操作",
    "summary": "掌握字符串的拼接、格式化、常用方法",
    "objectives": [
        "学会字符串拼接和重复",
        "掌握 f-string 格式化",
        "会用 len()、upper()、lower() 等方法",
        "理解索引和切片的基本概念",
    ],
    "content": """## 字符串基础

字符串就是一段文字，用单引号或双引号括起来：

```python
name = '小明'
greeting = "你好"
```

## 字符串拼接

用 `+` 可以把字符串连起来：

```python
first_name = "张"
last_name = "三"
full_name = first_name + last_name  # "张三"

# 加个空格
full_name = first_name + " " + last_name  # "张 三"
```

用 `*` 可以重复字符串：

```python
line = "-" * 20  # "--------------------"
print("哈" * 5)   # "哈哈哈哈哈哈"
```

## f-string 格式化（重点！）

这是最常用的字符串格式化方式：

```python
name = "小明"
age = 18
print(f"我叫{name}，今年{age}岁")  # 我叫小明，今年18岁
print(f"明年我就{age + 1}岁了")   # 明年我就19岁了
```

注意：引号前面要加 `f`，变量用 `{}` 包起来。`{}` 里可以放任何表达式！

## 常用字符串方法

```python
text = "  Hello Python  "

print(len(text))         # 17 — 求长度（包含空格）
print(text.upper())      # "  HELLO PYTHON  " — 全大写
print(text.lower())      # "  hello python  " — 全小写
print(text.strip())      # "Hello Python" — 去掉两头空格
print(text.replace("Hello", "Hi"))  # "  Hi Python  " — 替换文字
```

## 字符串索引

每个字符都有一个编号，从 0 开始：

```
 H  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1  (负数从右往左数)
```

```python
word = "Hello"
print(word[0])   # H — 第一个字符
print(word[-1])  # o — 最后一个字符
print(word[0:3]) # Hel — 取第 0 到第 2 个（不包含第 3 个）
```
""",
    "analogy": "字符串就像一串糖葫芦。每个字符是一颗山楂，串在一起形成完整的一串。索引就是从左边（或右边）数第几颗山楂。切片就是咬下中间的几颗。",
    "example_code": '''name = "小明"
age = 18

# f-string 格式化
intro = f"我叫{name}，今年{age}岁"
print(intro)

# 字符串方法
msg = "  hello  "
print("原始长度:", len(msg))
print("去空格后:", msg.strip())
print("全大写:", msg.upper())''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "定义字符串变量 name"},
        {"line": 2, "explanation": "定义整数变量 age"},
        {"line": 5, "explanation": "f-string：花括号里的变量会被替换成实际值"},
        {"line": 9, "explanation": "len() 计算字符串长度（包含空格）"},
        {"line": 10, "explanation": "strip() 去掉首尾空白字符"},
        {"line": 11, "explanation": "upper() 把字母全部变成大写"},
    ],
    "common_errors": [
        {"error": "name + age → TypeError", "explanation": "字符串和数字不能直接拼接。用 f-string: f'{name}{age}'"},
        {"error": "word[10] → IndexError", "explanation": "索引超出字符串长度，要确保索引 < len(word)"},
        {"error": "'小明's' → SyntaxError", "explanation": "英文单引号被误当作字符串结束，改用双引号包: \"小明's\""},
    ],
    "order_index": 4,
    "estimated_minutes": 25,
}

LESSON_5 = {
    "title": "数字与运算符",
    "summary": "学会 Python 中的数学运算和常用运算符",
    "objectives": [
        "掌握基本算术运算符",
        "理解整除、取余、幂运算",
        "学会使用复合赋值运算符",
        "了解运算优先级",
    ],
    "content": """## 基本算术运算符

| 运算符 | 含义 | 例子 | 结果 |
|--------|------|------|------|
| `+` | 加 | `5 + 3` | `8` |
| `-` | 减 | `5 - 3` | `2` |
| `*` | 乘 | `5 * 3` | `15` |
| `/` | 除（浮点） | `5 / 2` | `2.5` |
| `//` | 整除 | `5 // 2` | `2` |
| `%` | 取余（模） | `5 % 2` | `1` |
| `**` | 幂 | `5 ** 2` | `25` |

## 几个容易混淆的

```python
# / 和 // 的区别
print(5 / 2)   # 2.5 — 普通除法，结果是浮点数
print(5 // 2)  # 2 — 整除，只要整数部分（向下取整）

# % 取余数（非常实用！）
print(10 % 3)  # 1 — 10 除以 3 余 1
print(15 % 5)  # 0 — 能整除余数就是 0

# 判断奇数偶数
print(7 % 2)   # 1 → 奇数
print(8 % 2)   # 0 → 偶数
```

## 复合赋值运算符

就是"先算再赋值"的简写：

```python
x = 10
x += 5   # 等价于 x = x + 5，现在 x 是 15
x -= 3   # 等价于 x = x - 3，现在 x 是 12
x *= 2   # 等价于 x = x * 2，现在 x 是 24
x /= 4   # 等价于 x = x / 4，现在 x 是 6.0
```

## 运算优先级

从高到低：

1. `()` 括号
2. `**` 幂
3. `*` `/` `//` `%` 乘除
4. `+` `-` 加减

```python
print(2 + 3 * 4)     # 14（先乘后加）
print((2 + 3) * 4)   # 20（括号优先）
print(2 ** 3 * 2)    # 16（幂优先：8×2）
```

**小技巧：记不清优先级就加括号，代码更清晰。**
""",
    "analogy": "运算符就像厨房里的工具：+ 是菜刀切段、- 是削皮去掉、* 是复制多份、/ 是平分给几个人。// 整除就像分糖果——5 颗糖分给 2 个人，每人 2 颗，剩 1 颗（余数 %）。",
    "example_code": '''# 基本运算
a = 15
b = 4

print(f"{a} + {b} = {a + b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# 判断奇偶数
num = 17
parity = "偶数" if num % 2 == 0 else "奇数"
print(f"{num}是{parity}")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "定义整数 a = 15"},
        {"line": 2, "explanation": "定义整数 b = 4"},
        {"line": 5, "explanation": "整除：15 // 4 = 3（因为 4×3=12，余 3，向下取整）"},
        {"line": 6, "explanation": "取余：15 % 4 = 3（15 除以 4 剩 3）"},
        {"line": 7, "explanation": "幂：15 的 4 次方 = 50625"},
        {"line": 10, "explanation": "用取余判奇偶：除以 2 余 0 是偶数，余 1 是奇数"},
    ],
    "common_errors": [
        {"error": "10 / 0 → ZeroDivisionError", "explanation": "不能除以零，数学上也不允许"},
        {"error": "'5' + 3 → TypeError", "explanation": "字符串和数字不能运算，先 int('5') 转成数字"},
        {"error": "2 ** 3 ** 2 → 512 不是 64", "explanation": "幂运算从右往左算：3**2=9，2**9=512。用括号明确 (2**3)**2=64"},
    ],
    "order_index": 5,
    "estimated_minutes": 25,
}

# ============================================================
# Module 2: 流程控制 (Lessons 6-10)
# ============================================================

LESSON_6 = {
    "title": "条件判断 — if 语句",
    "summary": "学会让程序根据条件做出不同的选择",
    "objectives": [
        "理解 if 语句的执行逻辑",
        "掌握 if/elif/else 写法",
        "会用嵌套 if",
        "注意缩进的重要性",
    ],
    "content": """## 为什么需要条件判断？

生活中我们每天都在做判断：

> **如果** 下雨 → 带伞，**否则** → 不带伞
> **如果** 考试及格 → 庆祝，**否则如果** 补考通过 → 勉强过关，**否则** → 重修

Python 用 `if` 来做同样的事。

## if/elif/else 语法

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("需要加油")
# 输出：良好
```

**关键点：**
- `if` 后面跟一个条件，条件后面要加冒号 `:`
- 条件成立就执行下面**缩进**的代码块
- `elif` = "否则如果"，可以有多个
- `else` = "以上都不成立时"，只能有一个，可选
- Python 用缩进（4 个空格）来区分代码块

## 单行 if

简单的情况可以写在一行：

```python
age = 20
if age >= 18: print("成年了")

# 简写形式
status = "成年" if age >= 18 else "未成年"
print(status)  # 成年
```

## 嵌套 if

if 里面还可以放 if：

```python
age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("可以入场")
    else:
        print("请先购票")
else:
    print("未成年人不能入场")
```

## if 判断的"真"与"假"

Python 中有些值被视为"假"：

```python
# 以下都是 False/假
if 0:          # 数字 0
if "":         # 空字符串
if []:         # 空列表
if None:       # None

# 其他值都被看作 True/真
if 1:          # 真
if "hello":    # 非空字符串 → 真
```
""",
    "analogy": "if 语句就像交通信号灯：红灯（条件不成立）就停下，绿灯（条件成立）就通过。elif 就像黄灯——前面红灯不亮、黄灯亮了就走黄灯的规则。else 就是以上灯都不亮时的默认规则。",
    "example_code": '''# 成绩评级系统
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"你的分数是 {score}，等级是 {grade}")

# 简写判断
can_vote = "可以" if score >= 60 else "不可以"
print(f"考试通过？{can_vote}")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "定义分数变量"},
        {"line": 4, "explanation": "第一个判断：score >= 90？85 不小于 90，跳过"},
        {"line": 6, "explanation": "elif 判断：score >= 80？85 >= 80 成立，执行这个分支"},
        {"line": 7, "explanation": "grade 被赋值为 'B'，后面的 elif/else 不再执行"},
        {"line": 13, "explanation": "f-string 输出结果：你的分数是 85，等级是 B"},
        {"line": 16, "explanation": "单行 if/else 简写：条件成立取'可以'，不成立取'不可以'"},
    ],
    "common_errors": [
        {"error": "IndentationError: expected an indented block", "explanation": "if/elif/else 后面要缩进，空 4 个空格"},
        {"error": "if score = 90: → SyntaxError", "explanation": "判断相等要用 == 不是 =。= 是赋值，== 是比相等"},
        {"error": "if score >= 90 → SyntaxError", "explanation": "条件后面要加冒号！if score >= 90:"},
    ],
    "order_index": 6,
    "estimated_minutes": 25,
}

LESSON_7 = {
    "title": "比较运算符与逻辑运算符",
    "summary": "掌握判断条件中的比较和逻辑运算",
    "objectives": [
        "掌握 6 种比较运算符",
        "理解 and/or/not 逻辑运算符",
        "学会组合多个条件",
        "能写复杂的判断条件",
    ],
    "content": """## 比较运算符

比较两个值的关系，结果是 `True` 或 `False`：

| 运算符 | 含义 | 例子 | 结果 |
|--------|------|------|------|
| `==` | 等于 | `5 == 5` | `True` |
| `!=` | 不等于 | `5 != 3` | `True` |
| `>` | 大于 | `5 > 8` | `False` |
| `<` | 小于 | `5 < 8` | `True` |
| `>=` | 大于等于 | `5 >= 5` | `True` |
| `<=` | 小于等于 | `5 <= 3` | `False` |

**特别注意：** `==` 是判相等，`=` 是赋值，两个完全不同！

## 逻辑运算符

用来组合多个条件：

| 运算符 | 含义 | 例子 | 结果 |
|--------|------|------|------|
| `and` | 并且（都真才真） | `5>3 and 2<4` | `True` |
| `or` | 或者（一真就真） | `5<3 or 2<4` | `True` |
| `not` | 取反 | `not 5>3` | `False` |

```python
age = 22
has_id = True

# and：两个条件都要满足
if age >= 18 and has_id:
    print("可以买酒")  # ✅ 年龄够且有身份证

# or：满足一个就行
if age < 12 or age > 60:
    print("可以半价")  # ❌ 两个条件都不满足

# not：条件取反
is_weekend = False
if not is_weekend:
    print("今天是工作日")  # ✅ 不是周末就是工作日
```

## 组合多个条件

```python
# 判断一个年份是不是闰年
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
# 2024 是闰年
```

看不懂这个闰年条件没关系，重点是学会用括号把子条件包起来，让逻辑更清晰。

## 真值表

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |
""",
    "analogy": "and 就像公司打卡：必须上午打了 AND 下午打了才算全勤。or 就像小区开门：刷门禁卡 OR 输入密码都能开门。not 就像否定句：'我不饿'就是对'我饿'的否定。",
    "example_code": '''# 会员折扣计算器
age = 25
is_member = True
amount = 200

# 组合条件判断折扣
if age >= 60 or age <= 12:
    discount = 0.5  # 老人儿童半价
elif is_member and amount > 100:
    discount = 0.8  # 会员满100打8折
elif is_member:
    discount = 0.9  # 会员打9折
else:
    discount = 1.0  # 不打折

print(f"原价：{amount}元")
print(f"折扣：{discount}")
print(f"实付：{amount * discount}元")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "定义三个变量：年龄、是否会员、消费金额"},
        {"line": 6, "explanation": "or 条件：60 岁以上或 12 岁以下，满足一个就半价"},
        {"line": 8, "explanation": "and 条件：是会员且消费超 100，两个都满足才 8 折"},
        {"line": 10, "explanation": "elif：是会员但消费不超过 100，打 9 折"},
        {"line": 12, "explanation": "以上条件都不满足，不打折"},
        {"line": 16, "explanation": "最后的实付金额 = 原价 × 折扣"},
    ],
    "common_errors": [
        {"error": "if age = 18 → SyntaxError", "explanation": "判断相等用 ==，不要和赋值 = 搞混"},
        {"error": "if age > 18 and < 60 → SyntaxError", "explanation": "and 两边都要完整：if age > 18 and age < 60"},
        {"error": "if not age > 18 → 优先级混淆", "explanation": "not 优先级很高，not age > 18 等于 (not age) > 18，应写作 not (age > 18)"},
    ],
    "order_index": 7,
    "estimated_minutes": 20,
}

LESSON_8 = {
    "title": "while 循环",
    "summary": "学会用 while 让程序重复执行一段代码",
    "objectives": [
        "理解循环的作用",
        "掌握 while 循环写法",
        "学会用 break 退出循环",
        "避免死循环",
    ],
    "content": """## 为什么需要循环？

重复的事情不应该手动做。比如：

- 抄 100 遍课文 → 用循环
- 遍历一个班级的学生名单 → 用循环
- 一直询问直到用户输入正确的密码 → 用循环

## while 循环

**只要条件成立，就一直重复执行：**

```python
count = 1
while count <= 5:
    print(f"这是第 {count} 次")
    count += 1

# 这是第 1 次
# 这是第 2 次
# 这是第 3 次
# 这是第 4 次
# 这是第 5 次
```

**执行过程：**
1. 判断 `count <= 5` 是否成立
2. 成立 → 执行缩进里的代码
3. 回到第 1 步
4. 不成立 → 跳出循环

## break — 提前退出

用 `break` 可以随时跳出循环：

```python
password = ""
while True:   # True 永远成立
    password = input("请输入密码：")
    if password == "123456":
        print("密码正确！")
        break   # 密码对了就跳出
    else:
        print("密码错误，请重试")
```

## continue — 跳过本轮

用 `continue` 跳过本轮循环的剩余部分，直接开始下一轮：

```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # 偶数就不打印，跳回 while 判断
    print(num)
# 只输出：1 3 5 7 9
```

## 死循环 ⚠️

如果条件永远不会变成 False，程序就停不下来：

```python
# ❌ 死循环 — count 永远不会变
count = 1
while count <= 5:
    print("停不下来了……")

# ✅ 正确写法 — count 每次 +1
count = 1
while count <= 5:
    print("很快就结束")
    count += 1
```

**死循环的急救方法：** 在终端按 `Ctrl + C` 强制停止程序。
""",
    "analogy": "while 循环就像自动洗衣机：只要还有衣服没洗完（条件成立），就继续转。洗完了（条件不成立），就停下来。break 就像紧急停止按钮，不管洗没洗完，按了就停。continue 就像跳过漂洗直接脱水——跳过本轮剩下的步骤。",
    "example_code": '''# 猜数字游戏（简化版）
import random

target = random.randint(1, 100)
guess = 0
attempts = 0

print("我想了一个 1-100 之间的数字，来猜猜看！")

while guess != target:
    guess = int(input("你猜是多少："))
    attempts += 1
    
    if guess > target:
        print("大了，再小一点")
    elif guess < target:
        print("小了，再大一点")
    else:
        print(f"猜对了！你用了 {attempts} 次")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "导入 random 模块用来生成随机数"},
        {"line": 4, "explanation": "生成 1-100 的随机数作为目标"},
        {"line": 5, "explanation": "guess 初始值 0，确保第一次能进入循环"},
        {"line": 9, "explanation": "while 条件：只要没猜对就一直循环"},
        {"line": 10, "explanation": "input() 获取用户输入，int() 转成整数"},
        {"line": 11, "explanation": "尝试次数 +1"},
        {"line": 13, "explanation": "如果猜大了给出提示，继续下一轮循环"},
        {"line": 17, "explanation": "猜对了，break 隐式发生（条件变 False），循环结束"},
    ],
    "common_errors": [
        {"error": "死循环", "explanation": "没改变循环条件中的变量。确保循环体内有条件变量在变化"},
        {"error": "while guess = target: → SyntaxError", "explanation": "比较用 == 不是 ="},
        {"error": "input() → TypeError: '<' not supported", "explanation": "input() 返回字符串，和数字比较前要 int() 转换"},
    ],
    "order_index": 8,
    "estimated_minutes": 25,
}

LESSON_9 = {
    "title": "for 循环与 range()",
    "summary": "学会用 for 循环遍历序列和 range 生成数列",
    "objectives": [
        "理解 for 循环的用途",
        "掌握 for 循环基本语法",
        "会用 range() 生成数列",
        "区分 for 和 while 的使用场景",
    ],
    "content": """## for 循环

`for` 适合**已知循环次数**或**遍历一个序列**的情况：

```python
fruits = ["苹果", "香蕉", "橘子"]

for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 我喜欢吃苹果
# 我喜欢吃香蕉
# 我喜欢吃橘子
```

`for 变量 in 序列`：把序列里的每个元素依次赋给变量，执行一次循环体。

## 遍历字符串

```python
name = "Python"

for char in name:
    print(char)
# P
# y
# t
# h
# o
# n
```

## range() — 生成数字序列

`range()` 是最常用的循环搭档：

```python
# range(n)：0 到 n-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

# range(start, stop)：start 到 stop-1
for i in range(2, 6):
    print(i, end=" ")  # 2 3 4 5

# range(start, stop, step)：带步长
for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9

# 倒着数
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
```

## for vs while — 怎么选？

| 场景 | 用哪个 |
|------|--------|
| 循环固定次数 | `for i in range(n)` |
| 遍历列表/字符串 | `for item in 序列` |
| 不知道要循环几次 | `while 条件` |
| 等待用户正确输入 | `while True + break` |

## 实战：打印九九乘法表

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行
```
""",
    "analogy": "for 循环就像排队点名：老师拿著名单（列表），按顺序一个个点名（遍历）。每个被点到的人做同样的事（循环体）。range() 就是自动生成名单：range(1,6) 生成 [1,2,3,4,5] 这个名单。",
    "example_code": '''# 计算 1 到 100 的和
total = 0

for num in range(1, 101):
    total += num

print(f"1+2+...+100 = {total}")

# 九九乘法表（部分）
print("\n乘法表 1-3：\n")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="  ")
    print()''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "初始化累加变量 total = 0"},
        {"line": 4, "explanation": "range(1, 101) 生成 1 到 100 的整数序列"},
        {"line": 5, "explanation": "每次循环把 num 加到 total 上"},
        {"line": 7, "explanation": "输出结果：5050"},
        {"line": 11, "explanation": "外层 for 控制行数（1-3）"},
        {"line": 12, "explanation": "内层 for 控制每行打印几个（第 i 行打印 i 个）"},
        {"line": 13, "explanation": "end='  ' 让打印不换行，用空格隔开"},
        {"line": 14, "explanation": "空 print() 在每行结束后换行"},
    ],
    "common_errors": [
        {"error": "for i in 100: → TypeError", "explanation": "整数不能遍历，用 range：for i in range(100)"},
        {"error": "for i in range(5): 修改 i 无效", "explanation": "for 中修改循环变量 i 不会影响下一次迭代，每次循环 i 都会被重新赋值"},
        {"error": "range(10, 1) → 空", "explanation": "step 默认为 1，从 10 到 1 走不通，需要 range(10, 0, -1)"},
    ],
    "order_index": 9,
    "estimated_minutes": 25,
}

LESSON_10 = {
    "title": "循环进阶 — break/continue 与嵌套循环",
    "summary": "深入学习 break/continue 的使用以及嵌套循环",
    "objectives": [
        "掌握 break 跳出多层循环的技巧",
        "理解 continue 跳过本轮循环",
        "学会嵌套循环的实际应用",
        "能编写带循环的小程序",
    ],
    "content": """## break — 跳出循环

`break` 只能跳出**最内层**的一层循环：

```python
# 找到第一个能被 7 整除的数就停
for num in range(1, 50):
    if num % 7 == 0:
        print(f"找到了：{num}")
        break
# 输出：找到了：7
```

## continue — 跳过本轮

```python
# 只打印奇数
for i in range(10):
    if i % 2 == 0:
        continue  # 偶数直接跳过
    print(i, end=" ")  # 1 3 5 7 9
```

## 带 else 的循环

Python 特有的功能：循环正常结束（没被 break 中断）时执行 `else`：

```python
# 判断一个数是不是质数
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} 不是质数")
        break
else:
    print(f"{num} 是质数")
# 输出：17 是质数
```

## 嵌套循环的妙用

```python
# 打印直角三角形
for i in range(1, 6):
    print("*" * i)

# 输出：
# *
# **
# ***
# ****
# *****
```

```python
# 找出所有水仙花数（三位数，各位数字的立方和等于本身）
print("水仙花数：")
for num in range(100, 1000):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    if hundreds**3 + tens**3 + ones**3 == num:
        print(num)

# 153, 370, 371, 407
```

## for 循环 + enumerate()

有时候你需要同时知道**索引**和**值**：

```python
fruits = ["苹果", "香蕉", "橘子"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 0: 苹果
# 1: 香蕉
# 2: 橘子
```
""",
    "analogy": "嵌套循环就像时钟：时针每走一格（外层循环），分针要走完一整圈（内层循环）。break 就像闹钟响了——不管走到哪，马上停。continue 就像跳过广告——这节不看，下一节继续。",
    "example_code": '''# 简易菜单系统
print("===== 点餐系统 =====")
menu = ["汉堡", "薯条", "可乐"]
prices = [15, 8, 5]
total = 0

for i, (item, price) in enumerate(zip(menu, prices)):
    print(f"{i+1}. {item} - ¥{price}")

while True:
    choice = input("请选择编号（输入 q 退出）：")
    if choice == "q":
        break
    if choice in ["1", "2", "3"]:
        idx = int(choice) - 1
        total += prices[idx]
        print(f"已添加 {menu[idx]}，当前合计：¥{total}")
    else:
        print("无效选择，请重新输入")

print(f"点餐结束，总金额：¥{total}")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "定义菜单列表"},
        {"line": 6, "explanation": "enumerate 同时获取索引和值，zip 把两个列表配对"},
        {"line": 9, "explanation": "while True 无限循环，直到用户输入 q"},
        {"line": 12, "explanation": "用户输入 q 时 break 跳出循环"},
        {"line": 13, "explanation": "in 检查输入是否在有效选项列表中"},
        {"line": 15, "explanation": "累加价格到 total"},
        {"line": 20, "explanation": "循环结束后输出最终总价"},
    ],
    "common_errors": [
        {"error": "break 只能跳出最内层循环", "explanation": "嵌套循环中，break 只跳出所在的那一层，外层循环继续执行"},
        {"error": "for 循环中 remove() 导致漏项", "explanation": "遍历列表时不要修改列表，先创建一个副本再操作"},
        {"error": "无限循环忘记 break", "explanation": "while True 一定要有 break 条件，否则程序永远不停止"},
    ],
    "order_index": 10,
    "estimated_minutes": 25,
}

# ============================================================
# Module 3: 数据结构 (Lessons 11-15)
# ============================================================

LESSON_11 = {
    "title": "列表（List）基础",
    "summary": "学会创建、访问和修改列表——最常用的 Python 数据结构",
    "objectives": [
        "理解列表的概念",
        "学会创建和访问列表元素",
        "掌握添加、删除、修改元素",
        "会用 len()、in 等基本操作",
    ],
    "content": """## 什么是列表？

列表就是一个**有顺序的容器**，里面可以放各种东西：

```python
fruits = ["苹果", "香蕉", "橘子"]
scores = [95, 87, 92, 78]
mixed = ["小明", 18, True, 95.5]  # 可以混合类型，但不推荐
empty = []  # 空列表
```

## 访问元素（索引）

和字符串一样，从 0 开始编号：

```python
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]

print(fruits[0])    # 苹果
print(fruits[2])    # 橘子
print(fruits[-1])   # 西瓜（最后一个）
print(fruits[1:3])  # ['香蕉', '橘子']（切片，不包含索引 3）
```

## 修改元素

列表是**可变**的，可以改里面的内容：

```python
fruits = ["苹果", "香蕉", "橘子"]
fruits[1] = "草莓"       # ['苹果', '草莓', '橘子']
```

## 添加元素

```python
fruits = ["苹果", "香蕉"]

fruits.append("橘子")       # 加到最后：['苹果', '香蕉', '橘子']
fruits.insert(1, "草莓")   # 插到索引 1：['苹果', '草莓', '香蕉', '橘子']
```

## 删除元素

```python
fruits = ["苹果", "香蕉", "橘子", "香蕉"]

fruits.remove("香蕉")      # 删第一个匹配的：['苹果', '橘子', '香蕉']
removed = fruits.pop()     # 删除并返回最后一个：'香蕉', fruits → ['苹果', '橘子']
removed2 = fruits.pop(0)   # 删除索引 0：'苹果', fruits → ['橘子']
del fruits[0]              # 直接删除索引 0
fruits.clear()             # 清空整个列表
```

## 常用操作

```python
nums = [3, 1, 4, 1, 5]

print(len(nums))       # 5 — 列表长度
print(3 in nums)       # True — 判断是否存在
print(9 in nums)       # False
print(nums.count(1))   # 2 — 统计出现次数
print(nums.index(4))   # 2 — 查找元素位置
```
""",
    "analogy": "列表就像一排有编号的储物柜。每个柜子有门牌号（索引从 0 开始），里面可以放任意东西。你可以打开任意柜子看里面有什么（访问），换掉里面的东西（修改），加一个新的柜子（append），或者清空某个柜子（remove）。",
    "example_code": '''# 购物车模拟
cart = []

# 添加商品
cart.append("奶茶")
cart.append("蛋糕")
cart.append("冰淇淋")
print(f"购物车：{cart}")

# 查看数量
print(f"共 {len(cart)} 件商品")

# 删除商品
cart.remove("蛋糕")
print(f"删除蛋糕后：{cart}")

# 遍历购物车
print("\n您的购物清单：")
for i, item in enumerate(cart, 1):
    print(f"  {i}. {item}")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "创建空列表 cart"},
        {"line": 5, "explanation": "append() 依次添加 3 件商品"},
        {"line": 10, "explanation": "len() 获取列表长度：3 件"},
        {"line": 13, "explanation": "remove() 删除匹配的第一个元素"},
        {"line": 17, "explanation": "enumerate(cart, 1) 从 1 开始编号，而不是默认的 0"},
    ],
    "common_errors": [
        {"error": "fruits[5] → IndexError: list index out of range", "explanation": "索引超出范围，可用 len(fruits)-1 获取最大索引"},
        {"error": "fruits.remove('西瓜') → ValueError", "explanation": "删除不存在的元素会报错，先判断 if '西瓜' in fruits"},
        {"error": "cart = cart.append('a') → cart 变成 None", "explanation": "append() 直接修改原列表，不返回值，不要赋值"},
    ],
    "order_index": 11,
    "estimated_minutes": 25,
}

LESSON_12 = {
    "title": "列表的排序、遍历与推导式",
    "summary": "掌握列表的排序、遍历技巧和列表推导式",
    "objectives": [
        "学会 sort() 和 sorted() 排序",
        "掌握多种列表遍历方式",
        "理解列表推导式",
        "学会用 zip() 同时遍历多个列表",
    ],
    "content": """## 排序

```python
nums = [3, 1, 4, 1, 5, 9, 2]

# sort() — 原地排序，修改原列表
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)
print(nums)  # [9, 5, 4, 3, 2, 1, 1]

# sorted() — 返回新列表，不修改原列表
original = [3, 1, 4, 1, 5]
new = sorted(original)
print(original)  # [3, 1, 4, 1, 5] — 没变
print(new)       # [1, 1, 3, 4, 5] — 新列表
```

## 列表翻转

```python
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)  # [5, 4, 3, 2, 1]
```

## 常用内置函数

```python
nums = [3, 1, 4, 1, 5]

print(max(nums))  # 5 — 最大值
print(min(nums))  # 1 — 最小值
print(sum(nums))  # 14 — 总和
```

## zip() — 同时遍历多个列表

```python
names = ["小明", "小红", "小刚"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(f"{name} 的成绩是 {score} 分")
```

## 列表推导式（重要！）

一行代码生成新列表：

```python
# 传统写法
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
# [1, 4, 9, 16, 25]

# 列表推导式 — 一行搞定
squares = [i ** 2 for i in range(1, 6)]

# 带条件
evens = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]

# 处理字符串
names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]  # ['ALICE', 'BOB', 'CHARLIE']
```

**语法：** `[表达式 for 变量 in 序列 if 条件]`
""",
    "analogy": "列表推导式就像生产线上的机器：原材料（旧列表）进来，经过处理（表达式），如果合格（if 条件），就打包成新产品（新列表）。一行代码就完成了传统写法 3 行的工作。",
    "example_code": '''# 学生成绩分析
scores = [78, 92, 85, 66, 95, 73, 88]

# 排序
scores_sorted = sorted(scores, reverse=True)
print(f"成绩从高到低：{scores_sorted}")

# 统计
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"平均分：{sum(scores) / len(scores):.1f}")

# 列表推导式：找出所有及格分数
passing = [s for s in scores if s >= 60]
print(f"及格人数：{len(passing)}，及格率：{len(passing) / len(scores) * 100:.0f}%")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "原始成绩列表"},
        {"line": 5, "explanation": "sorted() 返回新列表，reverse=True 从高到低"},
        {"line": 9, "explanation": "max()、min()、sum() 是内置统计函数"},
        {"line": 11, "explanation": ":.1f 格式化保留一位小数"},
        {"line": 14, "explanation": "列表推导式：[表达式 for 变量 in 列表 if 条件]"},
        {"line": 15, "explanation": "len() 统计数量，计算及格率"},
    ],
    "common_errors": [
        {"error": "nums = nums.sort() → None", "explanation": "sort() 返回 None，直接调用 nums.sort() 就好，不要赋值"},
        {"error": "max([]) → ValueError", "explanation": "空列表无法取最大/最小值，先检查 if nums:"},
        {"error": "zip 长度不一致时停止在最短的列表", "explanation": "zip 以最短列表为准，多余的元素会被忽略"},
    ],
    "order_index": 12,
    "estimated_minutes": 25,
}

LESSON_13 = {
    "title": "元组（Tuple）",
    "summary": "理解元组的概念——不可变的列表，以及它的使用场景",
    "objectives": [
        "理解元组和列表的区别",
        "学会创建和访问元组",
        "掌握元组解包",
        "了解元组的使用场景",
    ],
    "content": """## 什么是元组？

元组就是**不能修改**的列表。用小括号 `()` 定义：

```python
point = (3, 5)           # 坐标，不需要改
colors = ("红", "绿", "蓝")  # 三原色，固定的
empty = ()               # 空元组
single = (42,)           # 单元素元组，注意逗号！
```

## 和列表的对比

| 特性 | 列表 | 元组 |
|------|------|------|
| 符号 | `[]` | `()` |
| 可修改 | ✅ 可以 | ❌ 不可以 |
| 可添加删除 | ✅ | ❌ |
| 速度 | 稍慢 | 稍快 |
| 用作字典 key | ❌ | ✅ |

## 什么时候用元组？

- **不需要修改的数据**：坐标、RGB 颜色、日期
- **函数的多个返回值**：后面函数章节会讲到
- **不希望被意外修改**的数据

```python
# 用元组定义不变的数据
WEEKDAYS = ("周一", "周二", "周三", "周四", "周五")
MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# 如果尝试修改
# WEEKDAYS[0] = "星期天"  ❌ TypeError!
```

## 元组解包（非常实用！）

```python
# 一行赋值多个变量
x, y = (3, 5)
print(x)  # 3
print(y)  # 5

# 交换变量，不需要临时变量！
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# 函数返回多个值本质也是元组
def get_user():
    return "小明", 18  # 实际返回 ("小明", 18)

name, age = get_user()
```

## 元组的其他操作

虽然不能修改，但可以访问、切片、遍历：

```python
t = (1, 2, 3, 4, 5)

print(t[0])       # 1
print(t[1:4])     # (2, 3, 4)
print(len(t))     # 5
print(3 in t)     # True

for item in t:
    print(item)
```
""",
    "analogy": "列表就像白板，可以随时擦掉重写。元组就像刻在石头上的字，刻好了就不能改。如果你有一些数据不希望被意外修改（比如一周七天、一年十二个月），用元组更安全。",
    "example_code": '''# 元组解包实用示例

# 1. 交换变量（一行搞定）
a = 10
b = 20
a, b = b, a
print(f"交换后: a={a}, b={b}")  # a=20, b=10

# 2. 同时解包
point = (300, 200)
x, y = point
print(f"坐标: ({x}, {y})")

# 3. 元组作为不可变数据
COLORS = ("红", "绿", "蓝")
for idx, color in enumerate(COLORS, 1):
    print(f"第{idx}种颜色: {color}")''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "a, b = b, a 是 Python 特有的交换技巧，本质是元组解包"},
        {"line": 10, "explanation": "把元组 (300, 200) 解包给 x 和 y"},
        {"line": 14, "explanation": "用大写命名表示这是常量（约定俗成，不强制）"},
        {"line": 15, "explanation": "遍历元组和遍历列表完全一样"},
    ],
    "common_errors": [
        {"error": "single = (42) → 这是整数不是元组", "explanation": "单元素元组要加逗号：single = (42,)"},
        {"error": "t[0] = 1 → TypeError: 'tuple' object does not support item assignment", "explanation": "元组不可修改，需要修改就改用列表"},
        {"error": "a, b = (1, 2, 3) → ValueError", "explanation": "解包时左右数量要一致，左边 2 个变量右边 3 个值对不上"},
    ],
    "order_index": 13,
    "estimated_minutes": 20,
}

LESSON_14 = {
    "title": "字典（Dict）基础",
    "summary": "学会创建和使用字典——Python 的键值对数据结构",
    "objectives": [
        "理解字典的键值对概念",
        "学会创建、访问、修改字典",
        "掌握字典的增删改查",
        "了解字典的常用场景",
    ],
    "content": """## 什么是字典？

字典是一种**键值对**存储结构。就像真正的字典：**词（key）→ 解释（value）**。

```python
# 创建字典
student = {
    "name": "小明",
    "age": 18,
    "score": 95.5,
    "is_passing": True
}
```

## 访问和修改

```python
student = {"name": "小明", "age": 18}

# 通过 key 访问
print(student["name"])    # 小明
print(student["age"])     # 18

# 修改已有 key
student["age"] = 19

# 添加新的 key
student["grade"] = "高三"

# 现在 student 是：
# {"name": "小明", "age": 19, "grade": "高三"}
```

## 使用 get() 安全访问

用 `[]` 访问不存在的 key 会报错，用 `get()` 不会：

```python
student = {"name": "小明", "age": 18}

# 用 []：key 不存在就报错
# print(student["height"])  # KeyError!

# 用 get()：不存在返回 None（或指定默认值）
print(student.get("height"))        # None
print(student.get("height", 170))   # 170（没找到就返回 170）
```

## 增删操作

```python
student = {"name": "小明", "age": 18}

# 删除
del student["age"]           # 删除 age
age = student.pop("age")     # 删除并返回值
student.clear()              # 清空整个字典

# 检查 key 是否存在
if "name" in student:
    print("存在")
```

## 遍历字典

```python
student = {"name": "小明", "age": 18, "grade": "高三"}

# 遍历所有 key
for key in student:
    print(key)  # name, age, grade

# 遍历所有 value
for value in student.values():
    print(value)

# 同时遍历 key 和 value（最常用）
for key, value in student.items():
    print(f"{key}: {value}")
# name: 小明
# age: 18
# grade: 高三
```
""",
    "analogy": "字典就像手机通讯录：每个联系人的名字（key）对应一个电话号码（value）。你可以按名字快速查到号码（访问），改号码（修改），加新联系人（添加），删联系人（删除）。不能两个联系人同名，但可以同号。",
    "example_code": '''# 学生信息管理
students = {
    "001": {"name": "小明", "score": 90},
    "002": {"name": "小红", "score": 85},
    "003": {"name": "小刚", "score": 95},
}

# 查找学生
sid = "002"
if sid in students:
    s = students[sid]
    info_str = "学号 " + sid + ": " + s["name"] + ", 成绩 " + str(s["score"])
    print(info_str)

# 遍历所有学生
print("\n所有学生：")
for sid, info in students.items():
    print("  " + sid + ": " + info["name"] + " - " + str(info["score"]) + "分")

# 统计
avg = sum(s["score"] for s in students.values()) / len(students)
print("\n平均分: " + str(round(avg, 1)))
''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "嵌套字典：学号对应一个包含姓名和成绩的字典"},
        {"line": 10, "explanation": "in 检查 key 是否存在，避免 KeyError"},
        {"line": 12, "explanation": "通过 key 访问内层字典，再通过内层 key 访问具体字段"},
        {"line": 16, "explanation": ".items() 同时遍历 key 和 value"},
        {"line": 20, "explanation": "生成器表达式计算平均分：遍历所有学生的 score 求和 ÷ 人数"},
    ],
    "common_errors": [
        {"error": "student['height'] → KeyError", "explanation": "key 不存在时 [] 会报错，用 get() 替代或先 if 'height' in student"},
        {"error": "{['name']: '小明'} → TypeError", "explanation": "字典的 key 必须是不可变类型（字符串、数字、元组），列表不能做 key"},
    ],
    "order_index": 14,
    "estimated_minutes": 25,
}

LESSON_15 = {
    "title": "字典的常用方法与嵌套结构",
    "summary": "掌握字典的高级用法和嵌套数据结构",
    "objectives": [
        "掌握 keys()、values()、items() 方法",
        "学会合并和复制字典",
        "理解嵌套字典和列表字典组合",
        "能处理 JSON-like 数据结构",
    ],
    "content": """## 字典常用方法

```python
d = {"a": 1, "b": 2, "c": 3}

# 获取所有 key
print(d.keys())    # dict_keys(['a', 'b', 'c'])

# 获取所有 value
print(d.values())  # dict_values([1, 2, 3])

# 获取所有键值对
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])
```

## 合并字典

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "b": 4}  # 注意 b 重复了

# | 运算符合并（Python 3.9+），后面的覆盖前面的
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 4, 'c': 3}

# update() 更新
d1.update(d2)
print(d1)  # {'a': 1, 'b': 4, 'c': 3}
```

## 字典推导式

和列表推导式类似：

```python
# 把列表转成字典：{元素: 长度}
words = ["apple", "banana", "cherry"]
word_len = {w: len(w) for w in words}
print(word_len)  # {'apple': 5, 'banana': 6, 'cherry': 6}

# 过滤
scores = {"小明": 90, "小红": 85, "小刚": 60, "小李": 95}
passing = {k: v for k, v in scores.items() if v >= 60}
```

## 嵌套结构（重点！）

实际开发中常用的复杂结构：

```python
# 列表套字典 — 最常见的数据格式（类似 JSON）
users = [
    {"name": "小明", "age": 18, "hobbies": ["篮球", "编程"]},
    {"name": "小红", "age": 20, "hobbies": ["画画", "读书"]},
    {"name": "小刚", "age": 19, "hobbies": ["足球", "游戏"]},
]

# 访问：第一个用户的第二个爱好
print(users[0]["hobbies"][1])  # 编程

# 遍历：打印所有用户名和年龄
for user in users:
    print(f"{user['name']}, {user['age']}岁")
```

```python
# 字典套字典 — 适合有 key 的场景
school = {
    "一班": {"人数": 45, "班主任": "张老师"},
    "二班": {"人数": 42, "班主任": "李老师"},
}

print(school["一班"]["班主任"])  # 张老师
```
""",
    "analogy": "嵌套字典就像俄罗斯套娃：外层娃娃打开后里面还有一层。`users[0]` 打开第一个用户，`['hobbies']` 找到兴趣列表，`[1]` 取第二个兴趣。一层一层往里找。实际项目中的 JSON 数据基本都是这个结构。",
    "example_code": '''# 图书管理系统
library = [
    {"title": "Python 入门", "author": "张三", "year": 2023, "borrowed": False},
    {"title": "算法导论", "author": "李四", "year": 2020, "borrowed": True},
    {"title": "数据结构", "author": "王五", "year": 2022, "borrowed": False},
]

# 查找所有未借出的书
print("可借阅的图书：")
available = [book for book in library if not book["borrowed"]]
for book in available:
    print(f"  《{book['title']}》— {book['author']} ({book['year']})")

# 统计
print(f"\
总藏书: {len(library)} 本")
print(f"可借: {len(available)} 本")

# 按年份排序
library.sort(key=lambda b: b["year"])
print(f"\
最新藏书: 《{library[-1]['title']}》({library[-1]['year']})")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "列表套字典：每本书是一个字典，所有书组成列表"},
        {"line": 9, "explanation": "列表推导式 + 条件筛选：借出状态为 False 的书"},
        {"line": 14, "explanation": "len() 计数"},
        {"line": 18, "explanation": "sort(key=...) 按指定字段排序，lambda 是一个匿名函数"},
    ],
    "common_errors": [
        {"error": "d['key'] 嵌套很深时容易 KeyError", "explanation": "用 d.get('a', {}).get('b', {}) 链式安全访问"},
        {"error": "遍历字典时修改字典 → RuntimeError", "explanation": "遍历过程中不要增删 key，先收集要修改的 key 再操作"},
    ],
    "order_index": 15,
    "estimated_minutes": 25,
}

# ============================================================
# Module 4: 函数与文件 (Lessons 16-20)
# ============================================================

LESSON_16 = {
    "title": "函数定义与调用",
    "summary": "学会把重复代码封装成函数，提高代码复用性",
    "objectives": [
        "理解函数的作用",
        "学会用 def 定义函数",
        "掌握函数的调用方式",
        "理解封装的意义",
    ],
    "content": """## 为什么需要函数？

看看这段没有函数的代码，很多重复：

```python
# 计算三个人的 BMI
# 小明
height1 = 1.75
weight1 = 70
bmi1 = weight1 / (height1 ** 2)
print(f"小明的 BMI: {bmi1:.1f}")

# 小红 — 重复的代码！
height2 = 1.62
weight2 = 55
bmi2 = weight2 / (height2 ** 2)
print(f"小红的 BMI: {bmi2:.1f}")

# 小刚 — 又是重复！
height3 = 1.80
weight3 = 80
bmi3 = weight3 / (height3 ** 2)
print(f"小刚的 BMI: {bmi3:.1f}")
```

有函数的版本：

```python
def calc_bmi(name, height, weight):
    bmi = weight / (height ** 2)
    print(f"{name} 的 BMI: {bmi:.1f}")

calc_bmi("小明", 1.75, 70)
calc_bmi("小红", 1.62, 55)
calc_bmi("小刚", 1.80, 80)
```

清爽多了！

## 定义函数

```python
def 函数名(参数1, 参数2):
    '''文档字符串（说明这个函数做什么）'''
    # 函数体
    return 结果  # return 可选
```

```python
def greet(name):
    '''向指定的人打招呼'''
    return f"你好，{name}！"

# 调用
print(greet("小明"))  # 你好，小明！
print(greet("小红"))  # 你好，小红！
```

## 函数的三个好处

1. **消除重复**：同样的代码只写一次
2. **便于修改**：改一处，所有调用的地方都更新
3. **让代码易读**：`calc_bmi("小明", 1.75, 70)` 比重复公式更容易理解
""",
    "analogy": "函数就像微波炉的预设按钮。按一下「热牛奶」按钮，微波炉自动用合适的时间和火力加热。你不需要每次都手动设置 1 分钟 + 中火。函数就是把一系列操作封装成按钮，要用时按一下就好。",
    "example_code": '''# 定义函数

def show_menu(restaurant_name, *dishes):
    """显示餐厅菜单"""
    print(f"===== {restaurant_name} =====")
    for i, dish in enumerate(dishes, 1):
        print(f"  {i}. {dish}")
    print("=" * (len(restaurant_name) + 10))

# 调用函数
show_menu("老张面馆", "牛肉面", "炸酱面", "西红柿鸡蛋面")
print()
show_menu("小李快餐", "汉堡", "薯条", "可乐", "炸鸡")''',
    "line_by_line_explanation": [
        {"line": 3, "explanation": "def 定义函数，*dishes 表示可以接收任意个参数"},
        {"line": 4, "explanation": "三引号字符串是文档字符串，说明函数做什么"},
        {"line": 5, "explanation": "f-string 使用参数 restaurant_name"},
        {"line": 6, "explanation": "enumerate(dishes, 1) 从 1 开始编号遍历"},
    ],
    "common_errors": [
        {"error": "函数定义后没调用（没输出）", "explanation": "def 只是定义，不调用就不会执行。要写 函数名() 才会运行"},
        {"error": "def func(): 后面的代码没缩进 → IndentationError", "explanation": "函数体必须缩进 4 个空格"},
        {"error": "return 后面代码不会执行", "explanation": "函数遇到 return 就结束了，return 之后的代码被忽略"},
    ],
    "order_index": 16,
    "estimated_minutes": 25,
}

LESSON_17 = {
    "title": "参数与返回值",
    "summary": "掌握函数的参数传递方式和返回值的使用",
    "objectives": [
        "区分形参和实参",
        "掌握默认参数和关键字参数",
        "理解 return 的多种用法",
        "学会用 *args 和 **kwargs",
    ],
    "content": """## 形参 vs 实参

```python
def greet(name):      # name 是形参（定义时）
    print(f"你好，{name}")

greet("小明")          # "小明" 是实参（调用时）
```

## 参数的类型

### 1. 位置参数（最常用）
```python
def introduce(name, age):
    print(f"{name} 今年 {age} 岁")

introduce("小明", 18)  # 按顺序对应
```

### 2. 关键字参数
```python
# 可以不按顺序，指定参数名传
introduce(age=18, name="小明")
```

### 3. 默认参数
```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("小明")                     # 你好，小明！
greet("Jack", greeting="Hello")   # Hello，Jack！
```

**注意：有默认值的参数必须放在没有默认值的参数后面。**

### 4. *args（可变数量参数）
```python
def sum_all(*numbers):
    '''求任意个数的和'''
    return sum(numbers)

print(sum_all(1, 2))           # 3
print(sum_all(1, 2, 3, 4, 5)) # 15
```

## return 返回值

```python
# 返回单个值
def add(a, b):
    return a + b

# 返回多个值（实际是元组）
def get_min_max(nums):
    return min(nums), max(nums)

m, M = get_min_max([3, 1, 4, 1, 5])
print(m, M)  # 1 5

# 没有 return 或 return 后面没东西 → 返回 None
def nothing():
    pass  # 什么都不做

print(nothing())  # None
```
""",
    "analogy": "参数就像点外卖时的备注：'不要香菜、少辣'。厨房（函数）根据备注（参数）调整做法。默认参数就是：'如果没有特别说明，默认微辣'。return 就是做好后把餐给你——你可以拿走去吃（使用返回值），也可以不要 return（厨房自己处理）。",
    "example_code": '''def get_grade(score, passing=60, excellent=90):
    """根据分数返回评语和等级"""
    if score >= excellent:
        return "优秀", "A"
    elif score >= passing:
        return "及格", "B"
    else:
        return "不及格", "F"

# 使用默认参数
result, level = get_grade(85)
print(f"成绩 85: {result}, 等级 {level}")

# 自定义参数
result, level = get_grade(85, passing=70, excellent=95)
print(f"成绩 85（严格标准）: {result}, 等级 {level}")

# 批量评判
scores = [55, 72, 88, 95]
for s in scores:
    result, level = get_grade(s)
    print(f"  {s} 分 → {result} ({level})")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "默认参数 passing=60, excellent=90，调用时可以不传"},
        {"line": 3, "explanation": "return 返回两个值（实际是返回元组 (str, str)）"},
        {"line": 10, "explanation": "解包接收：result='及格', level='B'"},
        {"line": 14, "explanation": "覆盖默认值：passing=70, excellent=95"},
    ],
    "common_errors": [
        {"error": "def f(a=[]): → 默认参数共享引用", "explanation": "默认参数不要用可变对象（列表、字典），用 None + 内部初始化"},
        {"error": "def f(a, b=1, c): → SyntaxError", "explanation": "有默认值的参数必须在无默认值参数后面"},
        {"error": "return 和 print 搞混", "explanation": "print 只是打印到屏幕；return 是把值返回给调用者，不打印"},
    ],
    "order_index": 17,
    "estimated_minutes": 25,
}

LESSON_18 = {
    "title": "变量作用域与 lambda 表达式",
    "summary": "理解变量的作用范围，学会写简单的匿名函数",
    "objectives": [
        "理解局部变量和全局变量",
        "掌握 global 关键字",
        "学会写 lambda 匿名函数",
        "了解 lambda 的常用场景",
    ],
    "content": """## 作用域 — 变量的活动范围

```python
x = 100  # 全局变量，整个文件都能用

def my_func():
    y = 50  # 局部变量，只能在这个函数内用
    print(f"函数内: x={x}, y={y}")

my_func()
print(f"函数外: x={x}")
# print(y)  # ❌ NameError! y 在外面不存在
```

**规则：**
- 函数**内**定义的变量（局部变量），外面不能用
- 函数**外**定义的变量（全局变量），里面可以读，但不能直接改

## global — 在函数内修改全局变量

```python
count = 0

def increment():
    global count    # 声明要修改全局变量
    count += 1

increment()
increment()
print(count)  # 2
```

**但尽量避免用 global**，最好的做法是：

```python
count = 0

def increment(n):
    return n + 1   # 通过参数和返回值来操作

count = increment(count)
```

## lambda 匿名函数

一行写完的简单函数，不需要 `def` 和名字：

```python
# 普通写法
def double(x):
    return x * 2

# lambda 写法
double = lambda x: x * 2

print(double(5))  # 10
```

**语法：** `lambda 参数: 返回值表达式`

## lambda 常用场景

```python
# 配合 sort 按指定规则排序
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 85},
    {"name": "小刚", "score": 95},
]

# 按成绩排序
students.sort(key=lambda s: s["score"])

# 配合 filter 筛选
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

# 配合 map 批量操作
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16, 25, 36]
```

**注意：** lambda 只适合简单操作。复杂的逻辑还是用 def 更清晰。
""",
    "analogy": "变量作用域就像公司的部门：部门内部的文件（局部变量）外面看不到；全公司公告（全局变量）所有人都能看。但部门不能随便改公告，除非申请授权（global）。lambda 就像便签纸——随手记一个简单计算，不值得单独建一个文档（def）。",
    "example_code": '''# 变量作用域示例
app_name = "PythonCoach"  # 全局
version = "1.0"

def show_info():
    user = "学员"  # 局部变量
    print(f"欢迎来到 {app_name} v{version}！")
    print(f"当前用户: {user}")

def update_version(new_version):
    global version  # 声明要改全局变量
    version = new_version

show_info()
print(f"\n旧版本: {version}")
update_version("1.1")
print(f"新版本: {version}")

# lambda 排序示例
print("\n--- 商品排序 ---")
items = [("苹果", 5), ("香蕉", 2), ("橙子", 4)]
items.sort(key=lambda x: x[1])  # 按价格排序
for name, price in items:
    print(f"  {name}: ¥{price}")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "全局变量 app_name 和 version"},
        {"line": 6, "explanation": "user 是局部变量，只在 show_info() 内可用"},
        {"line": 7, "explanation": "函数内可以读取全局变量 app_name 和 version"},
        {"line": 12, "explanation": "global 声明后才能在函数内修改全局变量"},
        {"line": 22, "explanation": "lambda x: x[1] — 对每个元组，取第二个元素（价格）作为排序依据"},
    ],
    "common_errors": [
        {"error": "UnboundLocalError: local variable 'x' referenced before assignment", "explanation": "函数内对全局变量赋值时没声明 global。要么加 global，要么用 return"},
        {"error": "lambda 里写复杂逻辑 → 代码难读", "explanation": "lambda 只做简单表达式，超过一行就用 def"},
    ],
    "order_index": 18,
    "estimated_minutes": 20,
}

LESSON_19 = {
    "title": "模块与 import",
    "summary": "学会使用 Python 标准库和导入外部模块",
    "objectives": [
        "理解模块的概念",
        "掌握 import 的几种写法",
        "了解常用的标准库",
        "学会安装和使用第三方库",
    ],
    "content": """## 什么是模块？

模块就是一个 `.py` 文件，里面写好了函数和变量供你使用。

Python 自带了很多模块（标准库），直接 import 就能用：

```python
import random    # 随机数
import math      # 数学函数
import datetime  # 日期时间
import os        # 操作系统相关
```

## import 的几种写法

```python
# 方式 1：导入整个模块
import random
num = random.randint(1, 10)

# 方式 2：导入特定函数
from random import randint
num = randint(1, 10)

# 方式 3：导入全部（不推荐，容易重名）
from random import *

# 方式 4：重命名（常用！）
import random as r
num = r.randint(1, 10)
```

## 常用标准库速览

```python
# random — 随机数
import random
print(random.randint(1, 100))   # 1-100 随机整数
print(random.choice(["A","B"]))  # 随机选一个
random.shuffle(my_list)          # 打乱列表

# math — 数学
import math
print(math.pi)         # π = 3.14159...
print(math.sqrt(16))   # 4.0（平方根）
print(math.ceil(3.2))  # 4（向上取整）

# datetime — 日期时间
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

# os — 系统操作
import os
print(os.getcwd())   # 当前目录
# os.listdir(".")    # 列出当前目录文件
```

## 第三方库

Python 生态最大的优势就是海量第三方库。

```bash
# 安装（在终端里运行）
pip install requests   # HTTP 请求
pip install pillow     # 图像处理
```

```python
# 使用
import requests
response = requests.get("https://api.example.com/data")
print(response.json())
```

## 自定义模块

你也可以把自己写的代码做成模块：

```python
# 创建 my_utils.py 文件
def greet(name):
    return f"你好，{name}！"

def add(a, b):
    return a + b
```

```python
# 在另一个文件里用
import my_utils
print(my_utils.greet("小明"))
```
""",
    "analogy": "模块就像工具箱。random 是骰子工具箱（专门生成随机数），math 是计算器工具箱，datetime 是日历工具箱。你需要什么功能就去对应的工具箱里拿，不用自己从头造。import 就是打开工具箱的钥匙。",
    "example_code": '''# 综合使用多个标准库
import random
import math
from datetime import datetime

# 生成随机圆的属性
radius = random.randint(5, 20)
area = math.pi * radius ** 2

# 当前时间
now = datetime.now()

print(f"计算时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"随机半径: {radius} cm")
print(f"圆的面积: {area:.2f} cm²")
print(f"圆的周长: {2 * math.pi * radius:.2f} cm")

# 随机幸运颜色
colors = ["红色", "橙色", "黄色", "绿色", "蓝色", "紫色"]
lucky = random.sample(colors, 2)
print(f"今日幸运色: {' 和 '.join(lucky)}")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "导入 random 模块（整个模块）"},
        {"line": 3, "explanation": "导入 math 模块（整个模块）"},
        {"line": 4, "explanation": "从 datetime 模块只导入 datetime 类"},
        {"line": 7, "explanation": "randint(5, 20) 生成 5-20 的随机整数"},
        {"line": 8, "explanation": "math.pi 是圆周率，**2 是平方"},
        {"line": 14, "explanation": "strftime 格式化日期时间为字符串"},
        {"line": 21, "explanation": "random.sample 不重复地随机抽取 2 个元素"},
    ],
    "common_errors": [
        {"error": "ModuleNotFoundError: No module named 'xxx'", "explanation": "先用 pip install xxx 安装；如果是自己写的模块，检查文件名和 import 是否在同一目录"},
        {"error": "import random 后 randint 不能用 → NameError", "explanation": "导入整个模块要用 random.randint()；如果只想写 randint()，用 from random import randint"},
    ],
    "order_index": 19,
    "estimated_minutes": 25,
}

LESSON_20 = {
    "title": "文件读写与综合复习",
    "summary": "学会读取和写入文件，复习全部所学知识",
    "objectives": [
        "学会用 open() 读写文件",
        "掌握 with 语句安全操作文件",
        "了解 CSV 文件读写",
        "复习 20 节课核心知识点",
    ],
    "content": """## 文件读写

### 读取文件

```python
# 方式 1：read() 一次读取全部
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 方式 2：readlines() 按行读取
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 方式 3：一行一行读（大文件）
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 写入文件

```python
# 'w' 模式：覆盖写入（如文件不存在则创建）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\\n")
    f.write("第二行\\n")

# 'a' 模式：追加写入（加在文件末尾）
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("追加一行\\n")
```

### 文件模式

| 模式 | 说明 |
|------|------|
| `'r'` | 读取（默认） |
| `'w'` | 写入（覆盖） |
| `'a'` | 追加 |
| `'r+'` | 读写 |

### with 语句 — 别忘了！

`with open(...) as f:` — Python 会在结束后自动关闭文件，不用手动 `f.close()`，安全又省心。

## 20 节课核心知识回顾

| 模块 | 核心内容 |
|------|----------|
| 入门 | 变量、数据类型（int/float/str/bool）、print()、input() |
| 字符串 | f-string、len()、索引、切片 |
| 运算符 | + - * / // % **、比较、逻辑 |
| 流程控制 | if/elif/else、while、for、break/continue |
| 数据结构 | list（增删改查排序推导式）、tuple、dict（键值对嵌套） |
| 函数 | def、参数、return、作用域、lambda |
| 模块 | import、标准库（random/math/datetime）、pip |

## 下一步

✅ 你已经完成了 Python 零基础入门全部课程！学完 20 节课，你已经掌握了：

- Python 核心语法
- 程序控制流程
- 三大数据结构
- 函数的编写
- 标准库的使用

接下来去**项目实战**页面，用所学知识完成真正的项目吧！
""",
    "analogy": "文件操作就像用记事本。open('r') 是打开看（读），open('w') 是新建一个写（覆盖原有内容），open('a') 是在末尾追加。with 就像一个负责任的助理，用完笔记本会自动帮你合上放好，不会出现'忘记关导致写不进去'的问题。",
    "example_code": '''# 日记本小程序
import os
from datetime import datetime

DIARY_FILE = "my_diary.txt"

def write_entry():
    """写一篇新日记"""
    content = input("今天发生了什么？\
> ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\
{'='*40}\
")
        f.write(f"📅 {now}\
")
        f.write(f"{'='*40}\
")
        f.write(content + "\
")
    
    print("✅ 日记已保存！")

def read_entries():
    """读取所有日记"""
    if not os.path.exists(DIARY_FILE):
        print("还没有日记哦，先写一篇吧！")
        return
    
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        print(f.read())

# 主菜单
while True:
    print("\
===== 日记本 =====")
    print("1. 写日记")
    print("2. 看日记")
    print("3. 退出")
    
    choice = input("请选择: ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("再见！")
        break
    else:
        print("无效选择")''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "导入 os 模块检查文件是否存在"},
        {"line": 5, "explanation": "定义日记文件名的全局常量"},
        {"line": 7, "explanation": "定义写日记函数"},
        {"line": 11, "explanation": "with open('a'模式) 追加写入，encoding='utf-8' 支持中文"},
        {"line": 19, "explanation": "用 os.path.exists 检查文件是否存在，避免 FileNotFoundError"},
        {"line": 28, "explanation": "while True 主菜单循环，选 3 时 break 退出"},
    ],
    "common_errors": [
        {"error": "FileNotFoundError: No such file or directory", "explanation": "文件不存在或路径错误。'r' 模式要求文件存在；'w' 和 'a' 会自动创建"},
        {"error": "写入中文出现乱码", "explanation": "打开文件时加 encoding='utf-8' 参数"},
        {"error": "忘记 with → 文件没关闭导致数据丢失", "explanation": "始终用 with open() as f: 语句，自动关闭文件更安全"},
    ],
    "order_index": 20,
    "estimated_minutes": 30,
}

# ============================================================
# Module 5: 错误处理与调试 (Lessons 21-25)
# ============================================================

LESSON_21 = {
    "title": "常见错误类型",
    "summary": "了解 Python 常见的错误类型，学会读懂报错信息",
    "objectives": [
        "认识 SyntaxError 语法错误",
        "认识 NameError / TypeError",
        "认识 IndexError / KeyError",
        "认识 ValueError / AttributeError",
        "学会根据报错定位问题",
    ],
    "content": """## 错误不可怕

写代码一定会遇到错误。高手和新手的区别在于：高手会**读**报错信息。

Python 的报错信息包含三个关键部分：
1. **错误类型**：发生了什么类型的错误
2. **错误信息**：具体哪里出了问题
3. **Traceback**：错误发生在哪个文件的第几行

## 常见错误一览

### SyntaxError — 语法错误

```python
# 少写了冒号
if True
    print("Hello")  # SyntaxError: expected ':'

# 少写了引号
print(Hello)  # SyntaxError? 其实是 NameError，往下看
```

### NameError — 变量名不存在

```python
print(message)  # NameError: name 'message' is not defined
# 变量没定义就用了！应该是 print("message") 或先定义 message
```

### TypeError — 类型错误

```python
result = "年龄：" + 18  # TypeError: can only concatenate str to str
# 正确：result = "年龄：" + str(18)
```

### IndexError / KeyError — 索引/键错误

```python
nums = [1, 2, 3]
print(nums[5])  # IndexError: list index out of range

user = {"name": "小明"}
print(user["age"])  # KeyError: 'age'
```

### ValueError — 值错误

```python
num = int("abc")  # ValueError: invalid literal for int()
# "abc" 不是合法数字
```

### AttributeError — 属性错误

```python
text = "hello"
text.append("!")  # AttributeError: 'str' object has no attribute 'append'
# 字符串没有 append 方法，列表才有
```

## 如何快速定位问题？

1. **看最后一行**：错误类型和消息
2. **看 Traceback 倒数第二行**：你的代码哪里出错了
3. **理解常见模式**：看到 TypeError → 检查类型，看到 IndexError → 检查索引范围
""",
    "analogy": "报错信息就像导航的'前方 200 米右转'——它不是骂你走错了，而是告诉你正确方向。SyntaxError = 你说的不是中文（电脑听不懂），TypeError = 你让狗学猫叫（类型不匹配），IndexError = 你找第 10 排但电影院只有 8 排（超出了范围）。",
    "example_code": '''# 故意制造错误并观察报错信息
def demonstrate_errors():
    errors = []

    try:
        result = "答案：" + 42
    except TypeError as e:
        errors.append(f"TypeError: {e}")

    try:
        nums = [1, 2, 3]
        x = nums[10]
    except IndexError as e:
        errors.append(f"IndexError: {e}")

    try:
        user = {"name": "小明"}
        age = user["age"]
    except KeyError as e:
        errors.append(f"KeyError: {e}")

    print("收集到的错误类型：")
    for err in errors:
        print(f"  {err}")

demonstrate_errors()''',
    "line_by_line_explanation": [
        {"line": 6, "explanation": "故意用字符串+数字制造 TypeError"},
        {"line": 11, "explanation": "访问超出范围的索引制造 IndexError"},
        {"line": 16, "explanation": "访问不存在的 key 制造 KeyError"},
        {"line": 20, "explanation": "展示所有收集到的错误类型"},
    ],
    "common_errors": [
        {"error": "只看最后一行忽略 Traceback → 不知道错误位置", "explanation": "Traceback 告诉你是哪个文件的第几行出错，这是最重要的信息"},
        {"error": "遇到错误就删代码重写 → 失去学习机会", "explanation": "先读懂错误信息，尝试理解原因，这样才能进步"},
    ],
    "order_index": 21,
    "estimated_minutes": 20,
}

LESSON_22 = {
    "title": "try/except 异常处理",
    "summary": "学会用 try/except 捕获和处理异常，让程序更健壮",
    "objectives": [
        "理解 try/except 的基本语法",
        "学会捕获特定异常",
        "学会捕获多个异常",
        "学会获取异常信息",
        "知道什么时候该用异常处理",
    ],
    "content": """## 为什么要处理异常？

```python
# 没有异常处理：用户输入非数字就崩溃
age = int(input("请输入年龄："))
print(f"明年你 {age + 1} 岁")
# 输入 "abc" → 程序崩溃！

# 有异常处理：友好提示
try:
    age = int(input("请输入年龄："))
    print(f"明年你 {age + 1} 岁")
except ValueError:
    print("请输入有效的数字！")
```

## try/except 基本语法

```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 出错后的处理
    print("除数不能为 0！")
```

## 捕获特定异常

```python
try:
    num = int(input("输入数字："))
    result = 100 / num
    print(f"100 / {num} = {result}")
except ValueError:
    print("输入的不是有效数字！")
except ZeroDivisionError:
    print("0 不能做除数！")
```

不同的异常类型可以有**不同的处理方式**。

## 捕获多个异常（同一处理）

```python
try:
    value = data["count"] / 2
except (KeyError, TypeError, ZeroDivisionError) as e:
    print(f"处理数据时出错：{e}")
    value = 0  # 使用默认值
```

## 获取异常信息

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print(f"文件找不到：{e.filename}")
    print(f"完整错误：{e}")
```

## 什么时候用 try/except？

- 用户输入 — 一定会有各种意外
- 文件操作 — 文件可能不存在
- 网络请求 — 网络可能断开
- 数据转换 — 格式可能不对

**不要用 try/except 掩盖 bug！** 如果不知道具体会出什么错，先让程序崩溃，看报错再修复。
""",
    "analogy": "try/except 就像开车时的安全气囊——平时不碍事，出事故时保护你（防止程序崩溃）。但你不能因为有了安全气囊就乱开车。好的异常处理是'预见到可能的危险，做好准备'，而不是'闭着眼睛开，撞了再说'。",
    "example_code": '''def safe_calculator():
    """安全的计算器：处理各种异常输入"""
    while True:
        try:
            expr = input("\\n输入算式 (如 10+20, q 退出): ")
            if expr.lower() == 'q':
                break

            # 分割数字和运算符
            for op in ['+', '-', '*', '/']:
                if op in expr:
                    a, b = expr.split(op)
                    a, b = float(a.strip()), float(b.strip())
                    if op == '+': result = a + b
                    elif op == '-': result = a - b
                    elif op == '*': result = a * b
                    elif op == '/': result = a / b
                    print(f"结果: {result}")
                    break
            else:
                print("不支持的运算符！支持 + - * /")
        except ValueError:
            print("输入格式错误！例如: 10+20")
        except ZeroDivisionError:
            print("除数不能为 0！")

safe_calculator()''',
    "line_by_line_explanation": [
        {"line": 4, "explanation": "while True 循环让用户可以多次计算"},
        {"line": 6, "explanation": "try 包裹可能出错的操作：类型转换、除法"},
        {"line": 15, "explanation": "float() 转换可能抛出 ValueError"},
        {"line": 20, "explanation": "捕获 ValueError 给友好提示而不是崩溃"},
        {"line": 22, "explanation": "单独捕获 ZeroDivisionError 给出具体提示"},
    ],
    "common_errors": [
        {"error": "except: 不指定异常类型 → 连 Ctrl+C 和 SystemExit 都捕获", "explanation": "永远指定异常类型：except ValueError: 而不是 except:"},
        {"error": "try 块太大 → 不知道哪里出的错", "explanation": "try 块只包裹可能出错的代码，不要包裹整个函数"},
    ],
    "order_index": 22,
    "estimated_minutes": 25,
}

LESSON_23 = {
    "title": "else/finally 与调试日志",
    "summary": "掌握 try/except/else/finally 完整流程和 logging 调试方法",
    "objectives": [
        "学会 else 在异常处理中的用法",
        "理解 finally 的用途",
        "学会用 logging 替代 print 调试",
        "了解日志级别的含义",
    ],
    "content": """## else — 没有异常时执行

```python
try:
    num = int(input("输入数字："))
except ValueError:
    print("不是数字！")
else:
    # 没有异常才执行
    print(f"你输入的是 {num}，平方是 {num ** 2}")
```

`else` 中的代码只在 try 没有抛出异常时执行。好处：把"正常逻辑"和"异常处理"清晰分开。

## finally — 无论怎样都执行

```python
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    # 不管有没有异常，都关闭文件
    if file:
        file.close()
        print("文件已关闭")
```

`finally` 通常用于**清理资源**：关闭文件、断开网络、释放锁等。

## 完整流程

```python
try:
    # 尝试执行
    result = risky_operation()
except SomeError:
    # 处理异常
    recover()
else:
    # 没有异常，正常处理
    process(result)
finally:
    # 无论如何都清理
    cleanup()
```

## logging — 专业的调试方式

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def find_max(nums):
    if not nums:
        logging.warning("空列表！")
        return None

    logging.debug(f"开始处理: {nums}")
    max_val = nums[0]
    for i, n in enumerate(nums):
        logging.debug(f"比较 {n} 和 {max_val}")
        if n > max_val:
            max_val = n
            logging.debug(f"更新最大值为 {max_val}")

    logging.info(f"最终结果: {max_val}")
    return max_val

find_max([3, 7, 2, 9, 1])
```

### 日志级别

| 级别 | 用途 |
|------|------|
| DEBUG | 详细调试信息 |
| INFO | 一般运行信息 |
| WARNING | 警告（可能出问题） |
| ERROR | 错误（功能出问题） |
| CRITICAL | 严重错误（程序崩溃） |

日志的优雅之处：调完 bug 不用删除，把 level 设高就行。
""",
    "analogy": "try/except/else/finally 就像约会：try = 出门去约会，except = 堵车了怎么办，else = 准时到了就开心约会，finally = 不管怎么样最后都要回家。logging 则像行车记录仪——默默记录一切，出问题时回放就知道发生了什么。",
    "example_code": '''import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def safe_divide(a, b):
    """安全除法，演示完整异常处理流程"""
    logging.debug(f"调用 safe_divide({a}, {b})")
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error(f"除数为 0！a={a}, b={b}")
        return None
    except TypeError as e:
        logging.error(f"类型错误: {e}")
        return None
    else:
        logging.info(f"计算成功: {a}/{b}={result}")
        return result
    finally:
        logging.debug("safe_divide 执行完毕")

print("结果:", safe_divide(10, 2))
print("结果:", safe_divide(10, 0))
print("结果:", safe_divide("a", 2))''',
    "line_by_line_explanation": [
        {"line": 9, "explanation": "try 块只包裹可能出错的操作"},
        {"line": 11, "explanation": "捕获特定异常：ZeroDivisionError"},
        {"line": 17, "explanation": "else 只在没有异常时执行，记录成功信息"},
        {"line": 19, "explanation": "finally 无论如何都执行，可用于清理"},
    ],
    "common_errors": [
        {"error": "print 调试完忘记删除", "explanation": "用 logging 替代 print，上线前把 level 设成 WARNING 就不会显示 DEBUG 信息"},
        {"error": "logging.basicConfig 多次调用只有第一次生效", "explanation": "basicConfig 只在第一次调用时生效，通常在程序入口处配置一次"},
    ],
    "order_index": 23,
    "estimated_minutes": 25,
}

LESSON_24 = {
    "title": "自定义异常",
    "summary": "学会创建自己的异常类型，让代码更语义化",
    "objectives": [
        "理解为什么需要自定义异常",
        "学会创建自定义异常类",
        "掌握 raise 的多种用法",
        "了解异常链 (raise ... from ...)",
    ],
    "content": """## 为什么需要自定义异常？

```python
def transfer(from_user, to_user, amount):
    if amount <= 0:
        raise ValueError("转账金额必须大于 0")
    if from_user.balance < amount:
        raise ValueError("余额不足")
```

两个不同的问题用了同一个 `ValueError`，外层代码没法区分！

## 创建自定义异常

```python
# 定义自己的异常类（只需继承 Exception）
class InsufficientFundsError(Exception):
    # 余额不足
    pass

class InvalidAmountError(Exception):
    # 金额无效
    pass

# 使用
def transfer(from_user, to_user, amount):
    if amount <= 0:
        raise InvalidAmountError(f"金额 {amount} 无效")
    if from_user.balance < amount:
        raise InsufficientFundsError(
            f"余额 {from_user.balance} 不足 {amount}"
        )
```

现在可以精确捕获不同的错误了：

```python
try:
    transfer(alice, bob, 1000)
except InsufficientFundsError as e:
    print(f"钱不够：{e}")
except InvalidAmountError as e:
    print(f"金额不对：{e}")
```

## 异常类可以加属性

```python
class ValidationError(Exception):
    def __init__(self, field, value, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"{field}='{value}' 验证失败: {reason}")

# 使用时能获取详细上下文
try:
    raise ValidationError("age", -1, "年龄不能为负")
except ValidationError as e:
    print(f"字段: {e.field}")
    print(f"错误值: {e.value}")
    print(f"原因: {e.reason}")
```

## raise ... from ... — 异常链

```python
class DataLoadError(Exception):
    pass

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise DataLoadError(f"配置文件 {path} 不存在") from e

# 保留了原始异常链，调试时能看到根本原因
```
""",
    "analogy": "自定义异常就像医院的科室分类——感冒去内科、骨折去骨科。你不会跟医生说'我身体有问题'然后等医生猜。raise InsufficientFundsError 就是在说'我是余额不足科的问题'，让捕获异常的代码能对症下药。",
    "example_code": '''class AgeError(Exception):
    """年龄相关异常"""
    def __init__(self, age, reason):
        self.age = age
        self.reason = reason
        super().__init__(f"年龄 {age}: {reason}")

class TooYoungError(AgeError):
    """年龄太小"""
    pass

class TooOldError(AgeError):
    """年龄太大"""
    pass

def register(name, age):
    if age < 0:
        raise AgeError(age, "年龄不能为负数")
    if age < 18:
        raise TooYoungError(age, "未满 18 岁不能注册")
    if age > 120:
        raise TooOldError(age, "请填写真实年龄")
    return f"{name} 注册成功！年龄：{age}"

# 测试不同年龄
test_ages = [25, 15, -1, 150]
for age in test_ages:
    try:
        result = register("小明", age)
        print(result)
    except TooYoungError as e:
        print(f"太年轻: {e}")
    except TooOldError as e:
        print(f"太老: {e}")
    except AgeError as e:
        print(f"年龄错误: {e}")''',
    "line_by_line_explanation": [
        {"line": 1, "explanation": "定义基类 AgeError，包含 age 和 reason 属性"},
        {"line": 9, "explanation": "TooYoungError 和 TooOldError 是 AgeError 的子类"},
        {"line": 17, "explanation": "根据年龄抛出不同类型的异常"},
        {"line": 27, "explanation": "捕获顺序很重要：先子类后父类"},
    ],
    "common_errors": [
        {"error": "自定义异常不继承 Exception → 无法被标准 except 捕获", "explanation": "自定义异常必须继承 Exception（或它的子类），不要继承 BaseException"},
        {"error": "捕获顺序错误：先写父类后写子类 → 子类永远匹配不到", "explanation": "except 从上到下匹配，子类异常要写在父类前面"},
    ],
    "order_index": 24,
    "estimated_minutes": 20,
}

LESSON_25 = {
    "title": "单元测试入门",
    "summary": "学会用 assert 和简单测试框架验证代码正确性",
    "objectives": [
        "理解测试的重要性",
        "学会用 assert 写测试",
        "了解测试用例的组织方式",
        "知道什么是测试驱动开发 (TDD)",
    ],
    "content": """## 为什么要测试？

你写完一段代码，怎么验证它对不对？
- 手动运行几次 → 耗时且容易漏
- 改了代码再跑一次 → 可能引入新 bug
- 自动化测试 → 一键验证所有情况

## assert — 最简单的测试

```python
def add(a, b):
    return a + b

# assert 断言：如果条件为 False，抛出 AssertionError
assert add(2, 3) == 5, "2+3 应该等于 5"
assert add(-1, 1) == 0, "-1+1 应该等于 0"
assert add(0, 0) == 0, "0+0 应该等于 0"
print("所有测试通过！")
```

## 测试函数

```python
def test_add():
    # 基本加法
    assert add(2, 3) == 5
    assert add(10, 20) == 30
    # 负数
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2
    # 零
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    # 异常测试
    try:
        divide(10, 0)
        assert False, "应该抛出异常！"
    except ValueError:
        pass  # 符合预期

# 运行所有测试
test_add()
test_divide()
print("全部通过！")
```

## 测试边界情况

```python
def get_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 60: return "C"
    else: return "F"

# 测试边界值
assert get_grade(90) == "A", "90 分应该 A"   # 左边界
assert get_grade(89) == "B", "89 分应该 B"   # 边界附近
assert get_grade(60) == "C", "60 分应该 C"   # 及格线
assert get_grade(59) == "F", "59 分应该 F"   # 不及格线
assert get_grade(0) == "F"                    # 极端值
assert get_grade(100) == "A"                  # 极端值
```

边界是最容易出 bug 的地方：>= 写成 >，多一个等号结果就错了。

## 测试驱动开发 (TDD) 思路

```
1. 写测试（描述期望的行为）
2. 运行测试（必然会失败——还没写代码呢）
3. 写代码（让测试通过）
4. 运行测试（通过就成功了）
5. 优化代码（重构），测试确保不破坏功能
```
""",
    "analogy": "测试就像汽车出厂前的安全检测。每辆车下线后不是直接卖，而是经过刹车测试、灯光测试、排放测试——全部通过才能出厂。软件也一样：每个函数的测试就是它的'安全检测'，通过了才放心交付。",
    "example_code": '''def run_tests(func, test_cases):
    """运行测试用例，统计结果"""
    passed = 0
    failed = 0

    for name, args, expected in test_cases:
        try:
            result = func(*args)
            if result == expected:
                passed += 1
                print("  OK", name)
            else:
                failed += 1
                print("  FAIL", name, f"(期望 {expected}，实际 {result})")
        except Exception as e:
            failed += 1
            print("  FAIL", name, f"(异常: {e})")

    print(f"\\n{'='*30}")
    print(f"通过: {passed}/{passed+failed}")
    print(f"失败: {failed}/{passed+failed}")

# 被测试的函数
def is_even(n):
    return n % 2 == 0

# 测试用例：(名称, 参数元组, 期望结果)
test_cases = [
    ("偶数 2", (2,), True),
    ("奇数 3", (3,), False),
    ("零", (0,), True),
    ("负数偶数", (-4,), True),
    ("负数奇数", (-5,), False),
]

run_tests(is_even, test_cases)''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "通用测试函数：接收被测函数和测试用例列表"},
        {"line": 7, "explanation": "每个测试用例包含名称、参数元组、期望结果"},
        {"line": 10, "explanation": "调用被测函数并比较实际结果和期望结果"},
        {"line": 21, "explanation": "打印统计：通过数和失败数"},
    ],
    "common_errors": [
        {"error": "assert 语句只用于调试，生产环境被 -O 跳过", "explanation": "不要依赖 assert 做生产环境的数据验证，仅用于测试和调试"},
        {"error": "assert (a == b, 'message') → 永远不会触发", "explanation": "元组永远为 True！assert a == b, 'message' 不要加括号"},
    ],
    "order_index": 25,
    "estimated_minutes": 25,
}

# ============================================================
# Module 6: 高级数据结构 (Lessons 26-30)
# ============================================================

LESSON_26 = {
    "title": "集合 (set) 操作",
    "summary": "掌握 set 的创建、操作和实际应用场景",
    "objectives": [
        "理解集合的无序、不重复特性",
        "学会添加、删除、查找元素",
        "掌握集合运算：交集、并集、差集",
        "了解集合的实际应用场景",
    ],
    "content": """## 什么是集合？

集合（set）是**无序、不重复**的元素集合。和数学中的集合概念一样。

```python
# 创建集合
fruits = {"apple", "banana", "orange"}
print(fruits)  # 顺序可能每次不同！

# 自动去重
nums = {1, 2, 2, 3, 3, 3}
print(nums)  # {1, 2, 3}

# 从列表去重
names = ["小明", "小红", "小明", "小刚"]
unique_names = set(names)
print(unique_names)  # {'小明', '小红', '小刚'}
```

## 基本操作

```python
s = {1, 2, 3}

# 添加
s.add(4)
s.add(2)  # 重复的不添加

# 删除
s.remove(3)  # 元素不存在会报错
s.discard(5)  # 不存在不报错（安全删除）

# 查找（O(1) 效率！）
print(2 in s)  # True
print(5 in s)  # False
```

## 集合运算

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 交集：两边都有的
print(a & b)  # {3, 4}

# 并集：合在一起（去重）
print(a | b)  # {1, 2, 3, 4, 5, 6}

# 差集：a 有但 b 没有的
print(a - b)  # {1, 2}

# 对称差集：只在其中一边的
print(a ^ b)  # {1, 2, 5, 6}
```

## 实际应用

### 去重

```python
# 统计访问过的用户
visitors = ["A", "B", "A", "C", "B", "D"]
unique_visitors = set(visitors)
print(f"访客总数: {len(visitors)}, 独立访客: {len(unique_visitors)}")
```

### 找共同元素

```python
python_users = {"小明", "小红", "小刚", "小李"}
java_users = {"小刚", "小李", "小王", "小张"}

# 两种语言都会的
both = python_users & java_users
print(f"会两种语言: {both}")

# 只会 Python 的
only_python = python_users - java_users
print(f"只会 Python: {only_python}")
```

### 成员检查（比列表快很多！）

```python
# 检查是否在黑名单中
blacklist = {"spam@test.com", "bot@test.com"}
email = "user@test.com"
if email in blacklist:
    print("该邮箱已被禁用")
```

集合的 `in` 操作是 O(1) 的（哈希表），列表是 O(n) 的。数据量大时差距巨大！
""",
    "analogy": "集合就像参加派对的人——每个人只出现一次（不重复），人群在房间里自由流动（无序）。你可以快速问'小明在不在？'（O(1) 查找）。交集就是'哪些人同时参加了 A 派对和 B 派对'，差集就是'谁在 A 派对但不在 B 派对'。",
    "example_code": '''# 用集合解决实际问题：共同好友推荐
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Eve", "Frank"}

# 共同好友
mutual = alice_friends & bob_friends
print(f"共同好友: {mutual}")

# 推荐给 Alice：Bob 的朋友中 Alice 还没加的
alice = "Alice"
alice_friends_real = {"Bob", "Charlie"}
recommendations = bob_friends - alice_friends_real - {alice}
print(f"推荐给 {alice}: {recommendations}")

# 查找可能认识的人（二度好友）
all_friends = {
    "Bob": {"Alice", "Charlie", "David"},
    "Charlie": {"Alice", "Bob", "Eve"},
}
my_friends = {"Bob", "Charlie"}
suggestions = set()
for friend in my_friends:
    if friend in all_friends:
        suggestions |= all_friends[friend]
suggestions -= my_friends
suggestions.discard("Alice")
print(f"可能认识的人: {suggestions}")''',
    "line_by_line_explanation": [
        {"line": 6, "explanation": "& 求两个集合的交集（共同好友）"},
        {"line": 11, "explanation": "- 运算：Bob 的朋友减去 Alice 已有的朋友"},
        {"line": 20, "explanation": "|= 合并每个好友的好友列表"},
        {"line": 21, "explanation": "去掉自己已有的好友和自己"},
    ],
    "common_errors": [
        {"error": "TypeError: unhashable type: 'list' → 集合元素必须是可哈希类型", "explanation": "集合元素必须是不可变类型（数字、字符串、元组），不能放列表或字典"},
        {"error": "sets[0] → TypeError: 'set' object is not subscriptable", "explanation": "集合无序、不支持索引。需要顺序时转为列表 list(s)"},
    ],
    "order_index": 26,
    "estimated_minutes": 25,
}

LESSON_27 = {
    "title": "列表推导式与生成器表达式",
    "summary": "掌握 Python 最优雅的语法之一：推导式",
    "objectives": [
        "学会列表推导式的基本语法",
        "学会带条件的列表推导式",
        "学会字典推导式和集合推导式",
        "理解生成器表达式的优势",
    ],
    "content": """## 传统方式 vs 推导式

```python
# 传统方式：创建平方数列表
squares = []
for i in range(10):
    squares.append(i ** 2)

# 列表推导式：一行搞定！
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

推导式 = **从现有可迭代对象构建新列表（或字典/集合）的简洁语法**。

## 带条件的列表推导式

```python
# 只保留偶数
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# if-else 在三元中（注意位置！）
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 6)]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']

# 过滤 + 转换
nums = [1, -2, 3, -4, 5]
pos_squares = [n ** 2 for n in nums if n > 0]
print(pos_squares)  # [1, 9, 25]
```

## 嵌套推导式

```python
# 展开嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 字典推导式

```python
# 键值互换
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# 过滤条件
scores = {"小明": 90, "小红": 75, "小刚": 85, "小李": 60}
passed = {name: score for name, score in scores.items() if score >= 80}
print(passed)  # {'小明': 90, '小刚': 85}

# 从列表构建字典
names = ["小明", "小红", "小刚"]
name_dict = {name: len(name) for name in names}
```

## 集合推导式

```python
# 去重并求平方
nums = [1, -1, 2, -2, 3, -3, 1, 2]
squares_set = {x ** 2 for x in nums}
print(squares_set)  # {1, 4, 9}
```

## 什么时候用/不用推导式？

- 简单转换：用推导式 ✓
- 多层嵌套循环：用普通 for ✗（可读性差）
- 有副作用（如 print）：用普通 for ✗
- 逻辑复杂：用普通 for ✗
""",
    "analogy": "列表推导式就像流水线——原料（range(10)）从传送带过来，经过加工（i**2），产出成品（新列表）。传统 for 循环是手工一个个做，推导式是自动化流水线。简洁、高效、但太复杂的工序（多层嵌套）不适合流水线。",
    "example_code": '''# 实战：处理学生成绩
students = [
    {"name": "小明", "scores": [90, 85, 92]},
    {"name": "小红", "scores": [88, 95, 91]},
    {"name": "小刚", "scores": [76, 82, 79]},
]

# 列表推导式：计算平均分
averages = [
    {
        "name": s["name"],
        "average": sum(s["scores"]) / len(s["scores"])
    }
    for s in students
]
print("平均分：")
for item in averages:
    print(f"  {item['name']}: {item['average']:.1f}")

# 字典推导式：姓名 -> 平均分
avg_dict = {
    s["name"]: round(sum(s["scores"]) / len(s["scores"]), 1)
    for s in students
}
print(f"\\n字典形式: {avg_dict}")

# 带过滤：优秀学生（平均分 >= 85）
excellent = {
    name: avg for name, avg in avg_dict.items() if avg >= 85
}
print(f"优秀学生: {excellent}")''',
    "line_by_line_explanation": [
        {"line": 9, "explanation": "列表推导式：遍历 students 列表，为每人创建字典"},
        {"line": 17, "explanation": "字典推导式：构建 {姓名: 平均分} 映射"},
        {"line": 22, "explanation": "带过滤的字典推导式：只保留平均分 >= 85 的学生"},
    ],
    "common_errors": [
        {"error": "推导式中 if 和 if-else 位置搞混", "explanation": "过滤用 [x for x in seq if cond]，选择用 [a if cond else b for x in seq]"},
        {"error": "嵌套太深可读性差", "explanation": "推导式最多 2 层 for。超过 2 层用普通 for 循环更清晰"},
    ],
    "order_index": 27,
    "estimated_minutes": 25,
}

LESSON_28 = {
    "title": "collections 模块（Counter, defaultdict）",
    "summary": "掌握 collections 中的实用数据结构：Counter、defaultdict、namedtuple",
    "objectives": [
        "学会用 Counter 统计频率",
        "学会用 defaultdict 简化代码",
        "了解 namedtuple 的用法",
        "知道 collections 中其他实用工具",
    ],
    "content": """## Counter — 计数器

```python
from collections import Counter

# 统计词频
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(words)
print(count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 最常用方法
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]
print(count["apple"])         # 3（不存在的 key 返回 0）

# 字符串中的字符频率
text = "hello world"
char_count = Counter(text)
print(char_count)  # Counter({'l': 3, 'o': 2, ...})
```

## defaultdict — 带默认值的字典

```python
from collections import defaultdict

# 普通字典的痛点
scores = {}
for name, score in [("小明", 90), ("小红", 85), ("小明", 92)]:
    if name not in scores:
        scores[name] = []
    scores[name].append(score)

# defaultdict：自动创建默认值
scores = defaultdict(list)
for name, score in [("小明", 90), ("小红", 85), ("小明", 92)]:
    scores[name].append(score)  # 不需要检查 key 是否存在！
print(dict(scores))  # {'小明': [90, 92], '小红': [85]}

# 其他常见默认类型
counter = defaultdict(int)   # 默认 0（计数）
groups = defaultdict(set)    # 默认空集合（分组）
nested = defaultdict(dict)   # 默认空字典（嵌套）
```

## 实战：分组和统计

```python
from collections import defaultdict, Counter

students = [
    ("一班", "小明", 90), ("一班", "小红", 85),
    ("二班", "小刚", 76), ("二班", "小李", 88),
    ("一班", "小王", 92),
]

# 按班级分组
by_class = defaultdict(list)
for cls, name, score in students:
    by_class[cls].append((name, score))

# 每班平均分
for cls, members in by_class.items():
    avg = sum(s[1] for s in members) / len(members)
    print(f"{cls}: 平均 {avg:.1f} 分")
```

## namedtuple — 有名字的元组

```python
from collections import namedtuple

# 定义一个 Point 类型
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 5)
print(p.x, p.y)  # 3 5
print(p[0], p[1])  # 3 5（也支持索引）
```

值不可变，内存比类小。适合表示坐标、RGB 颜色、数据库记录等。
""",
    "analogy": "Counter 就像超市收银台的计数器——每扫一个商品，对应品类 +1。defaultdict 就像酒店前台——你说'帮我订个房间'，前台不会说'房间不存在'，而是自动给你开一间。它省去了每次检查'这个 key 存在吗？'的麻烦。",
    "example_code": '''from collections import Counter, defaultdict

# 分析文章词频
article = """
Python is a programming language
Python is easy to learn
Python is powerful
"""

words = article.lower().split()
word_count = Counter(words)
print("词频统计:")
for word, count in word_count.most_common(5):
    print(f"  {word}: {count}")

# 按首字母分组
by_letter = defaultdict(list)
for word in word_count:
    if word:
        by_letter[word[0]].append(word)

print("\\n按首字母分组:")
for letter in sorted(by_letter):
    print(f"  {letter}: {by_letter[letter]}")

# 字符位置索引
text = "hello world hello python"
char_positions = defaultdict(list)
for i, ch in enumerate(text):
    if ch != ' ':
        char_positions[ch].append(i)

print(f"\\n字符 'o' 的位置: {char_positions['o']}")
print(f"字符 'l' 的位置: {char_positions['l']}")''',
    "line_by_line_explanation": [
        {"line": 10, "explanation": "Counter 统计每个单词出现的次数"},
        {"line": 12, "explanation": "most_common(5) 返回频率最高的 5 个"},
        {"line": 16, "explanation": "defaultdict(list) 自动为新 key 创建空列表"},
        {"line": 24, "explanation": "用 defaultdict 索引每个字符出现的位置"},
    ],
    "common_errors": [
        {"error": "Counter 不存在的 key 返回 0 而不是 KeyError", "explanation": "这是 Counter 的特性。如果需要 KeyError 行为，转为普通字典 dict(counter)"},
        {"error": "defaultdict 传入的函数不要加括号", "explanation": "defaultdict(list) 正确，defaultdict(list()) 错误。传入的是工厂函数，不是实例"},
    ],
    "order_index": 28,
    "estimated_minutes": 25,
}

LESSON_29 = {
    "title": "内置函数（zip, enumerate, any/all）",
    "summary": "掌握 Python 数据处理三剑客和其他实用内置函数",
    "objectives": [
        "学会用 enumerate 同时获取索引和值",
        "学会用 zip 并行遍历多个序列",
        "学会用 any/all 做条件聚合",
        "学会用 sorted 和 lambda 排序",
    ],
    "content": """## enumerate — 同时获取索引和值

```python
fruits = ["苹果", "香蕉", "橘子"]

# 不好的方式
for i in range(len(fruits)):
    print(f"{i+1}. {fruits[i]}")

# 好的方式 —— enumerate
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
# 1. 苹果  2. 香蕉  3. 橘子
```

## zip — 并行遍历

```python
names = ["小明", "小红", "小刚"]
scores = [90, 85, 78]

# 配对遍历
for name, score in zip(names, scores):
    print(f"{name}: {score} 分")

# 创建字典
score_dict = dict(zip(names, scores))
print(score_dict)  # {'小明': 90, '小红': 85, '小刚': 78}
```

长度不等时以最短的为准。

## any / all — 条件聚合

```python
# all：全部满足才 True
scores = [85, 90, 78, 92]
print(all(s >= 60 for s in scores))  # True（全部及格）
print(all(s >= 80 for s in scores))  # False（78 < 80）

# any：有一个满足就 True
features = [False, False, True, False]
print(any(features))  # True

# 实战：验证用户输入
def validate_password(pw):
    checks = [
        len(pw) >= 8,                # 长度
        any(c.isupper() for c in pw),  # 大写字母
        any(c.isdigit() for c in pw),  # 数字
        any(c in "!@#$" for c in pw),  # 特殊字符
    ]
    return all(checks)

print(validate_password("abc"))       # False
print(validate_password("Abc123!@#")) # True
```

## sorted + lambda

```python
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 85},
]

# 按分数排序（从低到高）
sorted_students = sorted(students, key=lambda s: s["score"])
# 按分数从高到低
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)

# 先按分数，分数相同按名字
sorted_students = sorted(students, key=lambda s: (-s["score"], s["name"]))
```

## 综合运用

```python
# 数据处理流水线
names = ["小明", "小红", "小刚"]
math = [90, 85, 78]
english = [88, 95, 82]

# zip + enumerate 组合
for i, (name, m, e) in enumerate(zip(names, math, english), 1):
    avg = (m + e) / 2
    print(f"{i}. {name}: 数学{m}, 英语{e}, 平均{avg:.1f}")
```
""",
    "analogy": "zip 就像拉链——把两条链（两个列表）的齿一个一个咬合在一起。enumerate 就像带编号的排队号码——你拿到的不只是等待位置（值），还有号码牌（索引）。any/all 就像安检——any 是'有一件危险品就不通过'，all 是'全部合规才通过'。",
    "example_code": '''# 综合实战：成绩分析
names = ["小明", "小红", "小刚", "小李"]
math = [90, 85, 78, 92]
english = [88, 95, 82, 76]

# 1. enumerate 排名
print("排名:")
for rank, (name, m, e) in enumerate(zip(names, math, english), 1):
    avg = (m + e) / 2
    print(f"  {rank}. {name} 平均{avg:.1f}")

# 2. all/any 分析
all_pass_math = all(m >= 60 for m in math)
print(f"\\n数学全部及格: {all_pass_math}")
any_perfect_eng = any(e == 100 for e in english)
print(f"英语有满分: {any_perfect_eng}")

# 3. sorted 排名
avgs = [(name, (m+e)/2) for name, m, e in zip(names, math, english)]
avgs.sort(key=lambda x: x[1], reverse=True)
print("\\n按平均分排名:")
for rank, (name, avg) in enumerate(avgs, 1):
    print(f"  {rank}. {name} {avg:.1f}分")''',
    "line_by_line_explanation": [
        {"line": 7, "explanation": "zip 同时遍历 3 个列表，enumerate 从 1 开始编号"},
        {"line": 13, "explanation": "all + 生成器表达式：判断全体数学及格？"},
        {"line": 16, "explanation": "any + 生成器表达式：判断是否存在英语满分？"},
        {"line": 20, "explanation": "zip 综合运用生成 (姓名, 平均分) 列表"},
    ],
    "common_errors": [
        {"error": "zip 长度不一致时以最短为准 → 数据被截断", "explanation": "zip([1,2], [3]) 只有 (1,3)。需要严格模式用 itertools.zip_longest"},
        {"error": "any([]) == False, all([]) == True", "explanation": "空列表的 any 是 False（没有 True），all 是 True（没有 False，逻辑上为 vacuously true）"},
    ],
    "order_index": 29,
    "estimated_minutes": 25,
}

LESSON_30 = {
    "title": "深浅拷贝与数据操作安全",
    "summary": "理解 Python 的引用机制和深浅拷贝的区别",
    "objectives": [
        "理解 Python 变量是引用而非值",
        "掌握浅拷贝和深拷贝的区别",
        "学会用 copy 模块",
        "避免修改列表/字典时的常见坑",
    ],
    "content": """## 变量是引用（标签）

```python
# 列表变量指向内存中的同一个对象
a = [1, 2, 3]
b = a          # b 和 a 指向同一个列表！
b.append(4)
print(a)       # [1, 2, 3, 4] — a 也被改了！

# 数字和字符串不一样，它们是不可变的
x = 10
y = x
y = 20
print(x)       # 10 — 数字不受影响
```

## 浅拷贝 (Shallow Copy)

```python
import copy

a = [1, 2, [3, 4]]

# 浅拷贝：只复制外层，内层列表还是共享的
b = copy.copy(a)  # 或 a.copy(), a[:]

b[0] = 99      # 改外层 → 不影响 a
b[2][0] = 999  # 改内层 → a 也被改了！
print(a)       # [1, 2, [999, 4]]
```

## 深拷贝 (Deep Copy)

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  # 所有层都复制，完全独立
b[2][0] = 999
print(a)  # [1, 2, [3, 4]] — 完全不受影响
```

## 函数参数的坑

```python
# 错误做法：默认参数用可变对象
def add_item(item, target=[]):
    target.append(item)
    return target

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] ← 默认列表被共享了！

# 正确做法
def add_item(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```
""",
    "analogy": "变量是标签不是盒子。一个列表可以贴多个标签（a 和 b 指向同一个对象）。浅拷贝是影印——封皮是新的，但里面内容还是原来那本。深拷贝是全本复印——从封皮到每一页都是新的，改任何一处都不影响原书。",
    "example_code": '''import copy

original = ["姓名", [90, 85, 95], "Python"]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# 修改内层列表
shallow[1][0] = 0
deep[1][1] = 0

print("原始:", original)
print("浅拷贝:", shallow)
print("深拷贝:", deep)
print()
print("浅拷贝改了内层 → 原始也被改了:", original[1][0] == 0)
print("深拷贝改了内层 → 原始不受影响:", original[1][1] == 85)''',
    "line_by_line_explanation": [
        {"line": 3, "explanation": "原始列表含嵌套列表 [90, 85, 95]"},
        {"line": 5, "explanation": "浅拷贝：外层独立，内层列表还是共享的"},
        {"line": 6, "explanation": "深拷贝：所有层都是独立的副本"},
        {"line": 9, "explanation": "shallow[1] 和 original[1] 是同一个列表"},
        {"line": 10, "explanation": "deep[1] 是完全独立的"},
    ],
    "common_errors": [
        {"error": "a = b = [] → a 和 b 指向同一个空列表", "explanation": "分别创建用 a=[]; b=[]。a=b=[] 两个变量指向同一个列表"},
        {"error": "deepcopy 大对象时很慢", "explanation": "深拷贝要递归复制所有层，大对象开销大。只在真正需要时才用"},
    ],
    "order_index": 30,
    "estimated_minutes": 20,
}

# ============================================================
# Module 7: 文件与数据处理 (Lessons 31-35)
# ============================================================

LESSON_31 = {
    "title": "CSV 文件读写",
    "summary": "学会用 Python 读取和写入 CSV 文件，处理表格数据",
    "objectives": [
        "理解 CSV 格式的结构",
        "学会用 csv.reader 读取 CSV",
        "学会用 csv.DictReader 按字典读取",
        "学会写入 CSV 文件",
        "处理中文编码问题",
    ],
    "content": """## 什么是 CSV？

CSV（Comma-Separated Values）是最常见的表格数据格式。Excel 能打开，文本编辑器也能编辑。

```csv
姓名,年龄,城市
小明,18,北京
小红,20,上海
```

本质上就是纯文本文件，每行一条记录，逗号分隔各列。

## 读取 CSV 文件

```python
import csv

with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # 跳过表头
    for row in reader:
        print(row)  # 每行是一个列表

# 字典读取
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["年龄"])  # 按列名访问
```

## 写入 CSV 文件

```python
import csv

data = [
    ["姓名", "年龄", "城市"],
    ["小明", "18", "北京"],
    ["小红", "20", "上海"],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 用 DictWriter
with open("output.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄"])
    writer.writeheader()
    writer.writerow({"姓名": "小明", "年龄": "18"})
```

## 中文编码注意事项

- Windows Excel 默认用 gbk 编码
- 写文件用 `utf-8-sig` 可避免 Excel 乱码
- open 记得加 `newline=""`（Windows 兼容）
""",
    "analogy": "CSV 就像餐厅的菜单——每行是一个菜品，每列是菜名、价格、辣度等属性。csv.reader 就是服务员，一行行帮你读出来。DictReader 更贴心，直接告诉你'这道菜的菜名是宫保鸡丁，价格是 38 元'，不用你数第几列是什么。",
    "example_code": '''import csv
import io

# 用字符串模拟 CSV 文件
csv_data = "姓名,年龄,城市\\n小明,18,北京\\n小红,20,上海\\n小刚,19,广州\\n"
f = io.StringIO(csv_data)

reader = csv.DictReader(f)
print("读取学生信息：")
for row in reader:
    print(f"  {row['姓名']}, {row['年龄']}岁, 来自{row['城市']}")''',
    "line_by_line_explanation": [
        {"line": 7, "explanation": "DictReader 按字典读取，表头作为 key"},
        {"line": 9, "explanation": "row['姓名'] 直接按列名取值，非常直观"},
    ],
    "common_errors": [
        {"error": "UnicodeDecodeError: 编码错误", "explanation": "文件编码不是 utf-8，尝试 encoding='gbk' 或 'gb18030'"},
        {"error": "写入 CSV 时行之间多空行", "explanation": "open 时加 newline='' 参数，这是 Windows 的历史问题"},
    ],
    "order_index": 31,
    "estimated_minutes": 25,
}

LESSON_32 = {
    "title": "JSON 数据处理",
    "summary": "掌握 JSON 格式的读写，理解序列化与反序列化",
    "objectives": [
        "理解 JSON 格式的用途",
        "学会 json.loads / json.dumps",
        "学会 json.load / json.dump 文件读写",
        "处理中文 JSON",
        "处理复杂嵌套 JSON",
    ],
    "content": """## 什么是 JSON？

JSON（JavaScript Object Notation）是最流行的数据交换格式。API 返回数据、配置文件、前后端通信——全用 JSON。

```json
{
  "name": "小明",
  "age": 18,
  "hobbies": ["编程", "篮球"],
  "address": {"city": "北京", "district": "海淀"}
}
```

### JSON vs Python 对照

| JSON | Python |
|------|--------|
| object {} | dict |
| array [] | list |
| string "..." | str |
| number 123 | int/float |
| true/false | True/False |
| null | None |

## json.loads / json.dumps

```python
import json

# JSON 字符串 → Python 对象
data = '{"name": "小明", "age": 18, "scores": [90, 85, 95]}'
obj = json.loads(data)
print(obj["name"])  # 小明

# Python 对象 → JSON 字符串
student = {"name": "小红", "age": 20, "graduated": False}
json_str = json.dumps(student, ensure_ascii=False, indent=2)
print(json_str)
```

`ensure_ascii=False` 让中文正常显示，`indent=2` 格式化输出。

## 读写 JSON 文件

```python
# 读取
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# 写入
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

注意：文件用 `load/dump`，字符串用 `loads/dumps`。

## 处理嵌套 JSON

```python
response = '''
{
  "status": "ok",
  "data": {
    "user": {
      "name": "小明",
      "repos": [
        {"name": "my-app", "stars": 42},
        {"name": "utils", "stars": 15}
      ]
    }
  }
}
'''
obj = json.loads(response)
print(obj["data"]["user"]["name"])  # 逐层访问
for repo in obj["data"]["user"]["repos"]:
    print(repo["name"], repo["stars"])
```
""",
    "analogy": "JSON 就像快递包裹的装箱单——发货方把物品信息写成标准格式（序列化），收货方按同样的格式解读（反序列化）。不管发货方用什么语言、收货方用什么语言，装箱单的格式都是统一的。Python 用 json.dumps 装箱，用 json.loads 拆箱。",
    "example_code": '''import json

# 模拟 API 返回的用户数据
user = {
    "name": "小明",
    "age": 18,
    "skills": ["Python", "JavaScript"],
    "contact": {
        "email": "xiaoming@example.com",
        "phone": "13800138000"
    }
}

# 序列化
json_str = json.dumps(user, ensure_ascii=False, indent=2)
print("序列化结果：")
print(json_str)

# 反序列化验证
restored = json.loads(json_str)
print(f"\\n反序列化验证：")
print(f"  姓名: {restored['name']}")
print(f"  技能: {', '.join(restored['skills'])}")''',
    "line_by_line_explanation": [
        {"line": 13, "explanation": "dumps 转为 JSON 字符串，ensure_ascii=False 保证中文可读"},
        {"line": 17, "explanation": "loads 把 JSON 字符串转回 Python 对象"},
        {"line": 19, "explanation": "访问嵌套字段验证数据正确"},
    ],
    "common_errors": [
        {"error": "json.decoder.JSONDecodeError", "explanation": "JSON 格式有问题，常见：用了单引号、最后多了逗号、key 没加引号"},
        {"error": "TypeError: datetime is not JSON serializable", "explanation": "datetime 等 Python 对象不能直接序列化，需要先转成字符串"},
    ],
    "order_index": 32,
    "estimated_minutes": 25,
}

LESSON_33 = {
    "title": "日期时间处理（datetime）",
    "summary": "学会用 datetime 模块处理日期、时间和时间计算",
    "objectives": [
        "获取当前日期和时间",
        "格式化日期输出 strftime",
        "解析字符串为日期 strptime",
        "计算日期差值和偏移 timedelta",
    ],
    "content": """## datetime 模块核心类

| 类 | 用途 | 示例 |
|----|------|------|
| datetime.date | 日期 | 2026-05-28 |
| datetime.time | 时间 | 14:30:00 |
| datetime.datetime | 日期+时间 | 2026-05-28 14:30:00 |
| datetime.timedelta | 时间差 | 3 天 5 小时 |

## 获取当前时间

```python
from datetime import date, datetime

today = date.today()
print(today)  # 2026-05-28

now = datetime.now()
print(now)    # 2026-05-28 14:30:15.123456

# 分别访问各部分
print(now.year, now.month, now.day)      # 2026 5 28
print(now.hour, now.minute, now.second)  # 14 30 15
```

## strftime — 格式化输出

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))      # 2026-05-28
print(now.strftime("%Y年%m月%d日"))   # 2026年05月28日
print(now.strftime("%H:%M:%S"))      # 14:30:15
print(now.strftime("%A"))            # Thursday
```

常用格式码：%Y 四位年，%m 月，%d 日，%H 时，%M 分，%S 秒

## strptime — 解析字符串

```python
dt = datetime.strptime("2026-05-28 14:30:00", "%Y-%m-%d %H:%M:%S")
print(dt.year, dt.month)  # 2026 5

# 各种格式都能解析
dt2 = datetime.strptime("28/05/2026", "%d/%m/%Y")
dt3 = datetime.strptime("2026年05月28日", "%Y年%m月%d日")
```

## timedelta — 时间计算

```python
from datetime import datetime, timedelta

now = datetime.now()

# 3 天后
print(now + timedelta(days=3))
# 2 周前
print(now - timedelta(weeks=2))
# 30 分钟后
print(now + timedelta(minutes=30))

# 计算日期差
birthday = datetime(2000, 1, 1)
age_days = (now - birthday).days
print(f"出生了 {age_days} 天")
```
""",
    "analogy": "datetime 就像一个日历加闹钟的组合。strftime 是翻译官——把计算机的时间格式翻译成人能看懂的格式。strptime 是反向翻译——把人类写的日期字符串翻译成计算机的时间对象。timedelta 就是时间的计算器。",
    "example_code": '''from datetime import datetime, timedelta

# 高考倒计时
gaokao = datetime(2026, 6, 7, 9, 0, 0)
now = datetime.now()
delta = gaokao - now

print(f"今天是: {now.strftime('%Y年%m月%d日 %H:%M')}")
print(f"高考时间: {gaokao.strftime('%Y年%m月%d日 %H:%M')}")
print(f"距离高考还有 {delta.days} 天")
print(f"也就是 {delta.total_seconds()/3600:.1f} 小时")

if delta.days > 100:
    print("还早呢，好好准备！")
elif delta.days > 0:
    print("马上就要高考了，加油！")
else:
    print("高考已经结束！")''',
    "line_by_line_explanation": [
        {"line": 4, "explanation": "创建高考时间对象"},
        {"line": 6, "explanation": "计算时间差，返回 timedelta 对象"},
        {"line": 10, "explanation": "total_seconds() 得到总秒数"},
    ],
    "common_errors": [
        {"error": "strftime 和 strptime 搞混", "explanation": "strFtime = Format（格式化输出），strPtime = Parse（解析输入）"},
        {"error": "date 对象没有 hour 属性", "explanation": "date 只有年月日，没有时分秒。用 datetime 对象才有"},
    ],
    "order_index": 33,
    "estimated_minutes": 25,
}

LESSON_34 = {
    "title": "正则表达式入门",
    "summary": "学会用正则表达式匹配和提取文本中的模式",
    "objectives": [
        "理解正则表达式的作用",
        "掌握常用元字符",
        "学会 re.search / re.match / re.findall",
        "学会用分组提取数据",
        "学会 re.sub 替换文本",
    ],
    "content": """## 什么是正则表达式？

正则表达式（regex）是一种**模式匹配工具**。就像搜索框输入关键词，但正则能匹配"模式"而不是具体文字。

用途：验证手机号/邮箱、提取网页数据、文本替换、日志分析。

## 常用元字符

| 符号 | 含义 | 示例 |
|------|------|------|
| . | 任意字符（除换行） | a.b 匹配 "aab", "acb" |
| \\d | 数字 | \\d{3} 匹配 3 位数字 |
| \\w | 字母/数字/下划线 | \\w+ 匹配一个单词 |
| * | 0 次或多次 | ab*c 匹配 "ac", "abc", "abbbc" |
| + | 1 次或多次 | ab+c 匹配 "abc", "abbbc" |
| ? | 0 次或 1 次 | ab?c 匹配 "ac", "abc" |
| {n} | 恰好 n 次 | \\d{3} 匹配 3 位数字 |
| {n,m} | n 到 m 次 | \\d{2,4} 匹配 2-4 位数字 |
| ^ | 开头 | ^Hello 匹配以 Hello 开头 |
| $ | 结尾 | world$ 匹配以 world 结尾 |
| [] | 字符类 | [aeiou] 匹配任一元音 |
| () | 分组 | (ab)+ 匹配 "ab", "abab" |

## re 模块常用函数

```python
import re

text = "我的手机号是 13812345678，邮箱是 abc@example.com"

# re.search — 找第一个匹配
match = re.search(r"\\d{11}", text)
if match:
    print(match.group())  # 13812345678

# re.findall — 找所有匹配
phones = re.findall(r"\\d{11}", text)
print(phones)  # ['13812345678']

# re.sub — 替换
masked = re.sub(r"\\d{11}", "***", text)
print(masked)  # 我的手机号是 ***
```

## 分组提取

```python
# 提取邮箱的用户名和域名
text = "联系我：hello@python.org 或 admin@test.com"
pattern = r"(\\w+)@(\\w+\\.\\w+)"

matches = re.findall(pattern, text)
for user, domain in matches:
    print(f"用户名: {user}, 域名: {domain}")
```

## 贪婪 vs 非贪婪

```python
s = "<p>第一段</p><p>第二段</p>"

# 贪婪 .* — 尽量多匹配
print(re.findall(r"<p>.*</p>", s))
# ['<p>第一段</p><p>第二段</p>']

# 非贪婪 .*? — 尽量少匹配
print(re.findall(r"<p>.*?</p>", s))
# ['<p>第一段</p>', '<p>第二段</p>']
```
""",
    "analogy": "正则表达式就像描述嫌疑人的画像：不需要说出具体名字，只要描述特征——'身高 180 左右、戴眼镜、穿黑色外套'。\\d{11} 就是在说'连续 11 位数字'，不管是 13812345678 还是 15900001111，都符合这个画像。",
    "example_code": '''import re

# 从日志中提取 IP 地址和时间
log = """
2026-05-28 10:30:15 INFO 192.168.1.100 登录成功
2026-05-28 10:31:02 ERROR 10.0.0.55 连接超时
2026-05-28 10:32:18 INFO 172.16.0.1 数据同步完成
"""

# 提取所有 IP 地址
ips = re.findall(r"\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}", log)
print("IP 地址:", ips)

# 提取时间和日志级别
pattern = r"(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}) (\\w+)"
records = re.findall(pattern, log)
print("\\n日志记录:")
for time, level in records:
    print(f"  时间: {time}, 级别: {level}")''',
    "line_by_line_explanation": [
        {"line": 12, "explanation": "IP 地址模式：1-3 位数字，点，重复 4 次"},
        {"line": 16, "explanation": "分组提取日期时间和日志级别"},
    ],
    "common_errors": [
        {"error": "忘记用 r 前缀 → 反斜杠被 Python 转义", "explanation": "r'\\d' 是正确的；'\\d' 中的 \\d 可能被 Python 解释成其他字符"},
        {"error": ".* 贪婪匹配超出预期", "explanation": "默认 .* 尽量多匹配，用 .*? 变成非贪婪模式"},
    ],
    "order_index": 34,
    "estimated_minutes": 30,
}

LESSON_35 = {
    "title": "路径操作（pathlib）",
    "summary": "学会用 pathlib 优雅地处理文件路径和目录操作",
    "objectives": [
        "理解 pathlib 相比 os.path 的优势",
        "学会 Path 对象的基本操作",
        "学会遍历目录和查找文件",
        "学会创建和删除目录",
    ],
    "content": """## 为什么用 pathlib？

```python
# 旧方式（os.path）
import os
path = os.path.join("data", "users", "info.json")
dir_name = os.path.dirname(path)

# 新方式（pathlib）
from pathlib import Path
path = Path("data") / "users" / "info.json"
dir_name = path.parent
```

## Path 对象基础

```python
from pathlib import Path

p = Path("data/config/settings.json")

print(p.name)       # settings.json
print(p.stem)       # settings (不带后缀)
print(p.suffix)     # .json
print(p.parent)     # data/config
print(p.exists())   # 是否存在

# 当前目录和用户目录
print(Path.cwd())   # 当前工作目录
print(Path.home())  # 用户主目录
```

## 遍历目录

```python
# 列出所有 .py 文件
for py_file in Path(".").glob("*.py"):
    print(py_file)

# 递归查找
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# 遍历目录内容
for item in Path("data").iterdir():
    if item.is_file():
        print(f"文件: {item.name}")
    elif item.is_dir():
        print(f"目录: {item.name}/")
```

## 文件操作

```python
# 创建目录
Path("output/reports").mkdir(parents=True, exist_ok=True)

# 读写文件
content = Path("input.txt").read_text(encoding="utf-8")
Path("output.txt").write_text(content.upper(), encoding="utf-8")

# 删除文件
Path("temp.txt").unlink(missing_ok=True)

# 文件大小和修改时间
p = Path("large_file.bin")
if p.exists():
    print(f"大小: {p.stat().st_size} 字节")
```
""",
    "analogy": "如果 os.path 是用螺丝刀拆装路径，那 pathlib 就是乐高积木——用 / 自然拼接，用 .name、.parent 直接看各个部分。`base / 'src' / 'main.py'` 比 `os.path.join(base, 'src', 'main.py')` 好读得多。",
    "example_code": '''from pathlib import Path

# 分析当前项目结构
project = Path(".")
print(f"项目根目录: {project.resolve()}")

# 统计各类型文件数量
stats = {}
for f in project.rglob("*"):
    if f.is_file() and not any(p.startswith(".") for p in f.parts):
        ext = f.suffix or "无后缀"
        stats[ext] = stats.get(ext, 0) + 1

print("\\n文件类型统计:")
for ext, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
    print(f"  {ext}: {count} 个")''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "resolve() 获取绝对路径"},
        {"line": 9, "explanation": "rglob('*') 递归遍历，跳过隐藏文件"},
        {"line": 10, "explanation": "取文件后缀名进行统计"},
    ],
    "common_errors": [
        {"error": "Path 对象传给某些库报错", "explanation": "大部分标准库支持 Path，但第三方库可能只接受字符串。用 str(path) 转换"},
        {"error": "mkdir() 默认不创建父目录", "explanation": "用 parents=True 自动创建中间的目录"},
    ],
    "order_index": 35,
    "estimated_minutes": 25,
}

# ============================================================
# Module 8: 面向对象编程 (Lessons 36-40)
# ============================================================

LESSON_36 = {
    "title": "类与对象",
    "summary": "理解面向对象编程的核心概念，学会创建类与对象",
    "objectives": [
        "理解类和对象的关系",
        "学会定义类和方法",
        "理解 __init__ 构造方法",
        "理解 self 的含义",
    ],
    "content": """## 什么是面向对象编程？

OOP 是一种用"事物"来组织代码的编程范式。**类**是蓝图/模板，**对象**是按蓝图造出来的实例。

## 第一个类

```python
class Dog:
    # 类属性（所有实例共享）
    species = "犬科"

    def __init__(self, name, age):
        # 实例属性（每个实例不同）
        self.name = name
        self.age = age

    def bark(self):
        # 实例方法
        print(f"{self.name}：汪汪！")

    def info(self):
        print(f"{self.name} 今年 {self.age} 岁")

# 创建实例
my_dog = Dog("旺财", 3)
your_dog = Dog("小白", 1)

my_dog.bark()       # 旺财：汪汪！
my_dog.info()       # 旺财 今年 3 岁
your_dog.info()     # 小白 今年 1 岁
```

## self 是什么？

`self` 代表调用该方法的对象本身。方法定义时第一个参数必须是 `self`（约定名称）。

## 实战：银行账户

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存入 {amount} 元，余额: {self.balance} 元")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"取出 {amount} 元，余额: {self.balance} 元")
        else:
            print("余额不足或金额无效")

acc = BankAccount("小明", 1000)
acc.deposit(500)     # 存入 500 元，余额: 1500 元
acc.withdraw(200)    # 取出 200 元，余额: 1300 元
```
""",
    "analogy": "类 = 饼干模具，对象 = 用模具做出的饼干。模具规定了饼干的形状（属性和方法），但每个饼干可以用不同颜色的糖霜（不同的属性值）。同一个 Dog 类可以造出叫'旺财'的狗，也能造出叫'小白'的狗——结构一样，数据不同。",
    "example_code": '''class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"已添加: {task}")

    def complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"已完成: {self.tasks[index]['task']}")

    def show(self):
        print("\\n待办事项:")
        for i, t in enumerate(self.tasks):
            status = "X" if t["done"] else " "
            print(f"  [{status}] {i+1}. {t['task']}")
        done_cnt = sum(1 for t in self.tasks if t["done"])
        print(f"完成: {done_cnt}/{len(self.tasks)}")

todo = TodoList()
todo.add("学习 Python")
todo.add("完成作业")
todo.complete(0)
todo.show()''',
    "line_by_line_explanation": [
        {"line": 2, "explanation": "__init__ 初始化空任务列表"},
        {"line": 5, "explanation": "add 方法接收任务描述，存为字典"},
        {"line": 14, "explanation": "show 用 enumerate 遍历并显示状态"},
    ],
    "common_errors": [
        {"error": "忘记 self 参数 → TypeError", "explanation": "实例方法第一个参数必须是 self，Python 自动传入调用对象"},
        {"error": "直接访问 _private 属性 → AttributeError", "explanation": "以双下划线开头的属性是私有属性（name mangling），用 _name 约定表示不建议外部访问"},
    ],
    "order_index": 36,
    "estimated_minutes": 30,
}

LESSON_37 = {
    "title": "继承与多态",
    "summary": "学会用继承复用代码，用多态写出灵活的程序",
    "objectives": [
        "理解继承的概念",
        "学会方法重写（override）",
        "学会用 super() 调用父类方法",
        "理解多态的含义",
    ],
    "content": """## 继承：复用代码

```python
# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "......"

# 子类（派生类）
class Dog(Animal):
    def speak(self):  # 重写父类方法
        return f"{self.name}：汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name}：喵喵～"

dog = Dog("旺财")
cat = Cat("咪咪")
print(dog.speak())  # 旺财：汪汪！
print(cat.speak())  # 咪咪：喵喵～
```

## super()：调用父类方法

```python
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类 __init__
        self.breed = breed           # 子类特有属性
```

## 多态：同一个接口，不同行为

```python
# 多态：遍历不同类型的对象，调用相同方法
animals = [Dog("旺财"), Cat("咪咪"), Bird("小蓝")]
for animal in animals:
    print(animal.speak())  # 各自执行各自的 speak
```

"鸭子类型"：如果它走路像鸭子，叫起来像鸭子，那它就是鸭子。

## 实战：员工奖金系统

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # 程序员奖金更高

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.salary * 0.15 + self.team_size * 1000
```
""",
    "analogy": "继承就像家族遗传——孩子继承父母的特征（属性和方法），但也可以有自己的特点（重写和扩展）。多态就像家用电器：电视、冰箱、洗衣机各有各的'开关'，你不关心里面的电路怎么设计，只要按开关就行。不同的电器，同一个开关动作，各自做各自的事。",
    "example_code": '''import math

class Shape:
    def area(self):
        pass  # 子类负责实现

    def describe(self):
        return f"{self.__class__.__name__} 面积: {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2

# 多态：统一处理不同图形
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for s in shapes:
    print(s.describe())''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "Shape 是基类，定义接口"},
        {"line": 7, "explanation": "describe 是多态方法，用 __class__.__name__ 获取实际类名"},
        {"line": 25, "explanation": "多态：遍历不同类型图形，统一调用 describe"},
    ],
    "common_errors": [
        {"error": "忘写 super().__init__() → 父类属性未初始化", "explanation": "子类重写 __init__ 时需要用 super() 调用父类初始化"},
        {"error": "AttributeError: 'Cat' object has no attribute 'bark'", "explanation": "子类没有这个方法。检查方法名是否拼写有误"},
    ],
    "order_index": 37,
    "estimated_minutes": 30,
}

LESSON_38 = {
    "title": "魔术方法（__str__ 与 __repr__）",
    "summary": "掌握 Python 的魔术方法，让自定义对象像内置类型一样好用",
    "objectives": [
        "理解魔术方法的触发时机",
        "学会 __str__ 和 __repr__ 的区别",
        "学会 __len__, __getitem__, __contains__",
        "学会 __eq__, __lt__ 等比较方法",
    ],
    "content": """## 什么是魔术方法？

魔术方法（Dunder Methods）是 Python 中双下划线包围的特殊方法。它们让自定义类的对象**表现得像内置类型**。

## __str__ vs __repr__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # 给人看的
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        # 给开发者看的（可重现对象）
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 5)
print(p)         # Point(3, 5)      调用 __str__
print(repr(p))   # Point(x=3, y=5)  调用 __repr__
print([p])       # [Point(x=3, y=5)]  列表中用 __repr__
```

## 让对象像容器

```python
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)    # len(playlist)

    def __getitem__(self, index):
        return self.songs[index]  # playlist[0]

    def __contains__(self, song):
        return song in self.songs # "song" in playlist

    def __iter__(self):
        return iter(self.songs)   # for song in playlist

playlist = Playlist("收藏", ["稻香", "晴天", "夜曲"])
print(len(playlist))       # 3
print(playlist[0])         # 稻香
print("晴天" in playlist)   # True
```

## 比较魔术方法

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score  # ==

    def __lt__(self, other):
        return self.score < other.score   # <（排序用）

students = [Student("小明", 90), Student("小红", 95), Student("小刚", 85)]
students.sort()  # 自动调用 __lt__
for s in students:
    print(f"{s.name}({s.score})")
```

## 常用魔术方法速查

| 方法 | 触发 |
|------|------|
| __str__ | print(), str() |
| __repr__ | repr(), 调试显示 |
| __len__ | len() |
| __getitem__ | obj[key] |
| __contains__ | x in obj |
| __iter__ | for x in obj |
| __eq__ | == |
| __lt__ | <, sort() |
| __add__ | + |
""",
    "analogy": "魔术方法就像饭店厨房——外在你看菜单（print、len、[]），内在厨房的魔术方法（__str__、__len__、__getitem__）在干活。顾客不关心菜是怎么做的，但厨房必须知道每道菜的操作流程。",
    "example_code": '''class Card:
    """扑克牌"""
    SUITS = {"spades": "♠", "hearts": "♥", "diamonds": "♦", "clubs": "♣"}
    RANKS = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rank_str = self.RANKS.get(self.rank, str(self.rank))
        return f"{self.SUITS[self.suit]}{rank_str}"

    def __repr__(self):
        return f"Card('{self.suit}', {self.rank})"

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

hand = [Card("hearts", 1), Card("spades", 13), Card("diamonds", 7)]
hand.sort()
print("排序后:", hand)
print("最大:", max(hand))''',
    "line_by_line_explanation": [
        {"line": 9, "explanation": "__str__ 显示为 ♠K、♥A 等友好格式"},
        {"line": 13, "explanation": "__repr__ 返回可重现对象的字符串"},
        {"line": 16, "explanation": "点数相同即相等，不论花色"},
        {"line": 19, "explanation": "__lt__ 使牌可以排序"},
    ],
    "common_errors": [
        {"error": "__str__ 和 __repr__ 必须返回 str 类型", "explanation": "这两个方法必须返回 str，否则 raise TypeError"},
        {"error": "定义 __eq__ 后 __hash__ 变为 None", "explanation": "对象默认不可哈希。要在 set/dict key 中用需要额外定义 __hash__"},
    ],
    "order_index": 38,
    "estimated_minutes": 30,
}

LESSON_39 = {
    "title": "属性装饰器（@property）",
    "summary": "学会用 @property 优雅地实现属性的访问控制和计算属性",
    "objectives": [
        "理解 @property 的用途",
        "学会定义只读属性",
        "学会用 @setter 控制属性赋值",
        "理解封装的意义",
    ],
    "content": """## 为什么需要 @property？

有时候属性不能直接赋值——需要验证、转换、或根据其他属性计算。

```python
# 不用 @property
class Student:
    def get_name(self): return self._name
    def set_name(self, value):
        if not value.strip():
            raise ValueError("名字不能为空")
        self._name = value.strip()

# 用 @property ——更优雅
class Student:
    def __init__(self, name): self._name = name

    @property
    def name(self): return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("名字不能为空")
        self._name = value.strip()

s = Student("小明")
print(s.name)   # 小明 — 像访问属性一样
s.name = "小红"  # 触发 setter 验证
```

## 计算属性

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(c.area)            # 78.53975
print(c.circumference)   # 31.4159
# c.area = 100           # AttributeError！只读
```

## 实战：带验证的属性

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self): return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("年龄必须是整数")
        if value < 0 or value > 150:
            raise ValueError("年龄必须在 0 到 150 之间")
        self._age = value

    @property
    def is_adult(self):
        return self._age >= 18
```
""",
    "analogy": "@property 就像银行柜台——你想看余额（读），可以；但你不能直接把余额改成一百万（不能直接写），必须通过存款/取款流程。@property 把'获取'和'设置'分开控制，让你能加验证、转换、日志等中间逻辑。",
    "example_code": '''class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self._discount = 0

    @property
    def price(self):
        """实际售价 = 原价 × 折扣"""
        if self._discount > 0:
            return self._price * (1 - self._discount)
        return self._price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not 0 <= value <= 1:
            raise ValueError("折扣必须在 0~1 之间")
        self._discount = value
        print(f"已设置 {value*100:.0f}% 折扣")

p = Product("Python 教程", 99.00)
print(f"{p.name}: ¥{p.price}")
p.discount = 0.2  # 8 折
print(f"折后价: ¥{p.price}")
p.discount = 0    # 取消折扣
print(f"原价: ¥{p.price}")''',
    "line_by_line_explanation": [
        {"line": 7, "explanation": "price 是计算属性：根据 _discount 动态计算"},
        {"line": 16, "explanation": "折扣的 setter，验证值在 0~1 范围内"},
        {"line": 22, "explanation": "设置 20% 折扣，自动触发 setter 验证"},
    ],
    "common_errors": [
        {"error": "RecursionError: 无限递归", "explanation": "在 setter 里写 self.age = value 而不是 self._age = value，导致无限递归"},
        {"error": "忘写 @property 直接定义 setter → 语法错误", "explanation": "必须先定义 @property，再用 @name.setter"},
    ],
    "order_index": 39,
    "estimated_minutes": 25,
}

LESSON_40 = {
    "title": "数据类（dataclass）",
    "summary": "用 dataclass 简化数据模型的创建，减少样板代码",
    "objectives": [
        "理解 dataclass 解决的问题",
        "学会 @dataclass 装饰器",
        "掌握 field() 的高级用法",
        "比较 dataclass 和普通类",
    ],
    "content": """## 传统写法的痛点

```python
# 传统写法：大量重复代码
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
```

## dataclass 一行搞定

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int
    scores: list = None

# 自动生成 __init__, __repr__, __eq__！
s1 = Student("小明", 18, 3)
s2 = Student("小明", 18, 3)
print(s1)       # Student(name='小明', age=18, grade=3, scores=None)
print(s1 == s2) # True
```

## field() 的高级用法

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    # 可变默认值用 default_factory
    tags: list = field(default_factory=list)
    # 不参与比较
    id: int = field(compare=False, default=0)
    # 计算字段（不参与 __init__）
    total: float = field(init=False, default=0.0)

    def __post_init__(self):
        self.total = self.price * self.quantity
```

## 不可变数据类

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3, 5)
# p.x = 10  # FrozenInstanceError！不可变
```

### dataclass vs 普通类 vs namedtuple

| 特性 | dataclass | 普通类 | namedtuple |
|------|-----------|--------|------------|
| 可变 | ✓ | ✓ | ✗ |
| 自动 __init__ | ✓ | ✗ | ✓ |
| 自动 __repr__ | ✓ | ✗ | ✓ |
| 自动 __eq__ | ✓ | ✗ | ✓ |
| 类型注解 | ✓ | 手动 | ✗ |
""",
    "analogy": "dataclass 就像预制菜——食材（字段类型）备好，微波炉一转（加 @dataclass 装饰器），自动生成全套工具（__init__、__repr__、__eq__）。不用从零切菜调味，但味道完全可以定制。",
    "example_code": '''from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    title: str
    priority: int = 0
    done: bool = False
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("任务标题不能为空")

tasks = [
    Task("学习 dataclass", priority=3),
    Task("写作业", priority=1),
    Task("运动", priority=2, tags=["健康", "每日"]),
]

tasks.sort(key=lambda t: t.priority, reverse=True)
print("按优先级排序：")
for t in tasks:
    done_str = "X" if t.done else " "
    tags_str = f" [{', '.join(t.tags)}]" if t.tags else ""
    print(f"  [{done_str}] {t.title} (优先级{t.priority}){tags_str}")''',
    "line_by_line_explanation": [
        {"line": 12, "explanation": "__post_init__ 在 __init__ 后调用，用于验证"},
        {"line": 18, "explanation": "创建 Task 实例，自动获得 __init__"},
    ],
    "common_errors": [
        {"error": "mutable default not allowed", "explanation": "dataclass 不允许可变默认值，必须用 field(default_factory=list)"},
        {"error": "继承时字段顺序报错", "explanation": "有默认值的字段必须放在无默认值的字段之后"},
    ],
    "order_index": 40,
    "estimated_minutes": 30,
}
# ============================================================
# Module 9: 函数进阶与工程化 (Lessons 41-45)
# ============================================================

LESSON_41 = {
    "title": "装饰器（Decorator）",
    "summary": "理解装饰器的原理和用法，用装饰器增强函数功能",
    "objectives": [
        "理解函数是一等公民",
        "理解闭包的概念",
        "学会编写简单的装饰器",
        "学会带参数的装饰器",
    ],
    "content": """## 函数是一等公民

在 Python 中，函数可以像变量一样传递、赋值、作为参数：

```python
def greet(name):
    return f"你好，{name}！"

# 把函数赋值给变量
say_hello = greet
print(say_hello("小明"))  # 你好，小明！

# 把函数作为参数
def call_twice(func, arg):
    return func(arg) + " " + func(arg)
```

## 什么是装饰器？

装饰器是一个**接收函数、返回增强版函数**的函数。它在不修改原函数的情况下增加功能。

```python
def my_decorator(func):
    def wrapper():
        print("函数执行前...")
        func()
        print("函数执行后...")
    return wrapper

@my_decorator
def say_hello():
    print("你好！")

say_hello()
# 函数执行前...
# 你好！
# 函数执行后...
```

`@my_decorator` 等价于 `say_hello = my_decorator(say_hello)`。

## 处理参数的装饰器

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"返回 {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(3, 5))
# 调用 add((3, 5), {})
# 返回 8
```

## 实用装饰器：计时器

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时: {elapsed:.4f}s")
        return result
    return wrapper
```

## 带参数的装饰器

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def roll_dice():
    import random
    return random.randint(1, 6)

print(roll_dice())  # [4, 6, 1]
```

三层嵌套：`repeat(n)` → `decorator` → `wrapper`。

## 常用内置装饰器

| 装饰器 | 用途 |
|--------|------|
| @staticmethod | 静态方法（不需要 self） |
| @classmethod | 类方法（第一个参数是 cls） |
| @property | 属性装饰器 |
| @functools.wraps | 保留原函数的元信息 |
""",
    "analogy": "装饰器就像手机壳——手机（原函数）的功能不变，但加了保护、支架、卡槽（额外功能）。你换不同的壳就能获得不同的增强，手机本身不需要任何改动。",
    "example_code": '''import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    """失败自动重试的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[尝试 {attempt}/{max_attempts}] 失败: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def unstable_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("网络超时")
    return "数据获取成功！"

for i in range(3):
    print(f"\\n第{i+1}次请求:")
    try:
        print(unstable_call())
    except ConnectionError:
        print("请求最终失败")''',
    "line_by_line_explanation": [
        {"line": 4, "explanation": "retry 是带参数的装饰器工厂"},
        {"line": 7, "explanation": "@wraps(func) 保留原函数的 __name__ 和 __doc__"},
        {"line": 9, "explanation": "循环尝试，成功直接返回；最后一次失败则抛出异常"},
    ],
    "common_errors": [
        {"error": "装饰器返回 None → TypeError", "explanation": "装饰器必须返回一个函数（wrapper），忘记 return wrapper 就会返回 None"},
        {"error": "带参数的装饰器少了中间层", "explanation": "需要三层嵌套：@deco(args) -> def deco: def real_deco: def wrapper"},
    ],
    "order_index": 41,
    "estimated_minutes": 30,
}

LESSON_42 = {
    "title": "上下文管理器（with 语句）",
    "summary": "深入理解 with 语句的原理，学会自定义上下文管理器",
    "objectives": [
        "理解 with 语句的工作机制",
        "学会用类实现上下文管理器",
        "学会用 contextlib 实现上下文管理器",
        "了解上下文管理器的实际应用",
    ],
    "content": """## with 语句回顾

```python
# 自动关闭文件
with open("data.txt", "r") as f:
    content = f.read()
# 离开 with 块，f 自动关闭
```

`with` 保证无论是否发生异常，资源都会被正确释放。

## 用类实现上下文管理器

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭文件: {self.filename}")
        if self.file:
            self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```

- `__enter__`：进入 with 块时调用，返回值赋给 as 后的变量
- `__exit__`：退出 with 块时调用（即使有异常也调用）

## 用 contextlib 简化

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield  # 把控制权交给 with 块
    end = time.time()
    print(f"耗时: {end - start:.4f}s")

with timer():
    total = sum(range(10_000_000))
```

`yield` 之前 = 进入逻辑，`yield` 之后 = 退出逻辑。

## 实战：数据库事务

```python
@contextmanager
def transaction(conn):
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
        print("事务已提交")
    except Exception as e:
        conn.rollback()
        print(f"事务已回滚: {e}")
        raise
```
""",
    "analogy": "上下文管理器就像租车——你进店（__enter__）拿到车钥匙，开走。不管你是正常还车还是出了事故（异常），最后车都要还回店里（__exit__）。with 语句保证你不会忘记还车。",
    "example_code": '''from contextlib import contextmanager
import time

@contextmanager
def progress(description="处理中"):
    """显示进度的上下文管理器"""
    print(f"{description}...", end="", flush=True)
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f" 完成! (耗时 {elapsed:.2f}s)")

with progress("加载数据"):
    time.sleep(0.5)
    data = list(range(1000))

with progress("处理数据"):
    time.sleep(0.3)
    result = sum(data)

with progress("保存结果"):
    time.sleep(0.2)
    print(f"结果: {result}")''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "@contextmanager 把生成器变成上下文管理器"},
        {"line": 7, "explanation": "yield 之前：进入时执行"},
        {"line": 9, "explanation": "yield 之后：退出时执行"},
    ],
    "common_errors": [
        {"error": "__exit__ 返回 True 吞掉了异常", "explanation": "除非你有意处理异常，否则返回 None/False 让异常正常传播"},
        {"error": "AttributeError: __enter__", "explanation": "with 后面的对象必须实现 __enter__ 和 __exit__"},
    ],
    "order_index": 42,
    "estimated_minutes": 25,
}

LESSON_43 = {
    "title": "迭代器与生成器",
    "summary": "深入理解迭代器协议和生成器的强大功能",
    "objectives": [
        "理解迭代器协议（__iter__ / __next__）",
        "学会用 yield 创建生成器",
        "理解生成器表达式的用法",
        "理解生成器的内存优势",
    ],
    "content": """## 迭代器协议

任何实现了 `__iter__` 和 `__next__` 的对象都是迭代器。

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in CountDown(5):
    print(n, end=" ")  # 5 4 3 2 1
```

## 生成器：最简单的迭代器

```python
def countdown(start):
    while start > 0:
        yield start  # "产出"一个值，暂停执行
        start -= 1

for n in countdown(5):
    print(n, end=" ")  # 5 4 3 2 1
```

`yield` 暂停函数、记住状态，下次从暂停处继续。

## 生成器的内存优势

```python
# 列表：一次性把 100 万个数据加载到内存（~8MB）
squares_list = [i**2 for i in range(1_000_000)]

# 生成器：用多少算多少（~112 bytes）
squares_gen = (i**2 for i in range(1_000_000))
print(sum(squares_gen))  # 逐个计算，用完就丢
```

## 生成器表达式

```python
# 列表推导式 → 立刻求值，返回列表
squares_list = [x**2 for x in range(10)]

# 生成器表达式 → 惰性求值（注意是圆括号）
squares_gen = (x**2 for x in range(10))
print(sum(squares_gen))
```

## yield from

```python
def chain(*iterables):
    for it in iterables:
        yield from it

result = list(chain([1, 2], "ab", [10]))
print(result)  # [1, 2, 'a', 'b', 10]
```

`yield from it` 等价于 `for x in it: yield x`，但更高效。
""",
    "analogy": "生成器就像餐厅后厨的出菜口——不是一次性把 100 道菜全端出来（列表），而是做好一道递一道（yield）。食客来一道吃一道，厨房按需制作。既省了端菜的空间（内存），又支持无限菜品（无限序列）。",
    "example_code": '''def fibonacci(limit=None):
    """生成斐波那契数列（惰性无限）"""
    a, b = 0, 1
    count = 0
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("前 10 个斐波那契数:")
print(list(fibonacci(10)))

print("\\n不超过 1000 的:")
for n in fibonacci():
    if n > 1000:
        break
    print(n, end=" ")

print("\\n\\n偶数的平方:")
even_squares = (n**2 for n in fibonacci(10) if n % 2 == 0)
print(list(even_squares))''',
    "line_by_line_explanation": [
        {"line": 3, "explanation": "limit=None 表示可以无限生成"},
        {"line": 6, "explanation": "yield 返回当前值并暂停"},
        {"line": 13, "explanation": "无 limit 时可无限生成，用 break 控制结束"},
    ],
    "common_errors": [
        {"error": "生成器只能遍历一次 → 第二次遍历为空", "explanation": "生成器是'一次性'的。需要多次遍历时用 list() 转成列表"},
        {"error": "send non-None to just-started generator → TypeError", "explanation": "生成器必须先调用一次 next() 到达第一个 yield"},
    ],
    "order_index": 43,
    "estimated_minutes": 30,
}

LESSON_44 = {
    "title": "类型注解（Type Hints）",
    "summary": "学会用类型注解提高代码可读性和借助工具发现错误",
    "objectives": [
        "理解类型注解的用途",
        "掌握基本类型注解语法",
        "学会 List, Dict, Optional 等泛型",
        "了解 mypy 静态类型检查",
    ],
    "content": """## 为什么需要类型注解？

```python
# 没有类型注解：不清楚参数应该是什么
def calculate(price, quantity, discount):
    return price * quantity * (1 - discount)

# 有类型注解：一目了然
def calculate(price: float, quantity: int, discount: float) -> float:
    return price * quantity * (1 - discount)
```

类型注解不影响运行，但 IDE 能提供更好的补全和错误提示。

## 基本类型注解

```python
name: str = "小明"
age: int = 18
score: float = 95.5

def greet(name: str) -> str:
    return f"你好，{name}！"

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b
```

## 容器类型注解

```python
from typing import List, Dict, Set, Tuple, Optional, Union

names: List[str] = ["小明", "小红"]
scores: Dict[str, int] = {"小明": 90, "小红": 85}
tags: Set[str] = {"Python", "编程"}
point: Tuple[float, float] = (3.5, 2.0)

# Optional[X] = X 或 None
def find_user(id: int) -> Optional[str]:
    users = {1: "小明", 2: "小红"}
    return users.get(id)

# Union[X, Y] = X 或 Y
def process(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return str(value * 2)
    return value.upper()
```

## Python 3.10+ 新语法

```python
# 直接用内置类型（不需要 from typing import）
def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}

# | 代替 Union，| None 代替 Optional
def parse(value: int | str) -> str: ...
def maybe_get(key: str) -> str | None: ...
```

## mypy 静态检查

```bash
pip install mypy
mypy my_script.py
```

mypy 在运行前就能发现类型错误，像给你的代码配了一个自动代码审查员。
""",
    "analogy": "类型注解就像食品标签上的成分表——虽然没有标签也能吃（Python 动态类型一样运行），但有了标签你就能快速知道里面有什么（参数类型）、会产出什么（返回类型）。IDE 就是扫码枪，mypy 就是质检员。",
    "example_code": '''from typing import List
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    scores: List[int]

def analyze_class(students: List[Student]) -> dict:
    """分析班级成绩"""
    if not students:
        return {"error": "班级为空"}

    all_scores = [s for stu in students for s in stu.scores]
    student_avgs = [
        (stu.name, sum(stu.scores) / len(stu.scores) if stu.scores else 0)
        for stu in students
    ]

    return {
        "学生数": len(students),
        "班级平均分": sum(all_scores) / len(all_scores) if all_scores else 0,
        "最高分": max(all_scores) if all_scores else 0,
    }

class_1 = [
    Student("小明", [90, 85, 92]),
    Student("小红", [88, 95, 91]),
]
result = analyze_class(class_1)
for key, value in result.items():
    print(f"{key}: {value}")''',
    "line_by_line_explanation": [
        {"line": 7, "explanation": "参数类型 List[Student]，返回类型 dict"},
        {"line": 12, "explanation": "有类型注解后，推导式中的属性会被 IDE 识别"},
    ],
    "common_errors": [
        {"error": "类型注解导致运行错误？不，运行时完全忽略", "explanation": "类型注解只在静态检查时生效，运行时完全被忽略。即使注解 str，传入 int 也不会报错"},
        {"error": "typing.List 在 Python 3.9+ 已废弃", "explanation": "Python 3.9+ 可直接用 list[int]，不需要 typing.List"},
    ],
    "order_index": 44,
    "estimated_minutes": 25,
}

LESSON_45 = {
    "title": "虚拟环境与包管理",
    "summary": "学会用虚拟环境隔离项目依赖，掌握 pip 包管理",
    "objectives": [
        "理解虚拟环境的作用",
        "学会创建和激活虚拟环境",
        "掌握 pip 常用命令",
        "学会用 requirements.txt 管理依赖",
    ],
    "content": """## 为什么需要虚拟环境？

不同项目可能需要不同版本的同一个包：
- 项目 A 需要 Django 3.2（老项目维护）
- 项目 B 需要 Django 5.0（新项目开发）

都装在系统 Python 里就打架了。虚拟环境给每个项目独立的包空间。

## 创建和激活

```bash
# 创建虚拟环境
python -m venv myenv

# 激活（Mac/Linux）
source myenv/bin/activate

# 激活（Windows）
myenv\\Scripts\\activate

# 退出
deactivate
```

激活后终端前面会显示 `(myenv)`。

## pip 常用命令

```bash
# 安装
pip install requests
pip install requests==2.28.0     # 指定版本

# 卸载
pip uninstall requests

# 查看已安装
pip list
pip show requests                 # 查看某个包详情

# 升级
pip install --upgrade requests
```

## 管理项目依赖

```bash
# 导出当前环境的包列表
pip freeze > requirements.txt

# 在新环境中一键安装
pip install -r requirements.txt
```

### requirements.txt 示例

```
requests==2.28.0
flask>=3.0.0
numpy>=1.24.0,<2.0.0
```

## 项目结构最佳实践

```
my_project/
├── venv/              # 虚拟环境（不提交到 git）
├── .gitignore         # 忽略 venv/
├── requirements.txt   # 依赖列表
├── src/
│   └── main.py
└── README.md
```

## 国内镜像源（加速下载）

```bash
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```
""",
    "analogy": "虚拟环境就像为每道菜准备一套独立的调料瓶——做川菜用川菜的调料架，做粤菜用粤菜的调料架。两套调料互不干扰。requirements.txt 就是菜谱的食材清单，换个厨房照着单子买就行。",
    "example_code": '''"""项目依赖管理演示"""
import sys
import subprocess

print("Python 路径:", sys.executable)
print("是否在虚拟环境:", "venv" in sys.executable)

# 列出已安装的包
result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True, text=True
)
lines = result.stdout.split("\\n")
print("\\n已安装的包（前 10 个）:")
for line in lines[:11]:
    if line.strip():
        print(f"  {line}")''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "sys.executable 显示 Python 解释器路径"},
        {"line": 6, "explanation": "检查是否在虚拟环境中"},
        {"line": 9, "explanation": "用 subprocess 运行 pip list"},
    ],
    "common_errors": [
        {"error": "pip install 报 Permission denied", "explanation": "系统 Python 需要 sudo。更推荐用虚拟环境避免权限问题"},
        {"error": "导入包成功但 pip list 找不到 → 装到别的环境了", "explanation": "确认虚拟环境已激活，用 which python 检查路径"},
    ],
    "order_index": 45,
    "estimated_minutes": 20,
}

# ============================================================
# Module 10: 实战技能 (Lessons 46-50)
# ============================================================

LESSON_46 = {
    "title": "HTTP 请求与 API 调用",
    "summary": "学会用 requests 库发送 HTTP 请求和调用 Web API",
    "objectives": [
        "理解 HTTP 请求的基本概念",
        "学会用 requests 发送 GET/POST 请求",
        "学会处理 JSON 响应",
        "学会处理请求错误和超时",
    ],
    "content": """## HTTP 基础

HTTP 是浏览器和服务器之间的通信协议：
- **GET** — 获取数据（打开网页、搜索）
- **POST** — 提交数据（登录、表单、上传）

```bash
pip install requests
```

## 发送 GET 请求

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200 = 成功
print(response.headers["Content-Type"])
data = response.json()  # 解析 JSON
```

## 带参数的请求

```python
# GitHub API：搜索仓库
url = "https://api.github.com/search/repositories"
params = {"q": "python 爬虫", "sort": "stars"}

response = requests.get(url, params=params)
data = response.json()

print(f"共找到 {data['total_count']} 个仓库")
for repo in data["items"][:3]:
    print(f"  {repo['full_name']}: {repo['stargazers_count']} stars")
```

## 发送 POST 请求

```python
payload = {"username": "admin", "password": "123456"}
headers = {"User-Agent": "MyApp/1.0"}

response = requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers=headers
)
print(response.json())
```

## 处理错误和超时

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # 状态码不是 200 就抛异常
    data = response.json()
except requests.exceptions.Timeout:
    print("请求超时！")
except requests.exceptions.ConnectionError:
    print("网络连接失败！")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误: {e}")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
```
""",
    "analogy": "HTTP 请求就像点外卖——你（客户端）通过手机下单（发送请求），告诉店家你要什么（URL + 参数），店家（服务器）做好后给你送来（返回响应）。GET 是'看看菜单'，POST 是'下单付款'。",
    "example_code": '''import requests

def get_quote():
    """获取随机名言"""
    try:
        resp = requests.get(
            "https://api.quotable.io/random",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()
        return f'"{data["content"]}"\\n  -- {data["author"]}'
    except requests.exceptions.RequestException as e:
        return f"获取失败: {e}"

def get_github_user(username):
    """获取 GitHub 用户信息"""
    url = f"https://api.github.com/users/{username}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        user = resp.json()
        return {
            "用户名": user["login"],
            "仓库数": user["public_repos"],
            "关注者": user["followers"],
        }
    except requests.exceptions.RequestException as e:
        return {"错误": str(e)}

print("今日名言:")
print(get_quote())

print("\\nGitHub 用户信息:")
info = get_github_user("torvalds")
for key, value in info.items():
    print(f"  {key}: {value}")''',
    "line_by_line_explanation": [
        {"line": 6, "explanation": "使用免费 API 获取随机名言"},
        {"line": 9, "explanation": "raise_for_status() 检查状态码"},
        {"line": 15, "explanation": "用 f-string 拼接 GitHub API URL"},
    ],
    "common_errors": [
        {"error": "ModuleNotFoundError: requests", "explanation": "pip install requests，注意在虚拟环境中安装"},
        {"error": "SSL 证书错误", "explanation": "公司内网可能有代理。正确做法是配置代理或证书，而不是 verify=False"},
    ],
    "order_index": 46,
    "estimated_minutes": 25,
}

LESSON_47 = {
    "title": "数据库操作（sqlite3）",
    "summary": "学会用 Python 内置的 sqlite3 进行数据库操作",
    "objectives": [
        "理解关系型数据库的基本概念",
        "学会创建数据库和表",
        "学会增删改查（CRUD）操作",
        "学会参数化查询防止 SQL 注入",
    ],
    "content": """## SQLite 简介

SQLite 是 Python 自带的轻量级数据库，数据存在单个文件中。手机 App、浏览器、桌面软件都在用。

```python
import sqlite3

conn = sqlite3.connect("my_app.db")  # 连接数据库（自动创建）
cursor = conn.cursor()               # 获取游标
```

## CRUD 操作

### 建表（CREATE）

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        score REAL DEFAULT 0.0
    )
''')
conn.commit()
```

### 插入数据（INSERT）

```python
# 参数化查询（? 占位符）防 SQL 注入！
cursor.execute(
    "INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
    ("小明", 18, 90.5)
)

# 批量插入
students = [("小红", 20, 88.0), ("小刚", 19, 95.5)]
cursor.executemany(
    "INSERT INTO students (name, age, score) VALUES (?, ?, ?)",
    students
)
conn.commit()
```

**永远用参数化查询，不要用字符串拼接！**

### 查询数据（SELECT）

```python
# 查询所有
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# 条件查询
cursor.execute(
    "SELECT name, score FROM students WHERE score > ?", (85,)
)
for name, score in cursor.fetchall():
    print(f"{name}: {score}")

# 查一条
cursor.execute("SELECT * FROM students WHERE id = ?", (1,))
student = cursor.fetchone()
```

### 更新和删除

```python
cursor.execute(
    "UPDATE students SET score = ? WHERE name = ?", (99.0, "小明")
)
cursor.execute("DELETE FROM students WHERE id = ?", (3,))
conn.commit()
```

### 统计查询

```python
cursor.execute("SELECT COUNT(*) FROM students")
cursor.execute("SELECT AVG(score) FROM students")
cursor.execute(
    "SELECT name, score FROM students ORDER BY score DESC LIMIT 3"
)
```
""",
    "analogy": "SQLite 数据库就像一个 Excel 文件——一个文件里有多张表（Sheet），每张表有列名（字段）和多行数据。connect 是双击打开，execute 是操作单元格，commit 是 Ctrl+S 保存。",
    "example_code": '''import sqlite3

# 内存数据库（演示用）
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        score REAL NOT NULL
    )
""")

data = [
    ("小明", "语文", 90), ("小明", "数学", 85), ("小明", "英语", 92),
    ("小红", "语文", 88), ("小红", "数学", 95), ("小红", "英语", 91),
    ("小刚", "语文", 76), ("小刚", "数学", 82), ("小刚", "英语", 79),
]
cursor.executemany(
    "INSERT INTO scores (name, subject, score) VALUES (?, ?, ?)", data
)
conn.commit()

print("平均分排名：")
cursor.execute("""
    SELECT name, ROUND(AVG(score), 1) as avg_score
    FROM scores
    GROUP BY name
    ORDER BY avg_score DESC
""")
for row in cursor:
    print(f"  {row[0]}: {row[1]} 分")

print("\\n各科最高分：")
cursor.execute("""
    SELECT subject, MAX(score), name
    FROM scores
    GROUP BY subject
""")
for row in cursor:
    print(f"  {row[0]}: {row[1]} 分 ({row[2]})")

conn.close()''',
    "line_by_line_explanation": [
        {"line": 4, "explanation": ":memory: 在内存中创建临时数据库"},
        {"line": 17, "explanation": "executemany 批量插入多行"},
        {"line": 22, "explanation": "GROUP BY 分组，AVG 计算平均分"},
        {"line": 29, "explanation": "MAX 找最高分，按科目分组"},
    ],
    "common_errors": [
        {"error": "sqlite3.OperationalError: no such table", "explanation": "表还没创建就查询。确保先 CREATE TABLE"},
        {"error": "忘记 commit → 数据没保存", "explanation": "INSERT/UPDATE/DELETE 后必须 conn.commit()"},
    ],
    "order_index": 47,
    "estimated_minutes": 30,
}

LESSON_48 = {
    "title": "命令行工具（argparse）",
    "summary": "学会用 argparse 创建专业的命令行工具",
    "objectives": [
        "理解命令行参数的作用",
        "学会定义位置参数和可选参数",
        "学会参数类型和默认值",
        "学会子命令（subparsers）",
    ],
    "content": """## 什么是命令行工具？

```bash
python script.py           # python 是程序，script.py 是参数
pip install requests       # install 和 requests 都是参数
git commit -m "message"    # -m 是可选参数
```

argparse 让你的 Python 脚本也能接受这些参数。

## 最简示例

```python
import argparse

parser = argparse.ArgumentParser(description="问候程序")
parser.add_argument("name", help="你的名字")
args = parser.parse_args()

print(f"你好，{args.name}！")
```

`--help` 自动生成！

## 位置参数 vs 可选参数

```python
parser = argparse.ArgumentParser(description="文件处理工具")

# 位置参数（必须提供）
parser.add_argument("filename", help="要处理的文件")

# 可选参数（-- 开头）
parser.add_argument("-o", "--output", default="output.txt")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-n", "--count", type=int, default=1)
```

## 参数类型和限制

```python
# 整数/浮点数
parser.add_argument("-p", "--port", type=int, default=8000)
parser.add_argument("-t", "--threshold", type=float, default=0.5)

# 限定选项
parser.add_argument(
    "--level",
    choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    default="INFO"
)
```

## 子命令（像 git 一样）

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="添加任务")
add_parser.add_argument("title")
add_parser.add_argument("-p", "--priority", type=int, default=0)

list_parser = subparsers.add_parser("list", help="列出任务")

args = parser.parse_args()

if args.command == "add":
    print(f"添加任务: {args.title}")
elif args.command == "list":
    print("列出任务")
```
""",
    "analogy": "argparse 就像给程序装了一个接待台——用户通过参数告诉接待员要做什么。位置参数是必填项（像'名字'必须写），可选参数像备注（不写就用默认值）。子命令就像公司的不同部门，先选部门再办业务。",
    "example_code": '''import argparse
import json
from pathlib import Path
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="简易日记工具")
    subparsers = parser.add_subparsers(dest="cmd")

    add_p = subparsers.add_parser("add", help="添加日记")
    add_p.add_argument("content", help="日记内容")
    add_p.add_argument("-t", "--tag", help="标签")

    list_p = subparsers.add_parser("list", help="列出日记")
    list_p.add_argument("-n", "--count", type=int, default=5)

    search_p = subparsers.add_parser("search", help="搜索日记")
    search_p.add_argument("keyword", help="搜索关键词")

    args = parser.parse_args()
    diary_file = Path("diary.json")

    entries = json.loads(diary_file.read_text()) if diary_file.exists() else []

    if args.cmd == "add":
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "content": args.content,
            "tag": args.tag or "无"
        }
        entries.append(entry)
        diary_file.write_text(json.dumps(entries, ensure_ascii=False, indent=2))
        print(f"已添加: {args.content}")

    elif args.cmd == "list":
        for e in entries[-args.count:]:
            print(f"[{e['time']}] ({e['tag']}) {e['content']}")

    elif args.cmd == "search":
        results = [e for e in entries if args.keyword in e['content']]
        print(f"找到 {len(results)} 条:")
        for e in results:
            print(f"  [{e['time']}] {e['content']}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()''',
    "line_by_line_explanation": [
        {"line": 8, "explanation": "add 子命令：content 位置参数，tag 可选参数"},
        {"line": 21, "explanation": "从 JSON 文件读取已有日记"},
        {"line": 23, "explanation": "添加日记条目并保存到 JSON"},
    ],
    "common_errors": [
        {"error": "SystemExit: 2 → 参数解析失败", "explanation": "命令行参数不符合定义，argparse 自动打印帮助并退出"},
        {"error": "Namespace 没有某属性 → 访问了未定义的参数", "explanation": "检查 add_argument 的 dest 名称"},
    ],
    "order_index": 48,
    "estimated_minutes": 25,
}

LESSON_49 = {
    "title": "并发编程入门（threading 与 asyncio）",
    "summary": "了解并发编程的基本概念，学会用多线程和异步 IO 提升效率",
    "objectives": [
        "理解并发与并行的区别",
        "学会用 threading 创建多线程",
        "了解 asyncio 的基本用法",
        "知道何时用线程、何时用异步",
    ],
    "content": """## 并发 vs 并行

- **并发**：交替执行多个任务（一个 CPU 核快速切换）
- **并行**：同时执行多个任务（多个 CPU 核同时工作）

Python 因 GIL（全局解释器锁），多线程不能真正并行——但 I/O 密集型任务（网络请求、文件读写）仍能大幅提速。

## threading 多线程

```python
import threading
import time

def worker(name, delay):
    print(f"{name} 开始工作")
    time.sleep(delay)  # 模拟 I/O 等待
    print(f"{name} 完成")

t1 = threading.Thread(target=worker, args=("线程1", 2))
t2 = threading.Thread(target=worker, args=("线程2", 1))

t1.start()  # 启动线程
t2.start()
t1.join()   # 等待完成
t2.join()
print("全部完成")
```

## 线程池：批量处理

```python
from concurrent.futures import ThreadPoolExecutor

def download(url):
    time.sleep(1)  # 模拟下载
    return f"{url} 下载完成"

urls = ["url1", "url2", "url3", "url4", "url5"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download, urls)

for result in results:
    print(result)
```

## asyncio 异步编程

```python
import asyncio

async def fetch_data(name, delay):
    print(f"开始获取 {name}")
    await asyncio.sleep(delay)  # 模拟异步 I/O
    print(f"{name} 获取完成")
    return f"{name} 的数据"

async def main():
    results = await asyncio.gather(
        fetch_data("用户信息", 2),
        fetch_data("订单列表", 1),
        fetch_data("商品详情", 1.5),
    )
    print(f"所有结果: {results}")

asyncio.run(main())
```

## 什么时候用什么？

| 场景 | 推荐方案 |
|------|---------|
| 网络请求（下载、爬虫） | threading 或 asyncio |
| 文件读写（多文件） | threading |
| CPU 密集计算 | multiprocessing |
| Web 服务器 | asyncio (FastAPI) |
| 简单并发 | ThreadPoolExecutor |
""",
    "analogy": "并发就是餐厅服务员——一个服务员不能同时炒 10 道菜（CPU 密集），但可以同时接待 10 桌客人（I/O 密集）：给 A 桌点菜，去 B 桌上菜，给 C 桌结账。等待时不占 CPU，所以一个人就能服务很多桌。",
    "example_code": '''import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_website(url):
    """模拟检查网站是否可访问"""
    import random
    delay = random.uniform(0.3, 1.0)
    time.sleep(delay)
    is_ok = random.random() > 0.2
    return url, is_ok, delay

websites = [f"https://example{i}.com" for i in range(1, 11)]

print("开始批量检查网站...")
start = time.time()

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(check_website, url): url for url in websites}
    for future in as_completed(futures):
        url, is_ok, delay = future.result()
        status = "OK" if is_ok else "FAIL"
        print(f"  {url}: {status} (响应: {delay:.2f}s)")

elapsed = time.time() - start
print(f"\\n检查 {len(websites)} 个网站，总耗时: {elapsed:.2f} 秒")
print(f"同步方式需要约: {len(websites) * 0.65:.1f} 秒")''',
    "line_by_line_explanation": [
        {"line": 14, "explanation": "ThreadPoolExecutor 创建最多 5 个并发线程"},
        {"line": 16, "explanation": "as_completed 按完成顺序迭代"},
        {"line": 21, "explanation": "10 个网站并发检查，只需约 1.3 秒"},
    ],
    "common_errors": [
        {"error": "多线程数据竞争：结果不一致", "explanation": "多个线程同时修改共享数据会导致不可预期的结果。用 queue.Queue 或 threading.Lock"},
        {"error": "asyncio 中用了 time.sleep → 阻塞整个事件循环", "explanation": "在 async 函数中必须用 await asyncio.sleep()"},
    ],
    "order_index": 49,
    "estimated_minutes": 25,
}

LESSON_50 = {
    "title": "Python 生态与进阶路线",
    "summary": "了解 Python 丰富生态和进阶学习路线，规划你的编程成长之路",
    "objectives": [
        "了解 Python 主流应用领域",
        "知道重要的第三方库",
        "了解代码质量和最佳实践",
        "规划自己的学习路线",
    ],
    "content": """## Python 应用领域

### Web 开发
| 框架 | 特点 |
|------|------|
| Django | 全栈框架，自带 ORM/Admin |
| Flask | 轻量灵活，插件丰富 |
| FastAPI | 异步、自动文档、高性能 |

### 数据科学
| 库 | 用途 |
|----|------|
| NumPy | 数值计算、多维数组 |
| Pandas | 数据分析、表格处理 |
| Matplotlib | 数据可视化 |
| Scikit-learn | 机器学习 |

### 自动化与爬虫
| 库 | 用途 |
|----|------|
| Selenium | 浏览器自动化 |
| Scrapy | 爬虫框架 |
| OpenPyXL | Excel 操作 |

### AI / 深度学习
| 库 | 用途 |
|----|------|
| PyTorch | 深度学习 |
| LangChain | LLM 应用开发 |

## 代码质量工具

```bash
pip install black     # 代码格式化
pip install flake8    # 代码检查
pip install mypy      # 类型检查
```

## 推荐的进阶路线

```
阶段 1: 基础语法 ✓ (你现在在这里！)
  - 变量、条件、循环、数据结构
  - 函数、面向对象、文件操作

阶段 2: 工程化
  - Git 版本控制
  - 单元测试 (pytest)
  - 虚拟环境 & 包管理

阶段 3: 专业方向
  - Web 后端: Django / FastAPI
  - 数据分析: Pandas + NumPy
  - 自动化: 爬虫 + 脚本

阶段 4: 高手进阶
  - 设计模式 & 系统设计
  - 性能优化
  - 开源贡献
```

## 如何持续进步？

1. **做项目**：编程是"做"会的，不是"看"会的。每学一部分就做一个项目
2. **读代码**：阅读优秀开源项目的源码，学习设计和风格
3. **写博客**：把学到的东西写下来，教别人是最好的学习方式
4. **参与开源**：从提 issue、修 typo 开始，逐渐参与功能开发
5. **保持好奇**：技术更新很快，但基础原理不变。理解"为什么"比"怎么做"更重要
""",
    "analogy": "Python 学习就像学做菜——前 50 节课你学会了刀工、火候、各种烹饪技巧（基础语法到高级特性）。现在你可以选择成为中餐大厨（Web 开发）、甜品师（数据科学）、或日料师傅（AI 开发）。每个方向有自己的工具和技法，但基础刀工是通用的。最重要的是——多下厨，多实践！",
    "example_code": '''"""
Python 50 节课学习总结
"""
from dataclasses import dataclass
from typing import List
import json
from pathlib import Path

@dataclass
class LearningGoal:
    topic: str
    completed: bool = False
    notes: str = ""

class PythonJourney:
    def __init__(self, name):
        self.name = name
        self.goals = [
            LearningGoal("基础语法", True, "变量、条件、循环"),
            LearningGoal("数据结构", True, "列表、字典、集合"),
            LearningGoal("函数与文件", True, "函数、文件读写"),
            LearningGoal("面向对象", False, "类、继承、多态"),
            LearningGoal("实战项目", False, "API、数据库、CLI"),
        ]

    def progress(self):
        done = sum(1 for g in self.goals if g.completed)
        total = len(self.goals)
        pct = done / total * 100
        bar = "#" * int(pct / 10) + "-" * (10 - int(pct / 10))
        print(f"\\n{self.name} 的学习进度")
        print(f"[{bar}] {pct:.0f}% ({done}/{total})\\n")

    def show_goals(self):
        for g in self.goals:
            status = "X" if g.completed else " "
            print(f"  [{status}] {g.topic}: {g.notes}")

    def save(self):
        data = {
            "name": self.name,
            "goals": [
                {"topic": g.topic, "completed": g.completed, "notes": g.notes}
                for g in self.goals
            ]
        }
        Path("journey.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2)
        )
        print("进度已保存到 journey.json")

journey = PythonJourney("小明")
journey.progress()
journey.show_goals()
journey.save()

print("\\n恭喜你完成了 Python 从入门到精通的所有课程！")
print("这只是开始——真正的编程能力在项目中成长。加油！")''',
    "line_by_line_explanation": [
        {"line": 5, "explanation": "dataclass — 第 40 课"},
        {"line": 15, "explanation": "面向对象 — 第 36-37 课"},
        {"line": 27, "explanation": "列表推导式 + 生成器"},
        {"line": 40, "explanation": "pathlib + JSON — 第 32、35 课"},
    ],
    "common_errors": [
        {"error": "学了这么多还是写不出大项目", "explanation": "大项目 = 小模块的组装。把需求拆成独立的小功能，逐个实现"},
        {"error": "追求学完所有库 → 学不完也没用", "explanation": "不要追求学完所有工具，需要什么学什么。基础扎实了，学新库就是看文档的事"},
    ],
    "order_index": 50,
    "estimated_minutes": 20,
}

LESSONS = [
    LESSON_1, LESSON_2, LESSON_3, LESSON_4, LESSON_5,
    LESSON_6, LESSON_7, LESSON_8, LESSON_9, LESSON_10,
    LESSON_11, LESSON_12, LESSON_13, LESSON_14, LESSON_15,
    LESSON_16, LESSON_17, LESSON_18, LESSON_19, LESSON_20,
    LESSON_21, LESSON_22, LESSON_23, LESSON_24, LESSON_25,
    LESSON_26, LESSON_27, LESSON_28, LESSON_29, LESSON_30,
    LESSON_31, LESSON_32, LESSON_33, LESSON_34, LESSON_35,
    LESSON_36, LESSON_37, LESSON_38, LESSON_39, LESSON_40,
    LESSON_41, LESSON_42, LESSON_43, LESSON_44, LESSON_45,
    LESSON_46, LESSON_47, LESSON_48, LESSON_49, LESSON_50,
]

COURSES = [COURSE, COURSE_2]
