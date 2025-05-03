import re
from fastapi import APIRouter
from app.gpt_model.recommendation_model import get_gpt_response

router = APIRouter()

@router.get("/recommendation")
async def generate_recommendation():

    prompt = (
        "Give me a list of 20 daily tasks in the following format only, with no additional explanation or comments:\n"
        "1. Task one\n2. Task two\n...\n10. Task ten"
    )    
    response_text = get_gpt_response(prompt)
    
    # Regex pattern to extract each task from the numbered list
    pattern = r"\d+\.\s+(.*?)(?=\n\d+\.|\Z)"
    tasks = re.findall(pattern, response_text, re.DOTALL)

    return {"response": tasks}
