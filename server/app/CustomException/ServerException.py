from fastapi.responses import JSONResponse
from fastapi import Request


class CustomTokenException(Exception):
    def __init__(self, msg: str):
        self.msg = msg


async def ServerExceptionHandler(request: Request, exc):
    return JSONResponse(
        status_code=200,
        content={
            "code": "5000",
            "msg": "123"
        },
    )
