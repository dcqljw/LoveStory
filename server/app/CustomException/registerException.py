from fastapi import FastAPI

from CustomException.TokenException import CustomTokenException, TokenExceptionHandler
from CustomException.ServerException import ServerExceptionHandler


def registerException(app: FastAPI):
    app.add_exception_handler(CustomTokenException, TokenExceptionHandler)
    # app.add_exception_handler(500, ServerExceptionHandler)
