"""
种子数据 - 8 个项目实战
从初级到进阶，覆盖所学知识点
"""

# ============================================================
# Project 1: 个人信息卡片 (初级)
# ============================================================
PROJECT_1 = {
    "title": "个人信息卡片",
    "description": "创建一个命令行程序，输入个人信息并生成一张漂亮的文字版名片。这是你的第一个 Python 实战小项目！",
    "difficulty": "beginner",
    "category": "python_basic",
    "estimated_minutes": 30,
    "final_result": "最终你的程序会像这样运行：\n\n请输入你的姓名：小明\n请输入你的年龄：18\n请输入你的爱好：打篮球\n\n==================\n  个人名片\n==================\n姓名：小明\n年龄：18 岁\n爱好：打篮球\n==================\n",
    "knowledge_points": ["变量", "字符串", "input() 输入", "print() 输出", "字符串拼接"],
    "order_index": 1,
}

PROJECT_1_TASKS = [
    {
        "title": "任务 1：获取用户信息",
        "description": "使用 input() 函数让用户输入姓名、年龄和爱好，并分别存到三个变量中。运行程序，确保能正确接收用户输入。",
        "starter_code": "# 任务 1：获取用户信息\n# 用 input() 获取输入，存到变量里\n\nname = input(\"请输入你的姓名：\")\n\n# TODO: 继续获取年龄和爱好\n",
        "hint": "和 name 一样的方式，用 input() 获取年龄和爱好。年龄存到 age 变量，爱好存到 hobby 变量。",
        "answer_code": 'name = input("请输入你的姓名：")\nage = input("请输入你的年龄：")\nhobby = input("请输入你的爱好：")\n\nprint("信息已收集！")',
        "test_cases": None,
        "order_index": 1,
    },
    {
        "title": "任务 2：打印名片框",
        "description": "用 print() 输出一个简单的名片框。先不要输出个人信息，只打印出分隔线和标题。",
        "starter_code": '# 任务 2：打印名片框\n# 在下方写代码\n\nprint("==================")\n\n# TODO: 打印标题 "个人名片"\n# TODO: 再打印一行分隔线\n',
        "hint": "使用 print() 分别输出每一行。先输出分隔线，再输出标题，最后再输出分隔线。",
        "answer_code": 'print("==================")\nprint("  个人名片")\nprint("==================")',
        "test_cases": None,
        "order_index": 2,
    },
    {
        "title": "任务 3：拼接完整名片",
        "description": "把任务 1 和任务 2 的代码合并，用之前获取的用户信息填充名片内容，形成完整的个人信息卡片。使用 f-string 将个人信息展示出来。",
        "starter_code": "# 任务 3：拼接完整名片\n# 复制任务 1 的输入代码\n\nname = input(\"请输入你的姓名：\")\nage = input(\"请输入你的年龄：\")\nhobby = input(\"请输入你的爱好：\")\n\n# TODO: 打印完整名片，包含分隔线、标题和个人信息\n",
        "hint": "先打印分隔线和标题，再用 f-string 分别打印姓名、年龄和爱好。f\"姓名：{name}\" 可以直接拼接变量。",
        "answer_code": 'name = input("请输入你的姓名：")\nage = input("请输入你的年龄：")\nhobby = input("请输入你的爱好：")\n\nprint("=" * 30)\nprint("  个人名片")\nprint("=" * 30)\nprint(f"姓名：{name}")\nprint(f"年龄：{age} 岁")\nprint(f"爱好：{hobby}")\nprint("=" * 30)',
        "test_cases": None,
        "order_index": 3,
    },
]

# ============================================================
# Project 2: 猜数字游戏 (中级)
# ============================================================
PROJECT_2 = {
    "title": "猜数字游戏",
    "description": "开发一个经典的命令行猜数字游戏。程序随机生成一个 1~100 之间的数字，玩家来猜。每次猜完给出「大了」或「小了」的提示，直到猜对为止，最后显示猜了几次。",
    "difficulty": "beginner",
    "category": "python_basic",
    "estimated_minutes": 30,
    "final_result": """运行效果：
我想了一个 1-100 之间的数字，来猜猜看！
你猜是多少：50
大了，再小一点
你猜是多少：25
小了，再大一点
你猜是多少：37
大了，再小一点
你猜是多少：31
猜对了！你一共猜了 4 次""",
    "knowledge_points": ["random", "while 循环", "if/elif/else", "input()", "类型转换 int()", "计数器"],
    "order_index": 2,
}

PROJECT_2_TASKS = [
    {
        "title": "任务 1：生成随机数字",
        "description": "导入 random 模块，生成一个 1~100 的秘密数字，然后打印出来让我们先看看（调试用，后面会删掉）。",
        "starter_code": "# 任务 1：生成随机数字\n# TODO: 导入 random 模块\n# TODO: 生成 1-100 的随机数\n\n",
        "hint": "import random 导入模块，用 random.randint(1, 100) 生成 1~100 的随机整数。",
        "answer_code": "import random\n\nsecret = random.randint(1, 100)\nprint(f\"(调试) 秘密数字是：{secret}\")",
        "test_cases": None,
        "order_index": 1,
    },
    {
        "title": "任务 2：单次猜 + 判断",
        "description": "用 input() 让用户输入一个数字（注意转成 int 类型），然后判断用户猜的数字和秘密数字的关系，输出「大了」「小了」或「猜对了」。",
        "starter_code": "import random\nsecret = random.randint(1, 100)\n\n# 任务 2：获取用户猜测并判断\n# TODO: 用 input 获取用户输入，转成 int\n# TODO: 判断大小关系，给出提示\n",
        "hint": "用 int(input('...')) 获取数字输入。然后用 if/elif/else 比较 guess 和 secret 的大小。",
        "answer_code": "import random\nsecret = random.randint(1, 100)\n\nguess = int(input(\"你猜是多少：\"))\n\nif guess > secret:\n    print(\"大了，再小一点\")\nelif guess < secret:\n    print(\"小了，再大一点\")\nelse:\n    print(\"猜对了！\")",
        "test_cases": None,
        "order_index": 2,
    },
    {
        "title": "任务 3：循环直到猜对",
        "description": "用 while 循环包裹任务 2 的代码，让玩家可以一直猜直到猜对。增加一个 attempts 变量记录猜了几次，猜对后显示次数。",
        "starter_code": "import random\nsecret = random.randint(1, 100)\nattempts = 0\n\nprint(\"我想了一个 1-100 之间的数字，来猜猜看！\")\n\n# TODO: 用 while 循环让玩家反复猜\n# TODO: 每次猜完 attempts += 1\n# TODO: 猜对了显示次数并退出\n",
        "hint": "用 while True 无限循环，猜对了用 break 跳出。每次输入后 attempts += 1 计数。比较 guess 和 secret。",
        "answer_code": "import random\n\nsecret = random.randint(1, 100)\nattempts = 0\n\nprint(\"我想了一个 1-100 之间的数字，来猜猜看！\")\n\nwhile True:\n    guess = int(input(\"你猜是多少：\"))\n    attempts += 1\n    \n    if guess > secret:\n        print(\"大了，再小一点\")\n    elif guess < secret:\n        print(\"小了，再大一点\")\n    else:\n        print(f\"猜对了！你一共猜了 {attempts} 次\")\n        break",
        "test_cases": None,
        "order_index": 3,
    },
    {
        "title": "任务 4：增加难度选择",
        "description": "在游戏开始时让玩家选择难度：简单(1-50)，中等(1-100)，困难(1-200)。根据选择调整随机数的范围。还要增加次数限制：简单 10 次，中等 7 次，困难 5 次。超过次数显示 Game Over。",
        "starter_code": "import random\n\nprint(\"===== 猜数字游戏 =====\")\nprint(\"1. 简单 (1-50, 10次机会)\")\nprint(\"2. 中等 (1-100, 7次机会)\")\nprint(\"3. 困难 (1-200, 5次机会)\")\n\n# TODO: 获取难度选择，设置 max_num 和 max_attempts\n# TODO: 生成对应范围的随机数\n# TODO: while 循环 + 计数 + 次数限制\n",
        "hint": "用 if/elif 根据选择设置 max_num 和 max_attempts。while 条件改为 attempts < max_attempts。循环结束后判断是否猜对了。",
        "answer_code": "import random\n\nprint(\"===== 猜数字游戏 =====\")\nprint(\"1. 简单 (1-50, 10次机会)\")\nprint(\"2. 中等 (1-100, 7次机会)\")\nprint(\"3. 困难 (1-200, 5次机会)\")\n\nchoice = input(\"请选择难度 (1/2/3): \")\n\nif choice == \"1\":\n    max_num, max_attempts = 50, 10\nelif choice == \"2\":\n    max_num, max_attempts = 100, 7\nelse:\n    max_num, max_attempts = 200, 5\n\nsecret = random.randint(1, max_num)\nattempts = 0\n\nprint(f\"\\n我想了一个 1-{max_num} 的数字，你有 {max_attempts} 次机会！\")\n\nwhile attempts < max_attempts:\n    guess = int(input(f\"第{attempts+1}次猜：\"))\n    attempts += 1\n    \n    if guess > secret:\n        print(\"大了\")\n    elif guess < secret:\n        print(\"小了\")\n    else:\n        print(f\"\\n🎉 猜对了！你用了 {attempts} 次\")\n        break\nelse:\n    print(f\"\\n😞 机会用完了！答案是 {secret}\")",
        "test_cases": None,
        "order_index": 4,
    },
]

# ============================================================
# Project 3: 待办事项管理器 (进阶)
# ============================================================
PROJECT_3 = {
    "title": "待办事项管理器",
    "description": "创建一个命令行 Todo 应用，支持添加、查看、完成、删除待办事项。数据存储在列表中，每个事项是一个字典。这是你学完 20 节课后第一个独立完成的应用！",
    "difficulty": "intermediate",
    "category": "python_basic",
    "estimated_minutes": 45,
    "final_result": """运行效果：
===== 待办事项管理器 =====
1. 查看所有事项
2. 添加事项
3. 标记完成
4. 删除事项
5. 退出
请选择: 2
输入事项：买水果
✅ 已添加：买水果

请选择: 1
[ ] 1. 买水果
[✓] 2. 写作业（已完成）

请选择: 3
输入要完成的事项编号：1
✅ 已标记完成：买水果""",
    "knowledge_points": ["列表", "字典", "while 循环", "if/elif/else", "函数", "f-string"],
    "order_index": 3,
}

PROJECT_3_TASKS = [
    {
        "title": "任务 1：创建数据结构和主菜单",
        "description": "创建一个 todos 列表存储待办事项（每个事项是 {'title': ..., 'done': False} 字典）。实现主菜单循环：显示选项，input() 获取用户选择，选择退出时 break。",
        "starter_code": "# 任务 1：创建数据结构和主菜单\n\ntodos = []  # 待办列表，每个元素是 {'title': '...', 'done': False}\n\nprint(\"===== 待办事项管理器 =====\")\n\n# TODO: while True 循环\n# TODO: 打印菜单选项\n# TODO: 获取用户选择\n# TODO: 如果选 5 就 break\n",
        "hint": "用 while True 无限循环 + print 显示菜单。input 获取选择。如果 choice == '5' 就 break。先不管其他选项。",
        "answer_code": 'todos = []\n\nprint("===== 待办事项管理器 =====")\n\nwhile True:\n    print("\\n1. 查看事项")\n    print("2. 添加事项")\n    print("3. 标记完成")\n    print("4. 删除事项")\n    print("5. 退出")\n    \n    choice = input("请选择: ")\n    \n    if choice == "5":\n        print("再见！")\n        break\n    else:\n        print("功能开发中...")',
        "test_cases": None,
        "order_index": 1,
    },
    {
        "title": "任务 2：实现添加和查看功能",
        "description": "实现选项 1（查看）和 2（添加）。查看时遍历所有事项，完成的显示 [✓]，未完成的显示 [ ]。添加时用 input 获取事项内容，append 到 todos 列表。",
        "starter_code": 'todos = []\n\nwhile True:\n    print("\\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        # TODO: 遍历 todos，显示每项\n        pass\n    elif choice == "2":\n        # TODO: input 获取事项，append 到 todos\n        pass\n    elif choice == "5":\n        break\n    else:\n        print("无效选项")',
        "hint": "查看时：if not todos: print('暂无事项')。遍历 for i, item in enumerate(todos): 编号用 i+1，完成状态用 '✓' if item['done'] else ' '。添加时：title = input('输入事项：'); todos.append({'title': title, 'done': False})。",
        "answer_code": 'todos = []\n\nwhile True:\n    print("\\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        if not todos:\n            print("暂无待办事项")\n        else:\n            for i, item in enumerate(todos):\n                mark = "✓" if item["done"] else " "\n                print(f"[{mark}] {i+1}. {item[\'title\']}")\n    elif choice == "2":\n        title = input("输入事项：")\n        todos.append({"title": title, "done": False})\n        print(f"✅ 已添加：{title}")\n    elif choice == "5":\n        print("再见！")\n        break\n    else:\n        print("无效选项")',
        "test_cases": None,
        "order_index": 2,
    },
    {
        "title": "任务 3：实现完成和删除功能",
        "description": "实现选项 3（标记完成）和 4（删除）。用户输入编号，把对应事项的 done 设为 True（完成）或从列表删除。注意校验编号是否有效。",
        "starter_code": 'todos = [{"title": "测试事项", "done": False}]\n\nwhile True:\n    print("\\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        for i, item in enumerate(todos):\n            mark = "✓" if item["done"] else " "\n            print(f"[{mark}] {i+1}. {item[\'title\']}")\n    elif choice == "2":\n        title = input("输入事项：")\n        todos.append({"title": title, "done": False})\n        print(f"✅ 已添加：{title}")\n    elif choice == "3":\n        # TODO: 输入编号，标记完成\n        pass\n    elif choice == "4":\n        # TODO: 输入编号，删除事项\n        pass\n    elif choice == "5":\n        break',
        "hint": "完成：先查看，再让用户输入编号 n。if 1 <= n <= len(todos): todos[n-1]['done'] = True。删除：同样获取编号，然后 del todos[n-1] 或 todos.pop(n-1)。都要检查编号合法。",
        "answer_code": 'todos = [{"title": "测试事项", "done": False}]\n\nwhile True:\n    print("\\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        if not todos:\n            print("暂无待办事项")\n        else:\n            for i, item in enumerate(todos):\n                mark = "✓" if item["done"] else " "\n                print(f"[{mark}] {i+1}. {item[\'title\']}")\n    elif choice == "2":\n        title = input("输入事项：")\n        todos.append({"title": title, "done": False})\n        print(f"✅ 已添加：{title}")\n    elif choice == "3":\n        if not todos:\n            print("暂无事项")\n            continue\n        for i, item in enumerate(todos):\n            mark = "✓" if item["done"] else " "\n            print(f"[{mark}] {i+1}. {item[\'title\']}")\n        n = int(input("输入要完成的事项编号："))\n        if 1 <= n <= len(todos):\n            todos[n-1]["done"] = True\n            print(f"✅ 已标记完成：{todos[n-1][\'title\']}")\n        else:\n            print("编号无效")\n    elif choice == "4":\n        if not todos:\n            print("暂无事项")\n            continue\n        for i, item in enumerate(todos):\n            mark = "✓" if item["done"] else " "\n            print(f"[{mark}] {i+1}. {item[\'title\']}")\n        n = int(input("输入要删除的事项编号："))\n        if 1 <= n <= len(todos):\n            removed = todos.pop(n-1)\n            print(f"🗑 已删除：{removed[\'title\']}")\n        else:\n            print("编号无效")\n    elif choice == "5":\n        print("再见！")\n        break\n    else:\n        print("无效选项")',
        "test_cases": None,
        "order_index": 3,
    },
]
# ============================================================
# Project 4: 学生成绩管理系统
# ============================================================
PROJECT_4 = {
    'title': '学生成绩管理系统',
    'description': '开发一个命令行成绩管理程序，用字典存储学生信息，支持添加学生、录入成绩、查看排名和保存到文件。串联文件读写、字典操作、排序和异常处理。',
    'difficulty': 'intermediate',
    'category': 'data_processing',
    'estimated_minutes': 45,
    'final_result': '运行效果：\n===== 学生成绩管理系统 =====\n1. 添加学生\n2. 录入成绩\n3. 查看排名\n4. 保存到文件\n5. 退出\n请选择: 1\n学生姓名: 小明 -> 已添加小明\n\n请选择: 2\n学生姓名: 小明\n语文: 90 数学: 85 英语: 92 -> 录入成功\n\n请选择: 3\n🥇 小明: 总分267, 平均89.0\n请选择: 4\n成绩已保存到 scores.csv',
    'knowledge_points': ['字典', '列表', '文件读写(CSV)', '排序', '异常处理', 'while循环'],
    'order_index': 4,
}

PROJECT_4_TASKS = [
    {
        'title': '任务 1：创建主菜单和学生存储结构',
        'description': "创建一个 students 字典（键为姓名，值为成绩字典{'语文':0, '数学':0, '英语':0}）。实现主菜单循环：显示 5 个选项，获取用户输入，选择 5 时退出。其他选项先显示 '功能开发中'。",
        'starter_code': '# 任务 1：创建数据结构和主菜单\nstudents = {}  # {name: {"语文": score, "数学": score, "英语": score}}\n\nprint("===== 学生成绩管理系统 =====")\n\n# TODO: while True 循环\n# TODO: 打印菜单 1-5\n# TODO: 获取用户选择\n# TODO: 选 5 就 break\n',
        'hint': "students 字典中每个学生的值是另一个字典。菜单用 print 输出。用 while True + input() 获取选择。choice == '5' 时 break。其他先 pass。",
        'answer_code': 'students = {}\n\nprint("===== 学生成绩管理系统 =====")\n\nwhile True:\n    print("\\n1. 添加学生")\n    print("2. 录入成绩")\n    print("3. 查看排名")\n    print("4. 保存到文件")\n    print("5. 退出")\n    \n    choice = input("请选择: ")\n    \n    if choice == "5":\n        print("再见！")\n        break\n    else:\n        print("功能开发中...")',
        'test_cases': None,
        'order_index': 1,
    },
    {
        'title': '任务 2：实现添加学生和录入成绩',
        'description': '实现选项 1 和 2。添加学生：输入姓名，如果已存在提示，否则创建成绩为 0 的字典。录入成绩：输入姓名，如果存在则分别输入三科成绩（int 类型），用 try/except 处理非数字输入。',
        'starter_code': 'students = {}\n\nwhile True:\n    print("\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        name = input("学生姓名: ")\n        # TODO: 检查是否已存在\n        # TODO: 添加到 students 字典\n        pass\n    elif choice == "2":\n        name = input("学生姓名: ")\n        # TODO: 检查学生是否存在\n        # TODO: 用 try/except 录入三科成绩\n        pass\n    elif choice == "5":\n        break\n    else:\n        print("功能开发中...")',
        'hint': "选 1：if name in students: 提示已存在，else: students[name] = {'语文':0, '数学':0, '英语':0}。选 2：检查 name in students 后，用 int(input(...)) 分别录入语文、数学、英语，放在 try 中。",
        'answer_code': 'students = {}\n\nwhile True:\n    print("\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "1":\n        name = input("学生姓名: ")\n        if name in students:\n            print(f"{name} 已存在")\n        else:\n            students[name] = {"语文": 0, "数学": 0, "英语": 0}\n            print(f"已添加 {name}")\n    elif choice == "2":\n        name = input("学生姓名: ")\n        if name not in students:\n            print("学生不存在，请先添加")\n        else:\n            try:\n                chinese = int(input("语文: "))\n                math = int(input("数学: "))\n                english = int(input("英语: "))\n                students[name] = {"语文": chinese, "数学": math, "英语": english}\n                print("录入成功")\n            except ValueError:\n                print("请输入有效数字")\n    elif choice == "5":\n        print("再见！")\n        break\n    else:\n        print("功能开发中...")',
        'test_cases': None,
        'order_index': 2,
    },
    {
        'title': '任务 3：实现查看排名',
        'description': '实现选项 3。计算每个学生的总分（三科之和），按总分降序排列并显示排名。第一名用 🥇，第二名用 🥈，第三名用 🥉。',
        'starter_code': 'students = {\n    "小明": {"语文": 90, "数学": 85, "英语": 92},\n    "小红": {"语文": 88, "数学": 95, "英语": 90},\n}\n\n# 任务 3：计算总分并排名\n# TODO: 遍历 students，计算每人总分\n# TODO: 按总分降序排列\n# TODO: 显示排名（前三用奖牌 emoji）\n\nwhile True:\n    print("\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "3":\n        # TODO: 排名逻辑\n        pass\n    elif choice == "5":\n        break',
        'hint': '先构建列表：[ (总分, name) for name, scores in students.items() sum(scores.values()) ]。sorted(data, reverse=True)。遍历时用 enumerate 获取名次（从 1 开始）。前三用 if rank == 1/2/3 判断。',
        'answer_code': 'students = {\n    "小明": {"语文": 90, "数学": 85, "英语": 92},\n    "小红": {"语文": 88, "数学": 95, "英语": 90},\n}\n\nwhile True:\n    print("\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "3":\n        if not students:\n            print("暂无学生数据")\n            continue\n        ranked = sorted(\n            [(sum(s.values()), name, sum(s.values())//3) for name, s in students.items()],\n            reverse=True\n        )\n        medals = {1: "🥇", 2: "🥈", 3: "🥉"}\n        for rank, (total, name, avg) in enumerate(ranked, 1):\n            medal = medals.get(rank, f"  {rank}.")\n            print(f"{medal} {name}: 总分{total}, 平均{avg}")\n    elif choice == "5":\n        print("再见！")\n        break',
        'test_cases': None,
        'order_index': 3,
    },
    {
        'title': '任务 4：保存到 CSV 文件',
        'description': '实现选项 4。将学生成绩数据保存到 scores.csv 文件，包含表头（姓名,语文,数学,英语,总分,平均分），每行一个学生的数据。使用 csv 模块。',
        'starter_code': 'import csv\n\nstudents = {\n    "小明": {"语文": 90, "数学": 85, "英语": 92},\n    "小红": {"语文": 88, "数学": 95, "英语": 90},\n}\n\n# 任务 4：保存到 CSV\n# TODO: 用 csv.writer 写入文件\n# TODO: 第一行写表头\n# TODO: 每行写学生数据\n\nwhile True:\n    print("\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出")\n    choice = input("请选择: ")\n    \n    if choice == "4":\n        # TODO: 保存逻辑\n        pass\n    elif choice == "5":\n        break',
        'hint': "with open('scores.csv', 'w', newline='', encoding='utf-8-sig') as f: writer = csv.writer(f)。writer.writerow(['姓名','语文','数学','英语','总分','平均分'])。遍历 students，计算总分和平均（总分//3），writer.writerow([name, ...])。",
        'answer_code': "import csv\n\nstudents = {\n    '小明': {'语文': 90, '数学': 85, '英语': 92},\n    '小红': {'语文': 88, '数学': 95, '英语': 90},\n}\n\nwhile True:\n    print('\\n1. 添加  2. 录入  3. 排名  4. 保存  5. 退出')\n    choice = input('请选择: ')\n    \n    if choice == '4':\n        if not students:\n            print('暂无数据')\n            continue\n        with open('scores.csv', 'w', newline='', encoding='utf-8-sig') as f:\n            writer = csv.writer(f)\n            writer.writerow(['姓名', '语文', '数学', '英语', '总分', '平均分'])\n            for name, scores in students.items():\n                total = sum(scores.values())\n                avg = total // 3\n                writer.writerow([name, scores['语文'], scores['数学'], scores['英语'], total, avg])\n        print('成绩已保存到 scores.csv')\n    elif choice == '5':\n        print('再见！')\n        break",
        'test_cases': None,
        'order_index': 4,
    },
]

# ============================================================
# Project 5: 天气查询工具
# ============================================================
PROJECT_5 = {
    'title': '天气查询工具',
    'description': '开发一个命令行天气查询工具。使用免费 API 获取城市天气信息，支持 JSON 数据处理、命令行参数和文件缓存。串联 HTTP 请求、JSON、argparse、文件操作。',
    'difficulty': 'intermediate',
    'category': 'tool',
    'estimated_minutes': 45,
    'final_result': '运行效果：\n$ python weather.py --city 北京\n城市: 北京\n温度: 22°C\n天气: 晴\n湿度: 45%\n\n$ python weather.py --city 上海 --save\n数据已保存到 weather_cache.json',
    'knowledge_points': ['HTTP请求(requests)', 'JSON', 'argparse', '文件读写', '异常处理', 'datetime'],
    'order_index': 5,
}

PROJECT_5_TASKS = [
    {
        'title': '任务 1：实现命令行参数解析',
        'description': '使用 argparse 模块实现命令行参数：--city（必选，目标城市）、--save（可选标志，保存结果到文件）。解析参数并打印出来确认。',
        'starter_code': '# 任务 1：命令行参数解析\n# TODO: 导入 argparse\n# TODO: 创建 ArgumentParser\n# TODO: 添加 --city 和 --save 参数\n# TODO: 解析并打印\n\nimport argparse\n',
        'hint': "parser = argparse.ArgumentParser(description='天气查询工具')。parser.add_argument('--city', required=True, help='城市名称')。parser.add_argument('--save', action='store_true', help='保存结果')。args = parser.parse_args()。",
        'answer_code': "import argparse\n\nparser = argparse.ArgumentParser(description='天气查询工具')\nparser.add_argument('--city', required=True, help='城市名称')\nparser.add_argument('--save', action='store_true', help='保存结果到文件')\n\nargs = parser.parse_args()\nprint(f'查询城市: {args.city}')\nprint(f'保存模式: {args.save}')",
        'test_cases': None,
        'order_index': 1,
    },
    {
        'title': '任务 2：模拟 API 请求获取天气',
        'description': '由于真实 API 需要注册，我们使用模拟数据。编写 get_weather(city) 函数，接受城市名，返回包含 weather 信息的字典。用 try/except 处理可能出现的 KeyError（城市不在模拟数据中）。',
        'starter_code': '# 任务 2：模拟天气 API\n\ndef get_weather(city):\n    # 模拟天气数据\n    weather_db = {\n        "北京": {"temp": 22, "desc": "晴", "humidity": 45},\n        "上海": {"temp": 25, "desc": "多云", "humidity": 60},\n        "广州": {"temp": 30, "desc": "阵雨", "humidity": 80},\n        "深圳": {"temp": 28, "desc": "阴", "humidity": 70},\n    }\n    # TODO: 查找城市，获取天气\n    # TODO: 城市不存在时给出提示\n    pass\n\n# 测试\nprint(get_weather("北京"))\nprint(get_weather("火星"))',
        'hint': "用 if city in weather_db 检查城市。返回的字典可以加入 city 字段和 timestamp。城市不存在时可以 raise ValueError(f'未找到城市数据: {city}')。",
        'answer_code': 'from datetime import datetime\n\ndef get_weather(city):\n    weather_db = {\n        "北京": {"temp": 22, "desc": "晴", "humidity": 45},\n        "上海": {"temp": 25, "desc": "多云", "humidity": 60},\n        "广州": {"temp": 30, "desc": "阵雨", "humidity": 80},\n        "深圳": {"temp": 28, "desc": "阴", "humidity": 70},\n    }\n    \n    if city not in weather_db:\n        raise ValueError(f"未找到城市数据: {city}")\n    \n    data = weather_db[city]\n    return {\n        "city": city,\n        "temp": data["temp"],\n        "desc": data["desc"],\n        "humidity": data["humidity"],\n        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),\n    }',
        'test_cases': None,
        'order_index': 2,
    },
    {
        'title': '任务 3：格式化输出天气信息',
        'description': '编写 display_weather(data) 函数，接收天气字典，以美观的格式打印。同时实现 --save 功能：如果 args.save 为 True，把天气数据保存为 JSON 文件（weather_cache.json）。',
        'starter_code': 'import json\nfrom datetime import datetime\n\n# 模拟数据\nweather_data = {\n    "city": "北京", "temp": 22, "desc": "晴", "humidity": 45,\n    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),\n}\n\nsave_to_file = True  # 模拟 args.save\n\n# 任务 3：格式化输出和保存\n# TODO: 打印美观的天气信息\n# TODO: 如果 save_to_file，保存为 JSON\n',
        'hint': "print 分行输出城市、温度、天气、湿度。JSON 保存：with open('weather_cache.json', 'w', encoding='utf-8') as f: json.dump(weather_data, f, ensure_ascii=False, indent=2)。",
        'answer_code': 'import json\nfrom datetime import datetime\n\nweather_data = {\n    "city": "北京", "temp": 22, "desc": "晴", "humidity": 45,\n    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),\n}\n\nsave_to_file = True\n\nprint(f"城市: {weather_data[\'city\']}")\nprint(f"温度: {weather_data[\'temp\']}°C")\nprint(f"天气: {weather_data[\'desc\']}")\nprint(f"湿度: {weather_data[\'humidity\']}%")\nprint(f"更新时间: {weather_data[\'timestamp\']}")\n\nif save_to_file:\n    with open(\'weather_cache.json\', \'w\', encoding=\'utf-8\') as f:\n        json.dump(weather_data, f, ensure_ascii=False, indent=2)\n    print(\'数据已保存到 weather_cache.json\')',
        'test_cases': None,
        'order_index': 3,
    },
    {
        'title': '任务 4：整合所有功能',
        'description': '把任务 1-3 整合成完整程序。程序接收 --city 参数，查询天气，显示结果，根据 --save 决定是否保存。城市不存在时打印友好提示。添加错误处理。',
        'starter_code': 'import argparse\nimport json\nfrom datetime import datetime\n\ndef get_weather(city):\n    # 从任务 2 复制过来\n    pass\n\n# 任务 4：整合\n# TODO: 解析参数\n# TODO: 调用 get_weather\n# TODO: try/except 处理错误\n# TODO: 显示 + 保存\n',
        'hint': '用 try/except 包裹主逻辑：try: data = get_weather(args.city); 显示; 保存。except ValueError as e: print(e)。把所有函数组合起来。',
        'answer_code': 'import argparse\nimport json\nfrom datetime import datetime\n\n\ndef get_weather(city):\n    weather_db = {\n        \'北京\': {\'temp\': 22, \'desc\': \'晴\', \'humidity\': 45},\n        \'上海\': {\'temp\': 25, \'desc\': \'多云\', \'humidity\': 60},\n        \'广州\': {\'temp\': 30, \'desc\': \'阵雨\', \'humidity\': 80},\n        \'深圳\': {\'temp\': 28, \'desc\': \'阴\', \'humidity\': 70},\n    }\n    if city not in weather_db:\n        raise ValueError(f\'未找到城市数据: {city}\')\n    data = weather_db[city]\n    return {\n        \'city\': city, \'temp\': data[\'temp\'], \'desc\': data[\'desc\'],\n        \'humidity\': data[\'humidity\'],\n        \'timestamp\': datetime.now().strftime(\'%Y-%m-%d %H:%M\'),\n    }\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\'天气查询工具\')\n    parser.add_argument(\'--city\', required=True, help=\'城市名称\')\n    parser.add_argument(\'--save\', action=\'store_true\', help=\'保存结果\')\n    args = parser.parse_args()\n\n    try:\n        data = get_weather(args.city)\n        print(f"城市: {data[\'city\']}")\n        print(f"温度: {data[\'temp\']}°C")\n        print(f"天气: {data[\'desc\']}")\n        print(f"湿度: {data[\'humidity\']}%")\n        print(f"更新时间: {data[\'timestamp\']}")\n\n        if args.save:\n            with open(\'weather_cache.json\', \'w\', encoding=\'utf-8\') as f:\n                json.dump(data, f, ensure_ascii=False, indent=2)\n            print(\'数据已保存到 weather_cache.json\')\n    except ValueError as e:\n        print(f\'错误: {e}\')\n\n\nif __name__ == \'__main__\':\n    main()',
        'test_cases': None,
        'order_index': 4,
    },
]

# ============================================================
# Project 6: 简易博客系统
# ============================================================
PROJECT_6 = {
    'title': '简易博客系统',
    'description': '开发一个基于类的简易博客管理程序。使用 Post 类封装文章数据（标题、内容、日期、标签），支持创建、查看、搜索和删除文章。串联 OOP、文件存储、datetime、正则表达式。',
    'difficulty': 'intermediate',
    'category': 'application',
    'estimated_minutes': 60,
    'final_result': '运行效果：\n===== 简易博客系统 =====\n1. 写文章\n2. 查看文章列表\n3. 查看文章详情\n4. 搜索文章（按标签）\n5. 删除文章\n6. 退出',
    'knowledge_points': ['类与对象', 'dataclass', 'datetime', '正则表达式', 'JSON文件存储', '列表操作'],
    'order_index': 6,
}

PROJECT_6_TASKS = [
    {
        'title': '任务 1：定义 Post 数据类',
        'description': '使用 @dataclass 定义 Post 类，包含属性：id (int)、title (str)、content (str)、tags (list[str])、created_at (str，默认当前时间)。定义 __str__ 方法返回摘要信息。',
        'starter_code': '# 任务 1：定义 Post 数据类\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\n\n# TODO: @dataclass 装饰 Post 类\n# TODO: 定义属性 id, title, content, tags, created_at\n# TODO: 可选：定义 __str__ 方法\n\n\n# 测试\npost = Post(1, "Python 学习笔记", "今天学了类和对象", ["Python", "OOP"])\nprint(post)',
        'hint': "@dataclass 装饰类，定义属性用类型注解。created_at 默认值用 field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))。__str__ 返回 f'[{post_id}] {title} ({created_at})'。",
        'answer_code': "from dataclasses import dataclass, field\nfrom datetime import datetime\n\n@dataclass\nclass Post:\n    id: int\n    title: str\n    content: str\n    tags: list[str] = field(default_factory=list)\n    created_at: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))\n    \n    def __str__(self):\n        tags_str = ', '.join(self.tags) if self.tags else '无标签'\n        return f'[{self.id}] {self.title} | {tags_str} | {self.created_at}'",
        'test_cases': None,
        'order_index': 1,
    },
    {
        'title': '任务 2：实现 Blog 类的基础功能',
        'description': '创建 Blog 类管理文章列表。实现 __init__（初始化 posts 列表和 next_id 计数器）、create_post(title, content, tags)（创建新文章并添加到列表）、list_posts()（显示所有文章的摘要）。',
        'starter_code': "# 任务 2：Blog 类和基础操作\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\n\n@dataclass\nclass Post:\n    id: int\n    title: str\n    content: str\n    tags: list[str] = field(default_factory=list)\n    created_at: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))\n    def __str__(self):\n        return f'[{self.id}] {self.title} | {self.created_at}'\n\nclass Blog:\n    # TODO: __init__ 方法\n    # TODO: create_post 方法\n    # TODO: list_posts 方法\n    pass",
        'hint': "__init__: self.posts = [], self.next_id = 1。create_post: 创建 Post 对象，append 到 self.posts，next_id += 1，返回 post。list_posts: 遍历 self.posts 打印每个 post。空时提示 '暂无文章'。",
        'answer_code': "from dataclasses import dataclass, field\nfrom datetime import datetime\n\n@dataclass\nclass Post:\n    id: int\n    title: str\n    content: str\n    tags: list[str] = field(default_factory=list)\n    created_at: str = field(default_factory=lambda: datetime.now().strftime('%Y-%m-%d %H:%M'))\n    def __str__(self):\n        return f'[{self.id}] {self.title} | {self.created_at}'\n\nclass Blog:\n    def __init__(self):\n        self.posts = []\n        self.next_id = 1\n\n    def create_post(self, title, content, tags=None):\n        post = Post(self.next_id, title, content, tags or [])\n        self.posts.append(post)\n        self.next_id += 1\n        print(f'文章已发布: {post}')\n        return post\n\n    def list_posts(self):\n        if not self.posts:\n            print('暂无文章')\n            return\n        for post in self.posts:\n            print(post)",
        'test_cases': None,
        'order_index': 2,
    },
    {
        'title': '任务 3：实现文章查看和搜索',
        'description': '为 Blog 类添加 get_post(post_id)（查看详情，找到打印标题、内容、标签、时间）和 search_by_tag(tag)（搜索含指定标签的文章）。完善菜单的选项 3 和 4。',
        'starter_code': 'class Blog:\n    def __init__(self):\n        self.posts = []\n        self.next_id = 1\n\n    # 前面任务的方法...\n\n    # TODO: get_post(self, post_id)\n    # TODO: search_by_tag(self, tag)\n    pass',
        'hint': "get_post: 遍历 self.posts 找 post.id == post_id，找到就打印详细信息，找不到提示 '文章不存在'。search_by_tag: 列表推导式 [p for p in self.posts if tag in p.tags]，然后调用 list_posts 风格显示。不区分大小写：tag.lower() in [t.lower() for t in p.tags]。",
        'answer_code': 'class Blog:\n    def __init__(self):\n        self.posts = []\n        self.next_id = 1\n\n    def get_post(self, post_id):\n        for post in self.posts:\n            if post.id == post_id:\n                print(f"\\n{chr(61)*40}")\n                print(f"标题: {post.title}")\n                print(f"日期: {post.created_at}")\n                print(f"标签: {", ".join(post.tags) if post.tags else "无"}")\n                print(f"{chr(61)*40}")\n                print(post.content)\n                print(f"{chr(61)*40}")\n                return\n        print(f"文章 #{post_id} 不存在")\n\n    def search_by_tag(self, tag):\n        results = [p for p in self.posts\n                   if tag.lower() in [t.lower() for t in p.tags]]\n        if not results:\n            print(f"未找到标签 "{tag}" 的文章")\n            return\n        print(f"找到 {len(results)} 篇文章:")\n        for p in results:\n            print(p)',
        'test_cases': None,
        'order_index': 3,
    },
    {
        'title': '任务 4：实现删除和文件保存',
        'description': '为 Blog 添加 delete_post(post_id) 和 save_to_file(filename) 方法。delete 找到并删除对应文章。save_to_file 将文章列表保存为 JSON 文件（处理 dataclass 序列化）。',
        'starter_code': 'import json\n\nclass Blog:\n    # 前面的方法...\n\n    # TODO: delete_post(self, post_id)\n    # TODO: save_to_file(self, filename)\n    pass',
        'hint': "delete: for i, post in enumerate(self.posts): if post.id == post_id: del self.posts[i]; print('已删除'); return。JSON 序列化 dataclass 需要用到 dataclasses.asdict(post)。save_to_file: [asdict(p) for p in self.posts]，然后 json.dump。",
        'answer_code': 'import json\nfrom dataclasses import asdict\n\nclass Blog:\n    def delete_post(self, post_id):\n        for i, post in enumerate(self.posts):\n            if post.id == post_id:\n                del self.posts[i]\n                print(f"文章 #{post_id} 已删除")\n                return\n        print(f"文章 #{post_id} 不存在")\n\n    def save_to_file(self, filename):\n        data = [asdict(p) for p in self.posts]\n        with open(filename, "w", encoding="utf-8") as f:\n            json.dump(data, f, ensure_ascii=False, indent=2)\n        print(f"已保存 {len(self.posts)} 篇文章到 {filename}")',
        'test_cases': None,
        'order_index': 4,
    },
    {
        'title': '任务 5：整合主程序和菜单',
        'description': '实现完整的 main() 函数和菜单循环。连接 Blog 类的所有功能。每项操作对应一个选项。运行效果见项目描述。',
        'starter_code': "# 任务 5：整合主程序\n# TODO: 整合前面所有代码\n# TODO: 实现 main() 菜单循环\n# TODO: 连接 Blog 的各个方法\n\nif __name__ == '__main__':\n    main()",
        'hint': "main(): blog = Blog(); while True: 显示菜单；input 获取选择；if/elif 分支调用 blog 的各个方法。选项 2（新增）需要用 input 获取标题、内容、标签（逗号分隔）。标签用 split(',') 分割。",
        'answer_code': 'from dataclasses import dataclass, field, asdict\nfrom datetime import datetime\nimport json\n\n@dataclass\nclass Post:\n    id: int\n    title: str\n    content: str\n    tags: list[str] = field(default_factory=list)\n    created_at: str = field(default_factory=lambda: datetime.now().strftime(\'%Y-%m-%d %H:%M\'))\n    def __str__(self):\n        return f\'[{self.id}] {self.title} | {self.created_at}\'\n\nclass Blog:\n    def __init__(self):\n        self.posts = []\n        self.next_id = 1\n    def create_post(self, title, content, tags=None):\n        post = Post(self.next_id, title, content, tags or [])\n        self.posts.append(post)\n        self.next_id += 1\n        print(f\'文章已发布: {post}\')\n    def list_posts(self):\n        if not self.posts:\n            print(\'暂无文章\')\n            return\n        for post in self.posts:\n            print(post)\n    def get_post(self, post_id):\n        for post in self.posts:\n            if post.id == post_id:\n                print(f\'\\n{"="*40}\\n标题: {post.title}\\n日期: {post.created_at}\')\n                print(f\'标签: {", ".join(post.tags) if post.tags else "无"}\')\n                print(f\'{"="*40}\\n{post.content}\\n{"="*40}\')\n                return\n        print(f\'文章 #{post_id} 不存在\')\n    def search_by_tag(self, tag):\n        results = [p for p in self.posts if tag.lower() in [t.lower() for t in p.tags]]\n        if not results:\n            print(f\'未找到标签 "{tag}" 的文章\')\n            return\n        print(f\'找到 {len(results)} 篇:\')\n        for p in results:\n            print(p)\n    def delete_post(self, post_id):\n        for i, post in enumerate(self.posts):\n            if post.id == post_id:\n                del self.posts[i]\n                print(f\'文章 #{post_id} 已删除\')\n                return\n        print(f\'文章 #{post_id} 不存在\')\n    def save_to_file(self, filename):\n        data = [asdict(p) for p in self.posts]\n        with open(filename, \'w\', encoding=\'utf-8\') as f:\n            json.dump(data, f, ensure_ascii=False, indent=2)\n        print(f\'已保存 {len(self.posts)} 篇到 {filename}\')\n\ndef main():\n    blog = Blog()\n    while True:\n        print(\'\\n===== 简易博客系统 =====\')\n        print(\'1. 写文章  2. 列表  3. 详情  4. 搜索  5. 删除  6. 保存  7. 退出\')\n        choice = input(\'请选择: \')\n        if choice == \'1\':\n            title = input(\'标题: \')\n            content = input(\'内容: \')\n            tags_input = input(\'标签(逗号分隔): \')\n            tags = [t.strip() for t in tags_input.split(\',\') if t.strip()]\n            blog.create_post(title, content, tags)\n        elif choice == \'2\':\n            blog.list_posts()\n        elif choice == \'3\':\n            blog.get_post(int(input(\'文章ID: \')))\n        elif choice == \'4\':\n            blog.search_by_tag(input(\'标签: \'))\n        elif choice == \'5\':\n            blog.delete_post(int(input(\'文章ID: \')))\n        elif choice == \'6\':\n            blog.save_to_file(input(\'文件名: \'))\n        elif choice == \'7\':\n            print(\'再见！\')\n            break\n\nif __name__ == \'__main__\':\n    main()',
        'test_cases': None,
        'order_index': 5,
    },
]

# ============================================================
# Project 7: 数据分析脚本
# ============================================================
PROJECT_7 = {
    'title': '数据分析脚本',
    'description': '编写一个数据分析脚本，读取 CSV 销售数据，进行数据清洗、统计分析和可视化准备。使用 collections.Counter 和列表推导式高效处理数据，输出分析报告。',
    'difficulty': 'advanced',
    'category': 'data_analysis',
    'estimated_minutes': 45,
    'final_result': "运行效果：\n===== 销售数据分析报告 =====\n总订单数: 120\n总销售额: ¥45,680.50\n平均订单金额: ¥380.67\n最畅销商品: iPhone 15 (32件)\n销售额最高月份: 2025-03 (¥12,450.00)\n各地区销售: {'华东': 28, '华南': 22, ...}",
    'knowledge_points': ['CSV读写', 'collections.Counter', '列表推导式', 'datetime', '数据排序', '字典统计'],
    'order_index': 7,
}

PROJECT_7_TASKS = [
    {
        'title': '任务 1：读取并解析 CSV 数据',
        'description': '使用 csv.DictReader 读取 sales.csv 文件（模拟数据）。将数据解析为字典列表。文件包含字段：date, product, category, region, quantity, unit_price。用列表推导式提取所需字段。',
        'starter_code': '# 任务 1：读取 CSV 数据\nimport csv\n\n# 模拟数据（实际应读取文件）\ndata = """date,product,category,region,quantity,unit_price\n2025-03-01,iPhone 15,手机,华东,2,6999\n2025-03-02,MacBook Pro,电脑,华北,1,12999\n2025-03-02,iPhone 15,手机,华南,3,6999\n2025-03-03,iPad Air,平板,华东,1,4799\n2025-03-03,MacBook Pro,电脑,华南,1,12999\n2025-03-04,iPhone 15,手机,华北,2,6999"""\n\n# TODO: 将 data 解析为字典列表\n# TODO: 把 quantity 和 unit_price 转为数字类型\n\nrecords = []\nprint(f"共读取 {len(records)} 条记录")',
        'hint': "用 data.split('\\n') 按行分割，csv.DictReader 需要行列表。records = list(reader)。遍历时 r['quantity'] = int(r['quantity'])，r['unit_price'] = float(r['unit_price'])。给每条记录加 amount = quantity * unit_price。",
        'answer_code': 'import csv\n\ndata = """date,product,category,region,quantity,unit_price\n2025-03-01,iPhone 15,手机,华东,2,6999\n2025-03-02,MacBook Pro,电脑,华北,1,12999\n2025-03-02,iPhone 15,手机,华南,3,6999\n2025-03-03,iPad Air,平板,华东,1,4799\n2025-03-03,MacBook Pro,电脑,华南,1,12999\n2025-03-04,iPhone 15,手机,华北,2,6999"""\n\nlines = data.strip().split(\'\\n\')\nreader = csv.DictReader(lines)\nrecords = []\nfor row in reader:\n    qty = int(row[\'quantity\'])\n    price = float(row[\'unit_price\'])\n    records.append({\n        \'date\': row[\'date\'],\n        \'product\': row[\'product\'],\n        \'category\': row[\'category\'],\n        \'region\': row[\'region\'],\n        \'quantity\': qty,\n        \'unit_price\': price,\n        \'amount\': qty * price,\n    })\n\nprint(f\'共读取 {len(records)} 条记录\')\nfor r in records[:3]:\n    print(f"  {r[\'date\']} | {r[\'product\']} | ¥{r[\'amount\']:.2f}")',
        'test_cases': None,
        'order_index': 1,
    },
    {
        'title': '任务 2：使用 Counter 进行统计分析',
        'description': '使用 collections.Counter 统计：1）每个商品的销售数量；2）每个地区的订单数；3）每个品类的销售额。找出最畅销商品和销售额最高的地区。',
        'starter_code': "from collections import Counter\n\n# 假设 records 已从上一步获取\nrecords = [\n    {'product': 'iPhone 15', 'region': '华东', 'quantity': 2, 'amount': 13998.0, 'category': '手机'},\n    {'product': 'MacBook Pro', 'region': '华北', 'quantity': 1, 'amount': 12999.0, 'category': '电脑'},\n    {'product': 'iPhone 15', 'region': '华南', 'quantity': 3, 'amount': 20997.0, 'category': '手机'},\n]\n\n# TODO: 统计商品销量 (product → 销售件数)\n# TODO: 统计地区订单数 (region → 订单数)\n# TODO: 统计品类销售额 (category → 销售额)\n# TODO: 找出最畅销商品",
        'hint': "Counter 可以累加：product_qty = Counter() 然后 for r in records: product_qty[r['product']] += r['quantity']。用 product_qty.most_common(1) 获取最畅销商品。地区订单数：Counter(r['region'] for r in records)。",
        'answer_code': "from collections import Counter\n\nrecords = [\n    {'product': 'iPhone 15', 'region': '华东', 'quantity': 2, 'amount': 13998.0, 'category': '手机'},\n    {'product': 'MacBook Pro', 'region': '华北', 'quantity': 1, 'amount': 12999.0, 'category': '电脑'},\n    {'product': 'iPhone 15', 'region': '华南', 'quantity': 3, 'amount': 20997.0, 'category': '手机'},\n]\n\nproduct_qty = Counter()\nregion_orders = Counter()\ncategory_amount = Counter()\n\nfor r in records:\n    product_qty[r['product']] += r['quantity']\n    region_orders[r['region']] += 1\n    category_amount[r['category']] += r['amount']\n\nprint(f'商品销量: {product_qty}')\nprint(f'地区订单: {region_orders}')\nprint(f'品类销售额: {dict(category_amount)}')\nprint(f'最畅销商品: {product_qty.most_common(1)[0]}')",
        'test_cases': None,
        'order_index': 2,
    },
    {
        'title': '任务 3：用列表推导式进行数据过滤和排序',
        'description': '使用列表推导式完成：1）筛选出销售额 > 10000 的大单；2）按销售额降序排列所有记录；3）提取所有华东地区的订单。',
        'starter_code': "records = [\n    {'product': 'iPhone 15', 'region': '华东', 'quantity': 2, 'amount': 13998.0},\n    {'product': 'MacBook Pro', 'region': '华北', 'quantity': 1, 'amount': 12999.0},\n    {'product': 'iPhone 15', 'region': '华南', 'quantity': 3, 'amount': 20997.0},\n    {'product': 'iPad Air', 'region': '华东', 'quantity': 1, 'amount': 4799.0},\n    {'product': 'MacBook Pro', 'region': '华南', 'quantity': 1, 'amount': 12999.0},\n]\n\n# TODO: 大单（amount >= 10000）\n# TODO: 按 amount 降序排列\n# TODO: 华东地区订单",
        'hint': "大单：[r for r in records if r['amount'] >= 10000]。排序：sorted(records, key=lambda r: r['amount'], reverse=True)。华东：[r for r in records if r['region'] == '华东']。",
        'answer_code': 'records = [\n    {\'product\': \'iPhone 15\', \'region\': \'华东\', \'quantity\': 2, \'amount\': 13998.0},\n    {\'product\': \'MacBook Pro\', \'region\': \'华北\', \'quantity\': 1, \'amount\': 12999.0},\n    {\'product\': \'iPhone 15\', \'region\': \'华南\', \'quantity\': 3, \'amount\': 20997.0},\n    {\'product\': \'iPad Air\', \'region\': \'华东\', \'quantity\': 1, \'amount\': 4799.0},\n    {\'product\': \'MacBook Pro\', \'region\': \'华南\', \'quantity\': 1, \'amount\': 12999.0},\n]\n\nbig_orders = [r for r in records if r[\'amount\'] >= 10000]\nprint(f\'大单 ({len(big_orders)} 笔):\')\nfor o in big_orders:\n    print(f"  {o[\'product\']} ¥{o[\'amount\']:.0f}")\n\nsorted_records = sorted(records, key=lambda r: r[\'amount\'], reverse=True)\nprint(f\'\\n按销售额排名:\')\nfor i, r in enumerate(sorted_records, 1):\n    print(f"  {i}. {r[\'product\']} ¥{r[\'amount\']:.0f}")\n\neast_orders = [r for r in records if r[\'region\'] == \'华东\']\nprint(f\'\\n华东地区 ({len(east_orders)} 笔):\')\nfor o in east_orders:\n    print(f"  {o[\'product\']} ¥{o[\'amount\']:.0f}")',
        'test_cases': None,
        'order_index': 3,
    },
    {
        'title': '任务 4：生成数据分析报告',
        'description': '汇总前面所有分析，打印格式化的分析报告（见项目描述）。包括：总订单数、总销售额、平均订单金额、最畅销商品、销售额最高月份、各地区销售分布。',
        'starter_code': '# 任务 4：生成报告\n# 汇总前三个任务的结果，输出格式化报告\n\n# TODO: 计算关键指标\n# TODO: 格式化输出报告\n\nprint("===== 销售数据分析报告 =====")\n# ... 等等',
        'hint': "总订单数 = len(records)。总销售额 = sum(r['amount'] for r in records)。平均 = 总额/总订单数。最畅销 = Counter.most_common(1)。月份销售额：用 datetime.strptime 解析日期，按月份分组。地区销售 = Counter(r['region'] for r in records)。",
        'answer_code': "from collections import Counter\nfrom datetime import datetime\n\nrecords = [\n    {'date': '2025-03-01', 'product': 'iPhone 15', 'region': '华东', 'amount': 13998.0},\n    {'date': '2025-03-02', 'product': 'MacBook Pro', 'region': '华北', 'amount': 12999.0},\n    {'date': '2025-03-02', 'product': 'iPhone 15', 'region': '华南', 'amount': 20997.0},\n    {'date': '2025-03-03', 'product': 'iPad Air', 'region': '华东', 'amount': 4799.0},\n    {'date': '2025-03-03', 'product': 'MacBook Pro', 'region': '华南', 'amount': 12999.0},\n    {'date': '2025-03-04', 'product': 'iPhone 15', 'region': '华北', 'amount': 13998.0},\n]\n\ntotal_orders = len(records)\ntotal_amount = sum(r['amount'] for r in records)\navg_amount = total_amount / total_orders\n\nproduct_qty = Counter()\nregion_orders = Counter()\nmonthly_amount = Counter()\n\nfor r in records:\n    product_qty[r['product']] += 1\n    region_orders[r['region']] += 1\n    month_key = r['date'][:7]\n    monthly_amount[month_key] += r['amount']\n\nprint('===== 销售数据分析报告 =====')\nprint(f'总订单数: {total_orders}')\nprint(f'总销售额: ¥{total_amount:,.2f}')\nprint(f'平均订单金额: ¥{avg_amount:,.2f}')\nprint(f'最畅销商品: {product_qty.most_common(1)[0][0]}')\ntop_month, top_month_amount = monthly_amount.most_common(1)[0]\nprint(f'销售额最高月份: {top_month} (¥{top_month_amount:,.2f})')\nprint(f'各地区销售: {dict(region_orders)}')",
        'test_cases': None,
        'order_index': 4,
    },
]

# ============================================================
# Project 8: 聊天机器人
# ============================================================
PROJECT_8 = {
    'title': '聊天机器人',
    'description': '开发一个基于规则的命令行聊天机器人。支持关键词匹配回复、天气查询、笔记功能和自定义规则。使用正则表达式进行意图识别，采用类设计组织代码。',
    'difficulty': 'advanced',
    'category': 'application',
    'estimated_minutes': 60,
    'final_result': '运行效果：\n你: 你好\n机器人: 你好！有什么可以帮你的？\n\n你: 现在几点了\n机器人: 现在是 2025-03-15 14:30:22\n\n你: 帮我记一下，明天下午3点开会\n机器人: 已记录: 明天下午3点开会\n\n你: 查看笔记\n机器人: 你的笔记:\n  1. 明天下午3点开会\n\n你: 天气怎么样\n机器人: 抱歉，请先设置城市（输入: 设置城市 北京）\n\n你: 再见\n机器人: 再见！期待下次聊天！',
    'knowledge_points': ['正则表达式', '类与对象', '字典', 'datetime', '文件读写', '字符串处理'],
    'order_index': 8,
}

PROJECT_8_TASKS = [
    {
        'title': '任务 1：定义 Bot 类和规则系统',
        'description': '创建 ChatBot 类，包含 __init__ 方法初始化 name（机器人名称）、rules（规则字典，键为正则模式，值为回复函数）和 notes（笔记列表）。定义一个简单的规则字典和一个问候规则。',
        'starter_code': '# 任务 1：ChatBot 类和基础规则\nimport re\n\nclass ChatBot:\n    # TODO: __init__ 初始化 name, rules, notes\n    # TODO: 添加基础的问候规则\n    # TODO: 规则值可以是字符串或函数（高级）\n    pass\n\nbot = ChatBot("小智")\nprint(bot.name)\nprint(bot.rules)',
        'hint': "self.rules = {} 存储规则。添加规则方法 add_rule(pattern, response)。pattern 是正则字符串，response 是回复内容（字符串）。self.notes = [] 存笔记。默认添加打招呼规则：re.compile(r'你好|嗨|hello', re.I)。",
        'answer_code': 'import re\n\nclass ChatBot:\n    def __init__(self, name=\'小智\'):\n        self.name = name\n        self.rules = {}  # {compiled_pattern: response}\n        self.notes = []\n        self._add_default_rules()\n\n    def _add_default_rules(self):\n        self.add_rule(r\'你好|嗨|hello|hi\', f\'你好！我是{self.name}，有什么可以帮你的？\')\n        self.add_rule(r\'再见|拜拜|bye\', f\'再见！期待下次聊天！\')\n        self.add_rule(r\'几点|时间\', lambda m: f\'现在是 {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\')\n\n    def add_rule(self, pattern, response):\n        self.rules[re.compile(pattern, re.IGNORECASE)] = response',
        'test_cases': None,
        'order_index': 1,
    },
    {
        'title': '任务 2：实现消息匹配和回复逻辑',
        'description': '实现 ChatBot.reply(message) 方法。遍历所有规则，用正则匹配用户消息。匹配成功时：如果规则值是字符串直接返回，如果是函数就调用它获取回复。没有匹配时返回默认回复。',
        'starter_code': "# 任务 2：消息匹配和回复\nimport re\n\nclass ChatBot:\n    def __init__(self, name='小智'):\n        self.name = name\n        self.rules = {}\n        self.notes = []\n        self._add_default_rules()\n\n    def _add_default_rules(self):\n        self.add_rule(r'你好|嗨|hello', f'你好！我是{self.name}！')\n        self.add_rule(r'再见|拜拜|bye', '再见！')\n\n    def add_rule(self, pattern, response):\n        self.rules[re.compile(pattern, re.IGNORECASE)] = response\n\n    # TODO: reply(self, message) 方法\n    # TODO: 遍历规则，找到第一个匹配\n    # TODO: 匹配到了就返回相应回复\n    # TODO: 没匹配到返回默认回复\n\nbot = ChatBot()\nprint(bot.reply('你好'))\nprint(bot.reply('今天天气怎么样'))",
        'hint': "for pattern, response in self.rules.items(): match = pattern.search(message); if match: ...。如果 callable(response): return response(match)（传 match 对象）；else: return response。默认回复：'抱歉，我不太理解。输入 帮助 查看功能列表。'。",
        'answer_code': 'import re\n\nclass ChatBot:\n    def __init__(self, name=\'小智\'):\n        self.name = name\n        self.rules = {}\n        self.notes = []\n        self._add_default_rules()\n\n    def _add_default_rules(self):\n        self.add_rule(r\'你好|嗨|hello\', f\'你好！我是{self.name}！\')\n        self.add_rule(r\'再见|拜拜|bye\', \'再见！\')\n\n    def add_rule(self, pattern, response):\n        self.rules[re.compile(pattern, re.IGNORECASE)] = response\n\n    def reply(self, message):\n        for pattern, response in self.rules.items():\n            match = pattern.search(message)\n            if match:\n                if callable(response):\n                    return response(match)\n                return response\n        return f\'抱歉，我不太理解。输入"帮助"查看功能列表。\'',
        'test_cases': None,
        'order_index': 2,
    },
    {
        'title': '任务 3：实现笔记功能',
        'description': "添加两个规则：1）匹配 '记一下' 或 '帮我记'，提取后面的内容存入 self.notes；2）匹配 '查看笔记|我的笔记|笔记'，显示所有笔记列表。使用正则捕获组（括号）提取笔记内容。",
        'starter_code': '# 任务 3：笔记功能\n# 在上一步的 ChatBot 基础上，添加两个新规则\n\n# TODO: 添加记笔记的规则\n# TODO: 正则匹配 "记一下xxx" 或 "帮我记xxx"\n# TODO: 提取匹配的内容（用 group(1)）\n# TODO: 添加到 self.notes 并回复确认\n\n# TODO: 添加查看笔记的规则\n# TODO: 显示所有笔记（编号 + 内容）\n\ndef _add_note_rules(self):\n    # 记笔记规则\n    pass',
        'hint': "记笔记：pattern = r'(?:记一下|帮我记|记录)[：:\\s]*(.+)'。用 match.group(1) 提取内容。self.notes.append(content); return f'已记录: {content}'。查看笔记：遍历 enumerate(self.notes, 1)，格式化显示。没有笔记时提示 '暂无笔记'。",
        'answer_code': "import re\n\nclass ChatBot:\n    def __init__(self, name='小智'):\n        self.name = name\n        self.rules = {}\n        self.notes = []\n        self._add_default_rules()\n        self._add_note_rules()\n\n    def _add_note_rules(self):\n        def add_note(match):\n            content = match.group(1).strip()\n            self.notes.append(content)\n            return f'已记录: {content}'\n        self.add_rule(r'(?:记一下|帮我记|记录)[：:\\s]*(.+)', add_note)\n\n        def show_notes(match):\n            if not self.notes:\n                return '暂无笔记'\n            lines = ['你的笔记:']\n            for i, note in enumerate(self.notes, 1):\n                lines.append(f'  {i}. {note}')\n            return '\\n'.join(lines)\n        self.add_rule(r'查看笔记|我的笔记|笔记列表', show_notes)",
        'test_cases': None,
        'order_index': 3,
    },
    {
        'title': '任务 4：实现天气和帮助功能',
        'description': "添加天气查询规则（匹配 '天气' 或 'weather'）和帮助规则（匹配 '帮助' 或 'help'）。天气功能需要先设置城市（用实例属性 self.city）。帮助功能列出所有可用命令。",
        'starter_code': '# 任务 4：天气和帮助\n\ndef _add_tool_rules(self):\n    # TODO: 设置城市规则\n    # TODO: 天气查询规则\n    # TODO: 帮助规则\n    pass',
        'hint': "设置城市：r'设置城市[：:\\s]*(.+)'，self.city = match.group(1)。天气：r'天气|weather'，如果没设置城市提示 '请先设置城市'。帮助：列出所有可用命令（你好、时间、记笔记、查看笔记、天气、设置城市、再见）。",
        'answer_code': "def _add_tool_rules(self):\n    self.city = None\n\n    def set_city(match):\n        self.city = match.group(1).strip()\n        return f'城市已设置为: {self.city}'\n    self.add_rule(r'设置城市[：:\\s]*(.+)', set_city)\n\n    def check_weather(match):\n        if not self.city:\n            return '抱歉，请先设置城市（输入: 设置城市 北京）'\n        weather_db = {'北京': '晴 22°C', '上海': '多云 25°C', '广州': '阵雨 30°C'}\n        info = weather_db.get(self.city, f'暂无{self.city}的天气数据')\n        return f'{self.city}天气: {info}'\n    self.add_rule(r'天气|weather', check_weather)\n\n    def show_help(match):\n        commands = [\n            '你好 - 打招呼',\n            '几点/时间 - 查看当前时间',\n            '记一下/帮我记 xxx - 记录笔记',\n            '查看笔记 - 查看所有笔记',\n            '设置城市 xxx - 设置天气城市',\n            '天气 - 查询天气',\n            '再见 - 退出',\n        ]\n        return '可用命令:\\n' + '\\n'.join(f'  - {c}' for c in commands)\n    self.add_rule(r'帮助|help|功能', show_help)",
        'test_cases': None,
        'order_index': 4,
    },
    {
        'title': '任务 5：整合主程序和聊天循环',
        'description': "实现完整的 main() 聊天循环。用户输入消息，机器人回复，直到用户说 '再见' 或 'bye'。整合所有功能。",
        'starter_code': '# 任务 5：整合聊天循环\n# TODO: 整合所有 ChatBot 代码\n# TODO: main() 循环：input → reply → print\n# TODO: "再见" 时退出\n\nif __name__ == \'__main__\':\n    main()',
        'hint': "while True: msg = input('你: ')；如果 msg 匹配 '再见|bye' 就打印告别语并 break；否则 print(f'{bot.name}: {bot.reply(msg)}')。使用 sys.exit(0) 或在 break 后自然结束。",
        'answer_code': 'import re\n\nclass ChatBot:\n    def __init__(self, name=\'小智\'):\n        self.name = name\n        self.rules = {}\n        self.notes = []\n        self.city = None\n        self._add_default_rules()\n        self._add_note_rules()\n        self._add_tool_rules()\n    def add_rule(self, pattern, response):\n        self.rules[re.compile(pattern, re.IGNORECASE)] = response\n    def reply(self, message):\n        for pattern, response in self.rules.items():\n            match = pattern.search(message)\n            if match:\n                if callable(response):\n                    return response(match)\n                return response\n        return \'抱歉，我不太理解。输入"帮助"查看功能列表。\'\n    def _add_default_rules(self):\n        self.add_rule(r\'你好|嗨|hello|hi\', f\'你好！我是{self.name}！\')\n        self.add_rule(r\'几点|时间\',\n                      lambda m: f\'现在是 {__import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\')\n    def _add_note_rules(self):\n        def add_note(m):\n            c = m.group(1).strip()\n            self.notes.append(c)\n            return f\'已记录: {c}\'\n        self.add_rule(r\'(?:记一下|帮我记|记录)[：:\\s]*(.+)\', add_note)\n        def show(m):\n            if not self.notes: return \'暂无笔记\'\n            return \'笔记:\\n\' + \'\\n\'.join(f\'  {i}. {n}\' for i, n in enumerate(self.notes, 1))\n        self.add_rule(r\'查看笔记|笔记列表\', show)\n    def _add_tool_rules(self):\n        def sc(m):\n            self.city = m.group(1).strip()\n            return f\'城市: {self.city}\'\n        self.add_rule(r\'设置城市[：:\\s]*(.+)\', sc)\n        def cw(m):\n            if not self.city: return \'请先设置城市\'\n            db = {\'北京\': \'晴 22°C\', \'上海\': \'多云 25°C\', \'广州\': \'阵雨 30°C\'}\n            return f\'{self.city}: {db.get(self.city, "暂无数据")}\'\n        self.add_rule(r\'天气|weather\', cw)\n        def help_cmd(m):\n            return \'可用命令:\\n  - 你好\\n  - 几点/时间\\n  - 记一下 xxx\\n  - 查看笔记\\n  - 设置城市 xxx\\n  - 天气\\n  - 帮助\\n  - 再见\'\n        self.add_rule(r\'帮助|help|功能\', help_cmd)\n\ndef main():\n    bot = ChatBot(\'小智\')\n    print(f\'{bot.name}: 你好！我是{bot.name}，输入"帮助"查看功能。\')\n    while True:\n        msg = input(\'\\n你: \')\n        if not msg:\n            continue\n        reply = bot.reply(msg)\n        print(f\'{bot.name}: {reply}\')\n        if re.search(r\'再见|拜拜|bye\', msg):\n            break\n\nif __name__ == \'__main__\':\n    main()',
        'test_cases': None,
        'order_index': 5,
    },
]


ALL_PROJECTS = {
    1: (PROJECT_1, PROJECT_1_TASKS),
    2: (PROJECT_2, PROJECT_2_TASKS),
    3: (PROJECT_3, PROJECT_3_TASKS),
    4: (PROJECT_4, PROJECT_4_TASKS),
    5: (PROJECT_5, PROJECT_5_TASKS),
    6: (PROJECT_6, PROJECT_6_TASKS),
    7: (PROJECT_7, PROJECT_7_TASKS),
    8: (PROJECT_8, PROJECT_8_TASKS),
}
