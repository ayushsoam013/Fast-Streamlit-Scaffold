from google import genai
from google.genai import types
from typing import List, Optional, Dict, Any
from app.core.config import settings

class GeminiGenService:
    def __init__(self, model_name: Optional[str] = None):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model_name = model_name or settings.GEMINI_GEN_MODEL

    async def generate_content(self, prompt: str, config: Optional[Dict[str, Any]] = None) -> str:
        """
        Generates content based on a text prompt.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=config
        )
        return response.text

    async def chat(self, messages: List[Dict[str, str]], config: Optional[Dict[str, Any]] = None) -> str:
        """
        Simple chat interface wrapper.
        Expects messages in format: [{"role": "user", "parts": "..."}]
        """
        # Note: google.genai has specific message types. 
        # For simplicity, we'll convert simple dicts to Content objects if needed or use the client direct.
        # Here we use the simplified contents list approach.
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=messages,
            config=config
        )
        return response.text

    def health_check(self) -> bool:
        try:
            # Quick ping
            self.client.models.generate_content(
                model=self.model_name,
                contents="ping",
                config=types.GenerateContentConfig(max_output_tokens=1)
            )
            return True
        except Exception:
            return False

gemini_gen_service = GeminiGenService()
