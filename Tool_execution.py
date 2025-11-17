from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()


hf_llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-genration",     
)


llm = ChatHuggingFace(llm=hf_llm)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

llm_with_tools = llm.bind_tools([multiply])

response = llm_with_tools.invoke("can you multiply 6 and 7 for me?")

multiply.invoke({'name':'multiply','args':{'a':6,'b':7}})

