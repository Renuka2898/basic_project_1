from fastapi import APIRouter

from app.schemas.subtraction import (
    SubtractionRequest,
    SubtractionResponse
)

from app.services.subtraction import subtract_numbers

router = APIRouter(
    prefix="/api",
    tags=["Subtraction"]
)


@router.post("/subtraction", response_model=SubtractionResponse)
def subtraction(request: SubtractionRequest):

    result = subtract_numbers(request.num1, request.num2)

    return SubtractionResponse(
        num1=request.num1,
        num2=request.num2,
        result=result
    )