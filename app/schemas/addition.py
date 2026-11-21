from pydantic import BaseModel


class AdditionRequest(BaseModel):
    num1: float
    num2: float


class AdditionResponse(BaseModel):
    num1: float
    num2: float
    result: float