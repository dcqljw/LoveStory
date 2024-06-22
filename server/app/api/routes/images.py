from fastapi import APIRouter, Depends, Cookie
from fastapi.responses import StreamingResponse, Response
from typing import Annotated
from PIL import Image

router = APIRouter(prefix="/images", tags=["user"])


@router.get("/home_data")
async def home_data(token: Annotated[str | None, Cookie()] = None):
    print(token)
    image_open = Image.open(r"D:\code\Project\LoveStory\server\output.jpg")

    def iterfile():
        with open(r"D:\code\Project\LoveStory\server\output.jpg", 'rb') as f:
            yield from f

    response = StreamingResponse(iterfile(), media_type="image/jpeg")
    """
    Cache-Control public, max-age=86400;
    """
    response.headers['Cache-Control'] = "max-age=8640"
    return response
