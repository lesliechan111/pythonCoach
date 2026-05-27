import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import Session

from app.database import get_session
from app.models.course import Lesson
from app.services.ai_provider import get_ai_provider

router = APIRouter()


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    lesson_id: Optional[int] = None
    history: List[ChatMessage] = []


class ExplainErrorRequest(BaseModel):
    code: str
    error: str
    lesson_id: Optional[int] = None


class ReviewCodeRequest(BaseModel):
    code: str
    lesson_id: Optional[int] = None
    exercise_id: Optional[int] = None


class GeneratePracticeRequest(BaseModel):
    lesson_id: int
    difficulty: str = "easy"
    count: int = 3


def _lesson_context(session: Session, lesson_id: Optional[int]) -> dict:
    if not lesson_id:
        return {}
    lesson = session.get(Lesson, lesson_id)
    if lesson:
        return {"lesson_title": lesson.title}
    return {}


@router.post("/chat")
async def chat(req: ChatRequest, session: Session = Depends(get_session)):
    try:
        provider = get_ai_provider()
        messages = [{"role": h.role, "content": h.content} for h in req.history]
        messages.append({"role": "user", "content": req.message})
        reply = await provider.chat(messages, _lesson_context(session, req.lesson_id))
        return {"data": {"reply": reply, "suggested_practice": None}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 服务暂时不可用：{str(e)}")


@router.post("/explain-error")
async def explain_error(req: ExplainErrorRequest, session: Session = Depends(get_session)):
    try:
        provider = get_ai_provider()
        prompt = (
            f"我写的 Python 代码报错了，请帮我用小白能听懂的语言解释。\n\n"
            f"我的代码：\n```python\n{req.code}\n```\n\n"
            f"报错信息：\n{req.error}\n\n"
            f"请告诉我：\n1. 这个错误是什么意思（用生活类比）\n"
            f"2. 为什么会出错\n3. 具体怎么改"
        )
        reply = await provider.chat(
            [{"role": "user", "content": prompt}],
            _lesson_context(session, req.lesson_id),
        )
        return {"data": {"reply": reply}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 服务暂时不可用：{str(e)}")


@router.post("/review-code")
async def review_code(req: ReviewCodeRequest, session: Session = Depends(get_session)):
    try:
        provider = get_ai_provider()
        prompt = (
            f"请帮我评审这段 Python 代码，我是一个初学者。\n\n"
            f"```python\n{req.code}\n```\n\n"
            f"请从以下方面点评：\n1. 代码写得好的地方（先鼓励我）\n"
            f"2. 可以改进的地方\n3. 具体的修改建议\n"
            f"用友好的语气，不要打击我的学习热情。"
        )
        reply = await provider.chat(
            [{"role": "user", "content": prompt}],
            _lesson_context(session, req.lesson_id),
        )
        return {"data": {"reply": reply}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 服务暂时不可用：{str(e)}")


@router.post("/generate-practice")
async def generate_practice(req: GeneratePracticeRequest, session: Session = Depends(get_session)):
    lesson = session.get(Lesson, req.lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="课程不存在")

    try:
        provider = get_ai_provider()
        prompt = (
            f"请根据以下课程内容，生成 {req.count} 道难度为「{req.difficulty}」的 Python 练习题。\n\n"
            f"课程标题：{lesson.title}\n"
            f"课程内容：{(lesson.content or '')[:2000]}\n\n"
            f"请返回 JSON 数组格式，每道题包含以下字段：\n"
            f'- title: 题目标题\n'
            f'- type: 题型（choice/judge/fill_blank/code_completion/code_fix/programming）\n'
            f'- description: 题目描述\n'
            f'- answer: 正确答案\n'
            f'- explanation: 答案解析\n'
            f'- options: 如果是选择题，提供选项数组 [{{"label": "A", "text": "..."}}]，其他题型省略\n\n'
            f"只返回 JSON 数组，不要其他内容。"
        )
        reply = await provider.chat(
            [{"role": "user", "content": prompt}],
            {"lesson_title": lesson.title},
        )

        exercises = []
        try:
            text = reply.strip()
            if text.startswith("```"):
                lines = text.split("\n")
                text = "\n".join(lines[1:]) if len(lines) > 1 else text
                if text.endswith("```"):
                    text = text[:-3]
            text = text.strip()
            parsed = json.loads(text)
            if isinstance(parsed, list):
                exercises = parsed
            elif isinstance(parsed, dict) and "exercises" in parsed:
                exercises = parsed["exercises"]
            else:
                exercises = [parsed]
        except (json.JSONDecodeError, Exception):
            exercises = [{
                "title": "AI 生成的练习题",
                "type": "programming",
                "description": reply,
                "answer": "",
                "explanation": "由 AI 生成",
            }]

        return {"data": {"exercises": exercises}}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI 服务暂时不可用：{str(e)}")
