from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from core.AIModel.DouBao import dou_bao_chat
from schemas.ChatSchema import InputDataSchema

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/doubao")
async def chat(input_data: InputDataSchema):
    print(input_data)
    chat_message = dou_bao_chat(input_data.input_data)
    return StreamingResponse(chat_message, media_type="text/event-stream")
