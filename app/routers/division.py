from fastapi import APIRouter, HTTPException

from app.schemas.division import (
    DivisionRequest,
    DivisionResponse
)

from app.services.division import divide_numbers


router = APIRouter(
    prefix="/api",
    tags=["Division"]
)


@router.post("/division", response_model=DivisionResponse)
def division(request: DivisionRequest):

    try:
        result = divide_numbers(request.num1, request.num2)

        return DivisionResponse(
            num1=request.num1,
            num2=request.num2,
            result=result
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )