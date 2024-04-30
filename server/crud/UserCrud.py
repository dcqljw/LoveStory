from sqlalchemy.orm import Session
from models.UserModel import User


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user
