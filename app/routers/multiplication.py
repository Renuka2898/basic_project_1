from fastapi import APIRouter

from app.schemas.multiplication import (
    MultiplicationRequest,
    MultiplicationResponse
)

from app.services.multiplication import multiply_numbers


router = APIRouter(
    prefix="/api",
    tags=["Multiplication"]
)


@router.post("/multiplication", response_model=MultiplicationResponse)
def multiplication(request: MultiplicationRequest):

    result = multiply_numbers(request.num1, request.num2)

    return MultiplicationResponse(
        num1=request.num1,
        num2=request.num2,
        result=result
    )