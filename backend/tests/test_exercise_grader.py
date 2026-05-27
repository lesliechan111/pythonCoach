import json
import os
import tempfile
import unittest

from app.models.exercise import Exercise
from app.services.code_grader import GradingConfigurationError
from app.services.exercise_grader import grade_exercise


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
    def test_judge_answer_b_accepts_false_and_rejects_true(self):
        item = exercise(type="judge", answer="B")

        accepted = grade_exercise(item, user_answer="false")
        rejected = grade_exercise(item, user_answer="true")

        self.assertTrue(accepted["is_correct"])
        self.assertEqual(100, accepted["score"])
        self.assertFalse(rejected["is_correct"])
        self.assertEqual(0, rejected["score"])

    def test_fill_blank_answer_list_accepts_python3_and_rejects_py(self):
        item = exercise(type="fill_blank", answer='["python", "python3"]')

        accepted = grade_exercise(item, user_answer="python3")
        rejected = grade_exercise(item, user_answer="py")

        self.assertTrue(accepted["is_correct"])
        self.assertFalse(rejected["is_correct"])

    def test_code_exercise_missing_hidden_cases_raises(self):
        item = exercise(type="programming", answer="print('unused')")

        with self.assertRaises(GradingConfigurationError):
            grade_exercise(item, user_code="print('hello')")

    def test_code_exercise_checks_complete_submission_against_explicit_test_cases(self):
        item = exercise(
            type="code_completion",
            answer="print('wrong reference path')",
            starter_code="print('starter should not run')",
            test_cases=json.dumps(
                [
                    {"stdin": "Ada\n", "expected_output": "Hello, Ada!\n"},
                    {"stdin": "Linus\n", "expected_output": "Hello, Linus!\n"},
                ]
            ),
        )

        result = grade_exercise(
            item,
            user_code=(
                "name = input().strip()\n"
                "print(f'Hello, {name}!')\n"
            ),
        )

        self.assertTrue(result["is_correct"])
        self.assertEqual(100, result["score"])
        self.assertEqual("Hello, Linus!\n", result["run_output"])
        self.assertIsNone(result["run_error"])

    def test_each_code_test_case_gets_a_fresh_working_directory(self):
        item = exercise(
            type="programming",
            answer="unused",
            test_cases=json.dumps(
                [
                    {"expected_output": "False\n"},
                    {"expected_output": "False\n"},
                ]
            ),
        )

        result = grade_exercise(
            item,
            user_code=(
                "import os\n"
                "state_path = os.path.join(os.getcwd(), 'state.txt')\n"
                "print(os.path.exists(state_path))\n"
                "with open(state_path, 'w', encoding='utf-8') as handle:\n"
                "    handle.write('seen')\n"
            ),
        )

        self.assertTrue(result["is_correct"])
        self.assertEqual(100, result["score"])
        self.assertEqual("False\n", result["run_output"])


if __name__ == "__main__":
    unittest.main()
