"""
种子数据 - 250 道练习题 (50 节课 × 5 题)
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

# ============================================================
# Lesson 21
# ============================================================
EXERCISES_LESSON_21 = [
    {
        "type": "choice",
        "title": '运行 print(name) 但 name 未定义，会报什么错？',
        "description": '选择正确的错误类型',
        "options": [
            {"label": 'A', "text": 'TypeError'},
            {"label": 'B', "text": 'NameError'},
            {"label": 'C', "text": 'SyntaxError'},
            {"label": 'D', "text": 'ValueError'},
        ],
        "answer": 'B',
        "explanation": 'NameError 表示使用了未定义的变量。Python 找不到 name 这个名字。',
        "difficulty": 'easy',
        "tags": ['错误类型', 'NameError'],
    },
    {
        "type": "judge",
        "title": "TypeError 表示操作类型不匹配，比如 '2' + 2",
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": "正确。'2' 是字符串，2 是整数，Python 不允许直接用 + 连接不同类型的值。",
        "difficulty": 'easy',
        "tags": ['错误类型', 'TypeError'],
    },
    {
        "type": "code_fix",
        "title": '修复 IndexError 错误',
        "description": '下面的代码会报 IndexError，请修复它',
        "answer": 'fruits = ["apple", "banana", "orange"]\nprint(fruits[3])',
        "explanation": '只有 3 个元素，索引范围是 0-2。应该改成 fruits[2] 访问最后一个，或者 fruits[-1] 获取最后一个元素。正解：print(fruits[2]) 或 print(fruits[-1])',
        "difficulty": 'easy',
        "tags": ['错误类型', 'IndexError'],
    },
    {
        "type": "fill_blank",
        "title": "想把字符串 '123' 转成整数，但用了 int('abc')，会报什么错？",
        "description": '填入错误类型名称（英文）',
        "answer": 'ValueError',
        "explanation": "int('abc') 中 'abc' 无法转换成数字，Python 抛出 ValueError：值本身没问题，但类型转换时内容不正确。",
        "difficulty": 'medium',
        "tags": ['错误类型', 'ValueError'],
    },
    {
        "type": "choice",
        "title": '以下哪种情况会引发 KeyError？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '除以 0'},
            {"label": 'B', "text": '打开不存在的文件'},
            {"label": 'C', "text": '访问字典中不存在的 key'},
            {"label": 'D', "text": '把字符串和整数相加'},
        ],
        "answer": 'C',
        "explanation": 'KeyError 发生在字典中访问不存在的键时。正确答案：访问字典中不存在的 key。',
        "difficulty": 'medium',
        "tags": ['错误类型', 'KeyError'],
    },
]

# ============================================================
# Lesson 22
# ============================================================
EXERCISES_LESSON_22 = [
    {
        "type": "code_completion",
        "title": '补全 try/except 结构',
        "description": '补全代码，用 try/except 处理除零错误',
        "answer": "try:\n    result = a / b\nexcept ZeroDivisionError:\n    print('除数不能为零')",
        "explanation": '用 try 包裹可能出错的代码，except 指定要捕获的异常类型。ZeroDivisionError 是除零错误的专属异常。',
        "difficulty": 'easy',
        "tags": ['异常处理', 'try/except'],
    },
    {
        "type": "choice",
        "title": '以下关于 try/except 的说法哪个正确？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'except 必须指定异常类型'},
            {"label": 'B', "text": 'try 中的代码出错时，会跳到 except 块执行'},
            {"label": 'C', "text": 'try/except 会降低程序运行速度，尽量不用'},
            {"label": 'D', "text": 'try 后面不能单独使用，必须有 except'},
        ],
        "answer": 'B',
        "explanation": 'except 可以捕获指定的异常类型，使程序不崩溃。A 错在不指定类型也行（但不推荐），C 错在 try/except 不降低性能（但滥用确实不好），D 错在 try 可以没有 except（有 finally 即可）。',
        "difficulty": 'easy',
        "tags": ['异常处理'],
    },
    {
        "type": "code_fix",
        "title": '修复 except 捕获范围过大',
        "description": '下面的代码会捕获所有异常，不够精确。修改它，只捕获 ValueError',
        "answer": "try:\n    age = int(input('年龄: '))\nexcept ValueError:\n    print('请输入有效数字')",
        "explanation": '原代码 except: 会捕获所有异常（包括 Ctrl+C、内存错误等），应该指定具体的异常类型。正解：except ValueError: 只捕获类型转换错误。',
        "difficulty": 'medium',
        "tags": ['异常处理', 'except'],
    },
    {
        "type": "judge",
        "title": '一个 try 可以搭配多个 except 来分别处理不同的异常',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。一个 try 可以接多个 except，每个处理不同的异常类型，像这样：try: ... except ValueError: ... except ZeroDivisionError: ...',
        "difficulty": 'medium',
        "tags": ['异常处理', 'multiple except'],
    },
    {
        "type": "programming",
        "title": '安全除法计算器',
        "description": '编写代码：让用户输入两个数字 a 和 b，计算 a / b。用 try/except 处理 ZeroDivisionError 和 ValueError，出错时给出友好提示。',
        "answer": 'try:\n    a = float(input("被除数: "))\n    b = float(input("除数: "))\n    result = a / b\n    print(f"结果: {result}")\nexcept ValueError:\n    print("请输入有效数字")\nexcept ZeroDivisionError:\n    print("除数不能为零")',
        "explanation": '需要捕获两种错误：ValueError（输入非数字）和 ZeroDivisionError（除数为零）。使用 float() 支持小数输入。',
        "difficulty": 'medium',
        "tags": ['异常处理', '综合'],
    },
]

# ============================================================
# Lesson 23
# ============================================================
EXERCISES_LESSON_23 = [
    {
        "type": "choice",
        "title": 'try/except 中的 else 子句在什么时候执行？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '无论是否出错都执行'},
            {"label": 'B', "text": 'try 块没有异常时执行'},
            {"label": 'C', "text": 'except 块执行完毕后执行'},
            {"label": 'D', "text": '在 try 块之前执行'},
        ],
        "answer": 'B',
        "explanation": 'else 子句只有在 try 块没有发生异常时才会执行。它通常用于放置「只有不出错才需要执行」的代码。',
        "difficulty": 'easy',
        "tags": ['else', '异常处理'],
    },
    {
        "type": "judge",
        "title": 'finally 子句中的代码无论是否发生异常都会执行',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。finally 中的代码一定会执行，即使 try 或 except 中有 return 语句。常用于关闭文件、释放资源等清理操作。',
        "difficulty": 'easy',
        "tags": ['finally', '异常处理'],
    },
    {
        "type": "code_completion",
        "title": '补全自定义异常类',
        "description": '定义一个自定义异常类 InvalidAgeError，继承自 Exception',
        "answer": 'class InvalidAgeError(Exception):\n    pass',
        "explanation": "自定义异常只需继承 Exception（或它的子类），pass 表示类体为空。使用时 raise InvalidAgeError('年龄不能为负')。",
        "difficulty": 'medium',
        "tags": ['自定义异常'],
    },
    {
        "type": "fill_blank",
        "title": '在 Python 中，用哪个关键字来引发异常？',
        "description": '填写关键字',
        "answer": 'raise',
        "explanation": "raise 关键字用于主动抛出异常。例如 raise ValueError('无效的值')。如果不指定异常类型，raise 会重新抛出当前异常（只能在 except 块内使用）。",
        "difficulty": 'easy',
        "tags": ['raise', '异常处理'],
    },
    {
        "type": "code_fix",
        "title": '修复代码：确保文件一定会被关闭',
        "description": '以下代码在读取文件后可能不关闭文件，用 try/finally 修复它',
        "answer": "f = None\ntry:\n    f = open('data.txt', 'r')\n    content = f.read()\n    print(content)\nfinally:\n    if f:\n        f.close()",
        "explanation": '需要把读文件放在 try 中，把 f.close() 放在 finally 中，这样即使读文件出错也能确保关闭。注意 f 可能未被赋值的情况。',
        "difficulty": 'medium',
        "tags": ['finally', '资源管理'],
    },
]

# ============================================================
# Lesson 24
# ============================================================
EXERCISES_LESSON_24 = [
    {
        "type": "choice",
        "title": '以下哪个是 Python 中最简单的调试方法？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '用 print() 打印变量值'},
            {"label": 'B', "text": '重装系统'},
            {"label": 'C', "text": '使用 Photoshop'},
            {"label": 'D', "text": '换一台电脑'},
        ],
        "answer": 'A',
        "explanation": '用 print() 打印变量值是新手最常用的调试方法，虽然简单但非常直观有效。更高级的方法包括使用 logging 模块和 pdb 调试器。',
        "difficulty": 'easy',
        "tags": ['调试'],
    },
    {
        "type": "judge",
        "title": 'logging 模块比 print 更适合生产环境的调试',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。logging 可以设置日志级别（DEBUG/INFO/WARNING/ERROR），可以输出到文件，可以控制格式，比 print 专业得多。',
        "difficulty": 'medium',
        "tags": ['logging', '调试'],
    },
    {
        "type": "fill_blank",
        "title": '日志级别从低到高：DEBUG < INFO < WARNING < ERROR < ____',
        "description": '填写最严重的日志级别',
        "answer": 'CRITICAL',
        "explanation": 'logging 模块定义了 5 个标准级别：DEBUG（调试信息）、INFO（一般信息）、WARNING（警告）、ERROR（错误）、CRITICAL（严重错误）。',
        "difficulty": 'medium',
        "tags": ['logging', '日志级别'],
    },
    {
        "type": "code_completion",
        "title": '补全 logging 基本配置',
        "description": '设置日志格式和级别',
        "answer": 'import logging\nlogging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")\nlogging.debug("这是一条调试信息")',
        "explanation": 'basicConfig 用于基本配置。level 设置最低显示级别（DEBUG 表示显示所有级别），format 定义输出格式。',
        "difficulty": 'medium',
        "tags": ['logging'],
    },
    {
        "type": "choice",
        "title": '用 pdb 调试时，哪个命令可以单步执行（步入函数内部）？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'next (n)'},
            {"label": 'B', "text": 'step (s)'},
            {"label": 'C', "text": 'continue (c)'},
            {"label": 'D', "text": 'quit (q)'},
        ],
        "answer": 'B',
        "explanation": 'step(s) 会进入函数内部单步执行，而 next(n) 是单步执行但不进入函数。continue(c) 继续执行到下一个断点。',
        "difficulty": 'hard',
        "tags": ['pdb', '调试'],
    },
]

# ============================================================
# Lesson 25
# ============================================================
EXERCISES_LESSON_25 = [
    {
        "type": "choice",
        "title": 'Python 标准库中用于单元测试的模块是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'unittest'},
            {"label": 'B', "text": 'pytest'},
            {"label": 'C', "text": 'jest'},
            {"label": 'D', "text": 'mocha'},
        ],
        "answer": 'A',
        "explanation": 'unittest 是 Python 标准库自带的测试框架，不需要安装。pytest 是更流行的第三方库，但不是标准库的一部分。',
        "difficulty": 'easy',
        "tags": ['unittest'],
    },
    {
        "type": "judge",
        "title": '写测试是为了证明代码没有 bug',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'B',
        "explanation": '错误。测试不能证明代码没有 bug，只能证明在特定输入下代码按预期工作。测试的目标是尽早发现问题，而不是保证完美无缺。',
        "difficulty": 'easy',
        "tags": ['测试', '观念'],
    },
    {
        "type": "code_completion",
        "title": '补全一个简单的测试用例',
        "description": '编写一个 unittest 测试用例，测试 add(a, b) 函数',
        "answer": 'import unittest\n\nclass TestAdd(unittest.TestCase):\n    def test_add_positive(self):\n        self.assertEqual(add(2, 3), 5)\n\n    def test_add_negative(self):\n        self.assertEqual(add(-1, -2), -3)',
        "explanation": '测试类继承 unittest.TestCase，测试方法以 test_ 开头。assertEqual 是最常用的断言，检查实际值和期望值是否相等。',
        "difficulty": 'medium',
        "tags": ['unittest', 'TestCase'],
    },
    {
        "type": "fill_blank",
        "title": 'unittest 中，以什么前缀开头的方法会被自动识别为测试方法？',
        "description": '填写前缀',
        "answer": 'test_',
        "explanation": 'unittest 只运行以 test_ 开头的方法。例如 test_add 会被执行，而 helper_method 不会。这是约定，也是规则。',
        "difficulty": 'easy',
        "tags": ['unittest', '命名'],
    },
    {
        "type": "choice",
        "title": '以下哪个断言用于检查是否会抛出指定异常？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'assertEqual'},
            {"label": 'B', "text": 'assertTrue'},
            {"label": 'C', "text": 'assertRaises'},
            {"label": 'D', "text": 'assertIn'},
        ],
        "answer": 'C',
        "explanation": 'assertRaises 检查代码是否抛出指定异常。用法：with self.assertRaises(ValueError): do_something()。',
        "difficulty": 'medium',
        "tags": ['unittest', '断言'],
    },
]

# ============================================================
# Lesson 26
# ============================================================
EXERCISES_LESSON_26 = [
    {
        "type": "choice",
        "title": '集合（set）的主要特点是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '有序且可重复'},
            {"label": 'B', "text": '无序且元素不重复'},
            {"label": 'C', "text": '有序且不可重复'},
            {"label": 'D', "text": '创建后不可修改'},
        ],
        "answer": 'B',
        "explanation": '集合是无序的、元素不重复的数据结构。它基于哈希表实现，查找速度非常快（O(1)）。A 错在集合是无序的，C 说反了，D 错在集合可以增加元素。',
        "difficulty": 'easy',
        "tags": ['集合', 'set'],
    },
    {
        "type": "judge",
        "title": '可以用 & 运算符求两个集合的交集',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。& 求交集，| 求并集，- 求差集，^ 求对称差集。例如 {1,2,3} & {2,3,4} 的结果是 {2,3}。',
        "difficulty": 'easy',
        "tags": ['集合', '运算'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：找出两个列表的共同元素',
        "description": '用集合操作找出 list1 和 list2 中共同出现的元素',
        "answer": 'list1 = [1, 2, 3, 4, 5]\nlist2 = [4, 5, 6, 7, 8]\ncommon = list(set(list1) & set(list2))\nprint(common)  # [4, 5]',
        "explanation": '先用 set() 把列表转成集合，然后 & 求交集，最后 list() 转回列表。集合的去重特性天然适合这种场景。',
        "difficulty": 'medium',
        "tags": ['集合', '交集'],
    },
    {
        "type": "fill_blank",
        "title": '使用 set 给列表去重，代码应为：list(____(my_list))',
        "description": '填写函数名',
        "answer": 'set',
        "explanation": '把一个列表传给 set() 就能去除重复元素。例如 list(set([1,1,2,2,3])) 结果是 [1,2,3]。但要注意顺序会丢失。',
        "difficulty": 'easy',
        "tags": ['集合', '去重'],
    },
    {
        "type": "programming",
        "title": '找出只出现一次的元素',
        "description": '给定列表 nums = [1,2,3,2,1,4,5,4]，找出只出现一次的数字（结果：[3,5]）。提示：可以用集合或字典统计次数。',
        "answer": 'nums = [1, 2, 3, 2, 1, 4, 5, 4]\ncount = {}\nfor n in nums:\n    count[n] = count.get(n, 0) + 1\nresult = [k for k, v in count.items() if v == 1]\nprint(result)',
        "explanation": '用字典统计每个数字的出现次数，然后筛选出次数为 1 的。也可以：遍历集合，用 count() 判断（但效率较低）。',
        "difficulty": 'medium',
        "tags": ['集合', '统计'],
    },
]

# ============================================================
# Lesson 27
# ============================================================
EXERCISES_LESSON_27 = [
    {
        "type": "choice",
        "title": '以下哪个是列表推导式的正确语法？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '(x for x in range(10))'},
            {"label": 'B', "text": '[x**2 for x in range(10)]'},
            {"label": 'C', "text": '{x for x in range(10)}'},
            {"label": 'D', "text": 'for x in range(10): [x]'},
        ],
        "answer": 'B',
        "explanation": '列表推导式语法：[表达式 for 变量 in 可迭代对象 if 条件]。if 条件是可选的。[x for x in range(10) if x % 2 == 0] 生成 [0,2,4,6,8]。',
        "difficulty": 'easy',
        "tags": ['列表推导式'],
    },
    {
        "type": "judge",
        "title": '列表推导式比等价的 for 循环更高效',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。列表推导式在 C 层面执行，比 Python 层面的 for 循环 append 要快。而且代码更简洁。但不要为了用而用——复杂逻辑还是 for 循环可读性好。',
        "difficulty": 'medium',
        "tags": ['列表推导式', '性能'],
    },
    {
        "type": "code_fix",
        "title": '修复生成器表达式：改为列表',
        "description": '以下代码得到的是一个生成器对象而非列表，修复它',
        "answer": 'squares = [x**2 for x in range(10)]',
        "explanation": '原代码 (x**2 for x in range(10)) 是生成器表达式，返回生成器对象。把圆括号改成方括号就是列表推导式。或者用 list(x**2 for x in range(10))。',
        "difficulty": 'easy',
        "tags": ['列表推导式', '生成器'],
    },
    {
        "type": "fill_blank",
        "title": '[x for x in range(10) if x % 2 == 0] 的结果是什么？（用列表格式回答）',
        "description": '填写结果',
        "answer": '[0, 2, 4, 6, 8]',
        "explanation": '列表推导式遍历 0-9，筛选出偶数（x % 2 == 0），结果是 0, 2, 4, 6, 8。这是最常用的用法之一。',
        "difficulty": 'medium',
        "tags": ['列表推导式', '筛选'],
    },
    {
        "type": "programming",
        "title": '用列表推导式生成九九乘法表',
        "description": "用列表推导式生成所有 'a*b=c' 格式的字符串（1-9），结果如 ['1*1=1', '1*2=2', ...]",
        "answer": "[f'{a}*{b}={a*b}' for a in range(1, 10) for b in range(1, 10)]",
        "explanation": '这是双层 for 循环的列表推导式写法。外层循环 a 从 1 到 9，内层循环 b 从 1 到 9。等价于两个嵌套的 for 循环。',
        "difficulty": 'medium',
        "tags": ['列表推导式', '嵌套'],
    },
]

# ============================================================
# Lesson 28
# ============================================================
EXERCISES_LESSON_28 = [
    {
        "type": "choice",
        "title": 'Counter 的主要用途是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '计算数学表达式'},
            {"label": 'B', "text": '统计元素出现次数'},
            {"label": 'C', "text": '倒计时'},
            {"label": 'D', "text": '生成随机数'},
        ],
        "answer": 'B',
        "explanation": 'Counter 是 collections 模块中用于统计元素出现次数的类。它会返回一个类似字典的对象，键是元素，值是出现次数。',
        "difficulty": 'easy',
        "tags": ['collections', 'Counter'],
    },
    {
        "type": "judge",
        "title": 'defaultdict 在访问不存在的 key 时不会报 KeyError',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。defaultdict 需要指定一个工厂函数（如 int、list），访问不存在的 key 时会自动用工厂函数生成默认值。例如 defaultdict(int) 的默认值是 0。',
        "difficulty": 'medium',
        "tags": ['collections', 'defaultdict'],
    },
    {
        "type": "fill_blank",
        "title": "Counter('abracadabra').most_common(2) 返回什么？",
        "description": '填写前两个最常见字符',
        "answer": "[('a', 5), ('b', 2)]",
        "explanation": 'Counter 统计各字符出现次数：a 出现 5 次，b 出现 2 次，r 出现 2 次... most_common(2) 返回频率最高的前 2 个。',
        "difficulty": 'medium',
        "tags": ['Counter', 'most_common'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：用 defaultdict 实现分组',
        "description": '把学生按成绩等级分组（>=90 优秀, >=60 及格, <60 不及格）',
        "answer": "from collections import defaultdict\nstudents = [('小明', 95), ('小红', 60), ('小刚', 45), ('小美', 88)]\ngroups = defaultdict(list)\nfor name, score in students:\n    if score >= 90:\n        groups['优秀'].append(name)\n    elif score >= 60:\n        groups['及格'].append(name)\n    else:\n        groups['不及格'].append(name)",
        "explanation": 'defaultdict(list) 自动为每个新 key 创建空列表，不需要判断 key 是否存在。比普通 dict 更简洁。',
        "difficulty": 'medium',
        "tags": ['defaultdict', '分组'],
    },
    {
        "type": "choice",
        "title": '以下哪种场景最适合使用 namedtuple？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '存储大量动态变化的数据'},
            {"label": 'B', "text": '需要频繁增删元素的场景'},
            {"label": 'C', "text": '表示坐标点这样的简单数据结构'},
            {"label": 'D', "text": '作为函数的可变参数'},
        ],
        "answer": 'C',
        "explanation": 'namedtuple 适合表示轻量级的、不可变的数据记录，比如坐标点 Point(x, y)。它既有元组的轻量，又有类的可读性。不需要完整类的场景用 namedtuple 最合适。',
        "difficulty": 'medium',
        "tags": ['namedtuple'],
    },
]

# ============================================================
# Lesson 29
# ============================================================
EXERCISES_LESSON_29 = [
    {
        "type": "choice",
        "title": 'enumerate() 函数的作用是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '给列表排序'},
            {"label": 'B', "text": '遍历时同时获取索引和值'},
            {"label": 'C', "text": '统计列表元素数量'},
            {"label": 'D', "text": '过滤列表中的元素'},
        ],
        "answer": 'B',
        "explanation": "enumerate() 在遍历可迭代对象时同时提供索引和值。例如 for i, v in enumerate(['a','b','c']): 得到 (0,'a'), (1,'b'), (2,'c')。",
        "difficulty": 'easy',
        "tags": ['enumerate'],
    },
    {
        "type": "judge",
        "title": 'zip() 可以把多个列表「拉」在一起同时遍历',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": "正确。zip([1,2,3], ['a','b','c']) 得到 (1,'a'), (2,'b'), (3,'c')。如果列表长度不同，zip 会在最短的列表用完时停止。",
        "difficulty": 'easy',
        "tags": ['zip'],
    },
    {
        "type": "fill_blank",
        "title": 'all([True, True, False]) 的返回值是什么？',
        "description": '填写布尔值',
        "answer": 'False',
        "explanation": 'all() 检查可迭代对象中所有元素是否为真。只要有一个 False 就返回 False。any() 则相反，只要有一个 True 就返回 True。',
        "difficulty": 'easy',
        "tags": ['all', 'any'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：同时遍历三个列表',
        "description": '用 zip 同时遍历 names, ages, cities 三个列表',
        "answer": 'names = ["小明", "小红", "小刚"]\nages = [18, 20, 19]\ncities = ["北京", "上海", "广州"]\nfor name, age, city in zip(names, ages, cities):\n    print(f"{name}，{age}岁，来自{city}")',
        "explanation": 'zip 可以接受多个可迭代对象，返回元组的迭代器。配合 for 循环的解包语法，可以一次性获取多个列表的对应元素。',
        "difficulty": 'medium',
        "tags": ['zip', '遍历'],
    },
    {
        "type": "programming",
        "title": '用 any/all 检查列表',
        "description": '编写代码：检查列表 nums 中是否所有数都大于 0（全正数），以及是否存在偶数。',
        "answer": "nums = [1, 3, 5, 7, 2]\nall_positive = all(n > 0 for n in nums)\nhas_even = any(n % 2 == 0 for n in nums)\nprint(f'全正数: {all_positive}')\nprint(f'存在偶数: {has_even}')",
        "explanation": '使用生成器表达式配合 all/any，避免先构造完整的列表，节省内存。all(n > 0 for n in nums) 在遇到第一个不满足条件时就停止。',
        "difficulty": 'medium',
        "tags": ['all', 'any'],
    },
]

# ============================================================
# Lesson 30
# ============================================================
EXERCISES_LESSON_30 = [
    {
        "type": "choice",
        "title": '以下哪个 lambda 表达式的写法是正确的？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'lambda x, y { return x + y }'},
            {"label": 'B', "text": 'lambda x, y: x + y'},
            {"label": 'C', "text": 'lambda(x, y) => x + y'},
            {"label": 'D', "text": 'function(x, y): x + y'},
        ],
        "answer": 'B',
        "explanation": 'lambda 表达式语法：lambda 参数: 表达式。不需要 return，表达式的结果就是返回值。lambda x, y: x + y 定义了一个两个参数求和的匿名函数。',
        "difficulty": 'easy',
        "tags": ['lambda'],
    },
    {
        "type": "judge",
        "title": 'sort() 方法的 key 参数可以接受 lambda 函数',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": "正确。key 参数指定排序依据。例如 students.sort(key=lambda s: s['score'], reverse=True) 按成绩降序排列学生。这是 lambda 最常见的用法之一。",
        "difficulty": 'easy',
        "tags": ['lambda', '排序'],
    },
    {
        "type": "code_fix",
        "title": '修复排序：按字符串长度排序',
        "description": "以下代码排序不正确，修复它：words = ['apple', 'a', 'banana', 'the']",
        "answer": "words = ['apple', 'a', 'banana', 'the']\nwords.sort(key=len)\nprint(words)  # ['a', 'the', 'apple', 'banana']",
        "explanation": '原代码 .sort() 默认按字母顺序排序。按长度排序需要指定 key=len（len 是内置函数，不需要 lambda）。lambda 版本：key=lambda w: len(w)。',
        "difficulty": 'medium',
        "tags": ['排序', 'key'],
    },
    {
        "type": "fill_blank",
        "title": 'sorted() 和 .sort() 的区别是：sorted() 返回____，.sort() 在____排序',
        "description": '填写：新列表 / 原地',
        "answer": '新列表,原地',
        "explanation": 'sorted() 返回一个新的排序后的列表，原列表不变。.sort() 是列表的方法，直接修改原列表，返回 None。需要保留原列表时用 sorted()。',
        "difficulty": 'medium',
        "tags": ['sorted', 'sort'],
    },
    {
        "type": "programming",
        "title": '多级排序',
        "description": "students = [('小明', 90), ('小红', 85), ('小刚', 90), ('小美', 85)]。要求：先按成绩降序，成绩相同按姓名升序。",
        "answer": "students = [('小明', 90), ('小红', 85), ('小刚', 90), ('小美', 85)]\nresult = sorted(students, key=lambda s: (-s[1], s[0]))\nprint(result)",
        "explanation": '利用元组排序的特性：先比较第一个元素，相同时比较第二个。成绩取负数实现降序，名字自然升序。也可以用 result = sorted(students, key=lambda s: s[0]); result.sort(key=lambda s: s[1], reverse=True)。',
        "difficulty": 'hard',
        "tags": ['排序', '多级'],
    },
]

# ============================================================
# Lesson 31
# ============================================================
EXERCISES_LESSON_31 = [
    {
        "type": "choice",
        "title": 'Python 标准库中用于读写 CSV 的模块是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'csv'},
            {"label": 'B', "text": 'pandas'},
            {"label": 'C', "text": 'openpyxl'},
            {"label": 'D', "text": 'json'},
        ],
        "answer": 'A',
        "explanation": 'csv 模块是 Python 标准库的一部分，提供了 reader 和 writer 来方便地读写 CSV 文件。',
        "difficulty": 'easy',
        "tags": ['CSV'],
    },
    {
        "type": "judge",
        "title": 'csv.reader() 默认用逗号作为分隔符',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。CSV 的全称就是 Comma-Separated Values（逗号分隔值）。csv.reader() 默认以逗号为分隔符，也可以通过 delimiter 参数指定其他分隔符。',
        "difficulty": 'easy',
        "tags": ['CSV', 'reader'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：逐行读取 CSV 文件',
        "description": '打开 data.csv 文件，跳过表头，打印每一行',
        "answer": "import csv\nwith open('data.csv', 'r', newline='', encoding='utf-8') as f:\n    reader = csv.reader(f)\n    next(reader)  # 跳过表头\n    for row in reader:\n        print(row)",
        "explanation": "打开文件时建议使用 newline='' 参数（CSV 模块自己处理换行）。next(reader) 可以跳过第一行（表头）。每一行是一个字符串列表。",
        "difficulty": 'medium',
        "tags": ['CSV', '读取'],
    },
    {
        "type": "fill_blank",
        "title": '把数据写入 CSV 文件应使用 csv.____(f)',
        "description": '填写函数名',
        "answer": 'writer',
        "explanation": "csv.writer(f) 创建一个写入器，然后用 writer.writerow(['列1', '列2']) 写入单行，writer.writerows([['a','b'], ['c','d']]) 写入多行。",
        "difficulty": 'medium',
        "tags": ['CSV', 'writer'],
    },
    {
        "type": "programming",
        "title": '读取 CSV 并计算平均值',
        "description": '读取 scores.csv（格式：姓名,成绩），计算所有成绩的平均分。提示：用 DictReader 可以通过列名访问数据。',
        "answer": "import csv\nwith open('scores.csv', 'r', encoding='utf-8') as f:\n    reader = csv.DictReader(f)\n    scores = [int(row['成绩']) for row in reader]\navg = sum(scores) / len(scores)\nprint(f'平均分: {avg:.1f}')",
        "explanation": 'DictReader 把每行转成字典，键是列名。配合列表推导式提取成绩列。用 sum / len 计算平均值。',
        "difficulty": 'medium',
        "tags": ['CSV', 'DictReader'],
    },
]

# ============================================================
# Lesson 32
# ============================================================
EXERCISES_LESSON_32 = [
    {
        "type": "choice",
        "title": '以下哪个 JSON ↔ Python 类型对应关系是正确的？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'JSON object → Python list'},
            {"label": 'B', "text": 'JSON object → Python dict'},
            {"label": 'C', "text": 'JSON array → Python dict'},
            {"label": 'D', "text": 'JSON string → Python int'},
        ],
        "answer": 'B',
        "explanation": 'json.loads() 把 JSON 字符串转为 Python 对象（JSON object→dict，JSON array→list）。json.dumps() 反过来，把 Python 对象转为 JSON 字符串。',
        "difficulty": 'easy',
        "tags": ['JSON'],
    },
    {
        "type": "judge",
        "title": 'json.load() 用于读取文件中的 JSON，json.loads() 用于解析 JSON 字符串',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。记忆技巧：load() 不带 s 读文件，loads() 带 s 读字符串（s = string）。dump/dumps 同理。',
        "difficulty": 'easy',
        "tags": ['JSON', 'load'],
    },
    {
        "type": "fill_blank",
        "title": '把 Python 字典转为格式化的 JSON 字符串使用 json.dumps(d, ____=2)',
        "description": '填写参数名',
        "answer": 'indent',
        "explanation": 'indent 参数指定缩进空格数，让输出的 JSON 更易读。json.dumps(data, indent=2, ensure_ascii=False) 可以正确显示中文。',
        "difficulty": 'medium',
        "tags": ['JSON', 'dumps'],
    },
    {
        "type": "code_fix",
        "title": '修复 JSON 中文字符显示为 \\uXXXX 的问题',
        "description": '下面的代码让中文变成了 Unicode 转义序列，修复它',
        "answer": "import json\ndata = {'name': '小明', 'age': 18}\nprint(json.dumps(data, ensure_ascii=False))",
        "explanation": '默认 ensure_ascii=True 会把非 ASCII 字符转义。设置 ensure_ascii=False 就能正常显示中文。正解：json.dumps(data, ensure_ascii=False)。',
        "difficulty": 'medium',
        "tags": ['JSON', '中文'],
    },
    {
        "type": "programming",
        "title": '读写 JSON 配置文件',
        "description": "编写代码：读取 config.json 文件，修改其中的 theme 为 'dark'，然后保存回去。用 try/except 处理文件不存在的情况。",
        "answer": 'import json\ntry:\n    with open("config.json", "r", encoding="utf-8") as f:\n        config = json.load(f)\nexcept FileNotFoundError:\n    config = {}\nconfig["theme"] = "dark"\nwith open("config.json", "w", encoding="utf-8") as f:\n    json.dump(config, f, indent=2, ensure_ascii=False)',
        "explanation": '先尝试读取，文件不存在就用默认空字典。修改后写回。json.dump(obj, file) 直接写到文件，json.dumps(obj) 返回字符串。',
        "difficulty": 'medium',
        "tags": ['JSON', '文件操作'],
    },
]

# ============================================================
# Lesson 33
# ============================================================
EXERCISES_LESSON_33 = [
    {
        "type": "choice",
        "title": '以下哪个方法可以获得当前日期和时间？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'datetime.now()'},
            {"label": 'B', "text": 'datetime.get()'},
            {"label": 'C', "text": 'datetime.current()'},
            {"label": 'D', "text": 'datetime.fetch()'},
        ],
        "answer": 'A',
        "explanation": 'datetime.now() 返回当前日期和时间。date.today() 只返回日期（不含时间）。time() 返回当前时间戳。',
        "difficulty": 'easy',
        "tags": ['datetime'],
    },
    {
        "type": "judge",
        "title": 'datetime 对象之间可以直接相减得到时间差 (timedelta)',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。两个 datetime 对象相减得到一个 timedelta 对象。timedelta 可以用 .days 获取天数，用 .seconds 获取秒数部分。',
        "difficulty": 'easy',
        "tags": ['datetime', 'timedelta'],
    },
    {
        "type": "fill_blank",
        "title": "把字符串 '2025-01-15' 转成 date 对象，需要使用哪个方法？",
        "description": '填写格式',
        "answer": 'strptime',
        "explanation": "strptime (string parse time) 用于把字符串解析为日期时间对象。用法：datetime.strptime('2025-01-15', '%Y-%m-%d').date()。",
        "difficulty": 'medium',
        "tags": ['datetime', 'strptime'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：计算两个日期相差几天',
        "description": '计算今天和 2026 年元旦之间相差多少天',
        "answer": "from datetime import date\ntoday = date.today()\nnew_year = date(2026, 1, 1)\ndiff = (new_year - today).days\nprint(f'距元旦还有 {diff} 天')",
        "explanation": '两个 date 对象相减得到 timedelta。用 .days 获取天数（整数）。注意：如果 new_year 已过，结果会是负数。',
        "difficulty": 'medium',
        "tags": ['datetime', '日期计算'],
    },
    {
        "type": "programming",
        "title": '计算自己的年龄',
        "description": "输入出生日期（格式 YYYY-MM-DD），输出精确到天的年龄。例如输入 2000-01-01，输出类似 '你已出生 9131 天'。",
        "answer": "from datetime import datetime\nbirth = input('出生日期(YYYY-MM-DD): ')\nbirth_date = datetime.strptime(birth, '%Y-%m-%d')\ndays = (datetime.now() - birth_date).days\nprint(f'你已出生 {days} 天')",
        "explanation": '用 datetime.strptime 解析输入。当前时间减去出生时间得到 timedelta。.days 获取天数。可以进一步计算年数 = days / 365.25。',
        "difficulty": 'medium',
        "tags": ['datetime', '计算'],
    },
]

# ============================================================
# Lesson 34
# ============================================================
EXERCISES_LESSON_34 = [
    {
        "type": "choice",
        "title": '正则表达式中 \\d 匹配什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '任意字母'},
            {"label": 'B', "text": '任意数字 0-9'},
            {"label": 'C', "text": '任意空白字符'},
            {"label": 'D', "text": '小数点'},
        ],
        "answer": 'B',
        "explanation": '\\d 匹配任意数字（0-9）。\\w 匹配字母数字下划线，\\s 匹配空白字符，. 匹配任意字符（除换行）。',
        "difficulty": 'easy',
        "tags": ['正则'],
    },
    {
        "type": "judge",
        "title": 're.search() 和 re.match() 完全一样',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'B',
        "explanation": '错误。re.match() 只从字符串开头匹配，re.search() 在字符串任意位置搜索第一个匹配。re.findall() 返回所有匹配。',
        "difficulty": 'medium',
        "tags": ['正则', 're'],
    },
    {
        "type": "fill_blank",
        "title": '正则中 + 和 * 的区别是：+ 表示 ____，* 表示 ____',
        "description": '填写：至少一次 / 零次或多次',
        "answer": '至少一次,零次或多次',
        "explanation": "a+ 匹配一个或多个 'a'（a、aa、aaa...）。a* 匹配零个或多个 'a'（空串、a、aa...）。? 表示 0 或 1 次。",
        "difficulty": 'medium',
        "tags": ['正则', '量词'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：验证手机号',
        "description": '验证输入的字符串是否是 11 位数字的手机号（以 1 开头）',
        "answer": "import re\nphone = input('手机号: ')\nif re.fullmatch(r'1\\d{10}', phone):\n    print('格式正确')\nelse:\n    print('格式错误')",
        "explanation": 'fullmatch 检查整个字符串是否匹配。1\\d{10} 表示以 1 开头，后面跟 10 位数字，共 11 位。\\d{10} 等价于 \\d\\d\\d\\d\\d\\d\\d\\d\\d\\d。',
        "difficulty": 'medium',
        "tags": ['正则', '验证'],
    },
    {
        "type": "programming",
        "title": '提取所有邮箱地址',
        "description": '从一段文本中找出所有的邮箱地址。邮箱格式：名称@域名.后缀。提示：用 re.findall()。',
        "answer": "import re\ntext = '请联系 admin@example.com 或者 support@site.cn'\npattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\nemails = re.findall(pattern, text)\nprint(emails)",
        "explanation": '邮箱正则解析：[\\w.+-]+ 匹配用户名部分（字母数字和特定符号），@ 是字面量，[\\w.-]+ 匹配域名，\\.[a-zA-Z]{2,} 匹配顶级域名（至少2个字母）。',
        "difficulty": 'hard',
        "tags": ['正则', 'findall'],
    },
]

# ============================================================
# Lesson 35
# ============================================================
EXERCISES_LESSON_35 = [
    {
        "type": "choice",
        "title": "Path('/a/b') / 'c' 的结果是什么？",
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": "'/a/b/c' （字符串）"},
            {"label": 'B', "text": "Path('/a/b/c')"},
            {"label": 'C', "text": "Path('/a/c')"},
            {"label": 'D', "text": '报错，不能使用 / 拼接'},
        ],
        "answer": 'B',
        "explanation": "pathlib 重载了 / 运算符用于路径拼接。Path('/a/b') / 'c' 的结果是 Path('/a/b/c')（在 Windows 上是 \\a\\b\\c）。",
        "difficulty": 'easy',
        "tags": ['pathlib'],
    },
    {
        "type": "judge",
        "title": 'pathlib 的 Path 对象比 os.path 的字符串操作更直观、更安全',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": "正确。pathlib 是现代化、面向对象的路径处理方式。Path.home() / 'documents' 比 os.path.join(os.path.expanduser('~'), 'documents') 更清晰。",
        "difficulty": 'easy',
        "tags": ['pathlib', 'os.path'],
    },
    {
        "type": "fill_blank",
        "title": "Path('data.csv').suffix 返回什么？",
        "description": '填写结果',
        "answer": '.csv',
        "explanation": '.suffix 返回文件扩展名（包含点）。.stem 返回不带扩展名的文件名。.name 返回完整文件名。.parent 返回父目录路径。',
        "difficulty": 'medium',
        "tags": ['pathlib', '属性'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：遍历目录中的所有 .txt 文件',
        "description": '用 pathlib 列出当前目录下所有 .txt 文件',
        "answer": "from pathlib import Path\nfor f in Path('.').glob('*.txt'):\n    print(f.name)",
        "explanation": "Path.glob() 支持通配符匹配文件名。'*.txt' 匹配所有 .txt 文件。'**/*.txt' 可以递归匹配子目录中的 .txt 文件。",
        "difficulty": 'medium',
        "tags": ['pathlib', 'glob'],
    },
    {
        "type": "code_fix",
        "title": '修复代码：安全创建目录',
        "description": '以下代码在目录已存在时会报错，修复它',
        "answer": "from pathlib import Path\nPath('output').mkdir(parents=True, exist_ok=True)",
        "explanation": "原代码：Path('output').mkdir() 在目录已存在时抛出 FileExistsError。修复方法：添加 exist_ok=True（已存在时不报错）和 parents=True（自动创建中间目录）。",
        "difficulty": 'medium',
        "tags": ['pathlib', 'mkdir'],
    },
]

# ============================================================
# Lesson 36
# ============================================================
EXERCISES_LESSON_36 = [
    {
        "type": "choice",
        "title": '在 Python 中定义类使用哪个关键字？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'class'},
            {"label": 'B', "text": 'def'},
            {"label": 'C', "text": 'struct'},
            {"label": 'D', "text": 'object'},
        ],
        "answer": 'A',
        "explanation": 'class 关键字用于定义类。类名通常使用驼峰命名法（PascalCase），如 class Student。',
        "difficulty": 'easy',
        "tags": ['类', 'OOP'],
    },
    {
        "type": "judge",
        "title": 'self 参数在调用方法时由 Python 自动传入',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。self 代表实例本身，定义方法时必须写 self 作为第一个参数，但调用时不需要传。例如 obj.method() 等价于 Class.method(obj)。',
        "difficulty": 'easy',
        "tags": ['self', 'OOP'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：定义一个 Dog 类',
        "description": '定义一个 Dog 类，包含 name 属性和 bark() 方法',
        "answer": "class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        return f'{self.name} says woof!'\n\n# 使用\ndog = Dog('Buddy')\nprint(dog.bark())  # Buddy says woof!",
        "explanation": '__init__ 是构造方法，在创建实例时自动调用。self.name = name 把参数存为实例属性。普通方法第一个参数必须是 self。',
        "difficulty": 'medium',
        "tags": ['类', '__init__'],
    },
    {
        "type": "fill_blank",
        "title": '类中定义的函数称为____，通过实例调用时自动接收____作为第一个参数',
        "description": '填写：方法 / self',
        "answer": '方法,self',
        "explanation": '在类内部定义的函数叫方法（method）。实例调用方法时，Python 自动把实例作为第一个参数传入，约定命名为 self。',
        "difficulty": 'easy',
        "tags": ['方法', 'self'],
    },
    {
        "type": "programming",
        "title": '创建一个 BankAccount 类',
        "description": '定义一个 BankAccount 类，包含：owner 属性（开户人名称），balance 属性（余额，默认 0），deposit(amount) 方法（存款），withdraw(amount) 方法（取款，余额不足时提示）。',
        "answer": "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n\n    def deposit(self, amount):\n        if amount > 0:\n            self.balance += amount\n            print(f'存入 {amount}，余额 {self.balance}')\n\n    def withdraw(self, amount):\n        if amount > self.balance:\n            print('余额不足')\n        elif amount > 0:\n            self.balance -= amount\n            print(f'取出 {amount}，余额 {self.balance}')",
        "explanation": '封装是 OOP 的核心概念：数据（balance）和操作数据的方法（deposit/withdraw）放在一起。通过方法操作属性可以加入验证逻辑（余额检查、金额必须为正）。',
        "difficulty": 'medium',
        "tags": ['类', '封装'],
    },
]

# ============================================================
# Lesson 37
# ============================================================
EXERCISES_LESSON_37 = [
    {
        "type": "choice",
        "title": '在 Python 中，子类如何继承父类？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'class Child extends Parent:'},
            {"label": 'B', "text": 'class Child inherits Parent:'},
            {"label": 'C', "text": 'class Child(Parent):'},
            {"label": 'D', "text": 'class Child <- Parent:'},
        ],
        "answer": 'C',
        "explanation": '语法：class Child(Parent):。子类继承父类的所有方法和属性。Python 支持多重继承（多个父类）。',
        "difficulty": 'easy',
        "tags": ['继承'],
    },
    {
        "type": "judge",
        "title": '子类可以覆盖（重写）父类的方法，这叫做方法重写（override）',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。子类定义同名方法会覆盖父类的实现。子类中可以用 super().method() 调用父类的原始方法。这是多态的基础。',
        "difficulty": 'easy',
        "tags": ['继承', 'override'],
    },
    {
        "type": "fill_blank",
        "title": '在子类中调用父类的 __init__ 方法，使用____函数',
        "description": '填写函数名',
        "answer": 'super()',
        "explanation": 'super() 返回父类的代理对象。super().__init__(name) 调用父类的构造方法。在多重继承中，super() 按照 MRO（方法解析顺序）查找。',
        "difficulty": 'medium',
        "tags": ['super', '继承'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：实现继承关系',
        "description": '创建 Animal 父类和 Cat 子类，Cat 覆盖 speak() 方法',
        "answer": "class Animal:\n    def speak(self):\n        return '...'\n\nclass Cat(Animal):\n    def speak(self):\n        return 'Meow'\n\ncat = Cat()\nprint(cat.speak())  # Meow",
        "explanation": 'Cat 继承 Animal，覆盖了 speak() 方法。调用 cat.speak() 时，Python 先找 Cat 类的方法，找到就用，不会去 Animal 中找。这就是多态。',
        "difficulty": 'medium',
        "tags": ['继承', '多态'],
    },
    {
        "type": "programming",
        "title": '实现形状继承体系',
        "description": '创建 Shape 基类（含 area() 方法返回 0），以及 Rectangle 和 Circle 子类，各自实现 area()。',
        "answer": 'import math\n\nclass Shape:\n    def area(self):\n        return 0\n\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\n\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return math.pi * self.radius ** 2',
        "explanation": '这是多态的经典示例：不同形状有各自的 area() 实现。遍历形状列表时，直接调用 shape.area()，不需要判断具体类型。开闭原则：对扩展开放（加新形状），对修改关闭。',
        "difficulty": 'medium',
        "tags": ['继承', '多态'],
    },
]

# ============================================================
# Lesson 38
# ============================================================
EXERCISES_LESSON_38 = [
    {
        "type": "choice",
        "title": '__str__ 方法在什么时候被调用？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '创建对象时'},
            {"label": 'B', "text": 'print(obj) 或 str(obj) 时'},
            {"label": 'C', "text": '删除对象时'},
            {"label": 'D', "text": '比较两个对象时'},
        ],
        "answer": 'B',
        "explanation": '__str__ 在 print(obj) 或 str(obj) 时调用，返回给用户看的友好字符串。__repr__ 在交互环境或 repr(obj) 时调用，返回给开发者看的详细信息。',
        "difficulty": 'easy',
        "tags": ['魔术方法', '__str__'],
    },
    {
        "type": "judge",
        "title": '__len__ 方法可以让自定义对象支持 len() 函数',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。定义了 __len__(self) 后，就可以对实例使用 len(obj)。类似地，__getitem__ 支持 obj[key]，__contains__ 支持 in 运算符。',
        "difficulty": 'easy',
        "tags": ['魔术方法', '__len__'],
    },
    {
        "type": "fill_blank",
        "title": '要实现 obj1 == obj2 的值比较（而非身份比较），需要定义哪个魔术方法？',
        "description": '填写方法名',
        "answer": '__eq__',
        "explanation": '默认的 == 比较对象的内存地址（is 语义）。定义 __eq__ 可以自定义比较逻辑。例如两个 Person 对象如果姓名相同就认为相等。',
        "difficulty": 'medium',
        "tags": ['魔术方法', '__eq__'],
    },
    {
        "type": "code_completion",
        "title": '补全魔术方法：让对象可以相加',
        "description": '为 Vector2D 类实现 __add__ 方法，支持 v1 + v2',
        "answer": "class Vector2D:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __add__(self, other):\n        return Vector2D(self.x + other.x, self.y + other.y)\n\n    def __str__(self):\n        return f'Vector({self.x}, {self.y})'",
        "explanation": '__add__ 定义 + 运算符的行为。self 是左操作数，other 是右操作数。返回新的 Vector2D 对象，不修改原对象（好的实践）。',
        "difficulty": 'medium',
        "tags": ['魔术方法', '__add__'],
    },
    {
        "type": "choice",
        "title": '以下哪个魔术方法可以让对象像函数一样被调用？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '__init__'},
            {"label": 'B', "text": '__func__'},
            {"label": 'C', "text": '__run__'},
            {"label": 'D', "text": '__call__'},
        ],
        "answer": 'D',
        "explanation": '实现了 __call__ 的类的实例可以直接像函数一样调用：obj()。这叫做可调用对象（callable）。常用于装饰器、回调函数等场景。',
        "difficulty": 'hard',
        "tags": ['魔术方法', '__call__'],
    },
]

# ============================================================
# Lesson 39
# ============================================================
EXERCISES_LESSON_39 = [
    {
        "type": "choice",
        "title": '@property 装饰器的主要作用是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '让方法像属性一样访问'},
            {"label": 'B', "text": '让属性像方法一样调用'},
            {"label": 'C', "text": '让方法运行更快'},
            {"label": 'D', "text": '让属性变成私有'},
        ],
        "answer": 'A',
        "explanation": '@property 让方法可以像属性一样访问（不加括号）。常用于：1）计算属性；2）属性访问时做验证；3）保护私有属性不被直接修改。',
        "difficulty": 'easy',
        "tags": ['@property'],
    },
    {
        "type": "judge",
        "title": '使用 @property 可以实现属性的 getter、setter 和 deleter',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。@property 定义 getter，@name.setter 定义 setter，@name.deleter 定义 deleter。可以在 setter 中加入验证逻辑。',
        "difficulty": 'medium',
        "tags": ['@property', 'setter'],
    },
    {
        "type": "code_fix",
        "title": '修复代码：让 temperature 属性不能低于 -273.15',
        "description": '当前代码允许设置任意温度值，添加 setter 来限制最低温度',
        "answer": "class Celsius:\n    def __init__(self, temperature=0):\n        self._temperature = temperature\n\n    @property\n    def temperature(self):\n        return self._temperature\n\n    @temperature.setter\n    def temperature(self, value):\n        if value < -273.15:\n            raise ValueError('温度不能低于绝对零度')\n        self._temperature = value",
        "explanation": '约定用 _前缀 表示私有属性。@property 定义 getter，@temperature.setter 在赋值时触发验证。这样保护了数据的完整性。',
        "difficulty": 'medium',
        "tags": ['@property', 'setter'],
    },
    {
        "type": "fill_blank",
        "title": '在 setter 中添加验证逻辑，当值不合法时通常抛出____异常',
        "description": '填写异常类型',
        "answer": 'ValueError',
        "explanation": 'ValueError 表示值本身没问题但内容不合适。例如温度低于绝对零度、年龄为负数等场景。',
        "difficulty": 'medium',
        "tags": ['@property', 'ValueError'],
    },
    {
        "type": "programming",
        "title": '实现 Person 类带 age 验证',
        "description": '创建 Person 类，使用 @property 定义 age 属性。getter 正常返回，setter 确保年龄在 0-150 之间，否则抛出 ValueError。',
        "answer": "class Person:\n    def __init__(self, name, age=0):\n        self.name = name\n        self._age = age\n\n    @property\n    def age(self):\n        return self._age\n\n    @age.setter\n    def age(self, value):\n        if not isinstance(value, int):\n            raise TypeError('年龄必须是整数')\n        if not (0 <= value <= 150):\n            raise ValueError('年龄必须在 0-150 之间')\n        self._age = value",
        "explanation": '使用 @property 封装属性，防止不合法的数据进入系统。外部看上去在设置属性 p.age = 200，实际上触发的是 setter 方法，可以拦截和验证。',
        "difficulty": 'medium',
        "tags": ['@property', '封装'],
    },
]

# ============================================================
# Lesson 40
# ============================================================
EXERCISES_LESSON_40 = [
    {
        "type": "choice",
        "title": '使用 dataclass 装饰器需要从哪个模块导入？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'collections'},
            {"label": 'B', "text": 'dataclasses'},
            {"label": 'C', "text": 'typing'},
            {"label": 'D', "text": 'attrs'},
        ],
        "answer": 'B',
        "explanation": 'dataclass 是 dataclasses 模块中的装饰器。Python 3.7+ 可用。使用 @dataclass 装饰器会自动生成 __init__、__repr__、__eq__ 等方法。',
        "difficulty": 'easy',
        "tags": ['dataclass'],
    },
    {
        "type": "judge",
        "title": '使用 @dataclass 后， Python 会自动生成 __init__ 方法',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。@dataclass 会根据类属性自动生成 __init__、__repr__、__eq__ 等方法，大大减少了样板代码。如果有默认值的属性必须放在没有默认值的属性后面。',
        "difficulty": 'easy',
        "tags": ['dataclass', '__init__'],
    },
    {
        "type": "fill_blank",
        "title": 'dataclass 中，如果想排除某个属性不让它参与 __repr__，应使用 field() 的哪个参数？',
        "description": '填写参数名',
        "answer": 'repr',
        "explanation": 'field(repr=False) 排除该属性。其他常用参数：compare=False（不参与比较），default=值（默认值），default_factory=list（可变默认值）。',
        "difficulty": 'medium',
        "tags": ['dataclass', 'field'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：定义一个数据类',
        "description": '用 @dataclass 定义一个 Student 类，包含 name, age, score 三个属性，score 默认 0',
        "answer": "from dataclasses import dataclass\n\n@dataclass\nclass Student:\n    name: str\n    age: int\n    score: float = 0\n\ns = Student('小明', 18)\nprint(s)  # Student(name='小明', age=18, score=0)",
        "explanation": '类属性用类型注解定义。有默认值的属性（score）必须排在后面。@dataclass 自动生成了 __init__ 和 __repr__，print(s) 直接打印可读的字符串。',
        "difficulty": 'medium',
        "tags": ['dataclass'],
    },
    {
        "type": "choice",
        "title": 'dataclass 的 frozen=True 参数的作用是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '自动给属性赋默认值'},
            {"label": 'B', "text": '让数据类可以比较大小'},
            {"label": 'C', "text": '让实例变为不可变对象'},
            {"label": 'D', "text": '自动持久化到数据库'},
        ],
        "answer": 'C',
        "explanation": 'frozen=True 让数据类变成不可变（immutable）的，类似于元组。创建后不能修改任何属性的值。适合于需要哈希的场景（放入 set 或作为 dict 的 key）。',
        "difficulty": 'medium',
        "tags": ['dataclass', 'frozen'],
    },
]
# ============================================================
# Lesson 41
# ============================================================
EXERCISES_LESSON_41 = [
    {
        "type": "choice",
        "title": '装饰器本质上是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '一种新的数据类型'},
            {"label": 'B', "text": '接受函数并返回函数的高阶函数'},
            {"label": 'C', "text": '一种性能优化工具'},
            {"label": 'D', "text": 'Python 内置的数据结构'},
        ],
        "answer": 'B',
        "explanation": '装饰器本质上是一个接受函数作为参数并返回新函数的高阶函数。@decorator 语法糖等价于 func = decorator(func)。',
        "difficulty": 'easy',
        "tags": ['装饰器'],
    },
    {
        "type": "judge",
        "title": '@timer 装饰器会永久改变被装饰函数的名称和文档字符串',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'B',
        "explanation": '错误。如果不使用 @functools.wraps，装饰后的函数会失去原来的 __name__ 和 __doc__。使用 @wraps(func) 可以保留这些元信息。',
        "difficulty": 'medium',
        "tags": ['装饰器', 'wraps'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：定义一个计时装饰器',
        "description": '定义一个 @timer 装饰器，打印函数的执行时间',
        "answer": "import time\nfrom functools import wraps\n\ndef timer(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'{func.__name__} 耗时: {end - start:.3f}s')\n        return result\n    return wrapper",
        "explanation": '装饰器返回 wrapper 函数。*args/**kwargs 确保能接受任意参数。@wraps(func) 保留原函数的元信息。wrapper 在调用前后记录时间。',
        "difficulty": 'medium',
        "tags": ['装饰器', '计时'],
    },
    {
        "type": "fill_blank",
        "title": '带参数的装饰器需要比普通装饰器多一层嵌套，本质是一个返回____的函数',
        "description": '填写：装饰器',
        "answer": '装饰器',
        "explanation": '带参数的装饰器写法：def repeat(n): 返回装饰器 def decorator(func): 返回 wrapper。三层嵌套：外层接收参数，中层接收函数，内层是实际包装。',
        "difficulty": 'hard',
        "tags": ['装饰器', '带参数'],
    },
    {
        "type": "programming",
        "title": '实现一个重试装饰器',
        "description": '编写 @retry(max_attempts) 装饰器：被装饰的函数如果抛出异常，自动重试，最多重试 max_attempts 次，所有尝试都失败后才抛出异常。',
        "answer": "from functools import wraps\n\ndef retry(max_attempts=3):\n    def decorator(func):\n        @wraps(func)\n        def wrapper(*args, **kwargs):\n            for attempt in range(1, max_attempts + 1):\n                try:\n                    return func(*args, **kwargs)\n                except Exception as e:\n                    if attempt == max_attempts:\n                        raise\n                    print(f'重试 {attempt}/{max_attempts}...')\n        return wrapper\n    return decorator",
        "explanation": '三层嵌套：retry 接收参数返回 decorator，decorator 接收函数返回 wrapper。wrapper 用 try/except 包裹调用，失败时循环重试。只有最后一次失败才真正抛出异常。',
        "difficulty": 'hard',
        "tags": ['装饰器', '重试'],
    },
]

# ============================================================
# Lesson 42
# ============================================================
EXERCISES_LESSON_42 = [
    {
        "type": "choice",
        "title": '使用 with 语句打开文件的好处是什么？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '读取速度更快'},
            {"label": 'B', "text": '文件不会被其他程序修改'},
            {"label": 'C', "text": '自动关闭文件，即使出现异常'},
            {"label": 'D', "text": '自动备份文件'},
        ],
        "answer": 'C',
        "explanation": 'with 语句会自动调用 __exit__ 方法，确保文件被正确关闭，即使发生异常也不怕。这就是上下文管理器的核心作用。',
        "difficulty": 'easy',
        "tags": ['with', '上下文管理器'],
    },
    {
        "type": "judge",
        "title": '任何实现了 __enter__ 和 __exit__ 方法的类都可以作为上下文管理器使用',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。with obj 会先调用 obj.__enter__() 获取上下文对象，离开时调用 obj.__exit__() 进行清理。这是协议，不是继承关系。',
        "difficulty": 'medium',
        "tags": ['with', '__enter__', '__exit__'],
    },
    {
        "type": "fill_blank",
        "title": 'Python 标准库中哪个模块提供了 @contextmanager 装饰器，可以用生成器函数简单创建上下文管理器？',
        "description": '填写模块名',
        "answer": 'contextlib',
        "explanation": 'contextlib.contextmanager 装饰器让生成器函数变成上下文管理器。yield 之前是 __enter__，yield 之后是 __exit__。代码更简洁。',
        "difficulty": 'medium',
        "tags": ['contextlib', 'contextmanager'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：实现自定义上下文管理器',
        "description": '创建一个 Timer 上下文管理器，用 with 语句测量代码块执行时间',
        "answer": "import time\n\nclass Timer:\n    def __enter__(self):\n        self.start = time.time()\n        return self\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        elapsed = time.time() - self.start\n        print(f'耗时: {elapsed:.3f}s')\n        return False  # 不抑制异常\n\nwith Timer():\n    sum(range(1000000))",
        "explanation": '__enter__ 记录开始时间并返回 self。__exit__ 计算耗时并打印。返回 False 让异常正常传播，返回 True 则抑制异常。',
        "difficulty": 'medium',
        "tags": ['上下文管理器', '__enter__', '__exit__'],
    },
    {
        "type": "programming",
        "title": '用 @contextmanager 实现临时目录切换',
        "description": '实现一个上下文管理器，进入时切换到指定目录，退出时恢复原目录。使用 contextlib.contextmanager 装饰器。',
        "answer": "import os\nfrom contextlib import contextmanager\n\n@contextmanager\ndef change_dir(path):\n    old_dir = os.getcwd()\n    try:\n        os.chdir(path)\n        yield\n    finally:\n        os.chdir(old_dir)\n\n# 使用\nwith change_dir('/tmp'):\n    print('当前在:', os.getcwd())\nprint('已恢复:', os.getcwd())",
        "explanation": 'yield 把控制权交给 with 块。yield 前是 __enter__ 逻辑（切换目录），yield 后的 finally 是 __exit__ 逻辑（恢复目录）。无论 with 块是否异常，finally 确保目录被恢复。',
        "difficulty": 'medium',
        "tags": ['contextmanager', '目录切换'],
    },
]

# ============================================================
# Lesson 43
# ============================================================
EXERCISES_LESSON_43 = [
    {
        "type": "choice",
        "title": '生成器函数使用什么关键字来返回值？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'return'},
            {"label": 'B', "text": 'await'},
            {"label": 'C', "text": 'yield'},
            {"label": 'D', "text": 'send'},
        ],
        "answer": 'C',
        "explanation": '生成器函数用 yield 代替 return。每次 yield 暂停函数并返回值，下次从暂停点继续。这使得生成器可以「惰性」产生值，节省内存。',
        "difficulty": 'easy',
        "tags": ['生成器', 'yield'],
    },
    {
        "type": "judge",
        "title": '生成器比等价的列表更节省内存',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。生成器是惰性求值，只在需要时才生成下一个值，不需要把全部结果存在内存中。range(1000000) 占几十字节，list(range(1000000)) 占约 8MB。',
        "difficulty": 'easy',
        "tags": ['生成器', '内存'],
    },
    {
        "type": "fill_blank",
        "title": '任何实现了 ____(self) 和 ____(self) 方法的类都可以作为迭代器',
        "description": '填写两个方法名',
        "answer": '__iter__,__next__',
        "explanation": '__iter__ 返回迭代器对象（通常是 self），__next__ 返回下一个值，没有更多值时抛出 StopIteration。for 循环自动处理这些。',
        "difficulty": 'medium',
        "tags": ['迭代器', '协议'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：用生成器实现斐波那契数列',
        "description": '编写生成器函数 fib(n)，生成前 n 个斐波那契数',
        "answer": "def fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\n# 使用\nfor num in fib(10):\n    print(num, end=' ')  # 0 1 1 2 3 5 8 13 21 34",
        "explanation": '生成器中 yield 逐个产出斐波那契数。每次调用 next() 或 for 循环迭代时，函数从上次 yield 处恢复执行。a, b = b, a+b 是经典的交换+前进。',
        "difficulty": 'medium',
        "tags": ['生成器', '斐波那契'],
    },
    {
        "type": "code_fix",
        "title": '修复代码：生成器只能用一次',
        "description": '下面的代码第二次遍历生成器为空，修复它（改成可以重复使用）',
        "answer": 'def square_numbers(n):\n    for i in range(1, n + 1):\n        yield i * i\n\n# 改成可以重复使用的形式\nsq = list(square_numbers(5))\nprint(sum(sq))  # 55\nprint(sum(sq))  # 55（现在可以了）',
        "explanation": '生成器是单向的、一次性的。如果需要多次使用，用 list() 把结果存到列表中。或者把生成器函数包装成一个可调用对象，每次调用都返回新的生成器。',
        "difficulty": 'medium',
        "tags": ['生成器', '一次性'],
    },
]

# ============================================================
# Lesson 44
# ============================================================
EXERCISES_LESSON_44 = [
    {
        "type": "choice",
        "title": 'Python 中以下哪个是正确的类型注解写法？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": "name: String = '小明'"},
            {"label": 'B', "text": "name: str = '小明'"},
            {"label": 'C', "text": "str name = '小明'"},
            {"label": 'D', "text": "name = str('小明')"},
        ],
        "answer": 'B',
        "explanation": "变量注解：name: str = '小明'。函数注解：def greet(name: str) -> str:。Python 的类型注解是可选的，运行时不强制检查。",
        "difficulty": 'easy',
        "tags": ['类型注解'],
    },
    {
        "type": "judge",
        "title": '类型注解会在运行时强制检查类型',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'B',
        "explanation": '错误。Python 的类型注解只是提示，运行时不检查。需要 mypy、pyright 等静态类型检查器或运行时库（pydantic、typeguard）来验证。',
        "difficulty": 'easy',
        "tags": ['类型注解', '运行时'],
    },
    {
        "type": "fill_blank",
        "title": '表示一个列表元素都是 int，应该写：____。表示一个字典的 key 是 str、value 是 int，应该写：____',
        "description": '填写两个类型注解',
        "answer": 'list[int],dict[str, int]',
        "explanation": 'Python 3.9+ 可以直接用 list[int]、dict[str, int]。3.8 及以前需要 from typing import List, Dict，写 List[int]、Dict[str, int]。',
        "difficulty": 'medium',
        "tags": ['类型注解', '泛型'],
    },
    {
        "type": "code_completion",
        "title": '补全类型注解：给函数加上完整的类型注解',
        "description": '为以下函数添加参数和返回值的类型注解',
        "answer": "from typing import Optional\n\ndef find_user(name: str) -> Optional[dict]:\n    users = {'admin': {'role': 'admin'}}\n    return users.get(name)\n\ndef process_numbers(nums: list[int]) -> list[int]:\n    return [n * 2 for n in nums]",
        "explanation": 'Optional[X] 等价于 Union[X, None]，表示可能返回 None。list[int] 表示整数列表。-> 后面是返回值类型。',
        "difficulty": 'medium',
        "tags": ['类型注解', 'Optional'],
    },
    {
        "type": "programming",
        "title": '为数据类添加完整类型注解',
        "description": '定义一个函数，接收字典列表和排序键，返回排序后的字典列表。为函数添加完整的类型注解。',
        "answer": "def sort_records(records: list[dict[str, object]], key: str, reverse: bool = False) -> list[dict[str, object]]:\n    return sorted(records, key=lambda r: r.get(key, ''), reverse=reverse)\n\ndata = [{'name': '小明', 'score': 90}, {'name': '小红', 'score': 85}]\nresult = sort_records(data, 'score', reverse=True)",
        "explanation": 'dict[str, object] 表示键为字符串、值为任意类型的字典。list[dict[str, object]] 表示这种字典的列表。-> 标注返回值类型。默认值参数也要标注类型。',
        "difficulty": 'medium',
        "tags": ['类型注解', '综合'],
    },
]

# ============================================================
# Lesson 45
# ============================================================
EXERCISES_LESSON_45 = [
    {
        "type": "choice",
        "title": '在 Python 中创建虚拟环境使用哪个命令？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'python -m venv myenv'},
            {"label": 'B', "text": 'python create-env myenv'},
            {"label": 'C', "text": 'pip create myenv'},
            {"label": 'D', "text": 'python virtual myenv'},
        ],
        "answer": 'A',
        "explanation": 'python -m venv myenv 创建虚拟环境。Python 会自动把 myenv 目录排除在 git 之外。',
        "difficulty": 'easy',
        "tags": ['venv'],
    },
    {
        "type": "judge",
        "title": '使用虚拟环境可以避免不同项目之间的依赖冲突',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。每个虚拟环境有独立的 site-packages 目录，项目 A 用 Django 4，项目 B 用 Django 5，互不干扰。这是 Python 项目开发的标准实践。',
        "difficulty": 'easy',
        "tags": ['venv', '依赖管理'],
    },
    {
        "type": "fill_blank",
        "title": '把当前环境的依赖导出到文件使用 pip ____ > requirements.txt',
        "description": '填写命令',
        "answer": 'freeze',
        "explanation": 'pip freeze 列出所有已安装的包及其版本。pip freeze > requirements.txt 保存依赖列表。pip install -r requirements.txt 在新环境中安装。',
        "difficulty": 'easy',
        "tags": ['pip', 'freeze'],
    },
    {
        "type": "code_fix",
        "title": '修复导入错误：安装了包但无法导入',
        "description": '小明用 pip install requests 安装了包，但在代码中 import requests 报 ModuleNotFoundError。可能的原因是什么？',
        "answer": '可能原因：1）安装到了全局环境，但运行代码时用的是虚拟环境（或反过来）；2）IDE 选择了错误的解释器。解决方案：在虚拟环境激活状态下重新 pip install requests。',
        "explanation": '当使用虚拟环境时，pip install 安装的包只在那个环境中可用。确保终端和 IDE 使用同一个 Python 解释器。可以用 pip list 和 which python 来排查。',
        "difficulty": 'medium',
        "tags": ['venv', '依赖'],
    },
    {
        "type": "choice",
        "title": 'requirements.txt 和 pyproject.toml 的关系是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '它们是同一个文件的不同名字'},
            {"label": 'B', "text": 'requirements.txt 可以完全替代 pyproject.toml'},
            {"label": 'C', "text": 'requirements.txt 是 pip 的简单依赖格式，pyproject.toml 是更完整的项目配置文件'},
            {"label": 'D', "text": '只能选一个使用，不能并存'},
        ],
        "answer": 'C',
        "explanation": 'requirements.txt 是 pip 的依赖文件格式（简单）。pyproject.toml 是现代 Python 项目的元数据文件（功能更全，包含项目配置、依赖、工具设置等）。',
        "difficulty": 'medium',
        "tags": ['依赖管理'],
    },
]

# ============================================================
# Lesson 46
# ============================================================
EXERCISES_LESSON_46 = [
    {
        "type": "choice",
        "title": 'Python 中最流行的 HTTP 请求库是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'requests'},
            {"label": 'B', "text": 'urllib'},
            {"label": 'C', "text": 'axios'},
            {"label": 'D', "text": 'fetch'},
        ],
        "answer": 'A',
        "explanation": "requests 是 Python 最流行的第三方 HTTP 库，号称 'HTTP for Humans'。urllib 是标准库但 API 不够友好。",
        "difficulty": 'easy',
        "tags": ['HTTP', 'requests'],
    },
    {
        "type": "judge",
        "title": 'GET 请求用于获取数据，POST 请求用于提交数据',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。GET 从服务器获取数据（参数在 URL 中），POST 向服务器提交数据（数据在请求体中）。还有其他方法如 PUT（更新）、DELETE（删除）。',
        "difficulty": 'easy',
        "tags": ['HTTP', '方法'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：发送 GET 请求并解析 JSON',
        "description": '请求一个 API 获取用户列表并打印',
        "answer": "import requests\n\nresponse = requests.get('https://api.example.com/users')\nif response.status_code == 200:\n    users = response.json()\n    for user in users:\n        print(user['name'])\nelse:\n    print(f'请求失败: {response.status_code}')",
        "explanation": 'requests.get() 发送 GET 请求。response.status_code 检查 HTTP 状态码（200 表示成功）。response.json() 把响应体解析为 Python 对象。',
        "difficulty": 'medium',
        "tags": ['HTTP', 'requests'],
    },
    {
        "type": "fill_blank",
        "title": '发送 POST 请求并附带 JSON 数据，应使用 requests.post(url, ____=data)',
        "description": '填写参数名',
        "answer": 'json',
        "explanation": "requests.post(url, json={'key': 'value'}) 自动设置 Content-Type: application/json 并序列化数据。也可以用 data= 发送表单数据。",
        "difficulty": 'medium',
        "tags": ['HTTP', 'POST'],
    },
    {
        "type": "programming",
        "title": '获取天气信息',
        "description": '编写函数 get_weather(city)，调用免费天气 API（使用提供的 url），处理可能的网络异常和 HTTP 错误。用 try/except 处理 requests.RequestException。',
        "answer": 'import requests\n\ndef get_weather(city):\n    url = f"https://api.example.com/weather?city={city}"\n    try:\n        response = requests.get(url, timeout=5)\n        response.raise_for_status()\n        data = response.json()\n        return f"{city}: {data.get(\'weather\', \'未知\')}"\n    except requests.ConnectionError:\n        return "网络连接失败"\n    except requests.Timeout:\n        return "请求超时"\n    except requests.RequestException as e:\n        return f"请求出错: {e}"',
        "explanation": 'raise_for_status() 在 HTTP 4xx/5xx 时抛出异常。timeout 参数避免无限等待。RequestException 是 requests 异常的基类，捕获它可以处理所有网络相关错误。',
        "difficulty": 'medium',
        "tags": ['HTTP', '异常处理'],
    },
]

# ============================================================
# Lesson 47
# ============================================================
EXERCISES_LESSON_47 = [
    {
        "type": "choice",
        "title": 'sqlite3 数据库中，游标 (cursor) 的作用是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '存储数据库文件'},
            {"label": 'B', "text": '执行 SQL 语句并获取结果'},
            {"label": 'C', "text": '管理数据库连接'},
            {"label": 'D', "text": '加密数据库'},
        ],
        "answer": 'B',
        "explanation": 'cursor 是执行 SQL 语句和获取结果的中介。通过 conn.cursor() 创建，cursor.execute() 执行 SQL，cursor.fetchall() 获取结果。',
        "difficulty": 'easy',
        "tags": ['sqlite3', 'cursor'],
    },
    {
        "type": "judge",
        "title": '使用参数化查询（? 占位符）可以有效防止 SQL 注入攻击',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。参数化查询将数据和 SQL 语句分离，数据不会被当作 SQL 代码执行。永远不要用字符串拼接来构造 SQL 查询。',
        "difficulty": 'easy',
        "tags": ['sqlite3', 'SQL 注入'],
    },
    {
        "type": "fill_blank",
        "title": '执行 INSERT/UPDATE/DELETE 后，需要调用 conn.____() 来保存更改',
        "description": '填写方法名',
        "answer": 'commit',
        "explanation": 'commit() 提交事务保存更改。如果不调用，更改可能在连接关闭时丢失。读取数据（SELECT）不需要 commit。',
        "difficulty": 'easy',
        "tags": ['sqlite3', 'commit'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：创建表并插入数据',
        "description": '创建 books 表（id, title, author, year），插入一条记录',
        "answer": "import sqlite3\nconn = sqlite3.connect('library.db')\ncursor = conn.cursor()\ncursor.execute('''\n    CREATE TABLE IF NOT EXISTS books (\n        id INTEGER PRIMARY KEY AUTOINCREMENT,\n        title TEXT NOT NULL,\n        author TEXT NOT NULL,\n        year INTEGER\n    )\n''')\ncursor.execute(\n    'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',\n    ('Python编程入门', '张三', 2024)\n)\nconn.commit()\nconn.close()",
        "explanation": '先用 IF NOT EXISTS 安全建表。参数化查询用 ? 占位符，元组传参。AUTOINCREMENT 让 id 自动递增。最后 commit + close。',
        "difficulty": 'medium',
        "tags": ['sqlite3', '建表'],
    },
    {
        "type": "programming",
        "title": '实现一个简单的电话簿',
        "description": '创建 contacts 表（id, name, phone），实现 add_contact(name, phone) 和 search_contact(name) 函数。search 使用 LIKE 模糊匹配。',
        "answer": "import sqlite3\n\ndef init_db():\n    conn = sqlite3.connect('contacts.db')\n    c = conn.cursor()\n    c.execute('''CREATE TABLE IF NOT EXISTS contacts\n                 (id INTEGER PRIMARY KEY AUTOINCREMENT,\n                  name TEXT NOT NULL, phone TEXT NOT NULL)''')\n    conn.commit()\n    return conn\n\ndef add_contact(name, phone):\n    conn = sqlite3.connect('contacts.db')\n    c = conn.cursor()\n    c.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))\n    conn.commit()\n    conn.close()\n\ndef search_contact(name):\n    conn = sqlite3.connect('contacts.db')\n    c = conn.cursor()\n    c.execute('SELECT * FROM contacts WHERE name LIKE ?', (f'%{name}%',))\n    results = c.fetchall()\n    conn.close()\n    return results",
        "explanation": 'LIKE 配合 % 实现模糊匹配（% 匹配任意字符序列）。fetchall() 返回所有匹配的结果列表，每行是一个元组。参数化查询也适用于 LIKE。',
        "difficulty": 'medium',
        "tags": ['sqlite3', 'CRUD'],
    },
]

# ============================================================
# Lesson 48
# ============================================================
EXERCISES_LESSON_48 = [
    {
        "type": "choice",
        "title": 'argparse 模块的主要用途是？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '解析 JSON 文件'},
            {"label": 'B', "text": '解析命令行参数'},
            {"label": 'C', "text": '解析正则表达式'},
            {"label": 'D', "text": '解析 CSV 文件'},
        ],
        "answer": 'B',
        "explanation": 'argparse 是 Python 标准库中用于解析命令行参数的模块。它支持位置参数、可选参数、帮助信息自动生成等功能。',
        "difficulty": 'easy',
        "tags": ['argparse'],
    },
    {
        "type": "judge",
        "title": 'argparse 会自动生成 --help 帮助信息',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。创建 ArgumentParser 后，自动获得 -h/--help 选项。可以通过 description 参数设置程序的描述信息，这些会显示在帮助中。',
        "difficulty": 'easy',
        "tags": ['argparse', 'help'],
    },
    {
        "type": "fill_blank",
        "title": 'add_argument 中，____=True 表示该参数是可选的且不需要值，加上即激活',
        "description": '填写参数名',
        "answer": 'action',
        "explanation": "action='store_true' 创建布尔标志。例如 add_argument('--verbose', action='store_true')，运行 python script.py --verbose 时 args.verbose 为 True。",
        "difficulty": 'medium',
        "tags": ['argparse', 'action'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：创建命令行计算器',
        "description": '实现一个命令行工具，接收 --operation (add/sub/mul/div) 和两个数字参数',
        "answer": "import argparse\n\nparser = argparse.ArgumentParser(description='命令行计算器')\nparser.add_argument('a', type=float, help='第一个数字')\nparser.add_argument('b', type=float, help='第二个数字')\nparser.add_argument('--operation', '-o', default='add',\n                    choices=['add', 'sub', 'mul', 'div'],\n                    help='运算类型')\n\nargs = parser.parse_args()\nif args.operation == 'add':\n    result = args.a + args.b\nelif args.operation == 'sub':\n    result = args.a - args.b\nelif args.operation == 'mul':\n    result = args.a * args.b\nelif args.operation == 'div':\n    result = args.a / args.b if args.b != 0 else '无穷大'\nprint(f'结果: {result}')",
        "explanation": '位置参数（a, b）必须提供。--operation 是可选的，choices 限制可选值。type=float 自动把输入转成浮点数。用法：python calc.py 10 5 -o mul。',
        "difficulty": 'medium',
        "tags": ['argparse', '命令'],
    },
    {
        "type": "programming",
        "title": '实现文件字数统计工具',
        "description": '创建命令行工具，接收文件路径（必选）和 --lines/--words/--chars 标志（可选，指定统计类型，默认全部统计）。输出相应的计数。',
        "answer": "import argparse\n\nparser = argparse.ArgumentParser(description='文件字数统计')\nparser.add_argument('file', help='文件路径')\nparser.add_argument('-l', '--lines', action='store_true', help='统计行数')\nparser.add_argument('-w', '--words', action='store_true', help='统计单词数')\nparser.add_argument('-c', '--chars', action='store_true', help='统计字符数')\n\nargs = parser.parse_args()\nshow_all = not (args.lines or args.words or args.chars)\n\nwith open(args.file, 'r', encoding='utf-8') as f:\n    content = f.read()\n\nif show_all or args.lines:\n    print(f'行数: {content.count(chr(10)) + 1}')\nif show_all or args.words:\n    print(f'单词数: {len(content.split())}')\nif show_all or args.chars:\n    print(f'字符数: {len(content)}')",
        "explanation": "三个布尔标志通过 action='store_true' 实现。如果用户没指定任何标志，show_all 为 True 表示全部输出。content.split() 默认按空白字符分割。",
        "difficulty": 'medium',
        "tags": ['argparse', '文件'],
    },
]

# ============================================================
# Lesson 49
# ============================================================
EXERCISES_LESSON_49 = [
    {
        "type": "choice",
        "title": 'Python 中 threading 模块适合处理什么类型的任务？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": 'CPU 密集型计算'},
            {"label": 'B', "text": 'IO 密集型任务（网络请求、文件读写）'},
            {"label": 'C', "text": '任何需要加速的任务'},
            {"label": 'D', "text": 'GPU 运算'},
        ],
        "answer": 'B',
        "explanation": '由于 GIL（全局解释器锁），Python 多线程不适合 CPU 密集型任务（只能用一个核）。多线程适合 IO 密集型任务：网络请求、文件读写等，一个线程等待 IO 时另一个可以运行。',
        "difficulty": 'easy',
        "tags": ['threading', 'GIL'],
    },
    {
        "type": "judge",
        "title": 'asyncio 是 Python 的异步编程框架，适合处理大量并发 IO 操作',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": '正确。asyncio 使用事件循环（event loop）在单线程中切换任务，一个协程 await 等待 IO 时，事件循环可以执行其他协程。适合高并发网络应用。',
        "difficulty": 'medium',
        "tags": ['asyncio'],
    },
    {
        "type": "fill_blank",
        "title": '在 async 函数中，使用____关键字来等待一个异步操作完成',
        "description": '填写关键字',
        "answer": 'await',
        "explanation": 'await 只能在 async def 函数中使用。它暂停当前协程，等待右侧的 awaitable 对象（如另一个协程）完成，期间事件循环可以运行其他任务。',
        "difficulty": 'medium',
        "tags": ['asyncio', 'await'],
    },
    {
        "type": "code_completion",
        "title": '补全代码：用 threading 并发下载',
        "description": '使用多线程同时请求多个 URL 并打印响应状态码',
        "answer": "import threading\nimport requests\n\ndef fetch(url):\n    try:\n        resp = requests.get(url, timeout=5)\n        print(f'{url}: {resp.status_code}')\n    except Exception as e:\n        print(f'{url}: 错误 - {e}')\n\nurls = ['https://httpbin.org/get', 'https://httpbin.org/delay/1']\nthreads = []\nfor url in urls:\n    t = threading.Thread(target=fetch, args=(url,))\n    threads.append(t)\n    t.start()\n\nfor t in threads:\n    t.join()\nprint('全部完成！')",
        "explanation": 'Thread(target=func, args=(arg,)) 创建线程。start() 启动线程。join() 等待线程完成。所有线程并发执行，总耗时约等于最慢的那个请求，而不是所有请求之和。',
        "difficulty": 'medium',
        "tags": ['threading', '并发'],
    },
    {
        "type": "programming",
        "title": '用 asyncio 实现并发爬虫',
        "description": '使用 aiohttp 和 asyncio 同时请求 3 个 URL，收集所有响应状态码。提示：用 asyncio.gather() 同时运行多个协程。',
        "answer": "import asyncio\n\n# 模拟异步 HTTP 请求\nasync def fetch(url):\n    print(f'开始请求: {url}')\n    await asyncio.sleep(1)  # 模拟网络延迟\n    return f'{url} -> 200 OK'\n\nasync def main():\n    urls = ['http://site1.com', 'http://site2.com', 'http://site3.com']\n    tasks = [fetch(url) for url in urls]\n    results = await asyncio.gather(*tasks)\n    for r in results:\n        print(r)\n\nasyncio.run(main())",
        "explanation": 'async def 定义协程函数。asyncio.gather() 并发运行多个协程。asyncio.run() 是程序入口。如果 3 个请求各需 1 秒，并发执行总共约 1 秒（而非 3 秒）。',
        "difficulty": 'hard',
        "tags": ['asyncio', 'gather'],
    },
]

# ============================================================
# Lesson 50
# ============================================================
EXERCISES_LESSON_50 = [
    {
        "type": "choice",
        "title": 'Python 在以下哪个领域不是主流选择？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '人工智能 / 机器学习'},
            {"label": 'B', "text": '数据科学 / 数据分析'},
            {"label": 'C', "text": 'Web 后端开发'},
            {"label": 'D', "text": '移动 App 开发'},
        ],
        "answer": 'D',
        "explanation": 'Python 在 AI/机器学习、数据科学、Web 后端领域是主流。但移动 App 开发（iOS/Android）还是 Swift/Kotlin 的天下，Python 在这方面应用很少。',
        "difficulty": 'easy',
        "tags": ['进阶路线'],
    },
    {
        "type": "judge",
        "title": 'Python 社区拥有丰富的第三方库，是它成为最流行语言之一的重要原因',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'A',
        "explanation": "正确。PyPI 上有超过 50 万个包，覆盖几乎所有领域。'Batteries included'（自带电池）+ 丰富的生态 = Python 的最大优势。",
        "difficulty": 'easy',
        "tags": ['进阶路线'],
    },
    {
        "type": "fill_blank",
        "title": '想深入学习 Python Web 开发，最主流的两个框架是 Django 和 ____',
        "description": '填写框架名',
        "answer": 'Flask',
        "explanation": 'Django 是全栈框架（自带 ORM、模板、后台管理），适合大型项目。Flask 是微框架（轻量灵活），适合小型项目和 API。FastAPI 是新兴的异步框架，增长很快。',
        "difficulty": 'medium',
        "tags": ['Web开发', '框架'],
    },
    {
        "type": "choice",
        "title": '以下关于 Python 进阶路线的建议，哪个最合理？',
        "description": '选择正确答案',
        "options": [
            {"label": 'A', "text": '先读完所有 Python 官方文档，再做项目'},
            {"label": 'B', "text": '直接读 Django/Flask 源码'},
            {"label": 'C', "text": '基础语法 → 多做项目 → 学习框架/工具'},
            {"label": 'D', "text": '学会所有 Python 标准库再做项目'},
        ],
        "answer": 'C',
        "explanation": '基础语法 → 实战项目 → 框架/工具 = 最有效的学习路径。做项目是最好的学习方式。A 不推荐（先深入理论容易放弃），B 不实际（没有基础看不懂源码），D 没必要（工作需要时再学就行）。',
        "difficulty": 'medium',
        "tags": ['进阶路线'],
    },
    {
        "type": "judge",
        "title": '学完这门课 50 节课，你已经是 Python 专家了',
        "description": '判断以下说法是否正确',
        "options": [
            {"label": 'A', "text": '正确'},
            {"label": 'B', "text": '错误'},
        ],
        "answer": 'B',
        "explanation": '错误。50 节课是很好的起点，但编程是一门实践的艺术。持续做项目、看文档、阅读他人的代码、解决实际问题，才能不断成长。保持好奇心和学习习惯最重要。',
        "difficulty": 'easy',
        "tags": ['进阶路线'],
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
    21: EXERCISES_LESSON_21,
    22: EXERCISES_LESSON_22,
    23: EXERCISES_LESSON_23,
    24: EXERCISES_LESSON_24,
    25: EXERCISES_LESSON_25,
    26: EXERCISES_LESSON_26,
    27: EXERCISES_LESSON_27,
    28: EXERCISES_LESSON_28,
    29: EXERCISES_LESSON_29,
    30: EXERCISES_LESSON_30,
    31: EXERCISES_LESSON_31,
    32: EXERCISES_LESSON_32,
    33: EXERCISES_LESSON_33,
    34: EXERCISES_LESSON_34,
    35: EXERCISES_LESSON_35,
    36: EXERCISES_LESSON_36,
    37: EXERCISES_LESSON_37,
    38: EXERCISES_LESSON_38,
    39: EXERCISES_LESSON_39,
    40: EXERCISES_LESSON_40,
    41: EXERCISES_LESSON_41,
    42: EXERCISES_LESSON_42,
    43: EXERCISES_LESSON_43,
    44: EXERCISES_LESSON_44,
    45: EXERCISES_LESSON_45,
    46: EXERCISES_LESSON_46,
    47: EXERCISES_LESSON_47,
    48: EXERCISES_LESSON_48,
    49: EXERCISES_LESSON_49,
    50: EXERCISES_LESSON_50,
}
