from fastapi import APIRouter, File, UploadFile
from app.gpt_model.gpt import get_image_description

router = APIRouter()

@router.post("/describe-image")
async def describe_image(file: UploadFile = File(...)):
    image_data = await file.read()
    description = get_image_description(image_data)
    return {"description": description}
