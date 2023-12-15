from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import pymongo
import random
import json

# mongoDB connection string:
mongo_conn_str = 'mongodb+srv://agi-user-prod:O0lfjQSLEi6v423z@agi-diary-cluster.mtxn3qw.mongodb.net/'
client = pymongo.MongoClient(mongo_conn_str)
py_db = client['agi-db']
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
    py_db['diary'].insert_one(diary.model_dump())
    return {"upload_status": "success"}


@app.get("/diary/fetch", description="拉取日记")
def fetch_diary():
    diary_list = []
    all_diary = py_db['diary'].find()
    for diary in all_diary:
        diary['_id'] = str(diary['_id'])
        diary_list.append(diary)
    return {"diary_list": diary_list}


@app.get("/diary/emotion", description="获取现在心情")
def get_emotion(current_text: str):
    moods = ["happy", "sad", "cry", "high", "low"]
    mood = random.choice(moods)
    return {"mood": mood}


@app.get("/", description="心跳测试接口")
def health_check():
    return {"Health": "OK"}