from sqlalchemy import and_
from sqlalchemy.orm import Session
from models.UserModel import User, OAuth_user
from schemas import UserSchema
from core.uid import idGenerator


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


def is_bind_oauth_user(db: Session, username: str, platform: str) -> OAuth_user | None:
    return db.query(OAuth_user).filter(
        and_(OAuth_user.username == username, OAuth_user.platform == platform)).first()


def register_oauth_user(db: Session, oauth_user: UserSchema.OAuthUserSchema) -> User:
    user = User(
        uid=idGenerator.generate_id(),
        username=oauth_user.username,
        email_address=oauth_user.email_address,
        avatar_url=oauth_user.avatar_url
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    # del oauth_user['avatar_url']
    o_auth_user = OAuth_user(user_id=user.uid,
                             username=oauth_user.username,
                             platform=oauth_user.platform,
                             email_address=oauth_user.email_address)
    db.add(o_auth_user)
    db.commit()
    db.refresh(o_auth_user)
    return user
