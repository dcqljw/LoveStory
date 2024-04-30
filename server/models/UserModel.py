from sqlalchemy import Column, Integer, String, DateTime, func

from databases.ConnectMysql import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(100))
    uid = Column(String(16))
    email_address = Column(String(100))
    create_datetime = Column(DateTime, default=func.now())

    # def __repr__(self):
    #     return f"username{self.username}"
    def _json(self):
        return {
            "username": self.username
        }
