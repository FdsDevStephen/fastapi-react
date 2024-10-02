from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from .models import ChatCollection
from .report_generator import generate_pdf_report
from .ollama_client import get_ollama_report

router = APIRouter()

@router.post("/generate_report")
async def generate_report(chat_collection: ChatCollection):
    try:
        report_content = get_ollama_report(chat_collection.chats)
        pdf_path = generate_pdf_report(report_content)
        return FileResponse(pdf_path, media_type='application/pdf', filename="report.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_class=HTMLResponse)
async def get():
    with open('app/static/index.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)
