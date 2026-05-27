import json

from sqlmodel import Session, select

from app.database import engine
from app.models import Exercise, Lesson, Project, ProjectTask
from app.seed.data.exercises import ALL_EXERCISES
from app.seed.data.grading_updates import (
    apply_exercise_updates,
    apply_project_task_updates,
)
from app.seed.data.projects import ALL_PROJECTS


def _dump_cases(cases):
    if cases is None:
        return None
    return json.dumps(cases, ensure_ascii=False)


def sync_grading_data(session: Session) -> None:
    exercises = apply_exercise_updates(ALL_EXERCISES)
    for lesson_no, authored_items in exercises.items():
        lesson = session.exec(
            select(Lesson).where(Lesson.order_index == lesson_no)
        ).first()
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
            stored.test_cases = _dump_cases(authored.get("test_cases"))

    projects = apply_project_task_updates(ALL_PROJECTS)
    for _project_no, (authored_project, authored_tasks) in projects.items():
        project = session.exec(
            select(Project).where(Project.title == authored_project["title"])
        ).first()
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
            stored.test_cases = _dump_cases(authored.get("test_cases"))

    session.commit()


def main() -> None:
    with Session(engine) as session:
        sync_grading_data(session)
    print("Grading content synchronized.")


if __name__ == "__main__":
    main()
