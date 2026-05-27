from copy import deepcopy


def _case(expected_output: str, stdin: str = ""):
    return [{"stdin": stdin, "expected_output": expected_output}]


def _cases(*entries):
    return [
        {"stdin": stdin, "expected_output": expected_output}
        for stdin, expected_output in entries
    ]


def _code_patch(
    starter_code: str,
    reference_code: str,
    expected_output: str,
    stdin: str = "",
    description: str = None,
):
    patch = {
        "starter_code": starter_code,
        "reference_code": reference_code,
        "test_cases": _case(expected_output, stdin),
    }
    if description is not None:
        patch["description"] = description
    return patch


def _inject_seed(code: str) -> str:
    if "random.seed(1)" in code:
        return code
    return code.replace("import random\n", "import random\nrandom.seed(1)\n", 1)


EXERCISE_UPDATES = {
    "运行 Python 程序的命令": {
        "answer": '["python", "python3"]',
    },
    "sort() 和 sorted() 的区别": {
        "description": "sort() 会修改 ____ 列表，sorted() 返回一个 ____ 列表。（依次填写：原,新）",
        "answer": "原,新",
    },
    "单元素元组的写法": {
        "description": "创建一个只包含数字 42 的元组，需要在 42 后写哪个符号？",
        "answer": ",",
    },
    "修复 print 语法错误": _code_patch(
        'print（"Hello, World!"）',
        'print("Hello, World!")',
        "Hello, World!\n",
    ),
    "修复 f-string 语法": _code_patch(
        'name = "小明"\nage = 18\nprint(f"我叫{name}，今年" + age + "岁")',
        'name = "小明"\nage = 18\nprint(f"我叫{name}，今年{age}岁")',
        "我叫小明，今年18岁\n",
    ),
    "修复 if 判断条件": _code_patch(
        'age = 18\nif age = 18:\n    print("成年")',
        'age = 18\nif age == 18:\n    print("成年")',
        "成年\n",
    ),
    "修复死循环": _code_patch(
        'count = 1\nwhile count <= 5:\n    print(count)',
        'count = 1\nwhile count <= 5:\n    print(count)\n    count += 1',
        "1\n2\n3\n4\n5\n",
    ),
    "修复嵌套循环中的 break": _code_patch(
        "for i in range(5):\n"
        "    for j in range(5):\n"
        "        if i * j > 10:\n"
        "            break\n"
        "print(i, j)",
        "for i in range(5):\n"
        "    for j in range(5):\n"
        "        if i * j > 10:\n"
        "            break\n"
        "    if i * j > 10:\n"
        "        break\n"
        "print(i, j)",
        "3 4\n",
    ),
    "修复列表访问越界": _code_patch(
        "nums = [10, 20, 30]\nprint(nums[3])",
        "nums = [10, 20, 30]\nprint(nums[-1])",
        "30\n",
    ),
    "修复元组修改错误": _code_patch(
        'colors = ("红", "绿", "蓝")\ncolors[0] = "黄"\nprint(colors)',
        'colors = ("红", "绿", "蓝")\ncolors = ("黄",) + colors[1:]\nprint(colors)',
        "('黄', '绿', '蓝')\n",
    ),
    "修复字典遍历": _code_patch(
        'student = {"name": "小明", "age": 18}\nfor k, v in student:\n    print(k, v)',
        'student = {"name": "小明", "age": 18}\nfor k, v in student.items():\n    print(k, v)',
        "name 小明\nage 18\n",
    ),
    "修复函数缩进错误": _code_patch(
        'def hello():\nprint("Hello")\nhello()',
        'def hello():\n    print("Hello")\nhello()',
        "Hello\n",
    ),
    "修复 UnboundLocalError": _code_patch(
        "count = 0\ndef increment():\n    count += 1\nincrement()\nprint(count)",
        "count = 0\ndef increment():\n    global count\n    count += 1\nincrement()\nprint(count)",
        "1\n",
    ),
    "修复 import 错误": _code_patch(
        "import random\nrandom.seed(1)\nprint(randint(1, 10))",
        "import random\nrandom.seed(1)\nprint(random.randint(1, 10))",
        "3\n",
    ),
    "补全第一个 Python 程序": _code_patch(
        "# 请写一行 print 输出指定文本",
        'print("我学会了！")',
        "我学会了！\n",
    ),
    "交换两个变量的值": _code_patch(
        "a = 1\nb = 2\n# 请补全交换语句\nprint(a, b)",
        "a = 1\nb = 2\na, b = b, a\nprint(a, b)",
        "2 1\n",
    ),
    "字符串去空格": _code_patch(
        'text = "  hello  "\nresult = None  # 请补全去空格表达式\nprint(result)',
        'text = "  hello  "\nresult = text.strip()\nprint(result)',
        "hello\n",
    ),
    "判断奇偶数": _code_patch(
        "num = 8\n# 请补全 result 的比较表达式\nresult = num % 2 == None\nprint(result)",
        "num = 8\nresult = num % 2 == 0\nprint(result)",
        "True\n",
    ),
    "三目表达式": _code_patch(
        'age = 18\n# 请补全 status 的条件表达式\nstatus = None\nprint(status)',
        'age = 18\nstatus = "成年" if age >= 18 else "未成年"\nprint(status)',
        "成年\n",
    ),
    "补全闰年判断条件": _code_patch(
        "year = 2024\n# 请补全闰年判断表达式\nis_leap = None\nprint(is_leap)",
        "year = 2024\nis_leap = year % 4 == 0 and year % 100 != 0\nprint(is_leap)",
        "True\n",
    ),
    "用 while 求 1 到 100 的和": _code_patch(
        "total = 0\ni = 1\n# 请补全 while 循环求和\nprint(total)",
        "total = 0\ni = 1\nwhile i <= 100:\n    total += i\n    i += 1\nprint(total)",
        "5050\n",
    ),
    "九九乘法表内层循环": _code_patch(
        "for i in range(1, 4):\n"
        "    # 请补全内层循环\n"
        "    print()",
        "for i in range(1, 4):\n"
        "    for j in range(1, i + 1):\n"
        '        print(f"{j}x{i}={i*j}", end=" ")\n'
        "    print()",
        "1x1=1 \n1x2=2 2x2=4 \n1x3=3 2x3=6 3x3=9 \n",
        description="输出九九乘法表的前三行",
    ),
    "列表判空": _code_patch(
        'items = []\nif False:  # 请补全空列表判断条件\n    print("为空")\nelse:\n    print("不为空")',
        'items = []\nif not items:\n    print("为空")\nelse:\n    print("不为空")',
        "为空\n",
        description="补全代码，判断列表是否为空并输出对应结果",
    ),
    "逆序列表": _code_patch(
        "nums = [1, 2, 3]\nreversed_list = []  # 请补全切片\nprint(reversed_list)",
        "nums = [1, 2, 3]\nreversed_list = nums[::-1]\nprint(reversed_list)",
        "[3, 2, 1]\n",
    ),
    "字典合并": _code_patch(
        'd1 = {"a": 1}\nd2 = {"b": 2}\nmerged = {}  # 请补全合并表达式\nprint(merged)',
        'd1 = {"a": 1}\nd2 = {"b": 2}\nmerged = d1 | d2\nprint(merged)',
        "{'a': 1, 'b': 2}\n",
    ),
    "统计单词频率": _code_patch(
        'text = "a b a c b a"\nfreq = {}\nfor w in text.split():\n    freq[w] = 0  # 请补全 get 调用\nprint(freq)',
        'text = "a b a c b a"\nfreq = {}\nfor w in text.split():\n    freq[w] = freq.get(w, 0) + 1\nprint(freq)',
        "{'a': 3, 'b': 2, 'c': 1}\n",
    ),
    "补全 return 语句": _code_patch(
        "def add(a, b):\n    # 请补全返回语句\n    pass\nprint(add(3, 5))",
        "def add(a, b):\n    return a + b\nprint(add(3, 5))",
        "8\n",
    ),
    "*args 收集多余参数": _code_patch(
        "def sum_all(nums):  # 请补全可变参数写法\n    return sum(nums)\nprint(sum_all(1, 2, 3))",
        "def sum_all(*nums):\n    return sum(nums)\nprint(sum_all(1, 2, 3))",
        "6\n",
    ),
    "获取当前日期时间": _code_patch(
        "from datetime # 请补全导入关键字 datetime\nnow = datetime.now()\nprint(isinstance(now, datetime))",
        "from datetime import datetime\nnow = datetime.now()\nprint(isinstance(now, datetime))",
        "True\n",
        description="补全代码，正确导入 datetime 并判断 now 是否是 datetime 类型",
    ),
    "读取文件所有行": _code_patch(
        'from io import StringIO\nf = StringIO("a\\nb\\n")\nlines = []  # 请补全读取方法\nprint(lines)',
        'from io import StringIO\nf = StringIO("a\\nb\\n")\nlines = f.readlines()\nprint(lines)',
        "['a\\n', 'b\\n']\n",
        description="补全代码，从模拟文本文件中读取所有行到列表",
    ),
}


PROGRAMMING_CASES = {
    "自我介绍程序": _case("我叫小明，今年18岁\n"),
    "名字处理程序": _case("处理后的名字是：张三\n"),
    "计算圆的面积": _case("圆的面积是：78.5\n"),
    "成绩等级判断": _case("良好\n"),
    "年龄范围判断": _case("在范围内\n"),
    "倒计时程序": _case("10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n发射！\n"),
    "求 1 到 100 之间的偶数和": _case("1-100偶数和：2550\n"),
    "找质数": _case("是质数\n"),
    "创建购物清单": _case("1. 牛奶\n2. 鸡蛋\n"),
    "成绩分析器": _case("及格人数：6\n及格均分：82.7\n最高分：95，最低分：59\n"),
    "元组解包练习": _case("坐标：(120, 350)\n交换后：(350, 120)\n"),
    "通讯录小程序": _cases(
        ("小明\n", "请输入联系人姓名：小明 的电话：13800138000\n"),
        ("小王\n", "请输入联系人姓名：未找到该联系人\n"),
    ),
    "学生成绩管理系统": _case(
        "小明: 88分\n小红: 95分\n小刚: 72分\n小李: 85分\n平均分: 85.0\n最高分: 小红 (95分)\n"
    ),
    "自定义计算器函数": _case("BMI: 22.9\n"),
    "温度转换器": _case("0°C = 32.0°F\n32°F = 0.0°C\n"),
    "sort 配合 lambda 排序": _case("小刚: 95分\n小明: 90分\n小红: 85分\n"),
    "随机点名器": _case("今天被点到的是：李四\n"),
    "综合：个人日记本（简化版）": _case(
        "写日记（输入 save 保存, show 查看, quit 退出）\n> > 已保存 1 条日记\n> 今天学习了列表\n\n> ",
        "今天学习了列表\nsave\nshow\nquit\n",
    ),
}


PROJECT_TASK_UPDATES = {
    (1, 1): {
        "test_cases": _case(
            "请输入你的姓名：请输入你的年龄：请输入你的爱好：信息已收集！\n",
            "小明\n18\nPython\n",
        ),
    },
    (1, 2): {
        "test_cases": _case("==================\n  个人名片\n==================\n"),
    },
    (1, 3): {
        "test_cases": _case(
            "请输入你的姓名：请输入你的年龄：请输入你的爱好：==============================\n"
            "  个人名片\n"
            "==============================\n"
            "姓名：小明\n"
            "年龄：18 岁\n"
            "爱好：Python\n"
            "==============================\n",
            "小明\n18\nPython\n",
        ),
    },
    (2, 1): {
        "starter_code": (
            "import random\n"
            "random.seed(1)\n\n"
            "# 任务 1：生成随机数字\n"
            "# TODO: 生成 1-100 的随机数并打印调试输出\n"
        ),
        "test_cases": _case("(调试) 秘密数字是：18\n"),
    },
    (2, 2): {
        "test_cases": _case("你猜是多少：猜对了！\n", "18\n"),
    },
    (2, 3): {
        "test_cases": _case(
            "我想了一个 1-100 之间的数字，来猜猜看！\n"
            "你猜是多少：小了，再大一点\n"
            "你猜是多少：猜对了！你一共猜了 2 次\n",
            "1\n18\n",
        ),
    },
    (2, 4): {
        "test_cases": _case(
            "===== 猜数字游戏 =====\n"
            "1. 简单 (1-50, 10次机会)\n"
            "2. 中等 (1-100, 7次机会)\n"
            "3. 困难 (1-200, 5次机会)\n"
            "请选择难度 (1/2/3): \n"
            "我想了一个 1-50 的数字，你有 10 次机会！\n"
            "第1次猜：小了\n"
            "第2次猜：\n"
            "🎉 猜对了！你用了 2 次\n",
            "1\n1\n9\n",
        ),
    },
    (3, 1): {
        "test_cases": _case(
            "===== 待办事项管理器 =====\n\n"
            "1. 查看事项\n"
            "2. 添加事项\n"
            "3. 标记完成\n"
            "4. 删除事项\n"
            "5. 退出\n"
            "请选择: 再见！\n",
            "5\n",
        ),
    },
    (3, 2): {
        "test_cases": _case(
            "\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: 输入事项：✅ 已添加：读书\n\n"
            "1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: [ ] 1. 读书\n\n"
            "1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: 再见！\n",
            "2\n读书\n1\n5\n",
        ),
    },
    (3, 3): {
        "test_cases": _case(
            "\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: [ ] 1. 测试事项\n"
            "输入要完成的事项编号：✅ 已标记完成：测试事项\n\n"
            "1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: [✓] 1. 测试事项\n"
            "输入要删除的事项编号：🗑 已删除：测试事项\n\n"
            "1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n"
            "请选择: 再见！\n",
            "3\n1\n4\n1\n5\n",
        ),
    },
}


def apply_exercise_updates(all_exercises):
    updated = deepcopy(all_exercises)

    for lesson_items in updated.values():
        for item in lesson_items:
            patch = EXERCISE_UPDATES.get(item["title"])
            if patch:
                item.update(deepcopy(patch))

            if item["title"] in PROGRAMMING_CASES:
                reference_code = item["answer"]
                starter_code = item.get("starter_code")
                if item["title"] == "随机点名器":
                    reference_code = _inject_seed(reference_code)
                    starter_code = (
                        "import random\n"
                        "random.seed(1)\n\n"
                        'names = ["张三", "李四", "王五", "赵六"]\n'
                        "# 请补全随机点名并打印结果\n"
                    )

                item.update(
                    {
                        "starter_code": starter_code,
                        "reference_code": reference_code,
                        "test_cases": deepcopy(PROGRAMMING_CASES[item["title"]]),
                    }
                )

    return updated


def apply_project_task_updates(all_projects):
    updated = deepcopy(all_projects)

    for _project_id, (project, tasks) in updated.items():
        for task in tasks:
            patch = PROJECT_TASK_UPDATES.get((project["order_index"], task["order_index"]))
            if not patch:
                continue

            task.update(deepcopy(patch))

            if project["order_index"] == 2:
                task["starter_code"] = _inject_seed(task["starter_code"])
                task["answer_code"] = _inject_seed(task["answer_code"])

    return updated
