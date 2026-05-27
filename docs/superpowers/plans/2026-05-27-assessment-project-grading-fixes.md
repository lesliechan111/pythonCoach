# Assessment And Project Grading Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make exercise and project submissions deterministically gradeable, preserve existing local learning data, and stop exposing reference answers to the browser.

**Architecture:** Introduce one shared test-case execution service consumed by exercise and project grading. Keep grading-specific content in a focused seed overlay/sync module rather than spreading test fixtures through the large lesson seed source, and filter public route responses at the API boundary. The frontend remains a thin consumer: it edits complete code templates and offers multiline stdin only for manual runs.

**Tech Stack:** Python 3.9, FastAPI, SQLModel, SQLite, standard-library `unittest`, Next.js 14, React, TypeScript.

---

## Working Tree Constraints

The application source files are currently untracked; the only committed application-related file is the approved design document. Every implementation commit must use explicit path arguments. Never stage `.env`, `backend/.env`, `*.db`, `venv/`, `node_modules/`, `.next/`, `.DS_Store`, or `tsconfig.tsbuildinfo`.

## File Map

| Path | Responsibility |
|---|---|
| `backend/app/services/code_runner.py` | Execute each submission in a disposable working directory so file-writing activities cannot contaminate later grading runs. |
| `backend/app/services/code_grader.py` | Run submitted code against JSON test cases and report a consistent grade result or content-configuration error. |
| `backend/app/services/exercise_grader.py` | Dispatch exercise types, normalize objective answers, and delegate code exercises to `code_grader`. |
| `backend/app/seed/data/grading_updates.py` | Hold grading-only overlays: acceptable text answers, code templates, reference solutions, and deterministic hidden test cases for affected exercises and all project tasks. |
| `backend/app/seed/init_db.py` | Apply grading overlays when building a fresh database. |
| `backend/app/seed/sync_grading_data.py` | Apply the same overlays to an existing database without deleting user-owned records. |
| `backend/app/routers/exercises.py` | Return public-safe exercise payloads and report grading configuration failures. |
| `backend/app/routers/projects.py` | Return public-safe project task payloads and grade tasks with hidden test cases. |
| `backend/tests/*.py` | Regression tests built with `unittest`, requiring no new package dependency. |
| `frontend/app/exercise/[id]/page.tsx` | Consume safe templates and continue submitting complete code. |
| `frontend/app/project/[id]/page.tsx` | Remove client-side answer shape and allow multiline manual stdin. |
| `frontend/components/dashboard/RecentActivity.tsx` | Clear the existing strict-TypeScript build blocker needed for verification. |

## Task 0: Establish A Reviewable Source Baseline

**Files:**
- Create: `.gitignore`
- Add existing source/config/docs only: `.env.example`, `HANDOFF.md`, `README.md`, `docker-compose.yml`, `code-runner/`, `backend/app/`, backend manifest/config files, `frontend/app/`, `frontend/components/`, `frontend/hooks/`, `frontend/lib/`, `frontend/types/`, frontend manifest/config files, and existing top-level docs.

The current repository contains only the approved design commit while the application tree is untracked. Complete this source-baseline checkpoint before behavioral edits so subsequent diffs show the actual grading fixes.

- [ ] **Step 1: Confirm the untracked baseline and inspect the example configuration**

Run:

```bash
git status --short --branch
git ls-files
git diff -- docs/superpowers/specs/2026-05-27-assessment-project-grading-fixes-design.md
```

Expected: application paths are untracked and only documentation from this planning/design sequence is tracked. Before staging `.env.example`, read it and confirm it contains example values only; if it contains a real credential, exclude it and replace that value with a documented sentinel in a separate reviewed step.

- [ ] **Step 2: Add ignore rules for local secrets, runtime data, and generated files**

Create `.gitignore`:

```gitignore
.DS_Store
.env
.env.*
!.env.example

__pycache__/
*.py[cod]
.venv/
venv/

node_modules/
.next/
*.tsbuildinfo

*.db
*.db-*
*.bak

.pytest_cache/
coverage/
```

- [ ] **Step 3: Stage only the existing maintainable baseline**

Run:

```bash
git add .gitignore .env.example HANDOFF.md README.md docker-compose.yml code-runner \
  backend/Dockerfile backend/alembic.ini backend/app backend/package.json backend/package-lock.json backend/requirements.txt \
  frontend/app frontend/components frontend/hooks frontend/lib frontend/types frontend/next.config.js frontend/next-env.d.ts \
  frontend/package.json frontend/package-lock.json frontend/postcss.config.js frontend/tailwind.config.ts frontend/tsconfig.json \
  docs/API.md docs/ARCHITECTURE.md docs/DATABASE.md docs/MVP_PLAN.md docs/PAGES.md
git diff --cached --name-only
```

Expected: the staged file list contains project source and documentation only; it contains no `.env`, `backend/.env`, database, dependency directory, build output, `.DS_Store`, or TypeScript build-info file.

- [ ] **Step 4: Commit the unmodified application baseline**

```bash
git commit -m "chore: establish application source baseline"
```

## Task 1: Establish The Shared Test-Case Grading Contract

**Files:**
- Create: `backend/tests/__init__.py`
- Create: `backend/tests/test_exercise_grader.py`
- Modify: `backend/app/services/code_runner.py`
- Create: `backend/app/services/code_grader.py`
- Modify: `backend/app/services/exercise_grader.py`

- [ ] **Step 1: Write failing unit tests for objective normalization and executable code grading**

Create `backend/tests/__init__.py` as an empty package marker and create `backend/tests/test_exercise_grader.py`:

```python
import json
import os
import tempfile
import unittest

from app.models.exercise import Exercise
from app.services.exercise_grader import grade_exercise
from app.services.code_grader import GradingConfigurationError


def exercise(**values):
    defaults = {
        "lesson_id": 1,
        "type": "choice",
        "title": "test",
        "description": "",
        "answer": "",
        "explanation": "explain",
    }
    defaults.update(values)
    return Exercise(**defaults)


class ExerciseGraderTests(unittest.TestCase):
    def test_judge_accepts_boolean_submission_for_ab_seed_answer(self):
        item = exercise(type="judge", answer="B")
        self.assertTrue(grade_exercise(item, user_answer="false")["is_correct"])
        self.assertFalse(grade_exercise(item, user_answer="true")["is_correct"])

    def test_fill_blank_accepts_declared_equivalent_answers(self):
        item = exercise(type="fill_blank", answer='["python", "python3"]')
        self.assertTrue(grade_exercise(item, user_answer="python3")["is_correct"])
        self.assertFalse(grade_exercise(item, user_answer="py")["is_correct"])

    def test_code_exercise_rejects_missing_hidden_cases(self):
        item = exercise(type="programming", answer="print('ok')")
        with self.assertRaises(GradingConfigurationError):
            grade_exercise(item, user_code="pass")

    def test_code_exercise_checks_complete_submission_against_cases(self):
        item = exercise(
            type="code_completion",
            answer="",
            test_cases=json.dumps([{"stdin": "", "expected_output": "8\n"}]),
        )
        self.assertTrue(grade_exercise(item, user_code="print(3 + 5)")["is_correct"])
        self.assertFalse(grade_exercise(item, user_code="pass")["is_correct"])

    def test_each_code_case_gets_a_fresh_working_directory(self):
        code = (
            "from pathlib import Path\n"
            "path = Path('state.txt')\n"
            "print(path.exists())\n"
            "path.write_text('saved', encoding='utf-8')\n"
        )
        item = exercise(
            type="programming",
            test_cases=json.dumps([
                {"stdin": "", "expected_output": "False\n"},
                {"stdin": "", "expected_output": "False\n"},
            ]),
        )
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp_dir:
            try:
                os.chdir(tmp_dir)
                self.assertTrue(grade_exercise(item, user_code=code)["is_correct"])
            finally:
                os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests to verify the contract is currently broken**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest tests.test_exercise_grader -v
```

Expected: ERROR because `app.services.code_grader` does not exist yet; this is the initial red state for the new grading contract.

- [ ] **Step 3: Add the shared code-case evaluator**

Create `backend/app/services/code_grader.py`:

```python
import json
from typing import Any, Dict, List, Optional

from app.services.code_runner import run_python_code


class GradingConfigurationError(ValueError):
    """Raised when authored grading data cannot verify a submission."""


def load_test_cases(raw_cases: Optional[str]) -> List[Dict[str, str]]:
    if not raw_cases:
        raise GradingConfigurationError("未配置自动判分测试用例")
    parsed = json.loads(raw_cases)
    if not isinstance(parsed, list) or not parsed:
        raise GradingConfigurationError("自动判分测试用例格式无效")
    for case in parsed:
        if not isinstance(case, dict) or "expected_output" not in case:
            raise GradingConfigurationError("自动判分测试用例格式无效")
    return parsed


def grade_code_against_cases(
    code: str,
    raw_cases: Optional[str],
    success_explanation: str,
) -> Dict[str, Any]:
    cases = load_test_cases(raw_cases)
    last_stdout = ""
    for case in cases:
        result = run_python_code(code, case.get("stdin", ""))
        last_stdout = result.stdout
        if result.exit_code != 0:
            return {
                "is_correct": False,
                "score": 0,
                "run_output": result.stdout,
                "run_error": result.stderr,
                "explanation": "代码运行出错，请根据报错继续修改。",
            }
        if result.stdout.strip() != case["expected_output"].strip():
            return {
                "is_correct": False,
                "score": 0,
                "run_output": result.stdout,
                "run_error": None,
                "explanation": "输出结果与要求不符，请检查程序逻辑。",
            }
    return {
        "is_correct": True,
        "score": 100,
        "run_output": last_stdout,
        "run_error": None,
        "explanation": success_explanation,
    }
```

- [ ] **Step 4: Route all exercise code types through the shared evaluator and normalize text answers**

Modify `backend/app/services/exercise_grader.py` so its public behaviors are:

```python
import json

from app.models.exercise import Exercise
from app.services.code_grader import grade_code_against_cases


def _normalize_judge_value(value: str) -> str:
    normalized = (value or "").strip().lower()
    truthy = {"a", "true", "对", "正确", "yes"}
    falsy = {"b", "false", "错", "错误", "no"}
    if normalized in truthy:
        return "true"
    if normalized in falsy:
        return "false"
    return normalized


def _accepted_text_answers(answer: str):
    text = answer or ""
    if text.lstrip().startswith("["):
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(value).strip() for value in parsed]
    return [text.strip()]


def grade_judge(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    is_correct = _normalize_judge_value(user_answer) == _normalize_judge_value(exercise.answer)
    return {"is_correct": is_correct, "score": 100 if is_correct else 0, "explanation": exercise.explanation}


def grade_fill_blank(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    is_correct = (user_answer or "").strip() in _accepted_text_answers(exercise.answer)
    return {"is_correct": is_correct, "score": 100 if is_correct else 0, "explanation": exercise.explanation}


def grade_code_fix(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    return grade_code_against_cases(user_code or user_answer or "", exercise.test_cases, exercise.explanation)


def grade_code_completion(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    return grade_code_against_cases(user_code or user_answer or "", exercise.test_cases, exercise.explanation)


def grade_programming(exercise: Exercise, _user_answer: str = None, user_code: str = None) -> dict:
    return grade_code_against_cases(user_code or "", exercise.test_cases, exercise.explanation)
```

Retain the existing `grade_exercise()` dispatch function and `grade_choice()` implementation.

- [ ] **Step 5: Isolate each executed program in a disposable working directory**

Modify `backend/app/services/code_runner.py` so `_run_subprocess()` writes and executes the script inside one `TemporaryDirectory` and supplies `cwd=run_dir` to `subprocess.run()`. Modify `_run_docker()` to use a disposable host directory for `code.py`, mount it read-only at `/sandbox/code.py`, and add `--tmpfs /work:rw,nosuid,size=1m`, `--workdir /work`; relative student file writes then succeed only for that run. Retain all timeout and resource-limit arguments.

- [ ] **Step 6: Run the contract tests to verify green**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest tests.test_exercise_grader -v
```

Expected: five tests PASS, including the repeated file-writing case.

- [ ] **Step 7: Commit only the grading service, runner, and tests**

```bash
git add backend/app/services/code_grader.py backend/app/services/code_runner.py backend/app/services/exercise_grader.py backend/tests/__init__.py backend/tests/test_exercise_grader.py
git commit -m "fix: establish deterministic exercise grading contract"
```

## Task 2: Author Complete Grading Content And Safe Database Synchronization

**Files:**
- Create: `backend/app/seed/data/grading_updates.py`
- Create: `backend/app/seed/sync_grading_data.py`
- Create: `backend/tests/test_grading_content.py`
- Modify: `backend/app/seed/init_db.py`

- [ ] **Step 1: Write failing tests requiring every authored code activity to be gradeable**

Create `backend/tests/test_grading_content.py`:

```python
import json
import unittest

from app.models.exercise import Exercise
from app.models.project import ProjectTask
from app.seed.data.exercises import ALL_EXERCISES
from app.seed.data.projects import ALL_PROJECTS
from app.seed.data.grading_updates import (
    apply_exercise_updates,
    apply_project_task_updates,
)
from app.services.exercise_grader import grade_exercise
from app.services.code_grader import grade_code_against_cases


class GradingContentTests(unittest.TestCase):
    def _exercise_from_authored(self, lesson_no, raw):
        fields = dict(raw)
        fields["test_cases"] = json.dumps(fields.get("test_cases"), ensure_ascii=False)
        return Exercise(lesson_id=lesson_no, **fields)

    def _task_from_authored(self, raw):
        fields = dict(raw)
        fields["test_cases"] = json.dumps(fields.get("test_cases"), ensure_ascii=False)
        return ProjectTask(project_id=1, **fields)

    def test_all_code_exercise_references_pass_and_pass_statement_fails(self):
        exercises = apply_exercise_updates(ALL_EXERCISES)
        for lesson_no, lesson_items in exercises.items():
            for raw in lesson_items:
                if raw["type"] not in {"code_fix", "code_completion", "programming"}:
                    continue
                item = self._exercise_from_authored(lesson_no, raw)
                reference = raw["reference_code"]
                self.assertTrue(grade_exercise(item, user_code=reference)["is_correct"], raw["title"])
                self.assertFalse(grade_exercise(item, user_code="pass")["is_correct"], raw["title"])

    def test_conflicting_fill_blanks_are_representable_in_the_ui(self):
        exercises = apply_exercise_updates(ALL_EXERCISES)
        command = exercises[2][3]
        sort_difference = exercises[12][0]
        tuple_item = exercises[13][1]
        self.assertEqual(json.loads(command["answer"]), ["python", "python3"])
        self.assertEqual(sort_difference["answer"], "原,新")
        self.assertIn("依次填写", sort_difference["description"])
        self.assertEqual(tuple_item["answer"], ",")

    def test_all_project_reference_solutions_pass_hidden_cases(self):
        projects = apply_project_task_updates(ALL_PROJECTS)
        for _, (_, tasks) in projects.items():
            for raw in tasks:
                item = self._task_from_authored(raw)
                result = grade_code_against_cases(
                    item.answer_code or "",
                    item.test_cases,
                    "ok",
                )
                self.assertTrue(result["is_correct"], raw["title"])
                self.assertFalse(
                    grade_code_against_cases("pass", item.test_cases, "ok")["is_correct"],
                    raw["title"],
                )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the new test to verify content support is absent**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest tests.test_grading_content -v
```

Expected: ERROR because `app.seed.data.grading_updates` does not exist.

- [ ] **Step 3: Create the grading overlay module**

Create `backend/app/seed/data/grading_updates.py`. Store each `expected_output` below as authored data; grading must never produce expected output by executing `answer_code` or `reference_code`.

```python
from copy import deepcopy


def _case(expected_output: str, stdin: str = ""):
    return [{"stdin": stdin, "expected_output": expected_output}]


def _code_patch(starter_code: str, reference_code: str, expected_output: str, stdin: str = ""):
    return {
        "starter_code": starter_code,
        "reference_code": reference_code,
        "test_cases": _case(expected_output, stdin),
    }


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
}

def apply_exercise_updates(all_exercises):
    updated = deepcopy(all_exercises)
    for lesson_items in updated.values():
        for item in lesson_items:
            patch = EXERCISE_UPDATES.get(item["title"])
            if patch:
                item.update(deepcopy(patch))
    return updated


def apply_project_task_updates(all_projects):
    updated = deepcopy(all_projects)
    for project_id, (project, tasks) in updated.items():
        for task in tasks:
            patch = PROJECT_TASK_UPDATES.get((project["order_index"], task["order_index"]))
            if patch:
                task.update(deepcopy(patch))
    return updated
```

Insert these eleven `code_fix` entries into `EXERCISE_UPDATES` by calling `_code_patch` with each row's starter, reference, output, and stdin values. Each `starter_code` is the complete `reference_code` after applying the stated single broken edit.

| Title | `reference_code` | Broken edit in `starter_code` | `expected_output` |
|---|---|---|---|
| 修复 print 语法错误 | `print("Hello, World!")` | Replace both ASCII parentheses with Chinese full-width parentheses. | `"Hello, World!\n"` |
| 修复 f-string 语法 | `name = "小明"\nage = 18\nprint(f"我叫{name}，今年{age}岁")` | Replace the last line with `print(f"我叫{name}，今年" + age + "岁")`. | `"我叫小明，今年18岁\n"` |
| 修复 if 判断条件 | `age = 18\nif age == 18:\n    print("成年")` | Replace `==` with `=`. | `"成年\n"` |
| 修复死循环 | `count = 1\nwhile count <= 5:\n    print(count)\n    count += 1` | Remove the final increment line. | `"1\n2\n3\n4\n5\n"` |
| 修复嵌套循环中的 break | `for i in range(1, 10):\n    for j in range(1, 10):\n        if i * j > 10:\n            break\n    if i * j > 10:\n        break\nprint(i, j)` | Remove the outer `if`/`break` pair. | `"3 4\n"` |
| 修复列表访问越界 | `nums = [10, 20, 30]\nprint(nums[-1])` | Replace `-1` with `3`. | `"30\n"` |
| 修复元组修改错误 | `colors = ("红", "绿", "蓝")\ncolors = ("黄",) + colors[1:]\nprint(colors)` | Replace the middle line with `colors[0] = "黄"`. | `"('黄', '绿', '蓝')\n"` |
| 修复字典遍历 | `student = {"name": "小明", "age": 18}\nfor k, v in student.items():\n    print(k, v)` | Replace the loop with `for k, v in student:` while retaining its print body. | `"name 小明\nage 18\n"` |
| 修复函数缩进错误 | `def hello():\n    print("Hello")\nhello()` | Remove indentation before `print`. | `"Hello\n"` |
| 修复 UnboundLocalError | `count = 0\ndef increment():\n    global count\n    count += 1\nincrement()\nprint(count)` | Remove the `global count` line. | `"1\n"` |
| 修复 import 错误 | `import random\nrandom.seed(1)\nprint(random.randint(1, 10))` | Replace `random.randint` with `randint`. | `"3\n"` |

Insert these sixteen `code_completion` entries. The full editor template is obtained by replacing the indicated span in `reference_code` with the stated instructional comment; it deliberately asks the learner to edit the complete program before submission.

| Title | `reference_code` | Replace in `starter_code` | `expected_output` |
|---|---|---|---|
| 补全第一个 Python 程序 | `print("我学会了！")` | Replace the line with `# 请写一行 print 输出指定文本`. | `"我学会了！\n"` |
| 交换两个变量的值 | `a = 1\nb = 2\na, b = b, a\nprint(a, b)` | Replace `a, b = b, a` with `# 请补全交换语句`. | `"2 1\n"` |
| 字符串去空格 | `text = "  hello  "\nresult = text.strip()\nprint(result)` | Replace `text.strip()` with `None  # 请补全去空格表达式`. | `"hello\n"` |
| 判断奇偶数 | `num = 8\nresult = num % 2 == 0\nprint(result)` | Replace `== 0` with `# 请补全比较表达式` and leave the assignment as an editable commented line. | `"True\n"` |
| 三目表达式 | `age = 18\nstatus = "成年" if age >= 18 else "未成年"\nprint(status)` | Replace the assignment with `# 请补全 status 的条件表达式`. | `"成年\n"` |
| 补全闰年判断条件 | `year = 2024\nis_leap = year % 4 == 0 and year % 100 != 0\nprint(is_leap)` | Replace the assignment with `# 请补全闰年判断表达式`. | `"True\n"` |
| 用 while 求 1 到 100 的和 | `total = 0\ni = 1\nwhile i <= 100:\n    total += i\n    i += 1\nprint(total)` | Replace the `while` block with `# 请补全 while 循环求和`. | `"5050\n"` |
| 九九乘法表内层循环 | `for i in range(1, 4):\n    for j in range(1, i + 1):\n        print(f"{j}x{i}={i*j}", end=" ")\n    print()` | Update the description to “输出九九乘法表的前三行”，then replace the inner `for` line with `# 请补全内层循环` plus its correctly indented body. | `"1x1=1 \n1x2=2 2x2=4 \n1x3=3 2x3=6 3x3=9 \n"` |
| 列表判空 | `items = []\nif not items:\n    print("为空")\nelse:\n    print("不为空")` | Update the description to ask for empty-list detection, then replace `not items` with `False  # 请补全条件`. | `"为空\n"` |
| 逆序列表 | `nums = [1, 2, 3]\nreversed_list = nums[::-1]\nprint(reversed_list)` | Replace `nums[::-1]` with `[]  # 请补全切片`. | `"[3, 2, 1]\n"` |
| 字典合并 | `d1 = {"a": 1}\nd2 = {"b": 2}\nmerged = d1 \| d2\nprint(merged)` | Replace `d1 \| d2` with `{ }  # 请补全合并表达式`. | `"{'a': 1, 'b': 2}\n"` |
| 统计单词频率 | `text = "a b a c b a"\nfreq = {}\nfor w in text.split():\n    freq[w] = freq.get(w, 0) + 1\nprint(freq)` | Replace `freq.get(w, 0)` with `0  # 请补全 get 调用`. | `"{'a': 3, 'b': 2, 'c': 1}\n"` |
| 补全 return 语句 | `def add(a, b):\n    return a + b\nprint(add(3, 5))` | Replace `return a + b` with `# 请补全返回语句`. | `"8\n"` |
| *args 收集多余参数 | `def sum_all(*nums):\n    return sum(nums)\nprint(sum_all(1, 2, 3))` | Replace `*nums` with `nums  # 请补全可变参数写法`. | `"6\n"` |
| 获取当前日期时间 | `from datetime import datetime\nnow = datetime.now()\nprint(isinstance(now, datetime))` | Replace `import` with `# 请补全导入关键字` and update the description to ask whether the imported value is a `datetime`. | `"True\n"` |
| 读取文件所有行 | `from io import StringIO\nf = StringIO("a\\nb\\n")\nlines = f.readlines()\nprint(lines)` | Update the description to use a simulated text file, then replace `readlines()` with `[]  # 请补全读取方法`. | `"['a\\n', 'b\\n']\n"` |

For every `programming` entry, retain the existing complete `starter_code` and use the current `answer` as `reference_code` unless the Notes column says otherwise. Insert the following literal test cases:

| Title | `stdin` | `expected_output` | Notes |
|---|---|---|---|
| 自我介绍程序 | `""` | `"我叫小明，今年18岁\n"` | Current answer. |
| 名字处理程序 | `""` | `"处理后的名字是：张三\n"` | Current answer. |
| 计算圆的面积 | `""` | `"圆的面积是：78.5\n"` | Current answer. |
| 成绩等级判断 | `""` | `"良好\n"` | Current answer. |
| 年龄范围判断 | `""` | `"在范围内\n"` | Current answer. |
| 倒计时程序 | `""` | `"10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n发射！\n"` | Current answer. |
| 求 1 到 100 之间的偶数和 | `""` | `"1-100偶数和：2550\n"` | Current answer. |
| 找质数 | `""` | `"是质数\n"` | Current answer. |
| 创建购物清单 | `""` | `"1. 牛奶\n2. 鸡蛋\n"` | Current answer. |
| 成绩分析器 | `""` | `"及格人数：6\n及格均分：82.7\n最高分：95，最低分：59\n"` | Current answer. |
| 元组解包练习 | `""` | `"坐标：(120, 350)\n交换后：(350, 120)\n"` | Current answer. |
| 通讯录小程序 | `"小明\n"` | `"请输入联系人姓名：小明 的电话：13800138000\n"` | Also add a second case: stdin `"小王\n"`, output `"请输入联系人姓名：未找到该联系人\n"`. |
| 学生成绩管理系统 | `""` | `"小明: 88分\n小红: 95分\n小刚: 72分\n小李: 85分\n平均分: 85.0\n最高分: 小红 (95分)\n"` | Current answer. |
| 自定义计算器函数 | `""` | `"BMI: 22.9\n"` | Current answer. |
| 温度转换器 | `""` | `"0°C = 32.0°F\n32°F = 0.0°C\n"` | Current answer. |
| sort 配合 lambda 排序 | `""` | `"小刚: 95分\n小明: 90分\n小红: 85分\n"` | Current answer. |
| 随机点名器 | `""` | `"今天被点到的是：李四\n"` | Insert `random.seed(1)` immediately after `import random` in both starter and reference code. |
| 综合：个人日记本（简化版） | `"今天学习了列表\nsave\nshow\nquit\n"` | `"写日记（输入 save 保存, show 查看, quit 退出）\n> > 已保存 1 条日记\n> 今天学习了列表\n\n> "` | Current answer; disposable code-runner directories keep `diary.txt` local to one run. |

Build `PROJECT_TASK_UPDATES` with all ten rows in this catalog. For project 2 only, insert `random.seed(1)` immediately after the existing `import random` in both its `starter_code` and `answer_code` before storing the patch.

| Project, task order | `stdin` | Exact `expected_output` |
|---|---|---|
| 个人信息卡片, 1 | `"小明\n18\nPython\n"` | `"请输入你的姓名：请输入你的年龄：请输入你的爱好：信息已收集！\n"` |
| 个人信息卡片, 2 | `""` | `"==================\n  个人名片\n==================\n"` |
| 个人信息卡片, 3 | `"小明\n18\nPython\n"` | `"请输入你的姓名：请输入你的年龄：请输入你的爱好：==============================\n  个人名片\n==============================\n姓名：小明\n年龄：18 岁\n爱好：Python\n==============================\n"` |
| 猜数字游戏, 1 | `""` | `"(调试) 秘密数字是：18\n"` |
| 猜数字游戏, 2 | `"18\n"` | `"你猜是多少：猜对了！\n"` |
| 猜数字游戏, 3 | `"1\n18\n"` | `"我想了一个 1-100 之间的数字，来猜猜看！\n你猜是多少：小了，再大一点\n你猜是多少：猜对了！你一共猜了 2 次\n"` |
| 猜数字游戏, 4 | `"1\n1\n9\n"` | `"===== 猜数字游戏 =====\n1. 简单 (1-50, 10次机会)\n2. 中等 (1-100, 7次机会)\n3. 困难 (1-200, 5次机会)\n请选择难度 (1/2/3): \n我想了一个 1-50 的数字，你有 10 次机会！\n第1次猜：小了\n第2次猜：\n🎉 猜对了！你用了 2 次\n"` |
| 待办事项管理器, 1 | `"5\n"` | `"===== 待办事项管理器 =====\n\n1. 查看事项\n2. 添加事项\n3. 标记完成\n4. 删除事项\n5. 退出\n请选择: 再见！\n"` |
| 待办事项管理器, 2 | `"2\n读书\n1\n5\n"` | `"\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: 输入事项：✅ 已添加：读书\n\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: [ ] 1. 读书\n\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: 再见！\n"` |
| 待办事项管理器, 3 | `"3\n1\n4\n1\n5\n"` | `"\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: [ ] 1. 测试事项\n输入要完成的事项编号：✅ 已标记完成：测试事项\n\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: [✓] 1. 测试事项\n输入要删除的事项编号：🗑 已删除：测试事项\n\n1. 查看  2. 添加  3. 完成  4. 删除  5. 退出\n请选择: 再见！\n"` |

- [ ] **Step 4: Make fresh seeding consume the overlays**

Modify the imports and dataset selection near the start of `seed()` in `backend/app/seed/init_db.py`:

```python
from app.seed.data.grading_updates import apply_exercise_updates, apply_project_task_updates

raw_exercises = ALL_EXERCISES
raw_projects = ALL_PROJECTS
all_exercises = apply_exercise_updates(raw_exercises)
all_projects = apply_project_task_updates(raw_projects)
```

Then replace lookup/iteration uses:

```python
lesson_exercises = all_exercises.get(i + 1, [])
for proj_id, (proj_data, tasks_data) in all_projects.items():
```

- [ ] **Step 5: Add an idempotent preservation-oriented sync command**

Create `backend/app/seed/sync_grading_data.py`:

```python
import json

from sqlmodel import Session, select

from app.database import engine
from app.models import Exercise, Lesson, Project, ProjectTask
from app.seed.data.exercises import ALL_EXERCISES
from app.seed.data.projects import ALL_PROJECTS
from app.seed.data.grading_updates import apply_exercise_updates, apply_project_task_updates


def sync_grading_data(session: Session) -> None:
    exercises = apply_exercise_updates(ALL_EXERCISES)
    for lesson_no, authored_items in exercises.items():
        lesson = session.exec(select(Lesson).where(Lesson.order_index == lesson_no)).first()
        if not lesson:
            continue
        stored_items = session.exec(
            select(Exercise).where(Exercise.lesson_id == lesson.id)
        ).all()
        by_title = {item.title: item for item in stored_items}
        for authored in authored_items:
            stored = by_title.get(authored["title"])
            if not stored:
                continue
            stored.answer = authored["answer"]
            stored.description = authored["description"]
            stored.explanation = authored["explanation"]
            stored.starter_code = authored.get("starter_code")
            stored.reference_code = authored.get("reference_code")
            stored.test_cases = json.dumps(authored.get("test_cases"), ensure_ascii=False) if authored.get("test_cases") else None

    projects = apply_project_task_updates(ALL_PROJECTS)
    for _, (authored_project, authored_tasks) in projects.items():
        project = session.exec(select(Project).where(Project.title == authored_project["title"])).first()
        if not project:
            continue
        stored_tasks = session.exec(
            select(ProjectTask).where(ProjectTask.project_id == project.id)
        ).all()
        by_order = {task.order_index: task for task in stored_tasks}
        for authored in authored_tasks:
            stored = by_order.get(authored["order_index"])
            if not stored:
                continue
            stored.description = authored["description"]
            stored.starter_code = authored.get("starter_code")
            stored.hint = authored.get("hint")
            stored.answer_code = authored.get("answer_code")
            stored.test_cases = json.dumps(authored.get("test_cases"), ensure_ascii=False) if authored.get("test_cases") else None
    session.commit()


def main() -> None:
    with Session(engine) as session:
        sync_grading_data(session)
    print("Grading content synchronized.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Expand tests to prove synchronization preserves user-owned rows**

Append to `backend/tests/test_grading_content.py` a temporary SQLite-engine test that inserts one lesson, one affected exercise, one project/task and one `UserExerciseAttempt`, runs `sync_grading_data(session)`, and asserts:

```python
self.assertEqual(session.exec(select(UserExerciseAttempt)).all()[0].score, 42)
self.assertTrue(session.get(Exercise, exercise.id).test_cases)
self.assertTrue(session.get(ProjectTask, task.id).test_cases)
```

Refactor `sync_grading_data` to accept its `Session` as shown above so the test never modifies `backend/pythoncoach.db`.

- [ ] **Step 7: Run grading-content and contract tests**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest tests.test_exercise_grader tests.test_grading_content -v
```

Expected: all tests PASS; output demonstrates all authored reference code passes and `pass` does not.

- [ ] **Step 8: Commit only seed/sync content and its tests**

```bash
git add backend/app/seed/data/grading_updates.py backend/app/seed/init_db.py backend/app/seed/sync_grading_data.py backend/tests/test_grading_content.py
git commit -m "fix: add verifiable grading content and sync workflow"
```

## Task 3: Hide Private Answers And Grade Project Submissions By Cases

**Files:**
- Create: `backend/tests/test_public_routes_and_projects.py`
- Modify: `backend/app/routers/exercises.py`
- Modify: `backend/app/routers/projects.py`

- [ ] **Step 1: Write failing route and project-grading tests**

Create `backend/tests/test_public_routes_and_projects.py` using a temporary SQLModel SQLite database:

```python
import json
import unittest

from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool

from app.models import Exercise, Project, ProjectTask, User
from app.routers.exercises import get_exercise, list_exercises
from app.routers.projects import (
    ProjectTaskSubmitRequest,
    get_project,
    list_project_tasks,
    submit_project_task,
)


class PublicPayloadTests(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        SQLModel.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def tearDown(self):
        self.session.close()

    def assert_private_fields_absent(self, payload, private_fields):
        fields = payload if isinstance(payload, dict) else payload.dict()
        for field in private_fields:
            self.assertNotIn(field, fields)

    def test_public_exercise_payload_omits_answers_and_hidden_cases(self):
        item = Exercise(
            lesson_id=1,
            type="programming",
            title="safe",
            description="",
            answer="secret",
            reference_code="secret-code",
            test_cases='[{"stdin": "", "expected_output": "secret"}]',
            starter_code="# editable",
            explanation="",
        )
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        detail = get_exercise(item.id, self.session)["data"]
        listed = list_exercises(item.lesson_id, self.session)["data"][0]
        self.assert_private_fields_absent(detail, {"answer", "reference_code", "test_cases"})
        self.assert_private_fields_absent(listed, {"answer", "reference_code", "test_cases"})
        self.assertEqual(detail["starter_code"], "# editable")

    def test_public_project_payload_omits_task_answer_and_hidden_cases(self):
        project = Project(title="p", difficulty="easy", category="basic")
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        task = ProjectTask(
            project_id=project.id,
            title="task",
            answer_code="secret",
            test_cases='[{"stdin": "", "expected_output": "ok"}]',
        )
        self.session.add(task)
        self.session.commit()
        detail = get_project(project.id, self.session)["data"]["tasks"][0]
        listed = list_project_tasks(project.id, self.session)["data"][0]
        self.assert_private_fields_absent(detail, {"answer_code", "test_cases"})
        self.assert_private_fields_absent(listed, {"answer_code", "test_cases"})

    def test_project_submission_uses_cases_without_running_reference_code(self):
        user = User(username="learner", email="learner@example.com", password_hash="hash")
        project = Project(title="graded", difficulty="easy", category="basic")
        self.session.add(user)
        self.session.add(project)
        self.session.commit()
        self.session.refresh(user)
        self.session.refresh(project)
        task = ProjectTask(
            project_id=project.id,
            title="case task",
            order_index=1,
            answer_code='raise RuntimeError("reference must not run")',
            test_cases=json.dumps([{"stdin": "x\n", "expected_output": "value=x\n"}]),
        )
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        result = submit_project_task(
            task.id,
            ProjectTaskSubmitRequest(code='value = input(); print(f"value={value}")'),
            user,
            self.session,
        )
        self.assertTrue(result["data"]["is_correct"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the route tests to prove answers currently leak**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest tests.test_public_routes_and_projects -v
```

Expected: the payload tests FAIL because current router functions return private fields, and the submission test FAILS because current grading executes the deliberately broken `answer_code`.

- [ ] **Step 3: Filter public exercise payloads and surface content errors**

Modify `backend/app/routers/exercises.py`:

```python
from fastapi import APIRouter, Depends, HTTPException
from app.services.code_grader import GradingConfigurationError


def _public_exercise(exercise: Exercise) -> dict:
    return exercise.dict(exclude={"answer", "reference_code", "test_cases"})


@router.get("/lessons/{lesson_id}/exercises")
def list_exercises(lesson_id: int, session: Session = Depends(get_session)):
    stmt = select(Exercise).where(Exercise.lesson_id == lesson_id).order_by(Exercise.id)
    return {"data": [_public_exercise(exercise) for exercise in session.exec(stmt).all()]}


@router.get("/exercises/{exercise_id}")
def get_exercise(exercise_id: int, session: Session = Depends(get_session)):
    exercise = session.get(Exercise, exercise_id)
    if not exercise:
        return {"error": {"code": "NOT_FOUND", "message": "Exercise not found"}}
    return {"data": _public_exercise(exercise)}
```

Wrap the `grade_exercise` call in `submit_exercise()`:

```python
try:
    result = grade_exercise(exercise, req.answer, req.code)
except GradingConfigurationError as exc:
    raise HTTPException(status_code=500, detail=str(exc))
```

- [ ] **Step 4: Filter project payloads and switch task submission to hidden cases**

Modify `backend/app/routers/projects.py` by removing `re` and `_mock_stdin_for_code`, importing `HTTPException`, `GradingConfigurationError`, and `grade_code_against_cases`, and adding:

```python
def _public_task(task: ProjectTask) -> dict:
    return task.dict(exclude={"answer_code", "test_cases"})
```

Use it from both public reads:

```python
return {"data": {**project.dict(), "tasks": [_public_task(task) for task in tasks]}}
return {"data": [_public_task(task) for task in tasks]}
```

Replace the task execution/comparison portion of `submit_project_task()`:

```python
try:
    grade = grade_code_against_cases(req.code, task.test_cases, "任务完成！")
except GradingConfigurationError as exc:
    raise HTTPException(status_code=500, detail=str(exc))

is_correct = grade["is_correct"]
submission = CodeSubmission(
    user_id=current_user.id,
    project_task_id=task_id,
    code=req.code,
    stdout=grade.get("run_output"),
    stderr=grade.get("run_error"),
    exit_code=0 if is_correct else 1,
    execution_time_ms=0,
)
```

Return the grade fields in the existing response shape:

```python
return {
    "data": {
        "is_correct": is_correct,
        "stdout": grade.get("run_output") or "",
        "stderr": grade.get("run_error") or "",
        "exit_code": 0 if is_correct else 1,
        "execution_time_ms": 0,
    }
}
```

- [ ] **Step 5: Run public route/project tests and the backend suite**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest discover -s tests -v
```

Expected: all tests PASS; route payload checks confirm secrets are absent.

- [ ] **Step 6: Commit the API and project grading boundary**

```bash
git add backend/app/routers/exercises.py backend/app/routers/projects.py backend/tests/test_public_routes_and_projects.py
git commit -m "fix: secure public exercise and project grading APIs"
```

## Task 4: Align Frontend Editing And Verification UI

**Files:**
- Modify: `frontend/app/project/[id]/page.tsx`
- Modify: `frontend/components/dashboard/RecentActivity.tsx`
- Verify: `frontend/app/exercise/[id]/page.tsx`

- [ ] **Step 1: Run the existing frontend type check to capture the red state**

Run:

```bash
cd frontend
./node_modules/.bin/tsc --noEmit --incremental false
```

Expected: FAIL with `components/dashboard/RecentActivity.tsx(67,75): error TS2538: Type 'undefined' cannot be used as an index type.`

- [ ] **Step 2: Remove the private answer field from the project client shape and enable multiline manual input**

Modify `frontend/app/project/[id]/page.tsx`:

```tsx
interface TaskData {
  id: number;
  project_id: number;
  title: string;
  description: string;
  starter_code: string | null;
  hint: string | null;
  order_index: number;
}
```

Replace the stdin control with:

```tsx
<textarea
  value={stdin}
  onChange={(e) => setStdin(e.target.value)}
  rows={3}
  placeholder={"标准输入（每个 input 一行）\n例如：小明\n18"}
  className="min-h-[4.5rem] flex-1 resize-y rounded border border-zinc-700 bg-zinc-800 px-2 py-1 font-mono text-xs text-zinc-300 focus:border-zinc-500 focus:outline-none"
/>
```

Use `items-start` instead of `items-center` for the toolbar container so the multiline field lays out correctly.

- [ ] **Step 3: Fix the strict optional-result narrowing blocker**

Modify `frontend/components/dashboard/RecentActivity.tsx` so the class lookup is narrowed on the same optional key:

```tsx
{ResultIcon && activity.result && (
  <ResultIcon className={`h-4 w-4 shrink-0 ${resultColors[activity.result]}`} />
)}
```

- [ ] **Step 4: Verify the exercise page already submits complete editor content**

Inspect `frontend/app/exercise/[id]/page.tsx` and retain the established code path:

```tsx
if (CODE_TYPES.includes(d.type)) {
  setCode(d.starter_code || "");
}
```

Confirm the submission handler still passes that entire editor value as the code submission:

```tsx
else if (CODE_TYPES.includes(exercise?.type || "")) userCode = code;
```

No modification is required unless implementation changed this path while integrating safe API output.

- [ ] **Step 5: Run TypeScript verification**

Run:

```bash
cd frontend
./node_modules/.bin/tsc --noEmit --incremental false
```

Expected: PASS with no TypeScript diagnostics.

- [ ] **Step 6: Commit frontend changes only**

```bash
git add frontend/app/project/'[id]'/page.tsx frontend/components/dashboard/RecentActivity.tsx
git commit -m "fix: support multiline project runs and restore type checks"
```

## Task 5: Verify In A Temporary Database, Then Synchronize The Local Data

**Files:**
- Verify: `backend/app/seed/sync_grading_data.py`
- Verify: `backend/pythoncoach.db` (local runtime data only; never commit)

- [ ] **Step 1: Run all backend regression tests and Python parsing checks**

Run:

```bash
cd backend
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m unittest discover -s tests -v
PYTHONDONTWRITEBYTECODE=1 ./venv/bin/python -B -c 'from pathlib import Path; files=list(Path("app").rglob("*.py")); [compile(p.read_text(encoding="utf-8"), str(p), "exec") for p in files]; print(f"parsed {len(files)} Python files")'
```

Expected: all backend tests PASS and all Python application files parse.

- [ ] **Step 2: Validate fresh seed data in an isolated temporary database**

Run with an isolated database URL:

```bash
cd backend
tmp_db="$(mktemp -t pythoncoach-grading-XXXXXX.db)"
DATABASE_URL="sqlite:///$tmp_db" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m app.seed.init_db
DATABASE_URL="sqlite:///$tmp_db" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m app.seed.sync_grading_data
sqlite3 "$tmp_db" "select count(*) from exercises where test_cases is not null; select count(*) from project_tasks where test_cases is not null;"
rm -f "$tmp_db"
```

Expected: seed and sync complete successfully; all 45 code exercises and all 10 project tasks report non-null test cases.

- [ ] **Step 3: Back up and synchronize the existing local backend database**

Run:

```bash
cd backend
cp pythoncoach.db "pythoncoach.db.before-grading-sync-20260527.bak"
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. ./venv/bin/python -B -m app.seed.sync_grading_data
sqlite3 pythoncoach.db "select count(*) from courses; select count(*) from lessons; select count(*) from exercises; select count(*) from projects; select count(*) from project_tasks;"
```

Expected counts remain `1`, `20`, `100`, `3`, `10`. The backup and database remain untracked local runtime files and must not be committed.

- [ ] **Step 4: Run the frontend type check**

Run:

```bash
cd frontend
./node_modules/.bin/tsc --noEmit --incremental false
```

Expected: PASS.

- [ ] **Step 5: Manually smoke-check the project editor when local servers are available**

Start existing backend and frontend development servers, open `/project/2` and `/project/3`, and verify that the standard-input area accepts multiple lines and manual runs display stdout/stderr. Submit reference-equivalent implementations for one guessing task and one todo task through authenticated UI and verify they are accepted.

- [ ] **Step 6: Inspect final Git state**

Run:

```bash
git status --short --branch
git log --oneline --decorate --max-count=8
```

Expected: implementation source/test commits are recorded; `.env`, database files, dependency trees and existing unrelated untracked files remain outside commits.
