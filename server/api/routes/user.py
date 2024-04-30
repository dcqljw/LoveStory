from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from schemas.CustomResponseSchema import ResponseSchema, Base
from schemas.UserSchema import LoginSchema
from crud import UserCrud
from databases.ConnectMysql import get_mysql_db

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login")
# @router.post("/login", response_model=TestResponseSchema)
def login(user: LoginSchema, db: Session = Depends(get_mysql_db)):
    get_user = UserCrud.get_user(db, user.username)
    print(get_user.dict())
    return ResponseSchema(code="2001", data={
        "data": "asdf",
        "sss": "xxx"
    })
    if get_user:
        return {"code": "2000", "msg": "123", "data": get_user}
    else:
        return ResponseSchema(code="2001")
