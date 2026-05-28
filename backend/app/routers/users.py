from datetime import date

from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from sqlalchemy import text

from app.database import get_session
from app.routers.auth import get_current_user
from app.models import (
    Course,
    Lesson,
    Exercise,
    Project,
    User,
    UserLessonProgress,
    UserExerciseAttempt,
    UserProjectProgress,
    WrongQuestion,
    CodeSubmission,
)

router = APIRouter()


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {"data": current_user}


@router.get("/me/dashboard")
def get_dashboard(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    uid = current_user.id

    total_lessons = session.exec(select(func.count(Lesson.id))).one()
    total_exercises = session.exec(select(func.count(Exercise.id))).one()
    total_projects = session.exec(select(func.count(Project.id))).one()

    completed_lessons = session.exec(
        select(func.count(UserLessonProgress.id)).where(
            UserLessonProgress.user_id == uid,
            UserLessonProgress.status == "completed",
        )
    ).one()

    completed_exercises = session.exec(
        select(func.count(func.distinct(UserExerciseAttempt.exercise_id))).where(
            UserExerciseAttempt.user_id == uid,
            UserExerciseAttempt.is_correct == True,
        )
    ).one()

    wrong_count = session.exec(
        select(func.count(WrongQuestion.id)).where(
            WrongQuestion.user_id == uid,
            WrongQuestion.mastered == False,
        )
    ).one()

    completed_projects = session.exec(
        select(func.count(UserProjectProgress.id)).where(
            UserProjectProgress.user_id == uid,
            UserProjectProgress.status == "completed",
        )
    ).one()

    total_attempts = session.exec(
        select(func.count(UserExerciseAttempt.id)).where(
            UserExerciseAttempt.user_id == uid,
        )
    ).one()

    correct_attempts = session.exec(
        select(func.count(UserExerciseAttempt.id)).where(
            UserExerciseAttempt.user_id == uid,
            UserExerciseAttempt.is_correct == True,
        )
    ).one()

    accuracy_rate = round(correct_attempts / total_attempts, 2) if total_attempts > 0 else 0.0

    study_days_result = session.exec(
        select(func.count(func.distinct(func.date(UserLessonProgress.updated_at)))).where(
            UserLessonProgress.user_id == uid,
        )
    ).one()

    last_completed = session.exec(
        select(UserLessonProgress)
        .where(UserLessonProgress.user_id == uid, UserLessonProgress.status == "completed")
        .order_by(UserLessonProgress.lesson_id.desc())
    ).first()

    continue_lesson_id = (last_completed.lesson_id + 1) if last_completed else 1
    if continue_lesson_id > total_lessons:
        continue_lesson_id = None

    activity_rows = session.execute(
        text("""
            SELECT 'lesson' AS type,
                   l.title AS title,
                   ulp.completed_at AS time,
                   NULL AS result,
                   ulp.id + 1000000 AS id
            FROM user_lesson_progress ulp
            JOIN lessons l ON l.id = ulp.lesson_id
            WHERE ulp.user_id = :uid AND ulp.status = 'completed'

            UNION ALL

            SELECT 'exercise' AS type,
                   e.title AS title,
                   uea.created_at AS time,
                   CASE WHEN uea.is_correct THEN 'success' ELSE 'fail' END AS result,
                   uea.id + 2000000 AS id
            FROM user_exercise_attempts uea
            JOIN exercises e ON e.id = uea.exercise_id
            WHERE uea.user_id = :uid

            UNION ALL

            SELECT 'project' AS type,
                   p.title AS title,
                   upp.updated_at AS time,
                   CASE WHEN upp.status = 'completed' THEN 'success' ELSE NULL END AS result,
                   upp.id + 3000000 AS id
            FROM user_project_progress upp
            JOIN projects p ON p.id = upp.project_id
            WHERE upp.user_id = :uid AND upp.status IN ('completed', 'in_progress')

            UNION ALL

            SELECT 'code' AS type,
                   COALESCE(e2.title, pt.title, l2.title, 'Code Run') AS title,
                   cs.created_at AS time,
                   CASE WHEN cs.exit_code = 0 THEN 'success' ELSE 'fail' END AS result,
                   cs.id + 4000000 AS id
            FROM code_submissions cs
            LEFT JOIN exercises e2 ON e2.id = cs.exercise_id
            LEFT JOIN project_tasks pt ON pt.id = cs.project_task_id
            LEFT JOIN lessons l2 ON l2.id = cs.lesson_id
            WHERE cs.user_id = :uid

            ORDER BY time DESC
            LIMIT 10
        """),
        {"uid": uid},
    ).fetchall()

    return {
        "data": {
            "welcome_message": f"欢迎回来，{current_user.username}！",
            "today_task": None,
            "stats": {
                "completed_lessons": completed_lessons,
                "total_lessons": total_lessons,
                "completed_exercises": completed_exercises,
                "total_exercises": total_exercises,
                "wrong_questions": wrong_count,
                "completed_projects": completed_projects,
                "total_projects": total_projects,
                "study_days": study_days_result,
                "accuracy_rate": accuracy_rate,
            },
            "recent_activities": [
                {
                    "id": row.id,
                    "type": row.type,
                    "title": row.title,
                    "result": row.result,
                    "time": row.time if isinstance(row.time, str) else (row.time.isoformat() if row.time else None),
                }
                for row in activity_rows
            ],
            "continue_lesson_id": continue_lesson_id,
        }
    }


@router.get("/me/progress")
def get_progress(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    uid = current_user.id
    courses = session.exec(select(Course)).all()

    course_progress = []
    for course in courses:
        lessons = session.exec(
            select(Lesson).where(Lesson.course_id == course.id).order_by(Lesson.order_index)
        ).all()

        progress_records = {
            p.lesson_id: p
            for p in session.exec(
                select(UserLessonProgress).where(
                    UserLessonProgress.user_id == uid,
                    UserLessonProgress.lesson_id.in_([l.id for l in lessons]),
                )
            ).all()
        }

        lesson_list = []
        for lesson in lessons:
            record = progress_records.get(lesson.id)
            lesson_list.append({
                "lesson_id": lesson.id,
                "title": lesson.title,
                "order_index": lesson.order_index,
                "status": record.status if record else "not_started",
                "completed_at": record.completed_at.isoformat() if record and record.completed_at else None,
            })

        completed = sum(1 for l in lesson_list if l["status"] == "completed")
        course_progress.append({
            "course_id": course.id,
            "course_title": course.title,
            "total_lessons": len(lessons),
            "completed_lessons": completed,
            "lessons": lesson_list,
        })

    return {"data": {"course_progress": course_progress}}


@router.get("/me/submissions")
def get_submissions(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    submissions = session.exec(
        select(CodeSubmission)
        .where(CodeSubmission.user_id == current_user.id)
        .order_by(CodeSubmission.created_at.desc())
        .limit(20)
    ).all()

    return {
        "data": [
            {
                "id": s.id,
                "code": s.code[:500],
                "language": s.language,
                "stdout": s.stdout,
                "stderr": s.stderr,
                "exit_code": s.exit_code,
                "execution_time_ms": s.execution_time_ms,
                "exercise_id": s.exercise_id,
                "lesson_id": s.lesson_id,
                "project_task_id": s.project_task_id,
                "created_at": s.created_at.isoformat(),
            }
            for s in submissions
        ]
    }
