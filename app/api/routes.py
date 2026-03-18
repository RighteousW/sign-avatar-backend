from fastapi import APIRouter
from app.models.schemas import TextRequest, ResponseModel
from app.services.translation import text_to_gloss
from fastapi import UploadFile, File
from app.services.vision import process_video
from app.db.fake_db import create_job, get_job, complete_job

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

@router.post("/predict/video")
async def predict_video(file: UploadFile = File(...)):
    contents = await file.read()

    result = process_video(file.filename)

    return {
        "filename": file.filename,
        "result": result
    }

@router.post("/predict/video-async")
async def predict_video_async(file: UploadFile = File(...)):
    job_id = create_job()

    # simulate processing
    complete_job(job_id)

    return {"job_id": job_id}


@router.get("/jobs/{job_id}")
def job_status(job_id: str):
    return get_job(job_id)