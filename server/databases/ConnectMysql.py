from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import SETTINGS

engine = create_engine(
    f'mysql+pymysql://{SETTINGS.MYSQL_USER}:{SETTINGS.MYSQL_PASSWORD}@{SETTINGS.MYSQL_HOST}:{SETTINGS.MYSQL_PORT}/lovestory?charset=utf8',
    echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_mysql_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
