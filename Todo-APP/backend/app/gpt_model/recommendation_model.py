import os
from dotenv import load_dotenv
import dspy
from dspy import Signature, InputField, OutputField
# Load .env variables
load_dotenv()

# Set up LiteLLM Azure OpenAI config
os.environ["AZURE_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_OPENAI_API_VERSION")
os.environ["AZURE_DEPLOYMENT_NAME"] = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# ✅ The model string must be: 'azure/<deployment_name>'
lm = dspy.LM(model=f"azure/{os.getenv('AZURE_OPENAI_DEPLOYMENT')}")
dspy.configure(lm=lm)

# Define a signature
class GPTQuery(Signature):
    user_input = InputField(desc="The user's query")
    answer = OutputField(desc="The assistant's response")

llm_program = dspy.ChainOfThought(GPTQuery)

def get_gpt_response(user_input: str) -> str:
    result = llm_program(user_input=user_input)
    return result.answer

