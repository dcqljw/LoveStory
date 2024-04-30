from fastapi import APIRouter
from api.routes import user

api_router = APIRouter(prefix="/api")
api_router.include_router(user.router)
