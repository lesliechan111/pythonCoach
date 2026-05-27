from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List, Dict, Any

from app.config import get_settings


class BaseAIProvider(ABC):
    @abstractmethod
    async def chat(self, messages: List[Dict[str, str]], context: Dict[str, Any] = None) -> str:
        """Send messages to AI and return reply text."""
        pass


class OpenAIProvider(BaseAIProvider):
    def __init__(self):
        self.settings = get_settings()
        import httpx
        self.client = httpx.AsyncClient(
            base_url=self.settings.openai_base_url,
            headers={"Authorization": f"Bearer {self.settings.openai_api_key}"},
            timeout=60.0,
        )

    async def chat(self, messages: List[Dict[str, str]], context: Dict[str, Any] = None) -> str:
        system_prompt = (
            "你是一个 Python 学习助手，专门帮助零基础用户学习 Python。\n"
            "教学原则：\n"
            "1. 使用小白能听懂的语言\n"
            "2. 先用生活例子解释，再给代码\n"
            "3. 每段代码都要逐行解释\n"
            "4. 不要一次讲太多\n"
            "5. 当用户代码报错时，先指出错误原因，再给修改后的代码\n"
            "6. 每次回答后给一个小练习\n"
            "7. 鼓励用户自己动手\n"
            "8. 如果用户完全不懂，要用非常简单的类比解释\n"
        )
        if context and context.get("lesson_title"):
            system_prompt += f"\n用户当前正在学习的课程是：{context['lesson_title']}"

        payload = {
            "model": self.settings.openai_model,
            "messages": [{"role": "system", "content": system_prompt}] + messages,
            "temperature": 0.7,
        }
        resp = await self.client.post("/chat/completions", json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]


class ClaudeProvider(BaseAIProvider):
    # TODO: implement Claude API integration
    async def chat(self, messages: List[Dict[str, str]], context: Dict[str, Any] = None) -> str:
        return "Claude provider not implemented yet."


@lru_cache
def get_ai_provider() -> BaseAIProvider:
    settings = get_settings()
    if settings.ai_provider in ("openai", "deepseek"):
        return OpenAIProvider()
    elif settings.ai_provider == "claude":
        return ClaudeProvider()
    raise ValueError(f"Unknown AI provider: {settings.ai_provider}")
