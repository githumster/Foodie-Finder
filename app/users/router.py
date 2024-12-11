from fastapi import APIRouter

from app.users.schemas import SUserAuth

router = APIRouter(
    prefix= "/auth",
    tags=["Auth & Пользователи"]
)

@router.post("/register")
async def register_user():
    return {"reg":"OK"}

@router.post("/login")
async def login():
    return {"reg":"OK"}