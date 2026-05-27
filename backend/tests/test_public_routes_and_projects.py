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
        fields = payload if isinstance(payload, dict) else payload.model_dump()
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
