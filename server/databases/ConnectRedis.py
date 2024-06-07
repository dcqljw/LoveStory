import redis

from config import SETTINGS

redis_client = redis.Redis(host=SETTINGS.REDIS_HOST, port=SETTINGS.REDIS_PORT)


def get_redis_db():
    db = redis_client
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    redis_client.set("123", "abb")
    redis_client.setex("123", 10, "abb")
