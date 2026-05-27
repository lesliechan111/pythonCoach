from pydantic import BaseModel
from typing import List, Optional


class ExerciseOption(BaseModel):
    label: str
    text: str


class TestCase(BaseModel):
    stdin: str = ""
    expected_output: str


class ExerciseResponse(BaseModel):
    id: int
    lesson_id: int
    type: str
    title: str
    description: str
    options: Optional[List[ExerciseOption]]
    difficulty: str
    tags: Optional[List[str]]
    starter_code: Optional[str]
    is_completed: Optional[bool] = False

    class Config:
        from_attributes = True


class ExerciseSubmitRequest(BaseModel):
    answer: Optional[str] = None
    code: Optional[str] = None


class ExerciseSubmitResponse(BaseModel):
    is_correct: bool
    score: int
    run_output: Optional[str] = None
    run_error: Optional[str] = None
    explanation: Optional[str] = None
    ai_feedback: Optional[str] = None
