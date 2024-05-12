from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import *
import cv2
import json




app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/ocr")
async def ocr(data:ORC_Check):
    #rgb image
    image = decode_base64_to_numpy(data.image)
    cv2.imwrite("test_image.png",image)
    return Response(json.dumps({"data":"hiih"}))