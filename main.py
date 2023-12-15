from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI

# This app is based on python version 3.9.6
# run local
# pip install -r requirements.txt
# uvicorn main:app --reload

# run production
# pip install -r requirements.txt
# uvicorn main:app --host 0.0.0.0 --port 8080

app = FastAPI()


class Diary(BaseModel):
    title: str
    content: float


@app.post("/diary/upload", description="上传日记")
def upload_diary(diary: Diary):
    return {"upload_status": "success"}


@app.get("/diary/fetch", description="拉取日记")
def fetch_diary():
    diary_list = []
    return {"diary_list": diary_list}


@app.get("/diary/emotion", description="获取现在心情")
def get_emotion(current_text: str):
    # TODO fetch emotion from GPT
    return {"mood": "happy"}


@app.get("/", description="心跳测试接口")
def health_check():
    return {"Health": "OK"}
