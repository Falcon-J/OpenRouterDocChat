from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    model: str = os.getenv("OPENROUTER_MODEL", "mistralai/mistral-7b-instruct")
    api_base: str = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
    site_url: str = os.getenv("SITE_URL", "http://localhost")
    site_name: str = os.getenv("SITE_NAME", "OpenRouterDocChat")

settings = Settings()
