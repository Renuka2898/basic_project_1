from pydantic import BaseModel


class MultiplicationRequest(BaseModel):
    num1: float
    num2: float


class MultiplicationResponse(BaseModel):
    num1: float
    num2: float
    result: float