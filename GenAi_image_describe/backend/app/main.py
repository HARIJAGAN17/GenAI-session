from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.gpt_model.gpt_route import router as image_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_route)
