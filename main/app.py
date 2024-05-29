from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import *
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from sql_contronler import insert_new_person,check_login
endpoint = os.getenv('OCR_ENDPOINT')
if not endpoint:
    endpoint = "http://127.0.0.1:3000"
ocr_endpoint = endpoint+"/ocr"
check_login_endpoint = endpoint+'/checkLogin'
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
    return templates.TemplateResponse("login.html", {"request": request,"endpoint": endpoint})

@app.get("/home", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"ocr_endpoint": ocr_endpoint})

@app.post("/checkLogin")
async def check_login(data: Login, request: Request):
    if data.tk == "a" and data.mk == "b":
        return Response(json.dumps({"data":f"{endpoint}/home"}))
    return Response(json.dumps({"data":"sai"}))
    

@app.post("/ocr")
async def ocr(data:ORC_Check):
    #rgb image pil image
    image = decode_base64_to_numpy(data.image)
    text  = get_text(image)
    return Response(json.dumps({"data":text}))