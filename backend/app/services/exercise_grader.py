"""
练习判题服务 - 根据题型分发到不同的判题逻辑
"""

import json

from app.models.exercise import Exercise
from app.services.code_grader import grade_code_against_cases


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
    is_correct = (user_answer or "").strip().upper() == exercise.answer.strip().upper()
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def _normalize_judge_value(value: str) -> str:
    normalized = (value or "").strip().lower()
    true_vals = {"a", "true", "对", "正确", "yes"}
    false_vals = {"b", "false", "错", "错误", "no"}

    if normalized in true_vals:
        return "true"
    if normalized in false_vals:
        return "false"
    return normalized


def _accepted_text_answers(raw_answer: str) -> list:
    answer = raw_answer or ""

    try:
        parsed = json.loads(answer)
    except json.JSONDecodeError:
        return [answer]

    if isinstance(parsed, list):
        return [str(item) for item in parsed]
    if isinstance(parsed, str):
        return [parsed]
    return [answer]


def grade_judge(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    normalized_answer = _normalize_judge_value(user_answer)
    normalized_expected = _normalize_judge_value(exercise.answer)
    is_correct = normalized_answer == normalized_expected
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def grade_fill_blank(exercise: Exercise, user_answer: str, _user_code: str = None) -> dict:
    is_correct = (user_answer or "").strip() in {
        answer.strip() for answer in _accepted_text_answers(exercise.answer)
    }
    return {
        "is_correct": is_correct,
        "score": 100 if is_correct else 0,
        "explanation": exercise.explanation,
    }


def grade_code_fix(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    code = user_code or user_answer or ""
    return grade_code_against_cases(code, exercise.test_cases, exercise.explanation)


def grade_code_completion(exercise: Exercise, user_answer: str = None, user_code: str = None) -> dict:
    code = user_code or user_answer or ""
    return grade_code_against_cases(code, exercise.test_cases, exercise.explanation)


def grade_programming(exercise: Exercise, _user_answer: str = None, user_code: str = None) -> dict:
    code = user_code or ""
    return grade_code_against_cases(code, exercise.test_cases, exercise.explanation)
