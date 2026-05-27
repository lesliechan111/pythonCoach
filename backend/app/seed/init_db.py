"""
数据库初始化脚本 - 写入种子数据
使用方式: python -m app.seed.init_db
"""

import json
from app.database import engine, create_db_and_tables, Session
from app.models import Course, Lesson, Exercise, Project, ProjectTask


def seed():
    create_db_and_tables()

    from app.seed.data.courses import COURSE, LESSONS
    from app.seed.data.exercises import ALL_EXERCISES
    from app.seed.data.grading_updates import (
        apply_exercise_updates,
        apply_project_task_updates,
    )
    from app.seed.data.projects import ALL_PROJECTS

    all_exercises = apply_exercise_updates(ALL_EXERCISES)
    all_projects = apply_project_task_updates(ALL_PROJECTS)

    with Session(engine) as session:
        # Check if already seeded
        from sqlmodel import select
        if session.exec(select(Course)).first():
            print("Database already seeded, skipping.")
            return

        # 1. Create course
        course = Course(**COURSE)
        session.add(course)
        session.flush()

        # 2. Create lessons
        for i, lesson_data in enumerate(LESSONS):
            lesson = Lesson(
                course_id=course.id,
                objectives=json.dumps(lesson_data["objectives"], ensure_ascii=False),
                line_by_line_explanation=json.dumps(
                    lesson_data["line_by_line_explanation"], ensure_ascii=False
                ),
                common_errors=json.dumps(
                    lesson_data.get("common_errors", []), ensure_ascii=False
                ),
                **{
                    k: v
                    for k, v in lesson_data.items()
                    if k
                    not in (
                        "objectives",
                        "line_by_line_explanation",
                        "common_errors",
                    )
                },
            )
            session.add(lesson)
            session.flush()

            # 3. Create exercises for each lesson
            lesson_exercises = all_exercises.get(i + 1, [])
            for ex_data in lesson_exercises:
                exercise = Exercise(
                    lesson_id=lesson.id,
                    options=(
                        json.dumps(ex_data["options"], ensure_ascii=False)
                        if ex_data.get("options")
                        else None
                    ),
                    test_cases=(
                        json.dumps(ex_data["test_cases"], ensure_ascii=False)
                        if ex_data.get("test_cases")
                        else None
                    ),
                    tags=(
                        json.dumps(ex_data.get("tags", []), ensure_ascii=False)
                        if ex_data.get("tags")
                        else None
                    ),
                    starter_code=ex_data.get("starter_code"),
                    reference_code=ex_data.get("reference_code"),
                    **{
                        k: v
                        for k, v in ex_data.items()
                        if k not in ("options", "test_cases", "tags", "starter_code", "reference_code")
                    },
                )
                session.add(exercise)

        # 4. Create project
        for proj_id, (proj_data, tasks_data) in all_projects.items():
            project = Project(
                knowledge_points=json.dumps(
                    proj_data["knowledge_points"], ensure_ascii=False
                ),
                **{
                    k: v
                    for k, v in proj_data.items()
                    if k != "knowledge_points"
                },
            )
            session.add(project)
            session.flush()

            for task_data in tasks_data:
                task = ProjectTask(
                    project_id=project.id,
                    test_cases=(
                        json.dumps(task_data["test_cases"], ensure_ascii=False)
                        if task_data.get("test_cases")
                        else None
                    ),
                    **{
                        k: v
                        for k, v in task_data.items()
                        if k != "test_cases"
                    },
                )
                session.add(task)

        session.commit()
        print("Database seeded successfully.")


if __name__ == "__main__":
    seed()
