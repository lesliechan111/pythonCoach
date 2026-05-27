from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class LessonResponse(BaseModel):
    id: int
    course_id: int
    title: str
    summary: Optional[str]
    objectives: Optional[List[str]]
    content: str
    analogy: Optional[str]
    example_code: Optional[str]
    line_by_line_explanation: Optional[List[dict]]
    common_errors: Optional[List[dict]]
    order_index: int
    estimated_minutes: int

    class Config:
        from_attributes = True


class CourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    category: str
    level: str
    order_index: int
    estimated_minutes: int

    class Config:
        from_attributes = True


class CourseDetailResponse(CourseResponse):
    lessons: List[LessonResponse]


class CompleteLessonResponse(BaseModel):
    progress_percent: int
    completed_at: datetime
