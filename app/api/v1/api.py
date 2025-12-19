from fastapi import APIRouter
from app.api.v1.endpoints import health, embeddings, items, generation

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(embeddings.router, prefix="/embeddings", tags=["embeddings"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(generation.router, prefix="/generation", tags=["generation"])
