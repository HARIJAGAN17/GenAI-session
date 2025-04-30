from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment="gpt4o",  # or your deployment
    api_version="2024-02-15-preview",  # or your api version
   
)

user_Input = input("You: ")

prompt = ChatPromptTemplate(
    [
        ("system",("Hey please assist the user with this query.")),
        ("human",user_Input),
    ]
)

response = llm.invoke(prompt.format(user_input=user_Input))
print(response.content)