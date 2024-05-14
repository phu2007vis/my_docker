from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import *
from fastapi.middleware.cors import CORSMiddleware
import json
import os
ocr_endpoint = os.getenv('OCR_ENDPOINT')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],  # This allows all HTTP methods
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"ocr_endpoint": ocr_endpoint})
@app.post("/ocr")
async def ocr(data:ORC_Check):
    #rgb image pil image
    image = decode_base64_to_numpy(data.image)
    text  = get_text(image)
    return Response(json.dumps({"data":text}))