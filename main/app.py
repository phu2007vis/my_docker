from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import *
import random
idintance ="ID may chay: "+ str(int(random.random()*1000))
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from sql_contronler import insert_new_person,check_login_sql

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],  # This allows all HTTP methods
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/begin_register", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("create_acc.html", {"request": request,"inid":idintance})
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request,"inid":idintance})
@app.get("/home", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"inid":idintance})

@app.post("/checkLogin")
async def check_login(data: Login, request: Request):
    if check_login_sql(data.tk,data.mk):
        return Response(json.dumps({"data":f"oke"}))
    return Response(json.dumps({"data":"sai"}))

@app.post("/register")
async def register(data: Login, request: Request):
    if not insert_new_person(data.tk,data.mk)[0] :
        return Response(json.dumps({"data":f"ok"}))
    return Response(json.dumps({"data":"tontai"}))

@app.post("/ocr")
async def ocr(data:ORC_Check):
    #rgb image pil image
    image = decode_base64_to_numpy(data.image)
    text  = get_text(image)
    return Response(json.dumps({"data":text}))