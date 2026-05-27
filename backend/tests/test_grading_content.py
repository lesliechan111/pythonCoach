import json
import unittest

from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.pool import StaticPool

from app.models import (
    Course,
    Exercise,
    Lesson,
    Project,
    ProjectTask,
    User,
    UserExerciseAttempt,
)
from app.seed.data.exercises import ALL_EXERCISES
from app.seed.data.grading_updates import (
    apply_exercise_updates,
    apply_project_task_updates,
)
from app.seed.data.projects import ALL_PROJECTS
from app.seed.sync_grading_data import sync_grading_data
from app.services.code_grader import grade_code_against_cases
from app.services.exercise_grader import grade_exercise


def build_exercise(raw):
    return Exercise(
        lesson_id=1,
        type=raw["type"],
        title=raw["title"],
        description=raw.get("description", ""),
        answer=raw.get("answer", ""),
        explanation=raw.get("explanation", ""),
        starter_code=raw.get("starter_code"),
        reference_code=raw.get("reference_code"),
        test_cases=(
            json.dumps(raw["test_cases"], ensure_ascii=False)
            if raw.get("test_cases") is not None
            else None
        ),
        difficulty=raw.get("difficulty", "easy"),
        tags=json.dumps(raw.get("tags", []), ensure_ascii=False),
    )


def build_project_task(raw):
    return ProjectTask(
        project_id=1,
        title=raw["title"],
        description=raw.get("description", ""),
        starter_code=raw.get("starter_code"),
        hint=raw.get("hint"),
        answer_code=raw.get("answer_code"),
        test_cases=(
            json.dumps(raw["test_cases"], ensure_ascii=False)
            if raw.get("test_cases") is not None
            else None
        ),
        order_index=raw.get("order_index", 0),
    )


class GradingContentTests(unittest.TestCase):
    def test_all_code_exercise_references_pass_and_pass_statement_fails(self):
        exercises = apply_exercise_updates(ALL_EXERCISES)

        for lesson_items in exercises.values():
            for raw in lesson_items:
                if raw["type"] not in {"code_fix", "code_completion", "programming"}:
                    continue

                item = build_exercise(raw)

                with self.subTest(title=raw["title"], case="reference"):
                    result = grade_exercise(item, user_code=raw["reference_code"])
                    self.assertTrue(result["is_correct"])

                with self.subTest(title=raw["title"], case="pass"):
                    result = grade_exercise(item, user_code="pass")
                    self.assertFalse(result["is_correct"])

    def test_conflicting_fill_blanks_are_representable_in_the_ui(self):
        exercises = apply_exercise_updates(ALL_EXERCISES)
        by_title = {
            item["title"]: item
            for lesson_items in exercises.values()
            for item in lesson_items
        }

        self.assertEqual(
            ["python", "python3"],
            json.loads(by_title["运行 Python 程序的命令"]["answer"]),
        )
        self.assertEqual(
            "原,新",
            by_title["sort() 和 sorted() 的区别"]["answer"],
        )
        self.assertIn(
            "依次填写",
            by_title["sort() 和 sorted() 的区别"]["description"],
        )
        self.assertEqual(",", by_title["单元素元组的写法"]["answer"])

    def test_all_project_reference_solutions_pass_hidden_cases(self):
        projects = apply_project_task_updates(ALL_PROJECTS)

        for _project_order, (_project, tasks) in projects.items():
            for raw in tasks:
                item = build_project_task(raw)

                with self.subTest(title=raw["title"], case="reference"):
                    result = grade_code_against_cases(
                        item.answer_code,
                        item.test_cases,
                        "ok",
                    )
                    self.assertTrue(result["is_correct"])

                with self.subTest(title=raw["title"], case="pass"):
                    result = grade_code_against_cases("pass", item.test_cases, "ok")
                    self.assertFalse(result["is_correct"])

    def test_sync_grading_data_preserves_user_rows_and_adds_hidden_cases(self):
        engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            course = Course(
                title="Course",
                description="desc",
                category="python_basic",
                level="beginner",
                order_index=1,
                estimated_minutes=10,
            )
            session.add(course)
            session.flush()

            lesson = Lesson(
                course_id=course.id,
                title="Lesson 2",
                summary="summary",
                objectives="[]",
                content="content",
                line_by_line_explanation="[]",
                common_errors="[]",
                order_index=2,
                estimated_minutes=10,
            )
            session.add(lesson)
            session.flush()

            exercise = Exercise(
                lesson_id=lesson.id,
                type="code_fix",
                title="修复 print 语法错误",
                description="stale description",
                answer="stale answer",
                explanation="stale explanation",
                starter_code="print（\"Hello, World!\"）",
                reference_code=None,
                test_cases=None,
                difficulty="easy",
                tags="[]",
            )
            session.add(exercise)

            project = Project(
                title="个人信息卡片",
                description="stale project",
                difficulty="beginner",
                category="python_basic",
                estimated_minutes=30,
                final_result="",
                knowledge_points="[]",
                order_index=1,
            )
            session.add(project)
            session.flush()

            task = ProjectTask(
                project_id=project.id,
                title="任务 1：获取用户信息",
                description="stale task",
                starter_code="# stale",
                hint="stale hint",
                answer_code="pass",
                test_cases=None,
                order_index=1,
            )
            session.add(task)

            user = User(
                username="alice",
                email="alice@example.com",
                password_hash="hash",
            )
            session.add(user)
            session.flush()

            attempt = UserExerciseAttempt(
                user_id=user.id,
                exercise_id=exercise.id,
                user_answer=None,
                user_code="print('mine')",
                is_correct=False,
                score=37,
                run_output="mine",
                run_error=None,
                ai_feedback="feedback",
            )
            session.add(attempt)
            session.commit()

            sync_grading_data(session)

            refreshed_attempt = session.exec(
                select(UserExerciseAttempt).where(UserExerciseAttempt.id == attempt.id)
            ).one()
            refreshed_exercise = session.exec(
                select(Exercise).where(Exercise.id == exercise.id)
            ).one()
            refreshed_task = session.exec(
                select(ProjectTask).where(ProjectTask.id == task.id)
            ).one()

            self.assertEqual(37, refreshed_attempt.score)
            self.assertIsNotNone(refreshed_exercise.test_cases)
            self.assertIsNotNone(refreshed_exercise.reference_code)
            self.assertIsNotNone(refreshed_task.test_cases)
            self.assertIn("请输入你的姓名", refreshed_task.answer_code)


if __name__ == "__main__":
    unittest.main()
