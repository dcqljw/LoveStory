from fastapi import Header, Request, Cookie
from fastapi.exceptions import HTTPException
from datetime import datetime, timedelta
from typing import Any, Annotated

from jose import jwt, JWTError
from passlib.context import CryptContext

from databases.ConnectRedis import redis_client
from CustomException.TokenException import CustomTokenException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, "123", algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(header_token: Annotated[str | None, Header()] = None,
                        cookie_token: Annotated[str | None, Header()] = None):
    if (header_token != "" or header_token is not None) and (cookie_token != "" or cookie_token is not None):
        try:
            decoded_token = jwt.decode(header_token, "123", algorithms=[ALGORITHM])
            token = redis_client.get(decoded_token["sub"])
            if token is None:
                raise CustomTokenException("token is invalid")
            if bytes.decode(token) == header_token:
                return decoded_token["sub"]
            else:
                raise CustomTokenException("token is invalid")
        except:
            raise CustomTokenException("token is invalid")
    else:
        raise CustomTokenException("not token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


if __name__ == '__main__':
    token = create_access_token("adsfasdf", timedelta(minutes=1))
    print(token)
    access_token = verify_access_token(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQyODE1MTIsInN1YiI6ImFkc2Zhc2RmIn0.sE8dt7lF0GFhCWKBlvxBL3VBe9fd_YHjqK1hdJraOqo")
    print(access_token)
    password_hash = get_password_hash("dcq.159357")
    print(password_hash)
    password = verify_password("aaa", password_hash)
    print(password)
