import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"status": "ok"}


if __name__ == '__main__':
    uvicorn.run(app)
