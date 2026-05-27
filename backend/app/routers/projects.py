from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select

from app.database import get_session
from app.models import Project, ProjectTask, CodeSubmission, UserProjectProgress
from app.models.user import User
from app.routers.auth import get_current_user
from app.services.code_grader import grade_code_against_cases, GradingConfigurationError

router = APIRouter()

TASK_PRIVATE_FIELDS = {"answer_code", "test_cases"}


def _public_task(task: ProjectTask) -> dict:
    return task.model_dump(exclude=TASK_PRIVATE_FIELDS)


class ProjectTaskSubmitRequest(BaseModel):
    code: str


@router.get("/projects")
def list_projects(session: Session = Depends(get_session)):
    stmt = select(Project).order_by(Project.order_index)
    projects = session.exec(stmt).all()
    return {"data": projects}


@router.get("/projects/{project_id}")
def get_project(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        return {"error": {"code": "NOT_FOUND", "message": "Project not found"}}
    tasks_stmt = select(ProjectTask).where(ProjectTask.project_id == project_id).order_by(ProjectTask.order_index)
    tasks = session.exec(tasks_stmt).all()
    return {"data": {**project.model_dump(), "tasks": [_public_task(task) for task in tasks]}}


@router.get("/projects/{project_id}/tasks")
def list_project_tasks(project_id: int, session: Session = Depends(get_session)):
    stmt = select(ProjectTask).where(ProjectTask.project_id == project_id).order_by(ProjectTask.order_index)
    tasks = session.exec(stmt).all()
    return {"data": [_public_task(task) for task in tasks]}


@router.post("/project-tasks/{task_id}/submit")
def submit_project_task(
    task_id: int,
    req: ProjectTaskSubmitRequest,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    task = session.get(ProjectTask, task_id)
    if not task:
        return {"error": {"code": "NOT_FOUND", "message": "Task not found"}}

    try:
        grade = grade_code_against_cases(req.code, task.test_cases, "任务完成！")
    except GradingConfigurationError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    is_correct = grade["is_correct"]
    submission = CodeSubmission(
        user_id=current_user.id,
        project_task_id=task_id,
        code=req.code,
        stdout=grade.get("run_output"),
        stderr=grade.get("run_error"),
        exit_code=0 if is_correct else 1,
        execution_time_ms=0,
    )
    session.add(submission)

    if is_correct:
        stmt = select(UserProjectProgress).where(
            UserProjectProgress.user_id == current_user.id,
            UserProjectProgress.project_id == task.project_id,
        )
        progress = session.exec(stmt).first()
        if not progress:
            progress = UserProjectProgress(
                user_id=current_user.id,
                project_id=task.project_id,
                current_task_id=task_id,
                status="in_progress",
                progress_percent=0,
            )
            session.add(progress)
        progress.current_task_id = task_id

        total_tasks = session.exec(
            select(ProjectTask).where(ProjectTask.project_id == task.project_id)
        ).all()
        completed_index = task.order_index
        progress.progress_percent = int((completed_index / len(total_tasks)) * 100)
        if completed_index >= len(total_tasks):
            progress.status = "completed"

    session.commit()

    return {
        "data": {
            "is_correct": is_correct,
            "stdout": grade.get("run_output") or "",
            "stderr": grade.get("run_error") or "",
            "exit_code": 0 if is_correct else 1,
            "execution_time_ms": 0,
        }
    }
