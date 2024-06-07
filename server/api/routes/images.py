from fastapi import APIRouter, Depends, Cookie
from fastapi.responses import StreamingResponse
from typing import Annotated
from PIL import Image
from io import BytesIO
from sqlalchemy.orm import Session
from datetime import timedelta
from schemas.UserSchema import LoginSchema, RegisterFromSchema, RegisterSchema
from crud import UserCrud
from databases.ConnectMysql import get_mysql_db
# from databases.ConnectRedis import redis_client
from core.security import get_password_hash, verify_password, create_access_token, verify_access_token
from core.uid import idGenerator
from config.SETTINGS import REDIS_EXPIRE

router = APIRouter(prefix="/images", tags=["user"])


@router.get("/home_data")
async def home_data(token: Annotated[str | None, Cookie()] = None):
    print(token)
    image_open = Image.open(r"D:\code\Project\LoveStory\server\output.jpg")

    def iterfile():
        with open(r"D:\code\Project\LoveStory\server\output.jpg", 'rb') as f:
            yield from f

    return StreamingResponse(iterfile(), media_type="image/jpeg")
