from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(..., description="The first number to multiply")
    b: int = Field(..., description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two numbers and returns the result."
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        """Multiplies two numbers and returns the result."""
        return a * b


multiply_tool = MultiplyTool()
result = multiply_tool.invoke({"a": 6, "b": 7})
print(result)
print(multiply_tool.description)



