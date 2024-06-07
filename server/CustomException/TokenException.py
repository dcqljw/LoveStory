from fastapi.responses import JSONResponse
from fastapi import Request


class CustomTokenException(Exception):
    def __init__(self, msg: str):
        self.msg = msg


async def TokenExceptionHandler(request: Request, exc):
    return JSONResponse(
        status_code=200,
        content={
            "code": "4001",
            "msg": str(exc)
        },
    )
