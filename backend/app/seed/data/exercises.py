"""
种子数据 - 100 道练习题 (20 节课 × 5 题)
6 种题型: choice, judge, fill_blank, code_completion, code_fix, programming
"""

# ============================================================
# Lesson 1: Python 是什么，能做什么
# ============================================================
EXERCISES_LESSON_1 = [
    {
        "type": "choice",
        "title": "Python 的创始人是谁？",
        "description": "选择正确答案",
        "options": [
            {"label": "A", "text": "Guido van Rossum"},
            {"label": "B", "text": "Linus Torvalds"},
            {"label": "C", "text": "Bill Gates"},
            {"label": "D", "text": "Steve Jobs"},
        ],
        "answer": "A",
        "explanation": "Guido van Rossum（龟叔）在 1991 年创造了 Python。名字来源于他喜欢的英国喜剧 Monty Python's Flying Circus，跟蛇没有关系。",
        "difficulty": "easy",
        "tags": ["Python", "历史"],
    },
    {
        "type": "judge",
        "title": "Python 只能用来做数据分析和 AI",
        "description": "判断下列说法是否正确",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。Python 的应用非常广泛，除了数据分析和 AI，还能做 Web 开发、自动化办公、爬虫、游戏开发等。可以说几乎所有领域都能用到 Python。",
        "difficulty": "easy",
        "tags": ["Python", "应用场景"],
    },
    {
        "type": "fill_blank",
        "title": "Python 的名字来源于什么？",
        "description": "填写正确答案",
        "answer": "喜剧",
        "explanation": "Python 的创始人是英国喜剧 Monty Python's Flying Circus 的粉丝，所以用 Monty Python 给这门语言命名，跟蛇（python 英文意为蟒蛇）没有直接关系。",
        "difficulty": "medium",
        "tags": ["Python", "命名"],
    },
    {
        "type": "choice",
        "title": "以下哪个不是 Python 的典型应用场景？",
        "description": "选出不是 Python 擅长领域的选项",
        "options": [
            {"label": "A", "text": "自动化办公"},
            {"label": "B", "text": "数据分析"},
            {"label": "C", "text": "操作系统内核开发"},
            {"label": "D", "text": "Web 网站开发"},
        ],
        "answer": "C",
        "explanation": "操作系统内核开发通常使用 C 语言等底层语言。Python 虽然功能强大，但不适合做操作系统内核这种需要直接操作硬件的底层开发。",
        "difficulty": "medium",
        "tags": ["Python", "应用场景"],
    },
    {
        "type": "judge",
        "title": "Python 的语法比较接近英文，对新手友好",
        "description": "判断下列说法是否正确",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "A",
        "explanation": "正确。Python 的设计理念之一就是可读性，语法接近自然语言（英文），代码结构清晰，是目前公认最适合新手入门的编程语言之一。",
        "difficulty": "easy",
        "tags": ["Python", "特点"],
    },
]

# ============================================================
# Lesson 2: 安装环境与运行第一个程序
# ============================================================
EXERCISES_LESSON_2 = [
    {
        "type": "fill_blank",
        "title": "print() 函数的功能是什么？",
        "description": "用中文回答：print('Hello') 会做什么？",
        "answer": "输出Hello",
        "explanation": "print() 是 Python 的输出函数，括号里的内容会显示在屏幕上。print('Hello') 会在屏幕上显示 Hello。",
        "difficulty": "easy",
        "tags": ["print", "基础"],
    },
    {
        "type": "code_fix",
        "title": "修复 print 语法错误",
        "description": "下面的代码不能运行，请写出正确的代码",
        "answer": 'print("Hello, World!")',
        "explanation": "print（'Hello'）用了中文括号，Python 只识别英文标点。正确写法：print(\"Hello, World!\") 或 print('Hello, World!')。",
        "difficulty": "easy",
        "tags": ["print", "语法"],
    },
    {
        "type": "choice",
        "title": "以下哪个是合法的 Python 文件名？",
        "description": "Python 源文件的后缀名是什么？",
        "options": [
            {"label": "A", "text": "hello.py"},
            {"label": "B", "text": "hello.txt"},
            {"label": "C", "text": "hello.java"},
            {"label": "D", "text": "hello.python"},
        ],
        "answer": "A",
        "explanation": "Python 源文件的后缀名是 .py。.txt 是文本文件，.java 是 Java 文件。",
        "difficulty": "easy",
        "tags": ["文件", "基础"],
    },
    {
        "type": "fill_blank",
        "title": "运行 Python 程序的命令",
        "description": "在终端执行 Python 文件 hello.py，命令是什么？（填 python 或 python3）",
        "answer": "python",
        "explanation": "Windows 通常用 python hello.py，Mac 有时需要用 python3 hello.py。两种都可以。",
        "difficulty": "easy",
        "tags": ["命令行", "基础"],
    },
    {
        "type": "code_completion",
        "title": "补全第一个 Python 程序",
        "description": "补全代码，在屏幕上显示 '我学会了！'",
        "answer": 'print("我学会了！")',
        "explanation": "输出内容用 print() 函数，文字要放在引号里。print(\"我学会了！\") 就能在屏幕上显示这句话。",
        "difficulty": "easy",
        "tags": ["print", "基础"],
    },
]

# ============================================================
# Lesson 3: 变量与数据类型
# ============================================================
EXERCISES_LESSON_3 = [
    {
        "type": "choice",
        "title": "以下哪个是正确的变量赋值？",
        "description": "选出语法正确的选项",
        "options": [
            {"label": "A", "text": "1name = '小明'"},
            {"label": "B", "text": "name = '小明'"},
            {"label": "C", "text": "name == '小明'"},
            {"label": "D", "text": "def = '小明'"},
        ],
        "answer": "B",
        "explanation": "变量名不能以数字开头（A），= 是赋值不是 ==（C），def 是关键字不能用（D）。只有 B 正确。",
        "difficulty": "easy",
        "tags": ["变量", "命名"],
    },
    {
        "type": "fill_blank",
        "title": "type(42) 的返回值是什么？",
        "description": "写出 type(42) 的 Python 类型名（英文）",
        "answer": "int",
        "explanation": "42 是整数，type(42) 返回 <class 'int'>。整数类型在 Python 中称为 int。",
        "difficulty": "medium",
        "tags": ["数据类型", "type"],
    },
    {
        "type": "judge",
        "title": "Python 变量必须先声明类型才能使用",
        "description": "判断：name = '小明' 之前需要写 string name 来声明类型",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。Python 是动态类型语言，变量不需要声明类型。直接 name = '小明' 就行，Python 会自动推断 name 是字符串类型。",
        "difficulty": "easy",
        "tags": ["变量", "动态类型"],
    },
    {
        "type": "code_completion",
        "title": "交换两个变量的值",
        "description": "补全代码，交换 a 和 b 的值",
        "answer": "a, b = b, a",
        "explanation": "Python 支持一行交换变量：a, b = b, a。这是 Python 特有的简洁写法，利用了元组解包的特性。",
        "difficulty": "medium",
        "tags": ["变量", "交换"],
    },
    {
        "type": "programming",
        "title": "自我介绍程序",
        "description": "创建 name 和 age 两个变量，分别存入你的名字和年龄，然后用 print() 输出一句话：\"我叫 xxx，今年 x 岁\"",
        "answer": 'name = "小明"\nage = 18\nprint(f"我叫{name}，今年{age}岁")',
        "explanation": "这是变量最基础的使用方式。先定义变量存储信息，再用 f-string 格式化输出。字符串要加引号，数字不用。",
        "difficulty": "easy",
        "tags": ["变量", "print", "f-string"],
    },
]

# ============================================================
# Lesson 4: 字符串操作
# ============================================================
EXERCISES_LESSON_4 = [
    {
        "type": "fill_blank",
        "title": "字符串拼接",
        "description": "\"Hello\" + \" \" + \"World\" 的结果是什么？(注意引号)",
        "answer": "Hello World",
        "explanation": "用 + 号拼接字符串：\"Hello\" + \" \" + \"World\" = \"Hello World\"。中间加了一个空格字符串。",
        "difficulty": "easy",
        "tags": ["字符串", "拼接"],
    },
    {
        "type": "code_fix",
        "title": "修复 f-string 语法",
        "description": "name = '小明'，下面代码报错，请修正：print(f'我叫{name}，今年' + age + '岁')",
        "answer": 'print(f"我叫{name}，今年{age}岁")',
        "explanation": "原代码有两个问题：1) age 如果不在 f-string 里面就不能自动转字符串，2) 字符串和数字不能直接拼接。全部放进 f-string 就解决了。",
        "difficulty": "medium",
        "tags": ["f-string", "字符串"],
    },
    {
        "type": "choice",
        "title": "\"Python\"[-1] 的值是什么？",
        "description": "字符串索引从 0 开始，-1 表示最后一个字符",
        "options": [
            {"label": "A", "text": "P"},
            {"label": "B", "text": "y"},
            {"label": "C", "text": "n"},
            {"label": "D", "text": "o"},
        ],
        "answer": "C",
        "explanation": "\"Python\" 有 6 个字符，索引分别是 P(0)、y(1)、t(2)、h(3)、o(4)、n(5)。负数索引从右到左：n(-1)、o(-2)。所以 [-1] 是 'n'。",
        "difficulty": "medium",
        "tags": ["字符串", "索引"],
    },
    {
        "type": "code_completion",
        "title": "字符串去空格",
        "description": "补全代码，去掉字符串两边的空格：text = '  hello  '，result = ???",
        "answer": "text.strip()",
        "explanation": "strip() 方法会去掉字符串开头和结尾的空白字符（空格、换行、tab）。text.strip() 返回 'hello'。",
        "difficulty": "easy",
        "tags": ["字符串", "方法"],
    },
    {
        "type": "programming",
        "title": "名字处理程序",
        "description": "创建变量 full_name = '  张三  '（注意首尾有空格）。请写代码：1) 去掉首尾空格 2) 转成大写 3) 用 f-string 输出 '处理后的名字是：XXX'",
        "answer": 'full_name = "  张三  "\nclean = full_name.strip().upper()\nprint(f"处理后的名字是：{clean}")',
        "explanation": "strip() 去空格，upper() 转大写。方法可以链式调用：full_name.strip().upper() 一步到位。",
        "difficulty": "easy",
        "tags": ["字符串", "方法链"],
    },
]

# ============================================================
# Lesson 5: 数字与运算符
# ============================================================
EXERCISES_LESSON_5 = [
    {
        "type": "choice",
        "title": "17 % 5 的结果是多少？",
        "description": "% 是取余运算符",
        "options": [
            {"label": "A", "text": "3"},
            {"label": "B", "text": "2"},
            {"label": "C", "text": "3.4"},
            {"label": "D", "text": "12"},
        ],
        "answer": "B",
        "explanation": "17 % 5 表示 17 除以 5 的余数。5×3=15，17-15=2。所以余数是 2。",
        "difficulty": "easy",
        "tags": ["运算符", "取余"],
    },
    {
        "type": "fill_blank",
        "title": "计算 2 的 10 次方",
        "description": "2 ** 10 的结果是多少？（填数字）",
        "answer": "1024",
        "explanation": "** 是幂运算符。2 ** 10 = 2×2×2×2×2×2×2×2×2×2 = 1024。",
        "difficulty": "easy",
        "tags": ["运算符", "幂"],
    },
    {
        "type": "judge",
        "title": "5 / 2 的结果是 2",
        "description": "判断：Python 中 5 / 2 得到 2",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。Python 中 / 是浮点除法，5 / 2 = 2.5。如果只要整数部分，用整除 //：5 // 2 = 2。",
        "difficulty": "easy",
        "tags": ["运算符", "除法"],
    },
    {
        "type": "code_completion",
        "title": "判断奇偶数",
        "description": "补全代码，判断 num 是不是偶数：result = num % 2 ____ 0",
        "answer": "==",
        "explanation": "num % 2 == 0 表示 num 除以 2 的余数等于 0，也就是能被 2 整除，即偶数。填 == 表示「等于」。",
        "difficulty": "medium",
        "tags": ["运算符", "取余"],
    },
    {
        "type": "programming",
        "title": "计算圆的面积",
        "description": "已知半径 r = 5，圆周率 π = 3.14。写代码计算圆的面积（πr²），并用 print 输出 '圆的面积是：XXX'",
        "answer": "r = 5\npi = 3.14\narea = pi * r ** 2\nprint(f\"圆的面积是：{area}\")",
        "explanation": "面积公式：πr²。Python 中 r² 写成 r ** 2。注意 ** 优先级高于 *，所以 pi * r ** 2 先算 r ** 2 再乘 pi。",
        "difficulty": "easy",
        "tags": ["运算符", "综合"],
    },
]

# ============================================================
# Lesson 6: 条件判断 if
# ============================================================
EXERCISES_LESSON_6 = [
    {
        "type": "fill_blank",
        "title": "if 语句的结尾符号",
        "description": "if score >= 60 ___ 冒号后面应该填什么？",
        "answer": ":",
        "explanation": "Python 的 if 语句格式：if 条件:。条件后面必须加冒号，表示接下来是条件成立时要执行的代码块。",
        "difficulty": "easy",
        "tags": ["if", "语法"],
    },
    {
        "type": "code_fix",
        "title": "修复 if 判断条件",
        "description": "以下代码想判 age 是否等于 18，但有错误：if age = 18: print('成年')",
        "answer": 'if age == 18:\n    print("成年")',
        "explanation": "= 是赋值，== 才是判断相等。把 = 改成 ==，同时确保 print 前面有 4 个空格的缩进。",
        "difficulty": "medium",
        "tags": ["if", "比较"],
    },
    {
        "type": "choice",
        "title": "以下 if/elif 代码输出什么？score = 75",
        "description": "score = 75\nif score >= 90: print('A')\nelif score >= 80: print('B')\nelif score >= 70: print('C')\nelse: print('D')",
        "options": [
            {"label": "A", "text": "A"},
            {"label": "B", "text": "B"},
            {"label": "C", "text": "C"},
            {"label": "D", "text": "D"},
        ],
        "answer": "C",
        "explanation": "执行顺序：先判断 >=90 不成立，再判断 >=80 不成立，再判断 >=70 成立！所以执行 print('C')。后面的 else 不再执行。if/elif 只执行第一个成立的分支。",
        "difficulty": "medium",
        "tags": ["if", "elif"],
    },
    {
        "type": "code_completion",
        "title": "三目表达式",
        "description": "补全代码：status = '成年' ___ age >= 18 ___ '未成年'",
        "answer": "if else",
        "explanation": "单行 if/else 的语法：值1 if 条件 else 值2。条件成立取值1，不成立取值2。这里填 'if' 和 'else'。",
        "difficulty": "medium",
        "tags": ["if", "三元表达式"],
    },
    {
        "type": "programming",
        "title": "成绩等级判断",
        "description": "写一个程序：score = 82。如果 >= 90 输出 '优秀'；>= 75 输出 '良好'；>= 60 输出 '及格'；否则输出 '不及格'。",
        "answer": 'score = 82\nif score >= 90:\n    print("优秀")\nelif score >= 75:\n    print("良好")\nelif score >= 60:\n    print("及格")\nelse:\n    print("不及格")',
        "explanation": "注意 elif 顺序：从大到小排。如果从 >=60 开始，后面的条件就永远不会执行了。82 分满足 >=75，输出 '良好'。",
        "difficulty": "easy",
        "tags": ["if", "分级判断"],
    },
]

# ============================================================
# Lesson 7: 比较运算符与逻辑运算符
# ============================================================
EXERCISES_LESSON_7 = [
    {
        "type": "choice",
        "title": "以下哪个表达式的结果是 True？",
        "description": "选出结果为 True 的选项",
        "options": [
            {"label": "A", "text": "5 == '5'"},
            {"label": "B", "text": "10 > 5 and 3 > 8"},
            {"label": "C", "text": "7 != 3 or 5 < 2"},
            {"label": "D", "text": "not (3 > 1)"},
        ],
        "answer": "C",
        "explanation": "A: 5==字符串'5'是 False（类型不同）。B: 10>5 真 but 3>8 假 → and 是 False。C: 7!=3 真，or 只要一个真就是 True。D: 3>1 是真，not 之后变 False。",
        "difficulty": "medium",
        "tags": ["逻辑", "比较"],
    },
    {
        "type": "fill_blank",
        "title": "and 运算符的真值表",
        "description": "True and False 的结果是什么？（填 True 或 False）",
        "answer": "False",
        "explanation": "and 运算符要求两边都为 True 才返回 True。True and False 有一边是 False，所以结果是 False。",
        "difficulty": "easy",
        "tags": ["逻辑", "and"],
    },
    {
        "type": "judge",
        "title": "not (5 > 3) 的结果是 True",
        "description": "判断这个说法的正误",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。5 > 3 是 True，not True 是 False。括号里的先算。",
        "difficulty": "easy",
        "tags": ["逻辑", "not"],
    },
    {
        "type": "code_completion",
        "title": "补全闰年判断条件",
        "description": "闰年规则：能被 4 整除但不能被 100 整除。补全条件：year % 4 == 0 ____ year % 100 != 0",
        "answer": "and",
        "explanation": "两个条件要同时满足：能被 4 整除 AND 不能被 100 整除。所以用 and 连接。",
        "difficulty": "medium",
        "tags": ["逻辑", "闰年"],
    },
    {
        "type": "programming",
        "title": "年龄范围判断",
        "description": "写程序判断 age=25 是否在 18 到 60 岁之间（含两端）。输出 '在范围内' 或 '不在范围内'。使用 and 运算符。",
        "answer": 'age = 25\nif age >= 18 and age <= 60:\n    print("在范围内")\nelse:\n    print("不在范围内")',
        "explanation": "在 18 到 60 之间就是 >= 18 且 <= 60。注意 and 两边都要写完整（不能写成 18 <= age <= 60 虽然 Python 也支持），但用 and 更通用。",
        "difficulty": "easy",
        "tags": ["逻辑", "范围判断"],
    },
]

# ============================================================
# Lesson 8: while 循环
# ============================================================
EXERCISES_LESSON_8 = [
    {
        "type": "fill_blank",
        "title": "while 循环的退出条件",
        "description": "while 循环会在条件变为 ____ 时停止循环",
        "answer": "False",
        "explanation": "while 循环每次执行前检查条件。条件为 True 时继续循环，条件变为 False 时退出循环。",
        "difficulty": "easy",
        "tags": ["while", "条件"],
    },
    {
        "type": "code_fix",
        "title": "修复死循环",
        "description": "以下代码会导致死循环：count = 1; while count <= 5: print(count)。请修复使得只输出 1~5 并停止。",
        "answer": "count = 1\nwhile count <= 5:\n    print(count)\n    count += 1",
        "explanation": "原代码 count 一直等于 1，条件永远成立。需要每次循环把 count + 1，让 count 最终超过 5 使条件变为 False。",
        "difficulty": "medium",
        "tags": ["while", "死循环"],
    },
    {
        "type": "choice",
        "title": "以下代码输出什么？",
        "description": "n = 3\nwhile n > 0:\n    print(n)\n    n -= 1",
        "options": [
            {"label": "A", "text": "3 2 1 0"},
            {"label": "B", "text": "3 2 1"},
            {"label": "C", "text": "3 2 1 0 -1 ...（无限循环）"},
            {"label": "D", "text": "以上都不对"},
        ],
        "answer": "B",
        "explanation": "n 初始为 3：先打印 3，n 变 2→打印 2，n 变 1→打印 1，n 变 0→条件 n>0 不成立，停止。所以输出 3 2 1。",
        "difficulty": "medium",
        "tags": ["while", "执行过程"],
    },
    {
        "type": "code_completion",
        "title": "用 while 求 1 到 100 的和",
        "description": "补全代码：total = 0; i = 1; ____ i <= 100: total += i; i += 1",
        "answer": "while",
        "explanation": "用 while 循环累加 1 到 100。每次循环把 i 加到 total 上，然后 i+1。while i <= 100 表示循环 100 次。",
        "difficulty": "medium",
        "tags": ["while", "累加"],
    },
    {
        "type": "programming",
        "title": "倒计时程序",
        "description": "从 10 倒数到 1，每行一个数字，最后打印 '发射！'",
        "answer": 'count = 10\nwhile count > 0:\n    print(count)\n    count -= 1\nprint("发射！")',
        "explanation": "从 10 开始，每次 count -= 1，直到 count 变成 0，条件 count > 0 不成立退出循环，最后打印发射。",
        "difficulty": "easy",
        "tags": ["while", "倒计时"],
    },
]

# ============================================================
# Lesson 9: for 循环与 range
# ============================================================
EXERCISES_LESSON_9 = [
    {
        "type": "choice",
        "title": "range(5) 生成的序列是什么？",
        "description": "选择正确的序列",
        "options": [
            {"label": "A", "text": "[1, 2, 3, 4, 5]"},
            {"label": "B", "text": "[0, 1, 2, 3, 4]"},
            {"label": "C", "text": "[0, 1, 2, 3, 4, 5]"},
            {"label": "D", "text": "[1, 2, 3, 4]"},
        ],
        "answer": "B",
        "explanation": "range(5) 生成从 0 到 4 的整数序列（左闭右开区间），共 5 个元素，不包含 5。",
        "difficulty": "easy",
        "tags": ["range", "for"],
    },
    {
        "type": "fill_blank",
        "title": "range 的参数",
        "description": "range(2, 10, 3) 生成哪些数字？（用逗号分隔，如 1,2,3）",
        "answer": "2,5,8",
        "explanation": "range(start=2, stop=10, step=3)：从 2 开始，每次加 3，直到 >=10 停止。所以是 2, 5, 8。9+3=12 超过了 10，不包含 11。",
        "difficulty": "medium",
        "tags": ["range", "步长"],
    },
    {
        "type": "judge",
        "title": "for 循环只能遍历数字",
        "description": "判断：for 循环只能配合 range() 遍历数字",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。for 可以遍历任何可迭代对象：字符串、列表、元组、字典、集合等。for char in 'Hello' 可以遍历每个字符。",
        "difficulty": "easy",
        "tags": ["for", "遍历"],
    },
    {
        "type": "code_completion",
        "title": "九九乘法表内层循环",
        "description": "补全代码：for i in range(1,10):\n    for ___ in range(1, i+1):\n        print(f'{j}×{i}={i*j}', end=' ')\n    print()",
        "answer": "j",
        "explanation": "外层 i 控制行，内层 j 控制每行打印几个。内层 range(1, i+1) 让第 i 行只打印 i 个乘法式子。",
        "difficulty": "medium",
        "tags": ["for", "嵌套"],
    },
    {
        "type": "programming",
        "title": "求 1 到 100 之间的偶数和",
        "description": "用 for 循环计算 1 到 100 之间所有偶数的和（提示：可以用 range 的 step 参数，或者用 if 判断）",
        "answer": "total = 0\nfor i in range(2, 101, 2):\n    total += i\nprint(f\"1-100偶数和：{total}\")",
        "explanation": "两种方法：1) range(2, 101, 2) 直接生成所有偶数。2) range(1, 101) + if i % 2 == 0 判断。第一种更高效。答案是 2550。",
        "difficulty": "easy",
        "tags": ["for", "range"],
    },
]

# ============================================================
# Lesson 10: 循环进阶
# ============================================================
EXERCISES_LESSON_10 = [
    {
        "type": "fill_blank",
        "title": "break 的作用",
        "description": "break 语句在循环中的作用是 ____（填两个中文字）",
        "answer": "退出",
        "explanation": "break 用于立即退出当前循环（最内层的那层），程序继续执行循环后面的代码。continue 不同，它只是跳过本轮继续下一轮。",
        "difficulty": "easy",
        "tags": ["break", "循环"],
    },
    {
        "type": "code_fix",
        "title": "修复嵌套循环中的 break",
        "description": "以下代码想在内层找到目标后完全停止所有循环，但没有做到：\nfor i in range(5):\n    for j in range(5):\n        if i*j > 10: break\n请给出一种解决方案",
        "answer": "found = False\nfor i in range(5):\n    for j in range(5):\n        if i * j > 10:\n            found = True\n            break\n    if found:\n        break",
        "explanation": "break 只跳出最内层循环。要跳出外层，可以用一个标记变量 found，内层 break 后外层检查标记再 break。",
        "difficulty": "hard",
        "tags": ["break", "嵌套"],
    },
    {
        "type": "choice",
        "title": "以下代码输出什么？",
        "description": "for i in range(5):\n    if i == 2: continue\n    print(i, end=' ')",
        "options": [
            {"label": "A", "text": "0 1 2 3 4"},
            {"label": "B", "text": "0 1 3 4"},
            {"label": "C", "text": "0 1"},
            {"label": "D", "text": "1 2 3 4"},
        ],
        "answer": "B",
        "explanation": "i==2 时执行 continue，跳过本轮剩余的 print(i)，直接进入下一轮 i=3。所以输出 0 1 3 4。",
        "difficulty": "easy",
        "tags": ["continue", "for"],
    },
    {
        "type": "judge",
        "title": "for 循环不能和 else 一起使用",
        "description": "判断：Python 中 for 循环后面不能接 else 语句",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。Python 特有的语法：for/while 后面可以接 else。当循环正常结束（没被 break 中断）时执行 else 块。这是一个不常见但很有用的特性。",
        "difficulty": "medium",
        "tags": ["for", "else"],
    },
    {
        "type": "programming",
        "title": "找质数",
        "description": "写程序判断 num=29 是不是质数。质数：只能被 1 和自己整除的数（大于 1）。使用 for 循环 + break + else。输出 '是质数' 或 '不是质数'。",
        "answer": 'num = 29\nfor i in range(2, int(num ** 0.5) + 1):\n    if num % i == 0:\n        print("不是质数")\n        break\nelse:\n    print("是质数")',
        "explanation": "循环从 2 检查到 sqrt(num)，如果能被整除就不是质数且 break；如果循环走完没 break，说明是质数，走 else 分支。这是 for/else 的典型用法。",
        "difficulty": "hard",
        "tags": ["for", "break", "else"],
    },
]

# ============================================================
# Lesson 11: 列表基础
# ============================================================
EXERCISES_LESSON_11 = [
    {
        "type": "choice",
        "title": "如何获取列表的长度？",
        "description": "选出正确的方法",
        "options": [
            {"label": "A", "text": "list.length()"},
            {"label": "B", "text": "len(list)"},
            {"label": "C", "text": "list.size()"},
            {"label": "D", "text": "list.count()"},
        ],
        "answer": "B",
        "explanation": "Python 获取长度的正确方式是 len() 函数：len([1,2,3]) 返回 3。.length() 和 .size() 是其他语言的写法。",
        "difficulty": "easy",
        "tags": ["列表", "len"],
    },
    {
        "type": "fill_blank",
        "title": "向列表末尾添加元素",
        "description": "fruits = ['苹果']，想在末尾加 '香蕉'，应该用什么方法？fruits.______('香蕉')",
        "answer": "append",
        "explanation": "append() 是列表的方法，在列表末尾添加元素。fruits.append('香蕉') 之后列表变为 ['苹果', '香蕉']。",
        "difficulty": "easy",
        "tags": ["列表", "append"],
    },
    {
        "type": "code_fix",
        "title": "修复列表访问越界",
        "description": "nums = [10, 20, 30]; print(nums[3]) 会报错 IndexError。如何正确获取最后一个元素？",
        "answer": "print(nums[-1])",
        "explanation": "nums 索引只有 0,1,2，索引 3 越界了。用 -1 索引可以安全获取最后一个元素 30。或者 nums[len(nums)-1]。",
        "difficulty": "easy",
        "tags": ["列表", "索引"],
    },
    {
        "type": "code_completion",
        "title": "列表判空",
        "description": "补全代码：判断列表是否为空：if ____ items: print('不为空')",
        "answer": "not",
        "explanation": "空列表在 Python 中被视为 False。if items 在空列表时为 False。if not items 在空列表时为 True。或者用 if len(items) == 0。",
        "difficulty": "medium",
        "tags": ["列表", "判空"],
    },
    {
        "type": "programming",
        "title": "创建购物清单",
        "description": "创建一个空列表 cart，依次添加 '牛奶'、'面包'、'鸡蛋'，然后删除 '面包'，最后打印购物清单（每行一个带编号）。",
        "answer": 'cart = []\ncart.append("牛奶")\ncart.append("面包")\ncart.append("鸡蛋")\ncart.remove("面包")\n\nfor i, item in enumerate(cart, 1):\n    print(f"{i}. {item}")',
        "explanation": "购物清单是列表的典型用例：空列表开始，append 添加，remove 删除，enumerate 遍历输出。",
        "difficulty": "easy",
        "tags": ["列表", "综合"],
    },
]

# ============================================================
# Lesson 12: 列表排序遍历推导式
# ============================================================
EXERCISES_LESSON_12 = [
    {
        "type": "fill_blank",
        "title": "sort() 和 sorted() 的区别",
        "description": "sort() 会修改 ____ 列表，sorted() 返回一个 ____ 列表。（两个空填同一个词：原/新）",
        "answer": "原,新",
        "explanation": "sort() 是原地排序，直接修改原来的列表，返回 None。sorted() 返回一个新的排序后的列表，不改变原列表。",
        "difficulty": "medium",
        "tags": ["排序", "列表"],
    },
    {
        "type": "choice",
        "title": "以下列表推导式生成什么？",
        "description": "[x*2 for x in range(1, 6) if x % 2 == 0]",
        "options": [
            {"label": "A", "text": "[2, 4, 6, 8, 10]"},
            {"label": "B", "text": "[4, 8]"},
            {"label": "C", "text": "[2, 6, 10]"},
            {"label": "D", "text": "[1, 4, 9, 16, 25]"},
        ],
        "answer": "B",
        "explanation": "range(1,6) 生成 1-5，if x%2==0 筛选出偶数 2 和 4，x*2 得到 4 和 8。所以结果是 [4, 8]。",
        "difficulty": "medium",
        "tags": ["列表推导式", "过滤"],
    },
    {
        "type": "judge",
        "title": "nums = nums.sort() 可以正确排序",
        "description": "判断：nums = [3,1,2]; nums = nums.sort() 之后 nums 是 [1,2,3]",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误！sort() 返回 None，所以 nums 会变成 None。正确写法：直接 nums.sort()，不要赋值。",
        "difficulty": "medium",
        "tags": ["sort", "常见错误"],
    },
    {
        "type": "code_completion",
        "title": "逆序列表",
        "description": "补全代码，将列表 [1,2,3] 变成 [3,2,1]：reversed_list = nums[____]",
        "answer": "::-1",
        "explanation": "切片 [::-1] 是 Python 中翻转序列的经典写法。意思是：取全部元素，步长为 -1（倒着走）。",
        "difficulty": "medium",
        "tags": ["切片", "翻转"],
    },
    {
        "type": "programming",
        "title": "成绩分析器",
        "description": "scores = [67, 82, 95, 73, 88, 59, 91]。写代码：1) 用列表推导式筛选及格（>=60）的成绩 2) 计算及格人数的平均分 3) 找出最高分和最低分",
        "answer": 'scores = [67, 82, 95, 73, 88, 59, 91]\npassing = [s for s in scores if s >= 60]\navg = sum(passing) / len(passing)\nprint(f"及格人数：{len(passing)}")\nprint(f"及格均分：{avg:.1f}")\nprint(f"最高分：{max(scores)}，最低分：{min(scores)}")',
        "explanation": "列表推导式筛选 + sum/len 求平均 + max/min 找极值。这是数据分析中最基础的操作组合。",
        "difficulty": "easy",
        "tags": ["列表推导式", "统计"],
    },
]

# ============================================================
# Lesson 13: 元组
# ============================================================
EXERCISES_LESSON_13 = [
    {
        "type": "choice",
        "title": "元组和列表的主要区别是什么？",
        "description": "选出最准确的区别",
        "options": [
            {"label": "A", "text": "元组用 {}，列表用 []"},
            {"label": "B", "text": "元组不可修改，列表可以修改"},
            {"label": "C", "text": "元组只能存数字"},
            {"label": "D", "text": "没有区别"},
        ],
        "answer": "B",
        "explanation": "元组的核心特点是不可变（immutable），创建后不能修改、添加、删除元素。列表是可变的。元组用 () 定义（不是 {}，那是字典）。",
        "difficulty": "easy",
        "tags": ["元组", "不可变"],
    },
    {
        "type": "fill_blank",
        "title": "单元素元组的写法",
        "description": "创建一个只包含数字 42 的元组，正确语法是：(42,____)",
        "answer": "",
        "explanation": "单元素元组需要加逗号：(42,)。如果写成 (42)，Python 会把它当作带括号的整数而不是元组。",
        "difficulty": "medium",
        "tags": ["元组", "语法"],
    },
    {
        "type": "code_fix",
        "title": "修复元组修改错误",
        "description": "colors = ('红', '绿', '蓝')，下面代码报错：colors[0] = '黄'。请改用正确的方法获取一个修改后的元组。",
        "answer": "colors = ('黄',) + colors[1:]",
        "explanation": "元组不可修改，但可以创建新元组：用切片取后面的元素，和新元素拼接成新元组。结果：('黄', '绿', '蓝')。",
        "difficulty": "medium",
        "tags": ["元组", "不可变"],
    },
    {
        "type": "judge",
        "title": "元组的访问速度比列表快",
        "description": "判断：访问元组元素比访问列表元素更快",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "A",
        "explanation": "正确。因为元组不可变，Python 可以对其做更多优化。虽然日常使用中差异很小，但理论上元组确实比列表稍快。",
        "difficulty": "medium",
        "tags": ["元组", "性能"],
    },
    {
        "type": "programming",
        "title": "元组解包练习",
        "description": "给定 point = (120, 350)。用一行代码把 x 和 y 分别赋值为 120 和 350，然后打印 '坐标：(120, 350)'。再写一行代码交换 x 和 y 的值并打印。",
        "answer": 'point = (120, 350)\nx, y = point\nprint(f"坐标：({x}, {y})")\nx, y = y, x\nprint(f"交换后：({x}, {y})")',
        "explanation": "元组解包：x, y = point 一行提取两个值。x, y = y, x 一行交换变量（Python 特色语法）。",
        "difficulty": "easy",
        "tags": ["元组", "解包"],
    },
]

# ============================================================
# Lesson 14: 字典基础
# ============================================================
EXERCISES_LESSON_14 = [
    {
        "type": "choice",
        "title": "以下哪个是合法的字典？",
        "description": "选出语法正确的字典定义",
        "options": [
            {"label": "A", "text": "{1, 2, 3}"},
            {"label": "B", "text": "('name': '小明')"},
            {"label": "C", "text": "{'name': '小明', 'age': 18}"},
            {"label": "D", "text": "['name': '小明']"},
        ],
        "answer": "C",
        "explanation": "A 是集合，B 的小括号不对，D 是列表语法。字典用花括号 {}，键值对用 key: value 格式。",
        "difficulty": "easy",
        "tags": ["字典", "语法"],
    },
    {
        "type": "fill_blank",
        "title": "字典安全访问",
        "description": "student = {'name': '小明'}。用 student.____('age', 0) 可以安全获取 age，不存在则返回 0",
        "answer": "get",
        "explanation": "get() 方法安全获取值：student.get('age', 0)。key 不存在返回默认值 0，不会报 KeyError。",
        "difficulty": "easy",
        "tags": ["字典", "get"],
    },
    {
        "type": "code_fix",
        "title": "修复字典遍历",
        "description": "以下代码想同时遍历 key 和 value：for k in student: print(k, student[k])。请改为更优雅的写法。",
        "answer": 'for k, v in student.items():\n    print(k, v)',
        "explanation": "student.items() 返回 (key, value) 对，用 for k, v 直接解包。比 for k + student[k] 更清晰高效。",
        "difficulty": "medium",
        "tags": ["字典", "遍历"],
    },
    {
        "type": "code_completion",
        "title": "字典合并",
        "description": "补全代码合并两个字典：d1 = {'a':1}; d2 = {'b':2}; merged = d1 ____ d2",
        "answer": "|",
        "explanation": "Python 3.9+ 支持用 | 运算符合并字典：d1 | d2。如果 key 重复，后面的覆盖前面的。",
        "difficulty": "medium",
        "tags": ["字典", "合并"],
    },
    {
        "type": "programming",
        "title": "通讯录小程序",
        "description": "创建字典 contacts，存入 2 个联系人（姓名→电话）。然后用 input() 接收用户输入的姓名，用 get() 查找电话。找到了打印电话，没找到打印 '未找到该联系人'。",
        "answer": 'contacts = {\n    "小明": "13800138000",\n    "小红": "13900139000"\n}\nname = input("请输入联系人姓名：")\nphone = contacts.get(name)\nif phone:\n    print(f"{name} 的电话：{phone}")\nelse:\n    print("未找到该联系人")',
        "explanation": "字典是存储键值对的最佳选择。get() 安全查找，不存在的 key 返回 None，避免 KeyError。",
        "difficulty": "easy",
        "tags": ["字典", "综合"],
    },
]

# ============================================================
# Lesson 15: 字典高级用法
# ============================================================
EXERCISES_LESSON_15 = [
    {
        "type": "fill_blank",
        "title": "字典推导式",
        "description": "把列表 words = ['a', 'ab', 'abc'] 转成 {单词: 长度} 的字典，用推导式：{w: ____ for w in words}",
        "answer": "len(w)",
        "explanation": "len(w) 获取单词长度。字典推导式语法：{key_表达式: value_表达式 for item in 序列}。结果：{'a':1, 'ab':2, 'abc':3}。",
        "difficulty": "medium",
        "tags": ["字典推导式", "len"],
    },
    {
        "type": "choice",
        "title": "嵌套字典中如何获取 users[0]['name']？",
        "description": "users = [{'name': '小明', 'age': 18}, {'name': '小红', 'age': 20}]。users[0]['name'] 的值是？",
        "options": [
            {"label": "A", "text": "小明"},
            {"label": "B", "text": "小红"},
            {"label": "C", "text": "18"},
            {"label": "D", "text": "报错"},
        ],
        "answer": "A",
        "explanation": "索引过程：users[0] 取列表第一个元素（字典 {'name':'小明','age':18}），['name'] 取字典中 key 为 'name' 的值。结果是 '小明'。",
        "difficulty": "medium",
        "tags": ["嵌套", "索引"],
    },
    {
        "type": "judge",
        "title": "字典的 key 必须唯一",
        "description": "判断：同一个字典中不能有两个相同的 key",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "A",
        "explanation": "正确。字典的 key 是唯一的。如果定义了重复的 key（如 {'a':1, 'a':2}），后面的值会覆盖前面的值，最终 {'a':2}。",
        "difficulty": "easy",
        "tags": ["字典", "key"],
    },
    {
        "type": "code_completion",
        "title": "统计单词频率",
        "description": "补全统计代码：text = 'a b a c b a'，words = text.split()，freq = {}。for w in words: freq[w] = freq.____(w, 0) + 1",
        "answer": "get",
        "explanation": "用 freq.get(w, 0) 安全获取当前计数（不存在则为 0），然后 +1。这是字典统计频率的经典模式。",
        "difficulty": "hard",
        "tags": ["字典", "统计"],
    },
    {
        "type": "programming",
        "title": "学生成绩管理系统",
        "description": "创建字典存储 3 个学生的成绩：{'小明':88, '小红':95, '小刚':72}。完成：1) 添加新学生 '小李': 85 2) 打印所有信息 3) 计算平均分 4) 找出最高分的学生名字。",
        "answer": 'scores = {"小明": 88, "小红": 95, "小刚": 72}\nscores["小李"] = 85\n\nfor name, score in scores.items():\n    print(f"{name}: {score}分")\n\navg = sum(scores.values()) / len(scores)\nprint(f"平均分: {avg:.1f}")\n\nbest = max(scores, key=scores.get)\nprint(f"最高分: {best} ({scores[best]}分)")',
        "explanation": "scores['小李']=85 直接添加，scores.values() 获取所有值，max(scores, key=scores.get) 按值找最大值对应的 key。",
        "difficulty": "medium",
        "tags": ["字典", "综合"],
    },
]

# ============================================================
# Lesson 16: 函数定义与调用
# ============================================================
EXERCISES_LESSON_16 = [
    {
        "type": "choice",
        "title": "函数定义的关键字是什么？",
        "description": "在 Python 中定义函数使用哪个关键字？",
        "options": [
            {"label": "A", "text": "function"},
            {"label": "B", "text": "def"},
            {"label": "C", "text": "func"},
            {"label": "D", "text": "define"},
        ],
        "answer": "B",
        "explanation": "Python 定义函数使用 def 关键字。语法：def 函数名(参数):。function 和 define 是其他语言的写法。",
        "difficulty": "easy",
        "tags": ["函数", "def"],
    },
    {
        "type": "fill_blank",
        "title": "调用函数",
        "description": "def greet(): print('你好') — 调用这个函数的代码是：____()",
        "answer": "greet",
        "explanation": "定义函数用 def greet():，调用时写 greet()。只写 greet 不写括号会返回函数对象本身而不是执行函数。",
        "difficulty": "easy",
        "tags": ["函数", "调用"],
    },
    {
        "type": "code_fix",
        "title": "修复函数缩进错误",
        "description": "以下代码有错：def hello():\nprint('Hello')。请修正（提示：函数体要缩进）",
        "answer": 'def hello():\n    print("Hello")',
        "explanation": "函数体必须缩进 4 个空格（或 1 个 Tab）。不缩进 Python 不知道哪些代码属于函数。IndentationError 是最常见的新手错误之一。",
        "difficulty": "easy",
        "tags": ["函数", "缩进"],
    },
    {
        "type": "code_completion",
        "title": "补全 return 语句",
        "description": "定义一个函数 add(a, b)，返回两数之和：def add(a, b): ____ a + b",
        "answer": "return",
        "explanation": "return 关键字用于从函数返回值。def add(a, b): return a + b。调用 add(3,5) 得到 8。",
        "difficulty": "easy",
        "tags": ["函数", "return"],
    },
    {
        "type": "programming",
        "title": "自定义计算器函数",
        "description": "定义函数 calc_bmi(weight, height)，计算 BMI = 体重(kg) / 身高(m)²。返回 BMI 值。然后调用函数计算体重 70kg、身高 1.75m 的 BMI，用 print 输出（保留 1 位小数）。",
        "answer": 'def calc_bmi(weight, height):\n    return weight / (height ** 2)\n\nbmi = calc_bmi(70, 1.75)\nprint(f"BMI: {bmi:.1f}")',
        "explanation": "函数封装了 BMI 计算公式，调用时只需传参数。return 返回计算结果。:.1f 格式化保留一位小数。BMI ≈ 22.9。",
        "difficulty": "easy",
        "tags": ["函数", "BMI"],
    },
]

# ============================================================
# Lesson 17: 参数与返回值
# ============================================================
EXERCISES_LESSON_17 = [
    {
        "type": "fill_blank",
        "title": "默认参数",
        "description": "def greet(name, greeting='你好')。调用 greet('小明') 时 greeting 的值是什么？",
        "answer": "你好",
        "explanation": "greeting 有默认值 '你好'。调用时不传 greeting 就使用默认值。如果传 greet('小明', 'Hello')，greeting 就是 'Hello'。",
        "difficulty": "easy",
        "tags": ["参数", "默认值"],
    },
    {
        "type": "choice",
        "title": "函数返回多个值本质上是什么？",
        "description": "def f(): return 1, 2 — 这个返回值是什么类型？",
        "options": [
            {"label": "A", "text": "列表"},
            {"label": "B", "text": "元组"},
            {"label": "C", "text": "字典"},
            {"label": "D", "text": "集合"},
        ],
        "answer": "B",
        "explanation": "return 1, 2 实际返回的是元组 (1, 2)。Python 自动把逗号分隔的多个值打包成元组。所以可以 a, b = f() 来解包接收。",
        "difficulty": "medium",
        "tags": ["return", "元组"],
    },
    {
        "type": "judge",
        "title": "有默认值的参数可以放在无默认值参数前面",
        "description": "判断：def f(a=1, b): 这样定义是合法的",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误！有默认值的参数必须放在无默认值参数后面。正确写法：def f(b, a=1):。Python 这样规定是为了避免参数传递时的歧义。",
        "difficulty": "medium",
        "tags": ["参数", "顺序"],
    },
    {
        "type": "code_completion",
        "title": "*args 收集多余参数",
        "description": "定义一个函数，能接收任意个参数并返回它们的和：def sum_all(____nums): return sum(nums)",
        "answer": "*",
        "explanation": "*nums 表示收集所有位置参数到一个元组 nums 中。这样 sum_all(1,2,3) 和 sum_all(1,2,3,4,5) 都能正常工作。",
        "difficulty": "hard",
        "tags": ["*args", "可变参数"],
    },
    {
        "type": "programming",
        "title": "温度转换器",
        "description": "写两个函数：1) celsius_to_fahrenheit(c) 把摄氏转华氏（F = C × 9/5 + 32）2) fahrenheit_to_celsius(f) 反过来。然后分别测试 0°C 和 32°F。",
        "answer": 'def celsius_to_fahrenheit(c):\n    return c * 9 / 5 + 32\n\ndef fahrenheit_to_celsius(f):\n    return (f - 32) * 5 / 9\n\nprint(f"0°C = {celsius_to_fahrenheit(0)}°F")\nprint(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")',
        "explanation": "摄氏转华氏：乘以 9/5 再加 32。华氏转摄氏：减 32 再乘 5/9。注意公式中的运算优先级，用括号确保正确。",
        "difficulty": "easy",
        "tags": ["函数", "温度转换"],
    },
]

# ============================================================
# Lesson 18: 作用域与 lambda
# ============================================================
EXERCISES_LESSON_18 = [
    {
        "type": "choice",
        "title": "以下代码输出什么？",
        "description": "x = 10\ndef f():\n    x = 5\nf()\nprint(x)",
        "options": [
            {"label": "A", "text": "5"},
            {"label": "B", "text": "10"},
            {"label": "C", "text": "15"},
            {"label": "D", "text": "报错"},
        ],
        "answer": "B",
        "explanation": "函数内的 x=5 创建了一个局部变量，不影响全局的 x。函数外打印的 x 还是 10。这是变量作用域的核心概念。",
        "difficulty": "medium",
        "tags": ["作用域", "局部变量"],
    },
    {
        "type": "fill_blank",
        "title": "lambda 表达式",
        "description": "用 lambda 定义平方函数：square = lambda x: x ____ 2",
        "answer": "**",
        "explanation": "lambda x: x ** 2 定义一个接收 x、返回 x 平方的匿名函数。** 是幂运算符。完整写法：square = lambda x: x ** 2; square(5) 返回 25。",
        "difficulty": "medium",
        "tags": ["lambda", "幂"],
    },
    {
        "type": "code_fix",
        "title": "修复 UnboundLocalError",
        "description": "count = 0\ndef increment():\n    count += 1\n调用 increment() 会报错 UnboundLocalError。请修复。",
        "answer": "count = 0\ndef increment():\n    global count\n    count += 1",
        "explanation": "函数内对全局变量赋值需要 global 声明。或者更好用 return：def increment(n): return n+1; count = increment(count)。",
        "difficulty": "medium",
        "tags": ["global", "作用域"],
    },
    {
        "type": "judge",
        "title": "lambda 里面可以写多行逻辑",
        "description": "判断：lambda x: if x>0: return x else: return -x 是合法的",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "B",
        "explanation": "错误。lambda 只能包含一个表达式，不能写多行、不能有 if/return 语句。需要用条件判断时用普通 def 函数，或者用三元表达式：lambda x: x if x>0 else -x。",
        "difficulty": "hard",
        "tags": ["lambda", "限制"],
    },
    {
        "type": "programming",
        "title": "sort 配合 lambda 排序",
        "description": "students = [('小明',90), ('小红',85), ('小刚',95)]。用 sort(key=lambda ...) 按成绩从高到低排序，然后打印结果。",
        "answer": 'students = [("小明", 90), ("小红", 85), ("小刚", 95)]\nstudents.sort(key=lambda s: s[1], reverse=True)\nfor name, score in students:\n    print(f"{name}: {score}分")',
        "explanation": "lambda s: s[1] 取每个元组的第二个元素（成绩）作为排序依据。reverse=True 表示从高到低。这是 lambda 最常用的场景。",
        "difficulty": "medium",
        "tags": ["lambda", "sort"],
    },
]

# ============================================================
# Lesson 19: 模块与 import
# ============================================================
EXERCISES_LESSON_19 = [
    {
        "type": "choice",
        "title": "导入模块的正确语法是？",
        "description": "选出正确的 import 语句",
        "options": [
            {"label": "A", "text": "import random.py"},
            {"label": "B", "text": "include random"},
            {"label": "C", "text": "import random"},
            {"label": "D", "text": "using random"},
        ],
        "answer": "C",
        "explanation": "Python 导入模块用 import 模块名，不需要加 .py 后缀。include 和 using 是其他语言的语法。",
        "difficulty": "easy",
        "tags": ["import", "语法"],
    },
    {
        "type": "fill_blank",
        "title": "生成随机整数",
        "description": "import random 之后，生成 1 到 10 之间的随机整数用 random.________(1, 10)",
        "answer": "randint",
        "explanation": "random.randint(a, b) 生成 a 到 b 之间（含两端）的随机整数。例如 random.randint(1, 10) 可能返回 1~10 中的任意整数。",
        "difficulty": "easy",
        "tags": ["random", "randint"],
    },
    {
        "type": "code_fix",
        "title": "修复 import 错误",
        "description": "以下代码报错 NameError：randint(1,10)。修复它使得能正常运行（已知已 import random）",
        "answer": "random.randint(1, 10)",
        "explanation": "import random 导入的是整个模块，调用函数时要用 random.randint()。如果只想写 randint()，应该用 from random import randint。",
        "difficulty": "easy",
        "tags": ["import", "命名空间"],
    },
    {
        "type": "code_completion",
        "title": "获取当前日期时间",
        "description": "补全代码获取当前时间：from datetime ____ datetime; now = datetime.now()",
        "answer": "import",
        "explanation": "from datetime import datetime 从 datetime 模块中只导入 datetime 类。然后 datetime.now() 返回当前日期时间。",
        "difficulty": "medium",
        "tags": ["import", "datetime"],
    },
    {
        "type": "programming",
        "title": "随机点名器",
        "description": "导入 random 模块，给定名字列表 names = ['张三', '李四', '王五', '赵六']，随机选出一个名字并打印 '今天被点到的是：XXX'。",
        "answer": 'import random\n\nnames = ["张三", "李四", "王五", "赵六"]\nlucky = random.choice(names)\nprint(f"今天被点到的是：{lucky}")',
        "explanation": "random.choice(seq) 从序列中随机选一个元素。比用 randint + 索引更简洁。运行多次结果会不一样。",
        "difficulty": "easy",
        "tags": ["random", "choice"],
    },
]

# ============================================================
# Lesson 20: 文件读写与综合复习
# ============================================================
EXERCISES_LESSON_20 = [
    {
        "type": "choice",
        "title": "with open() as f 的好处是什么？",
        "description": "为什么推荐用 with 语句操作文件？",
        "options": [
            {"label": "A", "text": "代码更短"},
            {"label": "B", "text": "自动关闭文件，防止资源泄漏"},
            {"label": "C", "text": "运行更快"},
            {"label": "D", "text": "没有特别的优势"},
        ],
        "answer": "B",
        "explanation": "with 语句最大的好处是会自动关闭文件（即使发生异常），避免文件句柄泄漏。不用手动 f.close()，更安全。",
        "difficulty": "easy",
        "tags": ["文件", "with"],
    },
    {
        "type": "fill_blank",
        "title": "文件打开模式",
        "description": "如果要以追加模式打开文件，模式参数应该填什么？open('log.txt', '____')",
        "answer": "a",
        "explanation": "'a' 表示 append（追加）模式。新内容写到文件末尾，不会覆盖原有内容。'w' 是覆盖写入，'r' 是只读。",
        "difficulty": "easy",
        "tags": ["文件", "模式"],
    },
    {
        "type": "judge",
        "title": "open('file.txt', 'w') 如果文件不存在会自动创建",
        "description": "判断：用 'w' 模式打开一个不存在的文件不会报错，会自动创建新文件",
        "options": [
            {"label": "A", "text": "正确"},
            {"label": "B", "text": "错误"},
        ],
        "answer": "A",
        "explanation": "正确。'w' 和 'a' 模式下如果文件不存在，Python 会自动创建。但 'r' 模式如果文件不存在会报 FileNotFoundError。",
        "difficulty": "medium",
        "tags": ["文件", "创建"],
    },
    {
        "type": "code_completion",
        "title": "读取文件所有行",
        "description": "补全代码读取文件所有行到列表：with open('data.txt') as f: lines = f.________()",
        "answer": "readlines",
        "explanation": "f.readlines() 读取文件所有行，返回列表，每行一个元素（保留换行符）。读大文件时更好的方法是用 for line in f 逐行读取。",
        "difficulty": "medium",
        "tags": ["文件", "readlines"],
    },
    {
        "type": "programming",
        "title": "综合：个人日记本（简化版）",
        "description": "写一个程序：1) 用列表存储多条日记（用 input 输入）2) 输入 'save' 时把全部日记写入 diary.txt（每行一条）3) 输入 'show' 时读取 diary.txt 并打印内容。（提示：用 while True + if/elif + break）",
        "answer": 'entries = []\nprint("写日记（输入 save 保存, show 查看, quit 退出）")\n\nwhile True:\n    text = input("> ")\n    if text == "quit":\n        break\n    elif text == "save":\n        with open("diary.txt", "w", encoding="utf-8") as f:\n            for entry in entries:\n                f.write(entry + "\\n")\n        print(f"已保存 {len(entries)} 条日记")\n    elif text == "show":\n        try:\n            with open("diary.txt", "r", encoding="utf-8") as f:\n                print(f.read())\n        except FileNotFoundError:\n            print("还没有日记")\n    else:\n        entries.append(text)',
    "explanation": "这道题综合了 while 循环、条件判断、列表操作和文件读写。是 20 节课核心知识的综合运用。注意 encoding='utf-8' 支持中文。",
    "difficulty": "hard",
    "tags": ["综合", "文件", "循环", "字典"],
    },
]

ALL_EXERCISES = {
    1: EXERCISES_LESSON_1,
    2: EXERCISES_LESSON_2,
    3: EXERCISES_LESSON_3,
    4: EXERCISES_LESSON_4,
    5: EXERCISES_LESSON_5,
    6: EXERCISES_LESSON_6,
    7: EXERCISES_LESSON_7,
    8: EXERCISES_LESSON_8,
    9: EXERCISES_LESSON_9,
    10: EXERCISES_LESSON_10,
    11: EXERCISES_LESSON_11,
    12: EXERCISES_LESSON_12,
    13: EXERCISES_LESSON_13,
    14: EXERCISES_LESSON_14,
    15: EXERCISES_LESSON_15,
    16: EXERCISES_LESSON_16,
    17: EXERCISES_LESSON_17,
    18: EXERCISES_LESSON_18,
    19: EXERCISES_LESSON_19,
    20: EXERCISES_LESSON_20,
}
