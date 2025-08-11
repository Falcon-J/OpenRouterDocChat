from .llm_client import OpenRouterClient
from typing import Optional

class DocChat:
    def __init__(self, client: OpenRouterClient, system_preamble: Optional[str] = None):
        self.client = client
        self.system_preamble = system_preamble or "You are a helpful assistant. Use the provided document context to answer questions."

    def build_system_message_with_doc(self, doc_text: str, max_len: int = 6000) -> str:
        """Build a system prompt embedding the doc or first chunk. Keep it short for context window safety."""
        text = doc_text if len(doc_text) <= max_len else doc_text[:max_len]
        return f"{self.system_preamble}\n\nDocument:\n{text}"

    def ask_with_doc(self, doc_text: str, user_query: str):
        system_msg = self.build_system_message_with_doc(doc_text)
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_query},
        ]
        return self.client.ask(messages)

    def ask_simple(self, user_query: str):
        messages = [
            {"role": "system", "content": self.system_preamble},
            {"role": "user", "content": user_query},
        ]
        return self.client.ask(messages)
