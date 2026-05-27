from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class CodeSubmission(SQLModel, table=True):
    __tablename__ = "code_submissions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    lesson_id: Optional[int] = Field(default=None, foreign_key="lessons.id")
    exercise_id: Optional[int] = Field(default=None, foreign_key="exercises.id")
    project_task_id: Optional[int] = Field(default=None, foreign_key="project_tasks.id")
    code: str = Field(default="")
    language: str = Field(default="python", max_length=20)
    stdout: Optional[str] = Field(default=None)
    stderr: Optional[str] = Field(default=None)
    exit_code: Optional[int] = Field(default=None)
    execution_time_ms: Optional[int] = Field(default=None)
    ai_feedback: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["User"] = Relationship(back_populates="code_submissions")
