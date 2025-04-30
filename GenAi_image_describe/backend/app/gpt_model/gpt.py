# backend/app/gpt_model/recommendation_model.py

from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from PIL import Image
import io
import base64

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment="gpt4o",
    api_version="2024-10-21",
)

def get_image_description(image_data: bytes) -> str:
    prompt = [
        ("system", "Describe the image provided by the user."),
        HumanMessage(
            content=[
                {"type": "text", "text": "Please describe this image in detail."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}"}}
            ]
        )
    ]

    response = llm.invoke(prompt)
    return response.content
