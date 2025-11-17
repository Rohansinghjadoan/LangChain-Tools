from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

# MUST USE chat-completion task
hf_llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="chat-completion",     # <-- FIXED
)

# Your version requires llm=
llm = ChatHuggingFace(llm=hf_llm)

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

llm_with_tools = llm.bind_tools([multiply])

response = llm_with_tools.invoke("can you multiply 6 and 7 for me?")
print(response)
