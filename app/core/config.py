import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Embeddings Optimization API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")  # local or prod

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_GEN_MODEL: str = os.getenv("GEMINI_GEN_MODEL", "gemini-2.0-flash")
    
    # Local Qdrant
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    
    # Prod Qdrant
    QDRANT_URL: Optional[str] = os.getenv("QDRANT_URL")
    QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY")

    class Config:
        case_sensitive = True

settings = Settings()
