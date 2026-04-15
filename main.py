from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb://localhost:27017/fastNotes")

@app.get("/")
def read_root():
    docs = conn.fastNotes.notes.find_one({})
    print(docs)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}