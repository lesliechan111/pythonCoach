from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: str = Field(default="")
    difficulty: str = Field(max_length=20)
    category: str = Field(max_length=50)
    estimated_minutes: int = Field(default=60)
    final_result: Optional[str] = Field(default=None)
    knowledge_points: Optional[str] = Field(default="[]")  # JSON string
    order_index: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    tasks: List["ProjectTask"] = Relationship(back_populates="project")


class ProjectTask(SQLModel, table=True):
    __tablename__ = "project_tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="projects.id")
    title: str = Field(max_length=100)
    description: str = Field(default="")
    starter_code: Optional[str] = Field(default=None)
    hint: Optional[str] = Field(default=None)
    answer_code: Optional[str] = Field(default=None)
    test_cases: Optional[str] = Field(default=None)  # JSON string
    order_index: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="tasks")
