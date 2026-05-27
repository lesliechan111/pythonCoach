import json

from app.services.code_runner import run_python_code


class GradingConfigurationError(ValueError):
    pass


def load_test_cases(raw_cases):
    if not raw_cases:
        raise GradingConfigurationError("Code exercises require test cases.")

    try:
        test_cases = json.loads(raw_cases)
    except json.JSONDecodeError as exc:
        raise GradingConfigurationError("Code exercises require valid test cases JSON.") from exc

    if not isinstance(test_cases, list) or not test_cases:
        raise GradingConfigurationError("Code exercises require at least one test case.")

    for case in test_cases:
        if not isinstance(case, dict):
            raise GradingConfigurationError("Each test case must be an object.")
        if "expected_output" not in case:
            raise GradingConfigurationError("Each test case must define expected_output.")
        if not isinstance(case["expected_output"], str):
            raise GradingConfigurationError("Each test case expected_output must be a string.")
        if "stdin" in case and not isinstance(case["stdin"], str):
            raise GradingConfigurationError("Each test case stdin must be a string when provided.")

    return test_cases


def grade_code_against_cases(code, raw_cases, success_explanation):
    test_cases = load_test_cases(raw_cases)
    last_stdout = None

    for case in test_cases:
        result = run_python_code(code, case.get("stdin", ""))
        last_stdout = result.stdout

        if result.exit_code != 0:
            return {
                "is_correct": False,
                "score": 0,
                "run_output": result.stdout,
                "run_error": result.stderr,
                "explanation": f"代码运行出错：{result.stderr}",
            }

        if result.stdout != case["expected_output"]:
            return {
                "is_correct": False,
                "score": 0,
                "run_output": result.stdout,
                "run_error": None,
                "explanation": "输出结果不正确，请检查代码逻辑。",
            }

    return {
        "is_correct": True,
        "score": 100,
        "run_output": last_stdout,
        "run_error": None,
        "explanation": success_explanation,
    }
