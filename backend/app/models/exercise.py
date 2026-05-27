from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Exercise(SQLModel, table=True):
    __tablename__ = "exercises"

    id: Optional[int] = Field(default=None, primary_key=True)
    lesson_id: int = Field(foreign_key="lessons.id")
    type: str = Field(max_length=20)  # choice, judge, fill_blank, code_completion, code_fix, programming
    title: str = Field(max_length=200)
    description: str = Field(default="")
    options: Optional[str] = Field(default=None)  # JSON string [{label, text}]
    answer: str = Field(max_length=500)
    explanation: str = Field(default="")
    starter_code: Optional[str] = Field(default=None)
    reference_code: Optional[str] = Field(default=None)
    test_cases: Optional[str] = Field(default=None)  # JSON string [{input, expected_output}]
    difficulty: str = Field(default="easy", max_length=20)
    tags: Optional[str] = Field(default="[]")  # JSON string
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    lesson: Optional["Lesson"] = Relationship(back_populates="exercises")
