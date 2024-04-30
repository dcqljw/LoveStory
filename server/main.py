import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from databases.ConnectMysql import engine, Base
from api.api_router import api_router


app = FastAPI()

# Base.metadata.create_all(engine)

origins = [
    "http://localhost:5173",
    "http://dcqljw.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost")
