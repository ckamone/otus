from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)

@router.get("")
def get_items():
    return {
        "data": [
            {
                "id": 1,
                "value": "qwerty",
            },
            {
                "id": 2,
                "value": "wasd",
            },
        ]
    }