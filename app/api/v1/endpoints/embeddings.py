from fastapi import APIRouter
from app.models.dtos import EmbeddingRequest, EmbeddingResponse, BatchEmbeddingRequest, BatchEmbeddingResponse
from app.services.gemini_service import gemini_service

router = APIRouter()

@router.post("/generate", response_model=EmbeddingResponse)
async def generate_embedding(request: EmbeddingRequest):
    vector = gemini_service.generate_embedding(request.text, request.dimension)
    return EmbeddingResponse(vector=vector)

@router.post("/generate/batch", response_model=BatchEmbeddingResponse)
async def generate_batch_embeddings(request: BatchEmbeddingRequest):
    vectors = gemini_service.generate_batch_embeddings(request.texts, request.dimension)
    return BatchEmbeddingResponse(vectors=vectors)
