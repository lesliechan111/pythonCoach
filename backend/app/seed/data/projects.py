"""
种子数据 - 3 个项目实战
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

ALL_PROJECTS = {
    1: (PROJECT_1, PROJECT_1_TASKS),
    2: (PROJECT_2, PROJECT_2_TASKS),
    3: (PROJECT_3, PROJECT_3_TASKS),
}
