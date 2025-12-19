from fastapi import APIRouter, HTTPException
from app.models.dtos import HealthResponse
from app.services.gemini_service import gemini_service
from app.repositories.qdrant_repo import qdrant_repo
from app.core.config import settings

router = APIRouter()

@router.get("/server", response_model=HealthResponse)
async def server_health():
    return HealthResponse(status="ok")

@router.get("/gemini", response_model=HealthResponse)
async def gemini_health():
    if gemini_service.health_check():
        return HealthResponse(status="ok")
    raise HTTPException(status_code=503, detail="Gemini service unavailable")

@router.get("/qdrant", response_model=HealthResponse)
async def qdrant_health():
    if qdrant_repo.health_check():
        return HealthResponse(status="ok", details={"environment": settings.ENVIRONMENT})
    raise HTTPException(status_code=503, detail="Qdrant service unavailable")

@router.get("/gemini-gen", response_model=HealthResponse)
async def gemini_gen_health():
    from app.services.gemini_gen_service import gemini_gen_service
    if gemini_gen_service.health_check():
        return HealthResponse(status="ok")
    raise HTTPException(status_code=503, detail="Gemini Generative service unavailable")
