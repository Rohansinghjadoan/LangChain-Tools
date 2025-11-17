from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel
from langchain.tools import tool



load_dotenv()

llm1= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm1)




@tool
def multiply(a:int,b:int) -> int:
    """Multiplies two numbers and returns the result."""
    return a * b




## tool binding
llm_with_tools=model.bind_tools([multiply])





