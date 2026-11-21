from fastapi import APIRouter
from app.schemas.addition import AdditionRequest, AdditionResponse
from app.services.addition import add_numbers

router = APIRouter(
    prefix="/api",
    tags=["Addition"]
)


@router.post("/addition", response_model=AdditionResponse)
def addition(request: AdditionRequest):

    result = add_numbers(request.num1, request.num2)

    return AdditionResponse(
        num1=request.num1,
        num2=request.num2,
        result=result
    )