from datetime import datetime
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class Course(SQLModel, table=True):
    __tablename__ = "courses"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: Optional[str] = Field(default=None)
    category: str = Field(max_length=50)
    level: str = Field(max_length=20)
    order_index: int = Field(default=0)
    estimated_minutes: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    lessons: List["Lesson"] = Relationship(back_populates="course")


class Lesson(SQLModel, table=True):
    __tablename__ = "lessons"

    id: Optional[int] = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="courses.id")
    title: str = Field(max_length=100)
    summary: Optional[str] = Field(default=None)
    objectives: Optional[str] = Field(default="[]")  # JSON string
    content: str = Field(default="")
    analogy: Optional[str] = Field(default=None)
    example_code: Optional[str] = Field(default=None)
    line_by_line_explanation: Optional[str] = Field(default="[]")  # JSON string
    common_errors: Optional[str] = Field(default="[]")  # JSON string
    order_index: int = Field(default=0)
    estimated_minutes: int = Field(default=15)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    course: Optional[Course] = Relationship(back_populates="lessons")
    exercises: List["Exercise"] = Relationship(back_populates="lesson")
