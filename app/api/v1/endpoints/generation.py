from fastapi import APIRouter, HTTPException
from app.models.dtos import GenerationRequest, GenerationResponse
from app.services.gemini_gen_service import GeminiGenService
from app.core.config import settings

router = APIRouter()

@router.post("/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest):
    """
    Generate content using Gemini generative models (e.g., Gemini 2.0 Flash).
    """
    try:
        # Use provided model or default from settings
        service = GeminiGenService(model_name=request.model)
        
        config = {
            "max_output_tokens": request.max_tokens,
            "temperature": request.temperature
        }
        
        text = await service.generate_content(request.prompt, config=config)
        return GenerationResponse(text=text, model=service.model_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
