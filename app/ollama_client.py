from typing import List
import requests
from .models import Chat
from fastapi import HTTPException

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"

def get_ollama_report(chats: List[Chat]):
    prompt_text = "Please write a report based on this information in the tex format: " + " ".join(chat.message for chat in chats)
    payload = {
        "model": "mistral:latest",
        "prompt": prompt_text,
        "stream": "false"
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to get report from Ollama")

    response_data = response.json()
    report_content = response_data.get('response', '')

    return report_content
