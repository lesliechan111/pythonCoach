"""
练习判题服务 - 根据题型分发到不同的判题逻辑
"""

from app.models.exercise import Exercise
from app.services.code_runner import run_python_code


def grade_exercise(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    """
    综合判题入口，根据题型分发。
    返回：{is_correct, score, run_output, run_error, explanation}
    """
    graders = {
        "choice": grade_choice,
        "judge": grade_judge,
        "fill_blank": grade_fill_blank,
        "code_fix": grade_code_fix,
        "code_completion": grade_code_completion,
        "programming": grade_programming,
    }

    grader = graders.get(exercise.type, grade_choice)
    return grader(exercise, user_answer, user_code)


def grade_choice(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    is_correct = user_answer.strip().upper() == exercise.answer.strip().upper()
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def grade_judge(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    normalized_answer = user_answer.strip().lower()
    normalized_expected = exercise.answer.strip().lower()
    true_vals = {"true", "对", "正确", "yes"}
    false_vals = {"false", "错", "错误", "no"}

    if normalized_answer in true_vals:
        normalized_answer = "true"
    elif normalized_answer in false_vals:
        normalized_answer = "false"

    is_correct = normalized_answer == normalized_expected
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def grade_fill_blank(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    is_correct = user_answer.strip() == exercise.answer.strip()
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def grade_code_fix(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    """
    代码纠错题：运行用户代码看是否有语法错误，并对比预期输出
    """
    code = user_code or user_answer or ""
    result = run_python_code(code)

    if result.exit_code != 0:
        return {
            "is_correct": False,
            "score": 0,
            "run_output": None,
            "run_error": result.stderr,
            "explanation": f"代码仍有错误：{result.stderr}",
        }

    expected = run_python_code(exercise.answer)
    is_correct = result.stdout.strip() == expected.stdout.strip()
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "run_output": result.stdout,
        "run_error": result.stderr,
        "explanation": exercise.explanation,
    }


def grade_code_completion(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    """
    代码补全题：将用户代码与 starter_code 拼接后运行
    """
    code = user_code or user_answer or ""
    full_code = (exercise.starter_code or "") + "\n" + code
    result = run_python_code(full_code)

    if result.exit_code != 0:
        return {
            "is_correct": False,
            "score": 0,
            "run_output": None,
            "run_error": result.stderr,
            "explanation": f"代码运行出错：{result.stderr}",
        }

    ref_result = run_python_code(
        (exercise.starter_code or "") + "\n" + exercise.answer
    )
    is_correct = result.stdout.strip() == ref_result.stdout.strip()
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "run_output": result.stdout,
        "run_error": result.stderr,
        "explanation": exercise.explanation,
    }


def grade_programming(exercise: Exercise, _user_answer: str = None, user_code: str = None) -> dict:
    """
    编程题：运行用户代码，逐个测试用例对比输出
    """
    code = user_code or ""
    import json

    test_cases = json.loads(exercise.test_cases or "[]") if exercise.test_cases else []

    if not test_cases:
        result = run_python_code(code)
        successful = result.exit_code == 0
        return {
            "is_correct": successful,
            "score": 100 if successful else 0,
            "run_output": result.stdout,
            "run_error": result.stderr,
            "explanation": exercise.explanation if successful else f"代码运行出错：{result.stderr}",
        }

    all_passed = True
    last_result = None
    for tc in test_cases:
        stdin = tc.get("stdin", "")
        expected = tc.get("expected_output", "")
        result = run_python_code(code, stdin)

        if result.exit_code != 0:
            return {
                "is_correct": False,
                "score": 0,
                "run_output": result.stdout,
                "run_error": result.stderr,
                "explanation": f"代码运行出错：{result.stderr}",
            }

        if result.stdout.strip() != expected.strip():
            all_passed = False
            last_result = result

    score = 100 if all_passed else max(0, 60)
    return {
        "is_correct": all_passed,
        "score": score,
        "run_output": last_result.stdout if last_result else None,
        "run_error": last_result.stderr if last_result else None,
        "explanation": exercise.explanation if all_passed else f"部分测试用例未通过，请检查代码逻辑",
    }
