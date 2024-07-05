from pydantic import BaseModel


class InputDataSchema(BaseModel):
    input_data: str
