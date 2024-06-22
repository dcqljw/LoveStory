from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from databases.ConnectMysql import Base


class User(Base):
    __tablename__ = "user"
    uid = Column(String(16), primary_key=True)
    username = Column(String(32))
    password = Column(String(100))
    email_address = Column(String(100))
    avatar_url = Column(String(255))
    create_datetime = Column(DateTime, default=func.now())


class OAuth_user(Base):
    __tablename__ = "oauth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(16), ForeignKey("user.uid"))
    username = Column(String(32))
    platform = Column(String(32))
    email_address = Column(String(100))
    create_datetime = Column(DateTime, default=func.now())
