from sqlalchemy.orm import Session
from models.UserModel import User
from schemas import UserSchema


def get_user(db: Session, email_address: str) -> User | None:
    user = db.query(User).filter(User.email_address == email_address).first()
    return user


def get_user_by_id(db: Session, uid: str):
    user = db.query(User).filter(User.uid == uid).first()
    return user


def create_user(db: Session, user: UserSchema.RegisterSchema) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
