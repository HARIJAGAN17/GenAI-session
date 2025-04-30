from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment="gpt4o",
    api_version="2024-10-21",
)

def get_gpt_response(user_input: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Hey please assist the user with this query."),
        ("human", "{user_input}"),
    ])
    
    formatted_prompt = prompt.format(user_input=user_input)
    response = llm.invoke(formatted_prompt)
    return response.content
