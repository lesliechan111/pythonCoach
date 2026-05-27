"""
种子数据 - 20 节完整 Python 零基础课程

课程结构:
- Module 1 (1-5): 入门基础
- Module 2 (6-10): 流程控制
- Module 3 (11-15): 数据结构
- Module 4 (16-20): 函数与文件
"""

COURSE = {
    "title": "Python 零基础入门",
    "description": "从零开始系统学习 Python，无需任何编程基础。20 节课涵盖变量、条件、循环、列表、字典、函数等核心知识，学完即可独立编写实用程序。",
    "category": "python_basic",
    "level": "beginner",
    "order_index": 1,
    "estimated_minutes": 600,
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

LESSONS = [
    LESSON_1, LESSON_2, LESSON_3, LESSON_4, LESSON_5,
    LESSON_6, LESSON_7, LESSON_8, LESSON_9, LESSON_10,
    LESSON_11, LESSON_12, LESSON_13, LESSON_14, LESSON_15,
    LESSON_16, LESSON_17, LESSON_18, LESSON_19, LESSON_20,
]
