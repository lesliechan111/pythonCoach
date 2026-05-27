from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Exercise, UserExerciseAttempt, WrongQuestion
from app.models.user import User
from app.routers.auth import get_current_user
from app.schemas.exercise import ExerciseSubmitRequest
from app.services.code_grader import GradingConfigurationError
from app.services.exercise_grader import grade_exercise

router = APIRouter()

PRIVATE_FIELDS = {"answer", "reference_code", "test_cases"}


def _public_exercise(exercise: Exercise) -> dict:
    return exercise.model_dump(exclude=PRIVATE_FIELDS)


@router.get("/lessons/{lesson_id}/exercises")
def list_exercises(lesson_id: int, session: Session = Depends(get_session)):
    stmt = select(Exercise).where(Exercise.lesson_id == lesson_id).order_by(Exercise.id)
    exercises = session.exec(stmt).all()
    return {"data": [_public_exercise(ex) for ex in exercises]}


@router.get("/exercises/{exercise_id}")
def get_exercise(exercise_id: int, session: Session = Depends(get_session)):
    exercise = session.get(Exercise, exercise_id)
    if not exercise:
        return {"error": {"code": "NOT_FOUND", "message": "Exercise not found"}}
    return {"data": _public_exercise(exercise)}


@router.post("/exercises/{exercise_id}/submit")
def submit_exercise(
    exercise_id: int,
    req: ExerciseSubmitRequest,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    exercise = session.get(Exercise, exercise_id)
    if not exercise:
        return {"error": {"code": "NOT_FOUND", "message": "Exercise not found"}}

    try:
        result = grade_exercise(exercise, req.answer, req.code)
    except GradingConfigurationError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    attempt = UserExerciseAttempt(
        user_id=current_user.id,
        exercise_id=exercise_id,
        user_answer=req.answer,
        user_code=req.code,
        is_correct=result["is_correct"],
        score=result["score"],
        run_output=result.get("run_output"),
        run_error=result.get("run_error"),
    )
    session.add(attempt)

    if result["is_correct"]:
        stmt = select(WrongQuestion).where(
            WrongQuestion.user_id == current_user.id,
            WrongQuestion.exercise_id == exercise_id,
        )
        wq = session.exec(stmt).first()
        if wq:
            wq.mastered = True
            wq.updated_at = datetime.utcnow()
    else:
        stmt = select(WrongQuestion).where(
            WrongQuestion.user_id == current_user.id,
            WrongQuestion.exercise_id == exercise_id,
        )
        wq = session.exec(stmt).first()
        if wq:
            wq.wrong_count += 1
            wq.last_wrong_at = datetime.utcnow()
            wq.mastered = False
            wq.updated_at = datetime.utcnow()
        else:
            wq = WrongQuestion(
                user_id=current_user.id,
                exercise_id=exercise_id,
                wrong_count=1,
                last_wrong_at=datetime.utcnow(),
                mastered=False,
            )
            session.add(wq)

    session.commit()

    return {"data": result}


@router.get("/users/me/wrong-questions")
def list_wrong_questions(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    stmt = (
        select(WrongQuestion, Exercise)
        .join(Exercise, WrongQuestion.exercise_id == Exercise.id)
        .where(
            WrongQuestion.user_id == current_user.id,
            WrongQuestion.mastered == False,
        )
        .order_by(WrongQuestion.last_wrong_at.desc())
    )
    rows = session.exec(stmt).all()
    results = []
    for wq, exercise in rows:
        results.append({
            "id": wq.id,
            "exercise_id": exercise.id,
            "exercise_title": exercise.title,
            "exercise_type": exercise.type,
            "wrong_count": wq.wrong_count,
            "last_wrong_at": wq.last_wrong_at.isoformat(),
            "mastered": wq.mastered,
        })
    return {"data": results}
