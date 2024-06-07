import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from databases.ConnectMysql import engine, Base
from api.api_router import api_router
from CustomException import registerException

app = FastAPI()

registerException.registerException(app)
# Base.metadata.create_all(engine)


# origins = [
#     "http://localhost:5173",
#     "http://dcqljw.com",
#     "http://localhost:8000"
# ]
origins = [
    "*"
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
    uvicorn.run(app, host="0.0.0.0")
