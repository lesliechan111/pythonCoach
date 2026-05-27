from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import Course, Lesson, UserLessonProgress
from app.models.user import User
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("/courses")
def list_courses(category: Optional[str] = None, session: Session = Depends(get_session)):
    stmt = select(Course)
    if category:
        stmt = stmt.where(Course.category == category)
    stmt = stmt.order_by(Course.order_index)
    courses = session.exec(stmt).all()
    return {"data": courses}


@router.get("/courses/{course_id}")
def get_course(course_id: int, session: Session = Depends(get_session)):
    course = session.get(Course, course_id)
    if not course:
        return {"error": {"code": "NOT_FOUND", "message": "Course not found"}}
    lessons_stmt = select(Lesson).where(Lesson.course_id == course_id).order_by(Lesson.order_index)
    lessons = session.exec(lessons_stmt).all()
    return {"data": {**course.dict(), "lessons": lessons}}


@router.get("/lessons/{lesson_id}")
def get_lesson(lesson_id: int, session: Session = Depends(get_session)):
    lesson = session.get(Lesson, lesson_id)
    if not lesson:
        return {"error": {"code": "NOT_FOUND", "message": "Lesson not found"}}
    return {"data": lesson}


@router.post("/lessons/{lesson_id}/complete")
def complete_lesson(
    lesson_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    lesson = session.get(Lesson, lesson_id)
    if not lesson:
        return {"error": {"code": "NOT_FOUND", "message": "Lesson not found"}}

    stmt = select(UserLessonProgress).where(
        UserLessonProgress.user_id == current_user.id,
        UserLessonProgress.lesson_id == lesson_id,
    )
    progress = session.exec(stmt).first()

    now = datetime.utcnow()
    if progress:
        progress.status = "completed"
        progress.progress_percent = 100
        progress.completed_at = now
        progress.last_studied_at = now
        progress.updated_at = now
    else:
        progress = UserLessonProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            status="completed",
            progress_percent=100,
            completed_at=now,
            last_studied_at=now,
        )
        session.add(progress)

    session.commit()
    return {
        "data": {
            "progress_percent": 100,
            "completed_at": now.isoformat(),
        }
    }
