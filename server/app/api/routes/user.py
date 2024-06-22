import os
import requests
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from datetime import timedelta

from schemas.UserSchema import LoginSchema, RegisterFromSchema, RegisterSchema, UserInfoSchema, OAuthUserSchema
from crud import UserCrud
from databases.ConnectMysql import get_mysql_db
from databases.ConnectRedis import redis_client
from core.security import get_password_hash, verify_password, create_access_token, verify_access_token
from core.uid import idGenerator
from config.SETTINGS import REDIS_EXPIRE

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_mysql_db)):
    get_user = UserCrud.get_user(db, user.email_address)
    verify = verify_password(user.password, get_user.password)
    if verify:
        token = create_access_token(get_user.uid, expires_delta=timedelta(days=1))
        redis_client.setex(get_user.uid, REDIS_EXPIRE, token)
        return {
            "code": "2000",
            "msg": "登录成功",
            "data": {
                "uid": get_user.uid,
                "username": get_user.username,
                "email_address": get_user.email_address,
                "token": token
            }
        }
    else:
        return {
            "code": "2001",
            "msg": "账号密码错误"
        }


@router.post("/register")
def register(user: RegisterFromSchema, db: Session = Depends(get_mysql_db)):
    get_user = UserCrud.get_user(db, user.email_address)
    if get_user:
        return {
            "code": "2001",
            "msg": "用户已存在"
        }
    else:
        password_hash = get_password_hash(user.password)
        user.password = password_hash
        uid = idGenerator.generate_id()
        print(len(str(uid)))
        register_user = RegisterSchema(uid=str(uid), **user.dict())
        UserCrud.create_user(db, register_user)
        return {
            "code": "2000",
            "msg": "注册成功"
        }


@router.post("/user_info", response_model=UserInfoSchema)
def get_user_info(db: Session = Depends(get_mysql_db), jwt=Depends(verify_access_token)):
    return UserCrud.get_user_by_id(db, jwt)


@router.post("/verify_token")
def verify_token():
    return {"code": "2000", "msg": "ok"}


@router.get("/env")
def get_env():
    return {"env": os.getenv("fast_env")}


@router.get("/auth/github/callback")
def github_callback(code: str, db: Session = Depends(get_mysql_db)):
    print(code)
    headers = {
        'Accept': 'application/json',
    }
    url = f"https://github.com/login/oauth/access_token?client_id=Ov23li5BelebTemvlHgp&client_secret=d32e48dbba9da2002ef5895dc1cb409eb18e8c19&code={code}"
    response = requests.get(url, headers=headers).json()
    user_url = "https://api.github.com/user"
    print(response)
    headers = {
        "Authorization": f"Bearer {response['access_token']}"
    }
    user_info = requests.get(user_url, headers=headers).json()
    oauth_schema = OAuthUserSchema(
        username=user_info["login"],
        platform="github",
        email_address=user_info["bio"],
        avatar_url=user_info["avatar_url"])
    is_bind = UserCrud.is_bind_oauth_user(db, username=oauth_schema.username, platform=oauth_schema.platform)
    if is_bind:
        token = create_access_token(is_bind.user_id, expires_delta=timedelta(days=1))
        redis_client.setex(is_bind.user_id, REDIS_EXPIRE, token)
        return {
            "code": "2000",
            "msg": "登录成功",
            "data": {
                "uid": is_bind.user_id,
                "username": is_bind.username,
                "email_address": is_bind.email_address,
                "token": token,
                "avatar_url": user_info["avatar_url"]
            }
        }
    else:
        UserCrud.register_oauth_user(db, oauth_schema)
        return {
            "code": "2001",
            "msg": "账号密码错误"
        }
