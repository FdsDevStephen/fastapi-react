from pydantic import BaseModel
from typing import List

class Chat(BaseModel):
    message: str

class ChatCollection(BaseModel):
    chats: List[Chat]
