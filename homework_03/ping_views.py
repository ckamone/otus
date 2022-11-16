from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
    tags=["Ping"],
)

@router.get("")
def get_items():
    return {"message": "pong"}