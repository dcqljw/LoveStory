import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api_router import api_router
from CustomException import registerException
from databases.ConnectMysql import Base, engine

app = FastAPI(root_path="/api")

# 注册自定义异常
registerException.registerException(app)
# Base.metadata.create_all(engine)

origins = [
    "http://localhost:5173",
    "http://dcqljw.com",
    "http://localhost:8000",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 添加路由
app.include_router(api_router)

if __name__ == '__main__':
    print(os.getenv("fast_env"))
    uvicorn.run(app, host="0.0.0.0")
