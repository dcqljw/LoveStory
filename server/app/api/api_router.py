from fastapi import APIRouter, Depends
from api.routes import user, images, chat
from core.security import verify_access_token

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(images.router)
api_router.include_router(chat.router)
