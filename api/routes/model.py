from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    name="hello"
)
async def hello():
    return "hello"
