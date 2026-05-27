import re

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select

from app.database import get_session
from app.models import Project, ProjectTask, CodeSubmission, UserProjectProgress
from app.models.user import User
from app.routers.auth import get_current_user
from app.services.code_runner import run_python_code

router = APIRouter()


def _mock_stdin_for_code(code: str) -> str:
    """生成模拟 stdin，数量等于代码中 input() 调用次数。"""
    count = len(re.findall(r"\binput\s*\(", code or ""))
    return "\n".join(["1"] * count) if count > 0 else ""


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
    return {"data": {**project.dict(), "tasks": tasks}}


@router.get("/projects/{project_id}/tasks")
def list_project_tasks(project_id: int, session: Session = Depends(get_session)):
    stmt = select(ProjectTask).where(ProjectTask.project_id == project_id).order_by(ProjectTask.order_index)
    tasks = session.exec(stmt).all()
    return {"data": tasks}


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

    mock_stdin = _mock_stdin_for_code(task.answer_code or "")
    user_result = run_python_code(req.code, stdin=mock_stdin)
    expected_result = run_python_code(task.answer_code or "", stdin=mock_stdin)

    is_correct = (
        user_result.exit_code == 0
        and expected_result.exit_code == 0
        and user_result.stdout.strip() == expected_result.stdout.strip()
    )

    submission = CodeSubmission(
        user_id=current_user.id,
        project_task_id=task_id,
        code=req.code,
        stdout=user_result.stdout,
        stderr=user_result.stderr,
        exit_code=user_result.exit_code,
        execution_time_ms=user_result.execution_time_ms,
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
            "stdout": user_result.stdout,
            "stderr": user_result.stderr,
            "exit_code": user_result.exit_code,
            "execution_time_ms": user_result.execution_time_ms,
        }
    }
