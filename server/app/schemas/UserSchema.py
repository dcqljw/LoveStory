from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email_address: EmailStr


class RegisterSchema(UserBase):
    uid: str

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    password: str
    email_address: EmailStr


class RegisterFromSchema(UserBase):
    password: str


class UserInfoSchema(UserBase):
    pass
