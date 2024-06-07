from sqlalchemy import Column, Integer, String, DateTime, func

from databases.ConnectMysql import Base


class User(Base):
    __tablename__ = "user"
    uid = Column(String(16), primary_key=True)
    username = Column(String(32))
    password = Column(String(100))
    email_address = Column(String(100))
    create_datetime = Column(DateTime, default=func.now())
