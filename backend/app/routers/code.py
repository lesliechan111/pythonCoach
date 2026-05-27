from fastapi import APIRouter
from pydantic import BaseModel

from app.services.code_runner import run_python_code

router = APIRouter()


class RunCodeRequest(BaseModel):
    language: str = "python"
    code: str
    stdin: str = ""


class RunCodeResponse(BaseModel):
    stdout: str
    stderr: str
    exit_code: int
    execution_time_ms: int


@router.post("/code/run", response_model=RunCodeResponse)
def run_code(req: RunCodeRequest):
    result = run_python_code(req.code, req.stdin)
    return result
