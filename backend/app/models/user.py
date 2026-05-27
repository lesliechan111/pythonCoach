from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, max_length=50)
    email: str = Field(index=True, unique=True, max_length=100)
    password_hash: str = Field(max_length=255)
    avatar_url: Optional[str] = Field(default=None, max_length=255)
    learning_goal: str = Field(default="python_basic", max_length=50)
    level: str = Field(default="beginner", max_length=20)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    lesson_progress: List["UserLessonProgress"] = Relationship(back_populates="user")
    exercise_attempts: List["UserExerciseAttempt"] = Relationship(back_populates="user")
    project_progress: List["UserProjectProgress"] = Relationship(back_populates="user")
    code_submissions: List["CodeSubmission"] = Relationship(back_populates="user")
    wrong_questions: List["WrongQuestion"] = Relationship(back_populates="user")


class UserLessonProgress(SQLModel, table=True):
    __tablename__ = "user_lesson_progress"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    lesson_id: int = Field(foreign_key="lessons.id")
    status: str = Field(default="not_started", max_length=20)  # not_started, in_progress, completed
    progress_percent: int = Field(default=0)
    completed_at: Optional[datetime] = Field(default=None)
    last_studied_at: Optional[datetime] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="lesson_progress")


class UserExerciseAttempt(SQLModel, table=True):
    __tablename__ = "user_exercise_attempts"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    exercise_id: int = Field(foreign_key="exercises.id")
    user_answer: Optional[str] = Field(default=None, max_length=500)
    user_code: Optional[str] = Field(default=None)
    is_correct: Optional[bool] = Field(default=None)
    score: Optional[int] = Field(default=None)
    run_output: Optional[str] = Field(default=None)
    run_error: Optional[str] = Field(default=None)
    ai_feedback: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="exercise_attempts")


class UserProjectProgress(SQLModel, table=True):
    __tablename__ = "user_project_progress"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    project_id: int = Field(foreign_key="projects.id")
    current_task_id: Optional[int] = Field(default=None, foreign_key="project_tasks.id")
    status: str = Field(default="not_started", max_length=20)
    progress_percent: int = Field(default=0)
    completed_at: Optional[datetime] = Field(default=None)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="project_progress")


class WrongQuestion(SQLModel, table=True):
    __tablename__ = "wrong_questions"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    exercise_id: int = Field(foreign_key="exercises.id")
    wrong_count: int = Field(default=1)
    last_wrong_at: datetime = Field(default_factory=datetime.utcnow)
    mastered: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="wrong_questions")
