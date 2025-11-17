# csutom tools
from langchain.tools import tool

@tool 
def add(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    return a * b
class MathToolkit:
    def get_tools(self):
        return [add, multiply]
toolkit = MathToolkit()
tools = toolkit.get_tools()
for tool in tools:
    print(f"Tool Name: {tool.name}")
    print(f"Description: {tool.description}")
    result = tool.invoke({"a": 6, "b": 7})
    print(f"Result of invoking {tool.name} with a=6 and b=7: {result}\n")
    
    