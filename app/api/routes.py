from fastapi import APIRouter
from app.models.schemas import TextRequest, ResponseModel
from app.services.translation import text_to_gloss

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API is running"}

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/translate/text-to-gloss", response_model=ResponseModel)
def translate_text(request: TextRequest):
    result = text_to_gloss(request.text)
    return {"result": result}