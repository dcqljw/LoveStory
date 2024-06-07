from typing import Any

from pydantic import BaseModel, model_validator
from config.CustomStatus import CustomStatus


class Base(BaseModel):
    username: str
    password: str


class ResponseSchema(BaseModel):
    code: str = "0000"
    msg: str = ""
    data: Any

    @model_validator(mode="after")
    def after_func(self):
        """
        验证之后根据code设置msg
        :return:
        """
        self.msg = CustomStatus.get(self.code, "未知错误")
        return self