from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///pythoncoach.db"
    redis_url: Optional[str] = None

    # JWT
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 10080  # 7 days

    # AI Provider
    ai_provider: str = "openai"  # openai, claude, etc.
    openai_api_key: Optional[str] = None
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-4o-mini"

    claude_api_key: Optional[str] = None
    claude_model: str = "claude-3-5-sonnet-20241022"

    # Code Runner
    code_runner_timeout_seconds: int = 5
    code_runner_memory_limit_mb: int = 128
    code_runner_cpu_limit: float = 0.5
    code_runner_use_docker: bool = False  # Set to True when Docker is available
    code_runner_image: str = "pythoncoach/code-runner:latest"

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()
