from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class ResponseModel(BaseModel):
    result: str