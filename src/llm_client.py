from openai import OpenAI
import time
from typing import Optional
from .config import settings

class OpenRouterClient:
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None, retries: int = 3):
        api_key = api_key or settings.openrouter_api_key
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not set in environment")
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=settings.api_base,
            default_headers={
                "HTTP-Referer": settings.site_url,
                "X-Title": settings.site_name,
            }
        )
        self.model = model or settings.model
        self.retries = retries

    def ask(self, messages, timeout: int = 30):
        """messages: list of message dicts compatible with ChatCompletion API"""
        backoff = 1
        for attempt in range(self.retries):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    timeout=timeout,
                )
                return resp.choices[0].message.content
            except Exception as e:
                if attempt + 1 == self.retries:
                    raise
                time.sleep(backoff)
                backoff *= 2
